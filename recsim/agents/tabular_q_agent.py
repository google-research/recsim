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
"""A Tabular Q-learning implementation."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import itertools

from absl import logging
from gym import spaces
import numpy as np

from recsim import agent
from recsim.agents import agent_utils


class TabularQAgent(agent.AbstractEpisodicRecommenderAgent):
  """Tabular Q-learning agent with universal function approximation.

  This agent provides a tabular implementation of the Q-learning algorithm.
  To construct a tabular representation of the state-action space, the agent
  does the following:
    1. the action space consists of all ordered k-tuples of document features
    available in observation['doc'];
    2. the state space consists of observation['user']
    and observation['response'];
    3. the observation and action space are joined and flattened;
    4. all continuoius values in the flattened state-action vector are
    discretized into a predefined number of bins.
  In the tabularized state-action space, the agent applies the standard
  Q-learning update of
    Q_{t+1}(s,a) = (1-a) * Q_t(s,a) + a * (R(s,a) + g * max_a(Q_t(s', a))).
  Assuming that the discretization of countinous attributes is fine enough, and
  the problem itself is Markovian given the observations, the output of this
  agent can be assumed to converge to a close approximation of the ground truth
  Q-function. Producing ground truth Q-functions is the main intended use of
  this agent, since discretization is prohibitively expensive in
  high-dimensional environments.
  """

  def __init__(self,
               observation_space,
               action_space,
               eval_mode=False,
               ignore_response=True,
               discretization_bounds=(0.0, 10.0),
               number_bins=100,
               exploration_policy='epsilon_greedy',
               exploration_temperature=0.99,
               learning_rate=0.1,
               gamma=0.99,
               **kwargs):
    """TabularQAgent init.

    Args:
      observation_space: a gym.spaces object specifying the format of
        observations.
      action_space: a gym.spaces object that specifies the format of actions.
      eval_mode: Boolean indicating whether the agent is in training or eval
        mode.
      ignore_response: Boolean indicating whether the agent should ignore the
        response part of the observation.
      discretization_bounds: pair of real numbers indicating the min and max
        value for continuous attributes discretization. Values below the min
        will all be grouped in the first bin, while values above the max will
        all be grouped in the last bin. See the documentation of numpy.digitize
        for further details.
      number_bins: positive integer number of bins used to discretize continuous
        attributes.
      exploration_policy: either one of ['epsilon_greedy', 'min_count'] or a
        custom function. TODO(mmladenov): formalize requirements of this
          function.
      exploration_temperature: a real number passed as parameter to the
        exploration policy.
      learning_rate: a real number between 0 and 1 indicating how much to update
        Q-values, i.e. Q_t+1(s,a) = (1 - learning_rate) * Q_t(s, a)
                                     + learning_rate * (R(s,a) + ...).
      gamma: real value between 0 and 1 indicating the discount factor of the
        MDP.
      **kwargs: additional arguments like eval_mode.
    """
    self._kwargs = kwargs
    super(TabularQAgent, self).__init__(action_space)
    # hard params
    self._gamma = gamma
    self._eval_mode = eval_mode
    self._previous_slate = None
    self._learning_rate = learning_rate
    # storage
    self._q_value_table = {}
    self._state_action_counts = {}
    self._previous_state_action_index = None
    # discretization and spaces
    self._discretization_bins = np.linspace(
        discretization_bounds[0], discretization_bounds[1], num=number_bins)
    single_doc_space = list(observation_space.spaces['doc'].spaces.values())[0]
    slate_tuple = tuple([single_doc_space] * self._slate_size)
    action_space = spaces.Tuple(slate_tuple)
    self._ignore_response = ignore_response
    state_action_space = {
        'user': observation_space.spaces['user'],
        'action': action_space
    }
    if not self._ignore_response:
      state_action_space['response'] = observation_space.spaces['response']
    self._state_action_space = spaces.Dict(state_action_space)
    self._observation_featurizer = agent_utils.GymSpaceWalker(
        self._state_action_space, self._discretize_gym_leaf)
    # exploration
    self._exploration_policy = exploration_policy
    self._exploration_temperature = exploration_temperature
    self._base_exploration_temperature = self._exploration_temperature
    self._exploration_functions = {
        'epsilon_greedy':
            lambda observation: agent_utils.epsilon_greedy_exploration(  # pylint: disable=g-long-lambda
                self._enumerate_state_action_indices(observation), self.
                _q_value_table, self._exploration_temperature),
        'min_count':
            lambda observation: agent_utils.min_count_exploration(  # pylint: disable=g-long-lambda
                self._enumerate_state_action_indices(observation),
                self._state_action_counts)
    }

  def _discretize_gym_leaf(self, gym_space, gym_observations):

    index = []
    for gym_observation in gym_observations:
      gym_observation = gym_observations[0]
      if isinstance(gym_space, spaces.box.Box):
        gym_observation = np.array(gym_observation)
        dis_obs = np.digitize(gym_observation.flatten(),
                              self._discretization_bins)
        index += list(dis_obs)
      elif isinstance(gym_space, spaces.discrete.Discrete):
        index.append(gym_observation)
      else:
        raise NotImplementedError('Gym space type ' + str(type(gym_space)) +
                                  ' not implemented yet.')
    return index

  def _enumerate_slates(self, doc_dict):
    documents = list(doc_dict.values())
    num_documents = len(documents)
    for slate in itertools.combinations(range(num_documents), self._slate_size):
      yield slate, tuple([documents[i] for i in slate])

  def _enumerate_state_action_indices(self, observation):
    for (slate, slate_features) in self._enumerate_slates(observation['doc']):
      state_action_pair = {
          'user': observation['user'],
          'action': slate_features
      }
      if not self._ignore_response:
        state_action_pair['response'] = observation['response']
      state_action_index = self._observation_featurizer.apply_and_flatten([
          state_action_pair,
      ])
      state_action_index = tuple(state_action_index)
      yield slate, state_action_index

  def step(self, reward, observation):
    """Records the most recent transition and returns the agent's next action.

    We store the observation of the last time step since we want to store it
    with the reward.

    Args:
      reward: The reward received from the agent's most recent action as a
        float.
      observation: A dictionary that includes the most recent observations and
        should have the following fields:
        - user: A NumPy array representing user's observed state. Assumes it is
          a concatenation of topic pull counts and topic click counts.
        - doc: A NumPy array representing observations of document features.
          Assumes it is a concatenation of one-hot encoding of topic_id and
          document quality.

    Returns:
      slate: An integer array of size _slate_size, where each element is an
        index into the list of doc_obs
    Raises:
      ValueError: if reward is not in [0, 1].
    """
    # Find max-Q action given the current state and Q-table.
    max_q_state_action = max(
        self._enumerate_state_action_indices(observation),
        key=lambda sa: self._q_value_table.get(sa[1], 0))
    max_q_next = self._q_value_table.get(max_q_state_action[1], 0)
    # Update the Q-table.
    if self._previous_state_action_index is not None:
      old_q = self._q_value_table.get(self._previous_state_action_index, 0.)
      self._q_value_table[self._previous_state_action_index] = (
          self._learning_rate * (reward + self._gamma * max_q_next) +
          (1. - self._learning_rate) * old_q)
      self._state_action_counts[
          self._previous_state_action_index] = self._state_action_counts.get(
              self._previous_state_action_index, 0) + 1
    # Pick next action.
    if not self._eval_mode:
      slate, state_action_index = self._exploration_functions[
          self._exploration_policy](
              observation)
      self._previous_state_action_index = state_action_index
    else:
      slate, state_action_index = max_q_state_action
    return slate

  def end_episode(self, reward, observation):
    self._exploration_temperature *= self._base_exploration_temperature
    self._exploration_functions = {
        'epsilon_greedy':
            lambda observation: agent_utils.epsilon_greedy_exploration(  # pylint: disable=g-long-lambda
                self._enumerate_state_action_indices(observation), self.
                _q_value_table, self._exploration_temperature),
        'min_count':
            lambda observation: agent_utils.min_count_exploration(  # pylint: disable=g-long-lambda
                self._enumerate_state_action_indices(observation),
                self._state_action_counts)
    }
    self._previous_state_action_index = None

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
    del checkpoint_dir  # Unused.
    del iteration_number  # Unused.
    bundle_dict = {'q_value_table': self._q_value_table}
    bundle_dict['sa_count'] = self._state_action_counts
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
    del checkpoint_dir  # Unused.
    del iteration_number  # Unused.
    if 'q_value_table' not in bundle_dict:
      logging.warning(
          'Could not unbundle from checkpoint files with exception.')
      return False
    self._q_value_table = bundle_dict['q_value_table']
    self._state_action_counts = bundle_dict.get('sa_count', {})
    return True
