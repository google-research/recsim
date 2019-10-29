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
"""Recsim-specific Dopamine DQN agent and related utilities."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections

from dopamine.agents.dqn import dqn_agent
from dopamine.replay_memory import circular_replay_buffer
import gin.tf
from gym import spaces
import numpy as np
import tensorflow as tf

DQNNetworkType = collections.namedtuple('dqn_network', ['q_values'])


class ResponseAdapter(object):
  """Custom flattening of responses to accommodate dopamine replay buffer."""

  def __init__(self, input_response_space):
    """Init function for ResponseAdapter.

    Args:
      input_response_space: this is assumed to be an instance of
        gym.spaces.Tuple; each element of the tuple is has to be an instance
        of gym.spaces.Dict consisting of feature_name: 0-d gym.spaces.Box
          (single float) key-value pairs.
    """
    self._input_response_space = input_response_space
    self._single_response_space = input_response_space.spaces[0]
    self._response_names = list(self._single_response_space.spaces.keys())
    self._response_shape = (len(input_response_space.spaces),
                            len(self._response_names))
    self._response_dtype = np.float32

  @property
  def response_names(self):
    return self._response_names

  @property
  def response_shape(self):
    return self._response_shape

  @property
  def response_dtype(self):
    return self._response_dtype

  def encode(self, responses):
    response_tensor = np.zeros(self._response_shape, dtype=self._response_dtype)
    for i, response in enumerate(responses):
      # Note: the order of dictionary keys in the self._input_response_space is
      # not necessarily the same as the order of the keys in the observation
      # dictionary itself. To guarrantee the position of elements are consistent
      # with the order in self._response_names, we iterate over keys explicitly.
      for j, key in enumerate(self.response_names):
        response_tensor[i, j] = response[key]
    return response_tensor


@gin.configurable
class ObservationAdapter(object):
  """An adapter to convert between user/doc observation and images."""

  def __init__(self, input_observation_space, stack_size=1):
    self._input_observation_space = input_observation_space
    user_space = input_observation_space.spaces['user']
    doc_space = input_observation_space.spaces['doc']
    self._num_candidates = len(doc_space.spaces)

    doc_space_shape = spaces.flatdim(list(doc_space.spaces.values())[0])
    # Use the longer of user_space and doc_space as the shape of each row.
    obs_shape = (np.max([spaces.flatdim(user_space), doc_space_shape]),)
    self._observation_shape = (self._num_candidates + 1,) + obs_shape
    self._observation_dtype = user_space.dtype
    self._stack_size = stack_size

  # Pads an array with zeros to make its shape identical to  _observation_shape.
  def _pad_with_zeros(self, array):
    width = self._observation_shape[1] - len(array)
    return np.pad(array, (0, width), mode='constant')

  @property
  def output_observation_space(self):
    """The output observation space of the adapter."""
    user_space = self._input_observation_space.spaces['user']
    doc_space = self._input_observation_space.spaces['doc']
    user_dim = spaces.flatdim(user_space)
    low = np.concatenate(
        [self._pad_with_zeros(np.ones(user_dim) * -np.inf).reshape(1, -1)] + [
            self._pad_with_zeros(np.ones(spaces.flatdim(d)) *
                                 -np.inf).reshape(1, -1)
            for d in doc_space.spaces.values()
        ])
    high = np.concatenate(
        [self._pad_with_zeros(np.ones(user_dim) * np.inf).reshape(1, -1)] + [
            self._pad_with_zeros(np.ones(spaces.flatdim(d)) *
                                 np.inf).reshape(1, -1)
            for d in doc_space.spaces.values()
        ])
    return spaces.Box(low=low, high=high, dtype=np.float32)

  def encode(self, observation):
    """Encode user observation and document observations to an image."""
    # It converts the observation from the simulator to a numpy array to be
    # consumed by DQN agent, which assume the input is a "image".
    # The first row is user's observation. The remaining rows are documents'
    # observation, one row for each document.
    image = np.zeros(
        self._observation_shape + (self._stack_size,),
        dtype=self._observation_dtype)
    image[0, :, 0] = self._pad_with_zeros(
        spaces.flatten(self._input_observation_space.spaces['user'],
                       observation['user']))
    doc_space = zip(self._input_observation_space.spaces['doc'].spaces.values(),
                    observation['doc'].values())
    image[1:, :, 0] = np.array([
        self._pad_with_zeros(spaces.flatten(doc_space, d))
        for doc_space, d in doc_space
    ])

    return image


# The following functions creates the DQN network for RecSim.
def recsim_dqn_network(user, doc, scope):
  inputs = tf.concat([user, doc], axis=1)
  with tf.compat.v1.variable_scope(scope, reuse=tf.compat.v1.AUTO_REUSE):
    hidden = tf.compat.v1.layers.dense(inputs, 256, activation=tf.nn.relu)
    hidden = tf.compat.v1.layers.dense(hidden, 32, activation=tf.nn.relu)
    q_value = tf.compat.v1.layers.dense(hidden, 1, name='output')
  return q_value


class DQNAgentRecSim(dqn_agent.DQNAgent):
  """RecSim-specific Dopamine DQN agent that converts the observation space."""

  def __init__(self, sess, observation_space, num_actions, stack_size,
               optimizer_name, eval_mode, **kwargs):
    if stack_size != 1:
      raise ValueError(
          'Invalid stack_size: %s. Only stack_size=1 is supported for now.' %
          stack_size)

    self._env_observation_space = observation_space
    # In our case, the observation is a data structure that stores observation
    # of the user and candidate documents. We uses an observation adapter to
    # convert it to an "image", which is required by dopamine DQNAgent.
    self._obs_adapter = ObservationAdapter(self._env_observation_space)

    if optimizer_name == 'adam':
      optimizer = tf.compat.v1.train.AdamOptimizer()
    elif optimizer_name == 'sgd':
      optimizer = tf.compat.v1.train.GradientDescentOptimizer(
          learning_rate=1e-3)
    else:
      optimizer = tf.compat.v1.train.RMSPropOptimizer(
          learning_rate=0.00025,
          decay=0.95,
          momentum=0.0,
          epsilon=0.00001,
          centered=True)

    dqn_agent.DQNAgent.__init__(
        self,
        sess,
        num_actions,
        observation_shape=self._obs_adapter.output_observation_space.shape,
        observation_dtype=self._obs_adapter.output_observation_space.dtype,
        stack_size=stack_size,
        network=recsim_dqn_network,
        optimizer=optimizer,
        eval_mode=eval_mode,
        **kwargs)

  def _validate_states(self, states):
    shape = states.get_shape()
    if len(shape) != 4 or shape[1] != self._num_candidates + 1:
      raise ValueError('Invalid states shape: %s. '
                       'Expecting [batch_size, %s, num_features, stack_size].' %
                       (shape, self._num_candidates + 1))


def wrapped_replay_buffer(**kwargs):
  return circular_replay_buffer.WrappedReplayBuffer(**kwargs)
