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
"""Tests for recsim.agents.random_agent."""

from gym import spaces
import numpy as np
from recsim import choice_model
from recsim.agents import random_agent
from recsim.environments import interest_evolution as iev
from recsim.environments import interest_exploration as ie
from recsim.simulator import environment
import tensorflow as tf


class RandomAgentTest(tf.test.TestCase):

  def setUp(self):
    super(RandomAgentTest, self).setUp()
    # The maximum length of videos in response
    iev.IEvResponse.MAX_VIDEO_LENGTH = 100.0

    # The number of features used to represent user state.
    iev.IEvUserState.NUM_FEATURES = 10

    # The number of features used to represent video.
    iev.IEvVideo.NUM_FEATURES = 10
    # The maximum length of videos
    iev.IEvVideo.MAX_VIDEO_LENGTH = 100.0

  def test_step(self):
    # Create a simple user
    slate_size = 2
    user_model = iev.IEvUserModel(
        slate_size,
        choice_model_ctor=choice_model.MultinomialLogitChoiceModel,
        response_model_ctor=iev.IEvResponse)

    # Create a candidate_set with 5 items
    num_candidates = 5
    document_sampler = iev.IEvVideoSampler()
    ievsim = environment.Environment(user_model, document_sampler,
                                     num_candidates, slate_size)

    # Create agent
    action_space = spaces.MultiDiscrete(num_candidates * np.ones((slate_size,)))
    agent = random_agent.RandomAgent(action_space, random_seed=0)

    # This agent doesn't use the previous user response
    observation, documents = ievsim.reset()
    slate = agent.step(1, dict(user=observation, doc=documents))
    self.assertAllEqual(slate, [2, 0])

  def test_slate_indices_and_length(self):
    # Initialize agent
    slate_size = 2
    num_candidates = 100
    action_space = spaces.MultiDiscrete(num_candidates * np.ones((slate_size,)))

    user_model = iev.IEvUserModel(
        slate_size,
        choice_model_ctor=choice_model.MultinomialLogitChoiceModel,
        response_model_ctor=iev.IEvResponse)
    agent = random_agent.RandomAgent(action_space, random_seed=0)

    # Create a set of documents
    document_sampler = iev.IEvVideoSampler()
    ievenv = environment.Environment(user_model, document_sampler,
                                     num_candidates, slate_size)

    # Test that slate indices in correct range and length is correct
    observation, documents = ievenv.reset()
    slate = agent.step(1, dict(user=observation, doc=documents))
    self.assertLen(slate, slate_size)
    self.assertAllInSet(slate, range(num_candidates))

  def test_bundle_and_unbundle_trivial(self):
    action_space = spaces.MultiDiscrete(np.ones((1,)))
    agent = random_agent.RandomAgent(action_space, random_seed=0)
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
    agent = random_agent.RandomAgent(action_space, random_seed=0)

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
