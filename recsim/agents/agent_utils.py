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
"""Convenience primitives relating to the implementation of agents."""
from gym import spaces
import numpy as np


class GymSpaceWalker(object):
  """Class for recursively applying a given function to a gym space.

  Gym spaces have nested structure in terms of container spaces (e.g. Dict and
  Tuple) containing basic spaces such as Discrete and Box. This class consumes a
  gym observation definition and a leaf operator is used to produce a flat list
  of the contents of the gym space, apply the leaf operator to all basic spaces
  in the proces. E.g., given a gym space of the form Tuple((Box(1), Box(1)) and
  a leaf operator f, this class can is used to transform an observation (a, b)
  to [f(a), f(b)].

  Args:
  gym_space: An instance of an OpenAI Gym space.
  leaf_op: A function taking as arguments an OpenAI Gym space and an observation
    conforming to that space. There are no requirements on its output.
  """

  def __init__(self, gym_space, leaf_op):
    self._gym_space = gym_space
    self._leaf_op = leaf_op

  def apply_and_flatten(self, gym_observations):
    return self._descend_and_flatten(self._gym_space, gym_observations)

  def _descend_and_flatten(self, gym_space, gym_observations):
    """Recursive implementation of flattening and leaf op application.

    Args:
      gym_space: An instance of an OpenAI Gym space.
      gym_observations: A list of observation conforming to the format
        of gym_space.

    Returns:
      flattened_apply: a list of the applications of leaf_op to the leaves of
        the gym space, as encountered in post-order traversal.
    """
    if isinstance(gym_space, spaces.dict.Dict):
      flattened_apply = []
      for key, space in gym_space.spaces.items():
        flattened_apply += self._descend_and_flatten(
            space,
            [gym_observation[key] for gym_observation in gym_observations])
    elif isinstance(gym_space, spaces.tuple.Tuple):
      flattened_apply = []
      for i, space in enumerate(gym_space.spaces):
        flattened_apply += self._descend_and_flatten(
            space, [gym_observation[i] for gym_observation in gym_observations])
    elif isinstance(gym_space, spaces.box.Box) or isinstance(
        gym_space, spaces.discrete.Discrete):
      return self._leaf_op(gym_space, gym_observations)
    else:
      raise NotImplementedError('Gym space type ' + str(type(gym_space)) +
                                ' not implemented yet.')
    return flattened_apply


def epsilon_greedy_exploration(state_action_iterator, q_function, epsilon):
  """Epsilon greedy exploration.

  Either picks a slate uniformly at random with probability epsilon, or returns
  a slate with maximal Q-value. TODO(mmladenov): more verbose doc.
  Args:
    state_action_iterator: an iterator over slate, state_action_index tuples.
    q_function: a container holding Q-values of state-action pairs.
    epsilon: probability of random action.
  Returns:
    slate: the picked slate.
    sa_index: the index of the picked slate in the Q-value table.
  """
  max_q_next = -np.Inf
  max_state_action_index = None
  max_slate = []
  random_state_action_index = None
  random_slate = []
  sa_index = None
  for slate_count, (slate, state_action_index) in enumerate(
      state_action_iterator, start=1):
    q_value = q_function.get(state_action_index, 0)
    if q_value > max_q_next:
      max_q_next = q_value
      max_state_action_index = state_action_index
      max_slate = slate
    # Pick a random action by reservoir sampling in order to avoid materializing
    # all possible slates.
    if slate_count == 1 or np.random.random() < 1.0 / (1.0 * slate_count):
      random_state_action_index = state_action_index
      random_slate = slate
  if np.random.random() <= epsilon:
    slate = random_slate
    sa_index = random_state_action_index
  else:
    slate = max_slate
    sa_index = max_state_action_index
  return slate, sa_index


def min_count_exploration(state_action_iterator, counts_function):
  """Minimum count exploration.

  Picks the state-action pair with minimum counts.
  Args:
    state_action_iterator: an iterator over slate, state_action_index tuples.
    counts_function: a container holding the number of times a state-action pair
      has been executed so far.
  Returns:
    slate: the picked slate.
    sa_index: the index of the picked slate in the counts table.
  """
  min_sa_count = np.Inf
  min_sa_count_slate = []
  min_sa_count_index = None
  for slate, state_action_index in state_action_iterator:
    sa_count = counts_function.get(state_action_index, 0)
    if sa_count < min_sa_count:
      min_sa_count_slate = slate
      min_sa_count_index = state_action_index
      min_sa_count = sa_count
    if sa_count == 0:
      break
  return min_sa_count_slate, min_sa_count_index
