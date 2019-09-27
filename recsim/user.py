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
"""Abstract classes that encode a user's state and dynamics."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc
from gym import spaces
import numpy as np


class AbstractResponse(object):  # pytype: disable=ignored-metaclass
  """Abstract class to model a user response."""

  __metaclass__ = abc.ABCMeta

  @staticmethod
  @abc.abstractmethod
  def response_space():
    """ArraySpec that defines how a single response is represented."""

  @abc.abstractmethod
  def create_observation(self):
    """Creates a tensor observation of this response."""


class AbstractUserState(object):  # pytype: disable=ignored-metaclass
  """Abstract class to represent a user's state."""
  __metaclass__ = abc.ABCMeta

  # Number of features to represent the user's interests.
  NUM_FEATURES = None

  @abc.abstractmethod
  def create_observation(self):
    """Generates obs of underlying state to simulate partial observability.

    Returns:
      obs: A float array of the observed user features.
    """

  @staticmethod
  @abc.abstractmethod
  def observation_space():
    """Gym.spaces object that defines how user states are represented."""


class AbstractUserSampler(object):  # pytype: disable=ignored-metaclass
  """Abstract class to sample users."""

  __metaclass__ = abc.ABCMeta

  def __init__(self, user_ctor, seed=0):
    """Creates a new user state sampler.

    User states of the type user_ctor are sampled.

    Args:
      user_ctor: A class/constructor for the type of user states that will be
        sampled.
      seed: An integer for a random seed.
    """
    self._user_ctor = user_ctor
    self._seed = seed
    self.reset_sampler()

  def reset_sampler(self):
    self._rng = np.random.RandomState(self._seed)

  @abc.abstractmethod
  def sample_user(self):
    """Creates a new instantiation of this user's hidden state parameters."""

  def get_user_ctor(self):
    """Returns the constructor/class of the user states that will be sampled."""
    return self._user_ctor


class AbstractUserModel(object):  # pytype: disable=ignored-metaclass
  """Abstract class to represent an encoding of a user's dynamics."""

  __metaclass__ = abc.ABCMeta

  def __init__(self, response_model_ctor, user_sampler, slate_size):
    """Initializes a new user model.

    Args:
      response_model_ctor: A class/constructor representing the type of
        responses this model will generate.
      user_sampler: An instance of AbstractUserSampler that can generate
        initial user states from an inital state distribution.
      slate_size: integer number of documents that can be served to the user at
        any interaction.
    """
    if not response_model_ctor:
      raise TypeError('response_model_ctor is a required callable')

    self._user_sampler = user_sampler
    self._user_state = self._user_sampler.sample_user()
    self._response_model_ctor = response_model_ctor
    self._slate_size = slate_size

  ## Transition model
  @abc.abstractmethod
  def update_state(self, slate_documents, responses):
    """Updates the user's state based on the slate and document selected.

    Args:
      slate_documents: A list of AbstractDocuments for items in the slate.
      responses: A list of AbstractResponses for each item in the slate.
    Updates: The user's hidden state.
    """

  def reset(self):
    """Resets the user."""
    self._user_state = self._user_sampler.sample_user()

  def reset_sampler(self):
    """Resets the sampler."""
    self._user_sampler.reset_sampler()

  @abc.abstractmethod
  def is_terminal(self):
    """Returns a boolean indicating whether this session is over."""

  ## Choice model
  @abc.abstractmethod
  def simulate_response(self, documents):
    """Simulates the user's response to a slate of documents.

    This could involve simulating models of attention, as well as random
    sampling for selection from scored documents.

    Args:
      documents: a list of AbstractDocuments

    Returns:
      (response) a list of AbstractResponse objects for each slate item
    """

  def response_space(self):
    res_space = self._response_model_ctor.response_space()
    return spaces.Tuple(tuple([
        res_space,
    ] * self._slate_size))

  def get_response_model_ctor(self):
    """Returns a constructor for the type of response this model will create."""
    return self._response_model_ctor

  def observation_space(self):
    """A Gym.spaces object that describes possible user observations."""
    return self._user_state.observation_space()

  def create_observation(self):
    """Emits obesrvation about user's state."""
    return self._user_state.create_observation()
