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
"""Tests for recsim.agents.layers.cluster_click_statistics."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from gym import spaces
import mock
import numpy as np
from recsim.agents import cluster_bandit_agent
from recsim.agents.layers import cluster_click_statistics
import tensorflow as tf


class ClusterClickStatisticsTest(tf.test.TestCase):

  def setUp(self):
    self.slate_size = 2
    self.num_clusters = 2
    super(ClusterClickStatisticsTest, self).setUp()
    self.test_action_space = mock.Mock(nvec=mock.Mock(shape=[
        2,
    ]))
    single_response_space = spaces.Dict({
        'click': spaces.Discrete(2),
        'cluster_id': spaces.Discrete(self.num_clusters)
    })

    self.test_observation_space = spaces.Dict({
        'user':
            spaces.Discrete(2),
        'response':
            spaces.Tuple(tuple([
                single_response_space,
            ] * self.slate_size)),
        'doc':
            spaces.Tuple((spaces.Discrete(4),))
    })
    self.mock_agent = mock.create_autospec(
        cluster_bandit_agent.ClusterBanditAgent)
    self.click_stats = cluster_click_statistics.ClusterClickStatsLayer(
        self.mock_agent,
        self.test_observation_space,
        self.test_action_space,
        kwarg_for_agent=-1)

  def test_initialization(self):
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
    suff_stat_space = spaces.Dict({
        'impression_count':
            spaces.Box(
                shape=(self.num_clusters,),
                dtype=np.float32,
                low=0.0,
                high=np.inf),
        'click_count':
            spaces.Box(
                shape=(self.num_clusters,),
                dtype=np.float32,
                low=0.0,
                high=np.inf)
    })
    self.assertEqual(
        augmented_observation_space.spaces['user']['sufficient_statistics'],
        suff_stat_space)

  def test_update_and_observation(self):
    observation = {'response': None}
    self.click_stats._update(observation)
    observation = {
        'response': ({
            'click': 1,
            'cluster_id': 0
        }, {
            'click': 0,
            'cluster_id': 1
        })
    }
    self.click_stats._update(observation)
    observation = {
        'response': ({
            'click': 0,
            'cluster_id': 0
        }, {
            'click': 1,
            'cluster_id': 1
        })
    }
    self.click_stats._update(observation)
    obs = self.click_stats._create_observation()
    self.assertAllEqual(obs['impression_count'], np.array([2, 2]))
    self.assertAllEqual(obs['click_count'], np.array([1, 1]))


if __name__ == '__main__':
  tf.test.main()
