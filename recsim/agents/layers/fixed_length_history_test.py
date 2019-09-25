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
"""Tests for recsim.agents.layers.fixed_length_history."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from gym import spaces
import mock
from recsim.agents import cluster_bandit_agent
from recsim.agents.layers import fixed_length_history
import tensorflow as tf


class FixedLengthHistoryTest(tf.test.TestCase):

  def setUp(self):
    self.history_length = 3
    self.slate_size = 1
    super(FixedLengthHistoryTest, self).setUp()
    self.test_action_space = mock.Mock(nvec=mock.Mock(shape=[2,]))
    self.test_observation_space = spaces.Dict({
        'user': spaces.Discrete(2),
        'response': spaces.Discrete(3),
        'doc': spaces.Tuple((spaces.Discrete(4),))
    })
    self.mock_agent = mock.create_autospec(
        cluster_bandit_agent.ClusterBanditAgent)
    self.history = fixed_length_history.FixedLengthHistoryLayer(
        self.mock_agent,
        self.test_observation_space,
        self.test_action_space,
        self.history_length,
        remember_user=True,
        remember_response=True,
        remember_doc=True,
        kwarg_for_agent=-1)

  def test_initialization(self):
    # Basic object properties initialized correctly.
    self.assertEqual(self.history._history_length, self.history_length)
    self.assertCountEqual(self.history._features, ['user', 'doc', 'response'])
    # Base agent got constructed correctly.
    self.mock_agent.assert_called_once()
    mock_agent_args, mock_agent_kwargs = self.mock_agent.call_args
    self.assertEmpty(mock_agent_args)
    self.assertCountEqual(
        mock_agent_kwargs.keys(),
        ['observation_space', 'action_space', 'kwarg_for_agent'])
    # Environment features and kwargs are passed down to base agent.
    self.assertEqual(mock_agent_kwargs['action_space'], self.test_action_space)
    self.assertEqual(mock_agent_kwargs['kwarg_for_agent'], -1)
    # Augmented observation is space properly formatted.
    augmented_observation_space = mock_agent_kwargs['observation_space']
    for field in ['doc', 'response']:
      self.assertEqual(augmented_observation_space.spaces[field],
                       self.test_observation_space[field])
    self.assertCountEqual(
        augmented_observation_space.spaces['user'].spaces.keys(),
        ['raw_observation', 'sufficient_statistics'])
    self.assertEqual(
        augmented_observation_space.spaces['user']['raw_observation'],
        self.test_observation_space['user'])
    self.assertLen(
        augmented_observation_space.spaces['user']
        .spaces['sufficient_statistics'].spaces, self.history_length)
    for space in (augmented_observation_space.spaces['user']
                  .spaces['sufficient_statistics'].spaces):
      self.assertEqual(space, self.test_observation_space)

  def test_update_and_observation(self):
    observation = self.test_observation_space.sample()
    self.assertIsNone(self.history._sufficient_statistics)
    self.history._update(observation)
    self.assertEqual(self.history._sufficient_statistics,
                     [observation, None, None])
    self.assertEqual(self.history._create_observation(),
                     (observation, None, None))

if __name__ == '__main__':
  tf.test.main()
