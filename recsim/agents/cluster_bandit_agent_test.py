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
"""Tests for recsim.agents.cluster_bandit_agent."""

from gym import spaces
import numpy as np
from recsim.agents import cluster_bandit_agent
from recsim.environments import interest_exploration as ie
import tensorflow as tf


class ClusterBanditAgentTest(tf.test.TestCase):

  def dummy_observation_space(self):
    single_response_space = spaces.Dict({
        'cluster_id': spaces.Discrete(2),
        'click': spaces.Discrete(2)
    })
    doc_space = spaces.Dict(
        {0: spaces.Dict({'cluster_id': spaces.Discrete(2)})})
    user_space = spaces.Dict({
        'sufficient_statistics':
            spaces.Dict({
                'impression_count':
                    spaces.Box(np.array([0] * 2), np.array([np.inf] * 2)),
                'click_count':
                    spaces.Box(np.array([0] * 2), np.array([np.inf] * 2))
            })
    })
    return spaces.Dict({
        'user': user_space,
        'doc': doc_space,
        'response': spaces.Tuple([
            single_response_space,
        ])
    })

  def doc_user_to_sufficient_stats(self, docs, observation):
    sufficient_stats_observation = {'user': {'sufficient_statistics': {}}}
    sufficient_stats_observation['user']['sufficient_statistics'][
        'impression_count'] = observation[:2]
    sufficient_stats_observation['user']['sufficient_statistics'][
        'click_count'] = observation[2:]
    sufficient_stats_observation['doc'] = docs
    return sufficient_stats_observation

  def test_step_with_bigger_slate(self):
    # Initialize agent.
    slate_size = 5
    num_candidates = 5
    action_space = spaces.MultiDiscrete(num_candidates * np.ones((slate_size,)))
    agent = cluster_bandit_agent.ClusterBanditAgent(
        self.dummy_observation_space(), action_space)

    # Create a set of documents
    document_sampler = ie.IETopicDocumentSampler(seed=1)
    documents = {}
    for i in range(num_candidates):
      video = document_sampler.sample_document()
      documents[i] = video.create_observation()

    # Past observation shows Topic 1 is better.
    user_obs = np.array([1, 1, 0, 1])
    sufficient_stats_observation = self.doc_user_to_sufficient_stats(
        documents, user_obs)
    slate = agent.step(0, sufficient_stats_observation)
    # Documents in Topic 0 sorted by quality: 1, 2.
    # Documents in Topic 1 sorted by quality: 0, 4, 3.
    self.assertAllEqual(slate, [0, 4, 3, 1, 2])

  def test_bundle_and_unbundle_trivial(self):
    action_space = spaces.MultiDiscrete(2 * np.ones((2,)))
    agent = cluster_bandit_agent.ClusterBanditAgent(
        self.dummy_observation_space(), action_space)
    self.assertFalse(agent.unbundle('', 0, {}))
    self.assertEqual(
        {
            'base_agent_bundle_0': {
                'episode_num': 0
            },
            'base_agent_bundle_1': {
                'episode_num': 0
            }
        }, agent.bundle_and_checkpoint('', 0))

  def test_bundle_and_unbundle(self):
    # Initialize agent
    slate_size = 2
    num_candidates = 5
    action_space = spaces.MultiDiscrete(num_candidates * np.ones((slate_size,)))

    agent = cluster_bandit_agent.ClusterBanditAgent(
        self.dummy_observation_space(), action_space)

    # Create a set of documents
    document_sampler = ie.IETopicDocumentSampler()
    documents = {}
    for i in range(num_candidates):
      video = document_sampler.sample_document()
      documents[i] = video.create_observation()

    # Test that slate indices in correct range and length is correct
    sufficient_stats_observation = self.doc_user_to_sufficient_stats(
        documents, np.array([0, 0, 0, 0]))

    agent.step(1, sufficient_stats_observation)

    bundle_dict = agent.bundle_and_checkpoint('', 0)
    self.assertTrue(agent.unbundle('', 0, bundle_dict))
    self.assertEqual(bundle_dict, agent.bundle_and_checkpoint('', 0))


if __name__ == '__main__':
  tf.test.main()
