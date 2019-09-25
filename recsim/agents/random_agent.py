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
"""A simple recommender system agent that recommends random slates."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from absl import logging

import numpy as np

from recsim import agent


class RandomAgent(agent.AbstractEpisodicRecommenderAgent):
  """An agent that recommends a random slate of documents."""

  def __init__(self, action_space, random_seed=0):
    super(RandomAgent, self).__init__(action_space)
    self._rng = np.random.RandomState(random_seed)

  def step(self, reward, observation):
    """Records the most recent transition and returns the agent's next action.

    We store the observation of the last time step since we want to store it
    with the reward.

    Args:
      reward: Unused.
      observation: A dictionary that includes the most recent observation.
        Should include 'doc' field that includes observation of all candidates.

    Returns:
      slate: An integer array of size _slate_size, where each element is an
        index into the list of doc_obs
    """
    del reward  # Unused argument.
    doc_obs = observation['doc']

    # Simulate a random slate
    doc_ids = list(range(len(doc_obs)))
    self._rng.shuffle(doc_ids)
    slate = doc_ids[:self._slate_size]
    logging.debug('Recommended slate: %s', slate)
    return slate
