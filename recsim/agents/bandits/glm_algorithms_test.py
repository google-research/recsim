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
"""Tests for recsim.agents.bandits.glm_algorithm."""

import numpy as np
from recsim.agents.bandits import glm_algorithms
from scipy import special
import tensorflow.compat.v1 as tf


class UCB_GLMTest(tf.test.TestCase):  # pylint: disable=invalid-name

  def setUp(self):
    super(UCB_GLMTest, self).setUp()
    self._dim = 3
    self._alg = glm_algorithms.UCB_GLM(self._dim, horizon=100)

  def add_random_arms(self, n_arms):
    # Add some random arms with rewards
    for _ in range(n_arms):
      arm = np.random.uniform(size=self._alg._dim)
      reward = np.random.binomial(1, 0.5)  # Random reward
      self._alg.update(reward, arm)

  def test_update(self):
    n_arms = 10
    self.add_random_arms(n_arms)
    self.assertLen(self._alg._arms, n_arms)

  def test_arm_matrix(self):
    n_arms = 10
    arms = [np.random.uniform(size=self._dim) for _ in range(n_arms)]
    arm_matrix = self._alg.get_arm_matrix(arms)
    self.assertEqual(np.shape(arm_matrix), (n_arms, self._alg._dim))

  def test_solve_logistic_bandit(self):
    n_arms = 10
    self.add_random_arms(n_arms)
    w, gram = self._alg.solve_logistic_bandit()
    self.assertEqual(np.shape(w), (self._dim,))
    self.assertEqual(np.shape(gram), (self._dim, self._dim))

  def test_learning(self):
    # Construct a set of arms
    n_arms = 10
    arms = [np.random.uniform(size=self._dim) for _ in range(n_arms)]
    # Sample weight vector
    w_star = np.random.normal(size=self._dim)
    rounds = 20
    for _ in range(rounds):
      arm, arm_id, scores = self._alg.get_arm(arms)
      self.assertLess(arm_id, len(arms))
      self.assertLen(scores, len(arms))
      reward = np.random.binomial(1, special.expit(np.dot(arm, w_star)))
      self._alg.update(reward, arm)


class GLM_TSTest(tf.test.TestCase):  # pylint: disable=invalid-name

  def setUp(self):
    super(GLM_TSTest, self).setUp()
    self._dim = 3
    self._alg = glm_algorithms.GLM_TS(self._dim)

  def test_learning(self):
    # Construct a set of arms
    n_arms = 20
    arms = [np.random.uniform(size=self._dim) for _ in range(n_arms)]
    # Sample weight vector
    w_star = np.random.normal(size=self._dim)
    rounds = 10
    for _ in range(rounds):
      arm, arm_id, scores = self._alg.get_arm(arms)
      self.assertLess(arm_id, len(arms))
      self.assertLen(scores, len(arms))
      reward = np.random.binomial(1, special.expit(np.dot(arm, w_star)))
      self._alg.update(reward, arm)


if __name__ == '__main__':
  tf.test.main()
