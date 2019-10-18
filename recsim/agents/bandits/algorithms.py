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
"""Classes for Bandit Algorithms."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import numpy as np


class MABAlgorithm(object):
  """Base class for Multi-armed bandit (MAB) algorithms.

  We implement multi-armed bandit algorithms with confidence width tuning
  proposed in Hsu et al. https://arxiv.org/abs/1904.02664.

  Attributes:
    pulls: A numpy array which counts number of pulls of each arm
    reward: A numpy array which sums up reward of each arm
    optimism_scaling: A float specifying the confidence level. Default value
      (1.0) corresponds to the exploration strategy presented in the literature.
      A smaller number means less exploration and more exploitation.
    _rng: An instance of random.RandomState for random number generation
  """

  def __init__(self, num_arms, params, seed=0):
    """Initializes MABAlgorithm.

    Args:
      num_arms: Number of arms. Must be greater than one.
      params: A dictionary which includes additional parameters like
        optimism_scaling. Default is an empty dictionary.
      seed: Random seed for this object. Default is zero.
    """
    if num_arms < 2:
      raise ValueError('num_arms must be greater than one.')
    self.pulls = np.zeros(num_arms)
    self.reward = np.zeros(num_arms)
    self._rng = np.random.RandomState(seed)

    self.optimism_scaling = 1.0
    for attr, val in params.items():
      setattr(self, attr, val)

  def set_state(self, pulls, reward):
    if len(pulls) != len(self.pulls) or len(reward) != len(self.reward):
      raise ValueError('Cannot set state with a different number of arms.')
    self.pulls[:] = pulls
    self.reward[:] = reward

  def update(self, arm, reward):
    if reward < 0 or reward > 1:
      raise ValueError('reward must be in [0, 1].')
    self.pulls[arm] += 1
    self.reward[arm] += reward


class UCB1(MABAlgorithm):
  """UCB1 algorithm.

  See "Finite-time Analysis of the Multiarmed Bandit Problem" by Auer,
  Cesa-Bianchi, and Fischer.
  """

  def get_score(self, t):
    """Computes upper confidence bounds of reward / pulls at round t."""
    # Pull any arm that we haven't pulled.
    if not all(self.pulls):
      return np.where(self.pulls > 0, 0, np.Inf)
    ct = self.optimism_scaling * np.sqrt(2 * np.log(t))
    return self.reward / self.pulls + ct * np.sqrt(1 / self.pulls)

  def get_arm(self, t):
    return np.argmax(self.get_score(t))

  @staticmethod
  def print():
    return 'UCB1'


class KLUCB(MABAlgorithm):
  """Kullback-Leibler Upper Confidence Bounds (KL-UCB) algorithm.

  See "The KL-UCB algorithm for bounded stochastic bandits and beyond" by
  Garivier and Cappe.
  """

  def get_score(self, t):
    """Computes upper confidence bounds of reward / pulls at round t."""
    # Pull any arm that we haven't pulled.
    if not all(self.pulls):
      return np.where(self.pulls > 0, 0, np.Inf)
    c = self.optimism_scaling**2 * (np.log(t) +
                                    3 * np.log(np.log(t))) / self.pulls
    p = self.reward / self.pulls

    # KL-divergence d(p, q) is strictly increasing over [p, 1].
    # Use binary search to find q such that d(p, q) <= c.
    qmin = p
    qmax = np.ones(p.size)
    for _ in range(16):  # Error bounded by 2^-16.
      q = (qmax + qmin) / 2
      ndx = (np.where(p > 0, p * np.log(p / q), 0) +
             np.where(p < 1, (1 - p) * np.log((1 - p) / (1 - q)), 0)) < c
      qmin[ndx] = q[ndx]
      qmax[~ndx] = q[~ndx]

    return q

  def get_arm(self, t):
    return np.argmax(self.get_score(t))

  @staticmethod
  def print():
    return 'KL-UCB'


class ThompsonSampling(MABAlgorithm):
  """Thompson Sampling algorithm for the Bernoulli bandit.

  See "Further Optimal Regret Bounds for Thompson Sampling" by Agrawal and
    Goyal.
  """

  def update(self, arm, reward):
    if reward > 0 and reward < 1:
      reward = float(self._rng.rand() < reward)
    MABAlgorithm.update(self, arm, reward)

  def get_score(self, t):
    """Samples scores from the posterior distribution."""
    del t
    # Generate a beta distribution based on the expectation of reward.
    alpha = 1 + self.reward / self.optimism_scaling**2
    beta = 1 + (self.pulls - self.reward) / self.optimism_scaling**2
    return self._rng.beta(alpha, beta)

  def get_arm(self, t):
    return np.argmax(self.get_score(t))

  @staticmethod
  def print():
    return 'ThompsonSampling'
