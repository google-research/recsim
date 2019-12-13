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
"""Classes for Bandit Algorithms for Generalized Linear Models."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import abc
import numpy as np
from scipy import special
import six


@six.add_metaclass(abc.ABCMeta)
class GLMAlgorithm(object):
  """Base class for Generalized Linear Models (GLM) bandit algorithms.

  In this setting each arm is represented by a feature vector x and there exists
  an unknown weight vector w*. In each round the algorithm pulls an arm and gets
  a noisy reward, which is assumed to be the result of composing the dot product
  x.w* with a link function, plus random noise. For example,
  sigmoid(x.w*) + eps, where eps is sub-Gaussian noise.

  Attributes:
    arms: the arms pulled so far
    rewards: the rewards observed so far
    dim: the dimension of the feature/weight vectors
    outer: the sum of outer products of the arms pulled so far (x.x^T)
    sigma0: a parameter scaling the identity matrix used for making the
      resulting Gram matrix positive definite.
    optimism_scaling: A float specifying the confidence level. Default value
      (1.0) corresponds to the exploration strategy presented in the literature.
      A smaller number means less exploration and more exploitation.
    _rng: An instance of random.RandomState for random number generation
  """

  def __init__(self, dim, sigma0=1., optimism_scaling=1.):
    self._rewards = np.array([])  # stores all rewards
    self._arms = np.ndarray([0, dim])  # stores arm differences
    self._dim = dim
    self._outer = np.zeros([dim, dim])
    self._sigma0 = sigma0
    self._optimism_scaling = optimism_scaling

  def update(self, reward, arm):
    """Updates state with arm and reward.

    Args:
      reward: the reward received
      arm: the arm that was pulled
    """
    assert len(arm) == self._dim, 'Expected dimension {}, got {}'.format(
        self._dim, len(arm))
    self._rewards = np.append(self._rewards, reward)
    self._arms = np.concatenate((self._arms, [arm]), axis=0)
    self._outer += np.outer(arm, arm)

  def solve_logistic_bandit(self, init_iters=10, num_iters=20, tol=1e-3):
    """Solves the maximum-likelihood problem.

    Implements iterative reweighted least squares for Bayesian logistic
    regression. See sections 4.3.3 and 4.5.1 in Pattern Recognition and Machine
    Learning, Bishop (2006)

    Args:
      init_iters: number of initial iterations to skip (returns zeros)
      num_iters: number of least squares iterations
      tol: tolerance level of change in solution between iterations before
        terminating
    Returns:
      w: maximum likelihood solution
      gram: Gram matrix
    """

    arms = self._arms
    w = np.zeros(self._dim)
    gram = np.eye(self._dim) / np.square(self._sigma0)
    if len(self._arms) > init_iters:
      for _ in range(num_iters):
        prev_w = np.copy(w)
        arms_w = arms.dot(w)
        sig_arms_w = special.expit(arms_w)
        r = np.diag(sig_arms_w * (1 - sig_arms_w))
        gram = (((arms.T).dot(r)).dot(arms) +
                np.eye(self._dim) / np.square(self._sigma0))
        rz = r.dot(arms_w) - (sig_arms_w - self._rewards)
        w = np.linalg.solve(gram, (arms.T).dot(rz))
        if np.linalg.norm(w - prev_w) < tol:
          break

    return w, gram

  def get_arm_matrix(self, arms):
    """Puts all arms into a matrix."""
    return np.stack(arms, axis=0)

  @abc.abstractmethod
  def get_arm(self, arms):
    """Computes which arm to pull next.

    Args:
      arms: a list of feature vectors, one for each arm

    Returns:
      arm: the chosen arm
      arm_ind: index of the chosen arm
      scores: an array with arm scores
    """


class UCB_GLM(GLMAlgorithm):  # pylint: disable=invalid-name
  """UCB-GLM algorithm.

  See "Provably Optimal Algorithms for Generalized Linear Contextual Bandits",
  by Li et al. (2017).
  """

  def __init__(self, dim, horizon, sigma0=1., optimism_scaling=1.):
    super(UCB_GLM, self).__init__(dim, sigma0, optimism_scaling)
    # Set confidence interval scaling, by
    # Theorem 2 in Li (2017)
    # Provably Optimal Algorithms for Generalized Linear Contextual Bandits
    crs = optimism_scaling  # confidence region scaling
    delta = 1. / float(horizon)
    sigma = 0.5
    kappa = 0.25
    # Confidence ellipsoid width (cew):
    cew = (sigma / kappa) * (np.sqrt((self._dim / 2) *
                                     np.log(1. + 2. * horizon / self._dim) +
                                     np.log(1 / delta)))
    self._ci_scaling = crs * cew

  def get_arm(self, arms):
    """Computes which arm to pull next.

    Args:
      arms: a list of feature vectors, one for each arm
    Returns:
      The selected arm, its index in arms, and the computed scores
    """
    arm_matrix = self.get_arm_matrix(arms)
    gram = self._outer + np.eye(self._dim) / np.square(self._sigma0)
    gram_inv = np.linalg.inv(gram)
    ucbs = np.sqrt((np.matmul(arm_matrix, gram_inv) * arm_matrix).sum(axis=1))
    # Estimate w
    w, _ = self.solve_logistic_bandit()
    # Compute UCB
    mu = np.matmul(arm_matrix, w) + self._ci_scaling * ucbs
    arm = np.random.choice(np.flatnonzero(mu == mu.max()))

    return arms[arm], arm, mu

  @staticmethod
  def print():
    return 'GLM-UCB'


class GLM_TS(GLMAlgorithm):  # pylint: disable=invalid-name
  """Thompson sampling algorithm for generalized linear models.

  See "Linear Thompson Sampling Revisited" by Abeille and Lazaric (2017).
  """

  def get_arm(self, arms):
    """Computes which arm to pull next.

    Args:
      arms: a list of feature vectors, one for each arm
    Returns:
      The selected arm, its index in arms, and the computed scores
    """
    arm_matrix = self.get_arm_matrix(arms)
    w, gram = self.solve_logistic_bandit()
    gram_inv = np.square(self._optimism_scaling) * np.linalg.inv(gram)

    # Posterior sampling
    w_tilde = np.random.multivariate_normal(w, gram_inv)
    mu = np.matmul(arm_matrix, w_tilde)
    # Argmax breaking ties randomly
    arm = np.random.choice(np.flatnonzero(mu == mu.max()))

    return arms[arm], arm, mu

  @staticmethod
  def print():
    return 'GLM-TS'
