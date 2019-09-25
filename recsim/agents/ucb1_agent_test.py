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
"""Tests for recsim.agents.ucb1_agent."""

import numpy as np
from recsim.agents import cluster_bandit_agent
from recsim.agents.layers import cluster_click_statistics
from recsim.environments import interest_exploration as ie
import tensorflow as tf


class UCB1AgentTest(tf.test.TestCase):

  def test_step(self):
    # Initialize agent.
    env_config = {
        'slate_size': 1,
        'num_candidates': 5,
        'resample_documents': True,
        'seed': 1,
    }
    env = ie.create_environment(env_config)
    kwargs = {
        'observation_space': env.observation_space,
        'action_space': env.action_space,
    }
    agent = cluster_click_statistics.ClusterClickStatsLayer(
        cluster_bandit_agent.ClusterBanditAgent, **kwargs)

    observation1, documents1 = env.environment.reset()
    slate1 = agent.step(0,
                        dict(user=observation1, doc=documents1, response=None))
    # Pick the document with the best quality in Topic 0.
    scores_c0 = [(features['quality'] if features['cluster_id'] == 0 else 0)
                 for _, features in documents1.items()]
    scores_c1 = [(features['quality'] if features['cluster_id'] == 1 else 0)
                 for _, features in documents1.items()]
    self.assertIn(slate1[0], [np.argmax(scores_c0), np.argmax(scores_c1)])
    picked_cluster = list(documents1.values())[slate1[0]]['cluster_id']

    observation2, documents, response1, _ = env.environment.step(slate1)
    response1_obs = [response.create_observation() for response in response1]
    response1_obs[0]['cluster_id'] = picked_cluster
    slate2 = agent.step(
        ie.total_clicks_reward(response1),
        dict(user=observation2, doc=documents, response=response1_obs))
    # Pick Topic 1 because we have no observation about it.
    # Pick the document with the best quality there.
    doc_qualities = [
        (features['quality'] if features['cluster_id'] != picked_cluster else 0)
        for _, features in documents.items()
    ]
    self.assertAllEqual(slate2, [
        np.argmax(doc_qualities),
    ])

    self.assertNotEqual(
        list(documents.values())[slate2[0]]['cluster_id'], picked_cluster)

    observation3, documents, response2, _ = env.environment.step(slate2)
    response2_obs = [response.create_observation() for response in response2]
    # Make a clicked response.
    response2_obs[0]['click'] = 1
    response2_obs[0]['cluster_id'] = 1 - picked_cluster
    slate3 = agent.step(
        ie.total_clicks_reward(response2),
        dict(user=observation3, doc=documents, response=response2_obs))
    # Pick the first topic which has the best UCB and then pick the document
    # with the best quality in it.
    pulls = np.array([1, 1], dtype=np.float)
    rewards = np.array([0, 0], dtype=np.float)
    rewards[1 - picked_cluster] = 1
    ct = np.sqrt(2.0 * np.log(2.0))
    topic_index = rewards / pulls + ct * np.sqrt(1.0 / pulls)
    doc_qualities = [(features['quality'] if
                      features['cluster_id'] == np.argmax(topic_index) else 0)
                     for _, features in documents.items()]
    self.assertAllEqual(slate3, [np.argmax(doc_qualities)])

    agent.end_episode(
        ie.total_clicks_reward(response2),
        dict(user=observation3, doc=documents, response=response2_obs))
    slate4 = agent.step(0,
                        dict(user=observation1, doc=documents1, response=None))
    self.assertAllEqual(slate4, slate1)


if __name__ == '__main__':
  tf.test.main()
