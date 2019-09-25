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
"""Tests for recsim.agents.greedy_pctr_agent."""

from gym import spaces
import numpy as np

from recsim.agents import greedy_pctr_agent
from recsim.environments import interest_exploration as ie
from recsim.simulator import environment
import tensorflow as tf


class GreedyPCTRAgentTest(tf.test.TestCase):

  def test_find_best_documents(self):
    action_space = spaces.MultiDiscrete(4 * np.ones((4,)))
    agent = greedy_pctr_agent.GreedyPCTRAgent(action_space, None)
    scores = [-1, -2, 4.32, 0, 15, -6, 4.32]
    indices = agent.findBestDocuments(scores)
    self.assertAllEqual(indices, [4, 2, 6, 3])

  def test_step(self):
    # Create a simple user
    slate_size = 2
    num_candidates = 5
    action_space = spaces.MultiDiscrete(num_candidates * np.ones((slate_size,)))
    user_model = ie.IEUserModel(
        slate_size,
        user_state_ctor=ie.IEUserState,
        response_model_ctor=ie.IEResponse)

    # Create a set of documents
    document_sampler = ie.IETopicDocumentSampler(seed=1)
    ieenv = environment.Environment(
        user_model,
        document_sampler,
        num_candidates,
        slate_size,
        resample_documents=True)

    # Create agent
    agent = greedy_pctr_agent.GreedyPCTRAgent(action_space,
                                              user_model.avg_user_state)

    # This agent doesn't use the previous user response
    observation, documents = ieenv.reset()
    slate = agent.step(1, dict(user=observation, doc=documents))
    scores = [
        user_model.avg_user_state.score_document(doc_obs)
        for doc_obs in list(documents.values())
    ]
    expected_slate = sorted(np.argsort(scores)[-2:])
    self.assertAllEqual(sorted(slate), expected_slate)

  def test_bundle_and_unbundle_trivial(self):
    action_space = spaces.MultiDiscrete(np.ones((1,)))
    agent = greedy_pctr_agent.GreedyPCTRAgent(action_space, None)
    self.assertFalse(agent.unbundle('', 0, {}))
    self.assertEqual({
        'episode_num': 0
    }, agent.bundle_and_checkpoint('', 0))

  def test_bundle_and_unbundle(self):
    # Initialize agent
    slate_size = 1
    num_candidates = 3
    action_space = spaces.MultiDiscrete(num_candidates * np.ones((slate_size,)))

    user_model = ie.IEUserModel(
        slate_size,
        user_state_ctor=ie.IEUserState,
        response_model_ctor=ie.IEResponse)
    agent = greedy_pctr_agent.GreedyPCTRAgent(action_space,
                                              user_model.avg_user_state)

    # Create a set of documents
    document_sampler = ie.IETopicDocumentSampler()
    documents = {}
    for i in range(num_candidates):
      video = document_sampler.sample_document()
      documents[i] = video.create_observation()

    # Test that slate indices in correct range and length is correct
    observation = dict(user=user_model.create_observation(), doc=documents)
    agent.step(1, observation)

    bundle_dict = agent.bundle_and_checkpoint('', 0)
    self.assertTrue(agent.unbundle('', 0, bundle_dict))
    self.assertEqual(bundle_dict, agent.bundle_and_checkpoint('', 0))


if __name__ == '__main__':
  tf.test.main()
