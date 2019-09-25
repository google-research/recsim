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
"""Agent that picks topics based on the UCB1 algorithm given past responses."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import functools

import gin
import numpy as np
from recsim import agent
from recsim.agents.bandits import algorithms
from recsim.agents.layers import abstract_click_bandit


@gin.configurable
class ClusterBanditAgent(abstract_click_bandit.AbstractClickBanditLayer):
  """An agent that recommends items with the highest UCBs of topic affinities.

  This agent assumes no knowledge of user's affinity for each topic but receives
  observations of user's past responses for each topic. When creating a slate,
  it utilizes a bandit algorithm to pick the best topics. Within the same best
  topic, we pick documents with the best document quality scores.
  """

  def __init__(self,
               observation_space,
               action_space,
               alg_ctor=algorithms.UCB1,
               ci_scaling=1.0,
               random_seed=0,
               **kwargs):
    """Initializes a new bandit agent for clustered arm exploration.

    Args:
      observation_space: Instance of a gym space corresponding to the
        observation format.
      action_space: A gym.spaces object that specifies the format of actions.
      alg_ctor: A class of an MABAlgorithm for exploration, default to UCB1.
      ci_scaling: A floating number specifying the scaling of confidence bound.
      random_seed: An integer for random seed.
      **kwargs: currently unused arguments.
    """
    num_topics = list(observation_space.spaces['doc'].spaces.values()
                     )[0].spaces['cluster_id'].n
    base_agent_ctors = [
        functools.partial(GreedyClusterAgent, cluster_id=i)
        for i in range(num_topics)
    ]
    super(ClusterBanditAgent, self).__init__(
        observation_space,
        action_space,
        base_agent_ctors,
        alg_ctor=alg_ctor,
        ci_scaling=ci_scaling,
        random_seed=random_seed,
        **kwargs)


class GreedyClusterAgent(agent.AbstractEpisodicRecommenderAgent):
  """Simple agent sorting all documents of a topic according to quality."""

  def __init__(self, observation_space, action_space, cluster_id, **kwargs):
    del observation_space
    super(GreedyClusterAgent, self).__init__(action_space)
    self._cluster_id = cluster_id

  def step(self, reward, observation):
    del reward
    my_docs = []
    my_doc_quality = []
    for i, doc in enumerate(observation['doc'].values()):
      if doc['cluster_id'] == self._cluster_id:
        my_docs.append(i)
        my_doc_quality.append(doc['quality'])
    if not bool(my_docs):
      return []
    sorted_indices = np.argsort(my_doc_quality)[::-1]
    return list(np.array(my_docs)[sorted_indices])
