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
"""Helper classes to record user response history on recommendations."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc
from gym import spaces

from recsim import agent


class SufficientStatisticsLayer(agent.AbstractHierarchicalAgentLayer):
  """A module to log user responses on different clusters.

  This module assumes each document belongs to single cluster and we know the
  number of possible clusters. Every time we increase impression count for a
  cluster if the agent recommends a document from that cluster. We also increase
  click count for a cluster if user responds a click.
  """

  def __init__(self, base_agent_ctor, observation_space, action_space,
               sufficient_statistics_space, **kwargs):
    """Initializes a UserClusterHistory object.

    Args:
      base_agent_ctor: a constructor for the base agent.
      observation_space: a gym.spaces object specifying the format of
        observations.
      action_space: A gym.spaces object that specifies the format of actions.
      sufficient_statistics_space: a gym.spaces object specifying the format of
        the created sufficient statistics.
      **kwargs: arguments to pass to the downstream agent at construction time.
    """
    super(SufficientStatisticsLayer, self).__init__(action_space,
                                                    base_agent_ctor)
    self._sufficient_statistcs_space = sufficient_statistics_space
    self._sufficient_statistics = None
    augmented_observation_space = {
        'user':
            spaces.Dict({
                'raw_observation': observation_space.spaces['user'],
                'sufficient_statistics': sufficient_statistics_space
            }),
        'response':
            observation_space.spaces['response'],
        'doc':
            observation_space.spaces['doc']
    }
    self._observation_space = observation_space
    self._base_observation_space = spaces.Dict(augmented_observation_space)
    kwargs['observation_space'] = self._base_observation_space
    kwargs['action_space'] = action_space
    self._base_agents = [
        self._base_agent_ctors[0](**kwargs),
    ]
    self._reset()

  @property
  def observation_space(self):
    return self._observation_space

  @abc.abstractmethod
  def _update(self, observation):
    """Updates self._sufficient_statistics given a new observation.

    If self._sufficient_statistics is None, this function must also initialize
    it.

    Args:
     observation: an observation conforming to self._observation_space.
    """

  @abc.abstractmethod
  def _create_observation(self):
    """Formats self._sufficient_statistics into an observation."""

  def _preprocess_reward_observation(self, reward, observation):
    self._update(observation)
    augmented_observation = {key: value for key, value in observation.items()}
    augmented_observation['user'] = {
        'raw_observation': augmented_observation['user'],
        'sufficient_statistics': self._create_observation()
    }
    return reward, augmented_observation

  def _postprocess_actions(self, action_list):
    # Does not modify the action of the base agent.
    return action_list[0]

  def step(self, reward, observation):
    reward, augmented_observation = self._preprocess_reward_observation(
        reward, observation)
    action_list = [
        base_agent.step(reward, augmented_observation)
        for base_agent in self._base_agents
    ]
    return self._postprocess_actions(action_list)

  def end_episode(self, reward, observation):
    super(SufficientStatisticsLayer, self).end_episode(reward, observation)
    self._reset()

  def _reset(self):
    """Resets the memory for a new user."""
    self._sufficient_statistics = None
