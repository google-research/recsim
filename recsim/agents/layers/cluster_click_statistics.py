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
"""Helper class to collect cluster click and impression counts."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from gym import spaces
import numpy as np

from recsim.agents.layers import sufficient_statistics


class ClusterClickStatsLayer(sufficient_statistics.SufficientStatisticsLayer):
  """Track impressions and clicks on a per-cluster basis and pass down to agent.

  This module assumes each document belongs to single cluster and we know the
  number of possible clusters. Every time we increase impression count for a
  cluster if the agent recommends a document from that cluster. We also increase
  click count for a cluster if user responds a click.
  """

  def __init__(self, base_agent_ctor, observation_space, action_space,
               **kwargs):
    """Initializes a ClusterClickStatsLayer object.

    Args:
      base_agent_ctor: a constructor for the base agent.
      observation_space: a gym.spaces object specifying the format of
        observations.
      action_space: A gym.spaces object that specifies the format of actions.
      **kwargs: arguments to pass to the downstream agent at construction time.
    """
    single_response_space = observation_space.spaces['response'].spaces[0]
    if 'cluster_id' not in single_response_space.spaces:
      raise ValueError('observation_space.spaces[\'response\']'
                       ' must contain \'cluster_id\' key.')
    cluster_id_space = single_response_space.spaces['cluster_id']
    if isinstance(cluster_id_space, spaces.Box):
      if len(cluster_id_space.high) > 1:
        raise ValueError('cluster_id response field must be 0 dimensional.')
      num_clusters = cluster_id_space.high
    elif isinstance(cluster_id_space, spaces.Discrete):
      num_clusters = cluster_id_space.n
    else:
      raise ValueError('cluster_id response field must be either gym.spaces.Box'
                       ' or gym spaces.Discrete')
    self._num_clusters = num_clusters
    if 'click' not in single_response_space.spaces:
      raise ValueError(
          'observation_space.spaces[\'response\'] must contain \'click\' key.')
    suf_stat_space = spaces.Dict({
        'impression_count':
            spaces.Box(
                shape=(num_clusters,), dtype=np.float32, low=0.0, high=np.inf),
        'click_count':
            spaces.Box(
                shape=(num_clusters,), dtype=np.float32, low=0.0, high=np.inf)
    })
    super(ClusterClickStatsLayer,
          self).__init__(base_agent_ctor, observation_space, action_space,
                         suf_stat_space, **kwargs)

  def _create_observation(self):
    return {
        'impression_count':
            np.array(self._sufficient_statistics['impression_count']),
        'click_count':
            np.array(self._sufficient_statistics['click_count']),
    }

  def _update(self, observation):
    """Updates user impression/click count given user response on each item."""
    if self._sufficient_statistics is None:
      self._sufficient_statistics = {
          'impression_count': [
              0,
          ] * self._num_clusters,
          'click_count': [
              0,
          ] * self._num_clusters
      }
    if observation['response'] is not None:
      for response in observation['response']:
        cluster_id = int(response['cluster_id'])
        self._sufficient_statistics['impression_count'][cluster_id] += 1
        if response['click']:
          self._sufficient_statistics['click_count'][cluster_id] += 1
