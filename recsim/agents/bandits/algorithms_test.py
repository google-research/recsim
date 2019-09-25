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
"""Tests for recsim.agents.bandits.algorithm."""

import numpy as np
from recsim.agents.bandits import algorithms
import tensorflow as tf


class UCB1Test(tf.test.TestCase):

  def setUp(self):
    super(UCB1Test, self).setUp()
    self._alg = algorithms.UCB1(2, {})
    self._alg.set_state(np.array([10, 10]), np.array([10, 0]))

  def test_get_score(self):
    ucb = self._alg.get_score(20)
    self.assertAlmostEqual(1.7740455, ucb[0])
    self.assertAlmostEqual(0.7740455, ucb[1])

  def test_get_arm(self):
    # Arm 0 is clearly the best.
    self.assertEqual(0, self._alg.get_arm(20))

  def test_get_arm_initial_stage(self):
    alg = algorithms.UCB1(3, {})
    alg.update(0, 1)
    alg.update(2, 1)
    # Pull Arm 1 which has not been pulled.
    self.assertEqual(1, alg.get_arm(1))


class KLUCBTest(tf.test.TestCase):

  def setUp(self):
    super(KLUCBTest, self).setUp()
    self._alg = algorithms.KLUCB(2, {})
    self._alg.set_state(np.array([10, 10]), np.array([10, 0]))

  def test_get_score(self):
    ucb = self._alg.get_score(20)
    self.assertAlmostEqual(1, ucb[0])
    self.assertAlmostEqual(0.5 - 2**-16, ucb[1])

  def test_get_arm(self):
    # Arm 0 is clearly the best.
    self.assertEqual(0, self._alg.get_arm(20))

  def test_get_arm_initial_stage(self):
    alg = algorithms.KLUCB(3, {})
    alg.update(0, 1)
    alg.update(2, 1)
    # Pull Arm 1 which has not been pulled.
    self.assertEqual(1, alg.get_arm(1))


class ThompsonSamplingTest(tf.test.TestCase):

  def setUp(self):
    super(ThompsonSamplingTest, self).setUp()
    self._alg = algorithms.ThompsonSampling(2, {})
    self._alg.set_state(np.array([10, 10]), np.array([10, 0]))

  def test_update(self):
    self._alg.update(0, 0.9)
    self._alg.update(1, 0)
    self.assertAllEqual(np.array([11, 11]), self._alg.pulls)
    self.assertAllEqual(np.array([11, 0]), self._alg.reward)

  def test_get_score(self):
    mu = self._alg.get_score(20)
    self.assertAlmostEqual(0.9570183, mu[0])
    self.assertAlmostEqual(0.0438080, mu[1])

  def test_get_arm(self):
    # Arm 0 is clearly the best.
    self.assertEqual(0, self._alg.get_arm(20))


if __name__ == '__main__':
  tf.test.main()
