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
"""Tests for recsim.environments.interest_exploration."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import numpy as np
from recsim.environments import interest_exploration
from recsim.choice_model import DependentClickModel
from recsim.agents.random_agent import RandomAgent


import recsim.testing.test_base as test_base


class InterestExplorationTest(test_base.TestCase):

  def setUp(self):
    super(InterestExplorationTest, self).setUp()
    self._num_topics = 2
    env_config = {
        'num_candidates': 20,
        'slate_size': 2,
        'resample_documents': False,
        'seed': 1,
    }
    self._env = interest_exploration.create_environment(env_config)

  def test_step(self):
    self._env.seed(0)
    obs0 = self._env.reset()
    self.assertEqual((0,), obs0['user'].shape)
    slate = np.array([0, 1])
    obs, reward, done, _ = self._env.step(slate)
    doc_obs0 = list(obs0['doc'].values())
    doc_obs = list(obs['doc'].values())
    for i, resp in enumerate(obs['response']):
      self.assertFalse(resp['click'])
      self.assertEqual(doc_obs0[i]['cluster_id'], resp['cluster_id'])
      self.assertEqual(doc_obs[i]['cluster_id'], resp['cluster_id'])
    self.assertEqual(0, reward)
    self.assertFalse(done)


class InterestExplorationDCMTest(test_base.TestCase):

  def setUp(self):
    super(InterestExplorationDCMTest, self).setUp()
    seed = 100
    np.random.seed(seed)
    choice_model = DependentClickModel(
      slate_size=3, next_probs=[0.8, 0.7, 0.6],score_scaling=0.2)
    self._env = interest_exploration.create_multiclick_environment(
      {'slate_size': 3, 'seed': seed, 'num_candidates': 15, 'resample_documents': True},
      choice_model
    )
    self._agent = RandomAgent(self._env.action_space, random_seed=seed)

  def test_multiple_clicks(self):
    observation = self._env.reset()
    action = self._agent.step(0, observation)
    self.assertAllEqual(action, [9, 1, 12])
    observation, reward, terminal, info = self._env.step(action)
    self.assertAlmostEqual(reward, 2.0)
    click_indices = [
      doc_resp['click'] for doc_resp in observation['response']]
    self.assertAllEqual(click_indices, [1, 1, 0])


if __name__ == '__main__':
  test_base.main()
