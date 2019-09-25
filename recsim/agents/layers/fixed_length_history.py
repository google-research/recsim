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
"""Helper classe to record fixed length history of observations."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from gym import spaces

from recsim.agents.layers import sufficient_statistics


class FixedLengthHistoryLayer(sufficient_statistics.SufficientStatisticsLayer):
  r"""Creates a buffer of the last k rewards and observations.

  This module introduces sufficient statistics in the form of a buffer holding
  the last k (specified by history_length) observations. This buffer is injected
  into observation_space[\'user\'][\'sufficient_statistics\'] in the form of a
  gym.spaces.Tuple of length up to k . In the first k-1 steps of the episode
  there are not enough observations to fill the buffer, so they will be filled
  with None. Each non-vacuous element of the tuple is an instance of
  (a subset of) observation_space.
  """

  def __init__(self,
               base_agent_ctor,
               observation_space,
               action_space,
               history_length,
               remember_user=True,
               remember_response=True,
               remember_doc=False,
               **kwargs):
    r"""Initializes a FixedLengthHistoryLayer object.

    Args:
      base_agent_ctor: a constructor for the base agent.
      observation_space: a gym.spaces object specifying the format of
        observations.
      action_space: A gym.spaces object that specifies the format of actions.
      history_length: positive integer number of observations to remember.
      remember_user: boolean, indicates whether to track
        observation_space[\'user\'].
      remember_response: boolean, indicates whether to track
        observation_space[\'response\'].
      remember_doc: boolean, indicates whether to track
        observation_space[\'doc\'].
      **kwargs: arguments to pass to the downstream agent at construction time.
    """

    self._history_length = history_length
    self._features = []
    if remember_user:
      self._features.append('user')
    if remember_response:
      self._features.append('response')
    if remember_doc:
      self._features.append('doc')
    observation_space_to_remember = spaces.Dict({
        feature: observation_space[feature] for feature in self._features
    })
    suf_stat_space = spaces.Tuple([
        observation_space_to_remember,
    ] * history_length)
    super(FixedLengthHistoryLayer,
          self).__init__(base_agent_ctor, observation_space, action_space,
                         suf_stat_space, **kwargs)

  def _create_observation(self):
    return tuple(self._sufficient_statistics)

  def _update(self, observation):
    """Updates user impression/click count given user response on each item."""
    if self._sufficient_statistics is None:
      self._sufficient_statistics = self._history_length * [
          None,
      ]

    observation_to_remember = {
        feature: observation[feature] for feature in self._features
    }
    self._sufficient_statistics = [
        observation_to_remember,
    ] + self._sufficient_statistics[:-1]
