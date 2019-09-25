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
import tensorflow as tf


class InterestExplorationTest(tf.test.TestCase):

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


if __name__ == '__main__':
  tf.test.main()
