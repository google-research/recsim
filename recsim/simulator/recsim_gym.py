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
"""A wrapper for using Gym environment."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import gym
from gym import spaces
import numpy as np


def _dummy_metrics_aggregator(responses, metrics, info):
  del responses  # Unused.
  del metrics  # Unused.
  del info  # Unused.
  return


def _dummy_metrics_writer(metrics, add_summary_fn):
  del metrics  # Unused.
  del add_summary_fn  # Unused.
  return


class RecSimGymEnv(gym.Env):
  """Class to wrap recommender system environment to gym.Env.

  Attributes:
    game_over: A boolean indicating whether the current game has finished
    action_space: A gym.spaces object that specifies the space for possible
      actions.
    observation_space: A gym.spaces object that specifies the space for possible
      observations.
  """

  def __init__(self,
               raw_environment,
               reward_aggregator,
               metrics_aggregator=_dummy_metrics_aggregator,
               metrics_writer=_dummy_metrics_writer):
    """Initializes a RecSim environment conforming to gym.Env.

    Args:
      raw_environment: A recsim recommender system environment.
      reward_aggregator: A function mapping a list of responses to a number.
      metrics_aggregator: A function aggregating metrics over all steps given
        responses and response_names.
      metrics_writer:  A function writing final metrics to TensorBoard.
    """
    self._environment = raw_environment
    self._reward_aggregator = reward_aggregator
    self._metrics_aggregator = metrics_aggregator
    self._metrics_writer = metrics_writer
    self.reset_metrics()

  @property
  def environment(self):
    """Returns the recsim recommender system environment."""
    return self._environment

  @property
  def game_over(self):
    return False

  @property
  def action_space(self):
    """Returns the action space of the environment.

    Each action is a vector that specified document slate. Each element in the
    vector corresponds to the index of the document in the candidate set.
    """
    return spaces.MultiDiscrete(self._environment.num_candidates * np.ones(
        (self._environment.slate_size,)))

  @property
  def observation_space(self):
    """Returns the observation space of the environment.

    Each observation is a dictionary with three keys `user`, `doc` and
    `response` that includes observation about user state, document and user
    response, respectively.
    """
    return spaces.Dict({
        'user': self._environment.user_model.observation_space(),
        'doc': self._environment.candidate_set.observation_space(),
        'response': self._environment.user_model.response_space(),
    })

  def step(self, action):
    """Runs one timestep of the environment's dynamics.

    When end of episode is reached, you are responsible for calling `reset()`
    to reset this environment's state. Accepts an action and returns a tuple
    (observation, reward, done, info).

    Args:
      action (object): An action provided by the environment

    Returns:
      A four-tuple of (observation, reward, done, info) where:
        observation (object): agent's observation that include
          1. User's state features
          2. Document's observation
          3. Observation about user's slate responses.
        reward (float) : The amount of reward returned after previous action
        done (boolean): Whether the episode has ended, in which case further
          step() calls will return undefined results
        info (dict): Contains responses for the full slate for
          debugging/learning.
    """
    user_obs, doc_obs, responses, done = self._environment.step(action)
    obs = dict(
        user=user_obs,
        doc=doc_obs,
        response=tuple(
            response.create_observation() for response in responses))

    # extract rewards from responses
    reward = self._reward_aggregator(responses)
    info = self.extract_env_info()
    return obs, reward, done, info

  def reset(self):
    user_obs, doc_obs = self._environment.reset()
    return dict(user=user_obs, doc=doc_obs, response=None)

  def reset_sampler(self):
    self._environment.reset_sampler()

  def render(self, mode='human'):
    raise NotImplementedError

  def close(self):
    raise NotImplementedError

  def seed(self, seed=None):
    np.random.seed(seed=seed)

  def extract_env_info(self):
    info = {'env': self._environment}
    return info

  def reset_metrics(self):
    """Resets every metric to zero.

    We reset metrics for every iteration but not every episode. On the other
    hand, reset() gets called for every episode.
    """
    self._metrics = collections.defaultdict(float)

  def update_metrics(self, responses, info=None):
    """Updates metrics with one step responses."""
    self._metrics = self._metrics_aggregator(
        responses, self._metrics, info)

  def write_metrics(self, add_summary_fn):
    """Writes metrics to TensorBoard by calling add_summary_fn."""
    self._metrics_writer(self._metrics, add_summary_fn)
