# coding=utf-8
# coding=utf-8
# Copyright 2019 The RecSim Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Abstract interface for recommender system agents."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc
from absl import logging


class AbstractRecommenderAgent(object):  # pytype: disable=ignored-metaclass
  """Abstract class to model a recommender system agent."""

  __metaclass__ = abc.ABCMeta

  def __init__(self, action_space):
    """Initializes AbstractRecommenderAgent.

    Args:
      action_space: A gym.spaces object that specifies the format of actions.
    """
    self._slate_size = action_space.nvec.shape[0]

  @abc.abstractmethod
  def step(self, reward, observation):
    """Records the most recent transition and returns the agent's next action.

    We store the observation of the last time step since we want to store it
    with the reward.

    Args:
      reward: The reward received from the agent's most recent action as a
        float.
      observation: A dictionary that includes the most recent observations.

    Returns:
      slate: An integer array of size _slate_size, where each element is an
        index into the list of doc_obs
    """

  @abc.abstractmethod
  def bundle_and_checkpoint(self, checkpoint_dir, iteration_number):
    """Returns a self-contained bundle of the agent's state.

    This is used for checkpointing. It will return a dictionary containing all
    non-TensorFlow objects (to be saved into a file by the caller), and it saves
    all TensorFlow objects into a checkpoint file.

    Args:
      checkpoint_dir: A string for the directory where objects will be saved.
      iteration_number: An integer of iteration number to use for naming the
        checkpoint file.

    Returns:
      A dictionary containing additional Python objects to be checkpointed by
        the experiment. Each key is a string for the object name and the value
        is actual object. If the checkpoint directory does not exist, returns
        empty dictionary.
    """

  @abc.abstractmethod
  def unbundle(self, checkpoint_dir, iteration_number, bundle_dict):
    """Restores the agent from a checkpoint.

    Restores the agent's Python objects to those specified in bundle_dict,
    and restores the TensorFlow objects to those specified in the
    checkpoint_dir. If the checkpoint_dir does not exist, will not reset the
    agent's state.

    Args:
      checkpoint_dir: A string that represents the path to the checkpoint saved
        by tf.Save.
      iteration_number: An integer that represents the checkpoint version and is
        used when restoring replay buffer.
      bundle_dict: A dict containing additional Python objects owned by the
        agent. Each key is an object name and the value is the actual object.

    Returns:
      bool, True if unbundling was successful.
    """


class AbstractEpisodicRecommenderAgent(AbstractRecommenderAgent):
  """Abstract class for recommender systems that solves episodic tasks."""

  def __init__(self, action_space, summary_writer=None):
    """Initializes AbstractEpisodicRecommenderAgent.

    Args:
      action_space: A gym.spaces object that specifies the format of actions.
      summary_writer: A Tensorflow summary writer to pass to the agent
        for in-agent training statistics in Tensorboard.
    """
    super(AbstractEpisodicRecommenderAgent, self).__init__(action_space)
    self._episode_num = 0
    self._summary_writer = summary_writer

  def begin_episode(self, observation=None):
    """Returns the agent's first action for this episode.

    Args:
      observation: numpy array, the environment's initial observation.

    Returns:
      slate: An integer array of size _slate_size, where each element is an
        index into the list of doc_obs
    """
    self._episode_num += 1
    return self.step(0, observation)

  def end_episode(self, reward, observation=None):
    """Signals the end of the episode to the agent.

    Args:
      reward: An float that is the last reward from the environment.
      observation: numpy array that represents the last observation of the
        episode.
    """
    pass

  def bundle_and_checkpoint(self, checkpoint_dir, iteration_number):
    """Returns a self-contained bundle of the agent's state.

    Args:
      checkpoint_dir: A string that represents the path to the checkpoint and is
        used when we save TensorFlow objects by tf.Save.
      iteration_number: An integer that represents the checkpoint version and is
        used when restoring replay buffer.

    Returns:
      A dictionary containing additional Python objects to be checkpointed by
        the experiment. Each key is a string for the object name and the value
        is actual object. If the checkpoint directory does not exist, returns
        empty dictionary.
    """
    del checkpoint_dir  # Unused.
    del iteration_number  # Unused.
    bundle_dict = {}
    bundle_dict['episode_num'] = self._episode_num
    return bundle_dict

  def unbundle(self, checkpoint_dir, iteration_number, bundle_dict):
    """Restores the agent from a checkpoint.

    Args:
      checkpoint_dir: A string that represents the path to the checkpoint and is
        used when we save TensorFlow objects by tf.Save.
      iteration_number: An integer that represents the checkpoint version and is
        used when restoring replay buffer.
      bundle_dict: A dict containing additional Python objects owned by the
        agent. Each key is an object name and the value is the actual object.

    Returns:
      bool, True if unbundling was successful.
    """
    del checkpoint_dir  # Unused.
    del iteration_number  # Unused.
    if 'episode_num' not in bundle_dict:
      logging.warning(
          'Could not unbundle from checkpoint files with exception.')
      return False
    self._episode_num = bundle_dict['episode_num']
    return True


class AbstractHierarchicalAgentLayer(AbstractRecommenderAgent):
  """Parent class for stackable agent layers."""

  def __init__(self, action_space, *base_agent_ctors):
    super(AbstractHierarchicalAgentLayer, self).__init__(action_space)
    self._base_agent_ctors = base_agent_ctors
    self._base_agents = None

  def _preprocess_reward_observation(self, reward, observation):
    r"""Modifies the reward and observation before passing to base agent.

    This function is used to modify the observation and reward before
    propagating it downward to the base agent. For example, it can
    inject additional features like sufficient statistics by inserting fields
    to observation[\'user\'], or, to implement regularization schemes by
    subtracting penalties from the reward.

    Args:
      reward: float number.
      observation: gym space in recsim format.

    Returns:
      reward: float number.
      observation: gym space in recsim format.
    """
    return reward, observation

  @abc.abstractmethod
  def _postprocess_actions(self, action_list):
    r"""Aggregates (possibly abstract) base agent actions into a valid slate."""

  def begin_episode(self, observation=None):
    if observation is not None:
      _, observation = self._preprocess_reward_observation(0, observation)
    action_list = [
        base_agent.begin_episode(observation=observation)
        for base_agent in self._base_agents
    ]
    return self._postprocess_actions(action_list)

  def end_episode(self, reward, observation):
    reward, observation = self._preprocess_reward_observation(
        reward, observation)
    action_list = [
        base_agent.end_episode(reward, observation=observation)
        for base_agent in self._base_agents
    ]
    return self._postprocess_actions(action_list)

  def bundle_and_checkpoint(self, checkpoint_dir, iteration_number):
    """Returns a self-contained bundle of the agent's state.

    Args:
      checkpoint_dir: A string for the directory where objects will be saved.
      iteration_number: An integer of iteration number to use for naming the
        checkpoint file.

    Returns:
      A dictionary containing additional Python objects to be checkpointed by
        the experiment. Each key is a string for the object name and the value
        is actual object. If the checkpoint directory does not exist, returns
        empty dictionary.
    """
    bundle_dict = {}
    for i, base_agent in enumerate(self._base_agents):
      base_bundle_dict = base_agent.bundle_and_checkpoint(
          checkpoint_dir, iteration_number)
      bundle_dict['base_agent_bundle_{}'.format(i)] = base_bundle_dict
    return bundle_dict

  def unbundle(self, checkpoint_dir, iteration_number, bundle_dict):
    """Restores the agent from a checkpoint.

    Args:
      checkpoint_dir: A string that represents the path to the checkpoint saved
        by tf.Save.
      iteration_number: An integer that represents the checkpoint version and is
        used when restoring replay buffer.
      bundle_dict: A dict containing additional Python objects owned by the
        agent. Each key is an object name and the value is the actual object.

    Returns:
      bool, True if unbundling was successful.
    """
    success = True
    for i, base_agent in enumerate(self._base_agents):
      if 'base_agent_bundle_{}'.format(i) not in bundle_dict:
        logging.warning('Base agent bundle not found in bundle.')
        return False
      success &= base_agent.unbundle(
          checkpoint_dir, iteration_number,
          bundle_dict['base_agent_bundle_{}'.format(i)])
    return success
