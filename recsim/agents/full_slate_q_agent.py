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
"""Agent that implements the Slate-Q algorithms."""

import itertools
import gin.tf
from gym import spaces
from recsim import agent as abstract_agent
from recsim.agents.dopamine import dqn_agent
import tensorflow as tf


@gin.configurable
class FullSlateQAgent(dqn_agent.DQNAgentRecSim,
                      abstract_agent.AbstractEpisodicRecommenderAgent):
  """A recommender agent implements full slate Q-learning based on DQN agent.

  This is a standard, nondecomposed Q-learning method that treats each slate
  atomically (i.e., holistically) as a single action.
  """

  def __init__(self,
               sess,
               observation_space,
               action_space,
               optimizer_name='',
               eval_mode=False,
               **kwargs):
    """Initializes a FullSlateQAgent.

    Args:
      sess: a Tensorflow session.
      observation_space: A gym.spaces object that specifies the format of
        observations.
      action_space: A gym.spaces object that specifies the format of actions.
      optimizer_name: The name of the optimizer.
      eval_mode: A bool for whether the agent is in training or evaluation mode.
      **kwargs: Keyword arguments to the DQNAgent.
    """
    self._num_candidates = int(action_space.nvec[0])
    abstract_agent.AbstractEpisodicRecommenderAgent.__init__(self, action_space)
    # Each slate is a single action. Assume ordering of items matters.
    self._all_possible_slates = [
        x for x in itertools.permutations(
            range(self._num_candidates), action_space.nvec.shape[0])
    ]
    num_actions = len(self._all_possible_slates)
    self._env_action_space = spaces.Discrete(num_actions)

    dqn_agent.DQNAgentRecSim.__init__(
        self,
        sess,
        observation_space,
        num_actions=num_actions,
        stack_size=1,
        optimizer_name='',
        eval_mode=eval_mode,
        **kwargs)

  # Builds a tower to compute Q-value for each possible slate.
  def _network_adapter(self, states, scope):
    self._validate_states(states)

    with tf.compat.v1.name_scope('network'):
      q_value_list = []
      for slate in self._all_possible_slates:
        user = tf.squeeze(states[:, 0, :, :], axis=2)
        docs = []
        for i in slate:
          docs.append(tf.squeeze(states[:, i + 1, :, :], axis=2))
        q_value_list.append(self.network(user, tf.concat(docs, axis=1), scope))
      q_values = tf.concat(q_value_list, axis=1)

    return dqn_agent.DQNNetworkType(q_values)

  def _build_networks(self):
    with tf.compat.v1.name_scope('networks'):
      self._replay_net_outputs = self._network_adapter(self._replay.states,
                                                       'Online')
      self._replay_next_target_net_outputs = self._network_adapter(
          self._replay.states, 'Target')
      self._net_outputs = self._network_adapter(self.state_ph, 'Online')
      self._q_argmax = tf.argmax(input=self._net_outputs.q_values, axis=1)[0]

  def step(self, reward, observation):
    """Receives observations of environment and returns a slate.

    Args:
      reward: A double representing the overall reward to the recommended slate.
      observation: A dictionary that stores all the observations including:
        - user: A list of floats representing the user's observed state
        - doc: A list of observations of document features
        - response: A vector valued response signal that represent user's
          response to each document

    Returns:
      slate: An integer array of size _slate_size, where each element is an
        index in the list of document observvations.
    """
    return self._all_possible_slates[super(FullSlateQAgent, self).step(
        reward, self._obs_adapter.encode(observation))]

  def _build_replay_buffer(self, use_staging):
    """Creates the replay buffer used by the agent.

    Args:
      use_staging: bool, if True, uses a staging area to prefetch data for
        faster training.

    Returns:
      A WrapperReplayBuffer object.
    """
    return dqn_agent.wrapped_replay_buffer(
        observation_shape=self.observation_shape,
        stack_size=self.stack_size,
        use_staging=use_staging,
        update_horizon=self.update_horizon,
        gamma=self.gamma,
        observation_dtype=self.observation_dtype)

  def begin_episode(self, observation):
    """Returns the agent's first action for this episode.

    Args:
      observation: numpy array, the environment's initial observation.

    Returns:
      An integer array of size _slate_size, the selected slated, each
      element of which is an index in the list of doc_obs.
    """
    return self._all_possible_slates[super(FullSlateQAgent, self).begin_episode(
        self._obs_adapter.encode(observation))]

  def end_episode(self, reward, observation):
    """Signals the end of the episode to the agent.

    We store the observation of the current time step, which is the last
    observation of the episode.

    Args:
      reward: float, the last reward from the environment.
      observation: numpy array, the environment's initial observation.
    """
    super(FullSlateQAgent, self).end_episode(reward)
