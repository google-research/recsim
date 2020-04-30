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
"""Tests for recsim.environment."""

import numpy as np
from recsim.environments import interest_exploration as ie
from recsim.simulator import environment
import recsim.testing.test_base as test_base


class EnvironmentTest(test_base.TestCase):

  def setUp(self):
    super(EnvironmentTest, self).setUp()
    self._slate_size = 2
    self._num_candidates = 20
    user_model = ie.IEUserModel(
        self._slate_size,
        user_state_ctor=ie.IEUserState,
        response_model_ctor=ie.IEResponse)
    document_sampler = ie.IETopicDocumentSampler()
    self._environment = environment.Environment(user_model, document_sampler,
                                                self._num_candidates,
                                                self._slate_size)

  def test_environment(self):
    user_obs, documents = self._environment.reset()
    self.assertAllEqual(np.array([]), user_obs)
    self.assertAllEqual([
        str(doc)
        for doc in range(self._num_candidates, 2 * self._num_candidates)
    ], sorted(documents.keys()))
    slate = [0, 0]
    for i, doc_id in enumerate(list(documents)):
      if documents[doc_id]['cluster_id'] > 0.5:
        slate[0] = i
      else:
        slate[1] = i
      if slate[0] != 0 and slate[1] != 0:
        break
    user_obs, documents, _, done = self._environment.step(slate)
    self.assertAllEqual(np.array([]), user_obs)
    self.assertAllEqual([
        str(doc)
        for doc in range(2 * self._num_candidates, 3 * self._num_candidates)
    ], sorted(documents.keys()))
    self.assertFalse(done)


class MultiUserEnvironmentTest(test_base.TestCase):

  def setUp(self):
    super(MultiUserEnvironmentTest, self).setUp()
    self._slate_size = 2
    self._num_candidates = 20
    self._num_users = 100
    user_models = []
    for _ in range(self._num_users):
      user_models.append(ie.IEUserModel(self._slate_size,
                                        user_state_ctor=ie.IEUserState,
                                        response_model_ctor=ie.IEResponse))
    document_sampler = ie.IETopicDocumentSampler()
    self._environment = environment.MultiUserEnvironment(
        user_models, document_sampler, self._num_candidates, self._slate_size)

  def test_multi_user_environment(self):
    user_obs_list, documents = self._environment.reset()
    for user_obs in user_obs_list:
      self.assertAllEqual(np.array([]), user_obs)
    self.assertAllEqual([
        str(doc)
        for doc in range(self._num_candidates, 2 * self._num_candidates)
    ], sorted(documents.keys()))
    slate = [0, 0]
    for i, doc_id in enumerate(list(documents)):
      if documents[doc_id]['cluster_id'] > 0.5:
        slate[0] = i
      else:
        slate[1] = i
      if slate[0] != 0 and slate[1] != 0:
        break
    slates = [slate for _ in range(self._num_users)]
    user_obs_list, documents, _, done = self._environment.step(slates)
    for user_obs in user_obs_list:
      self.assertAllEqual(np.array([]), user_obs)
    self.assertAllEqual([
        str(doc)
        for doc in range(2 * self._num_candidates, 3 * self._num_candidates)
    ], sorted(documents.keys()))
    self.assertFalse(done)


if __name__ == '__main__':
  test_base.main()
