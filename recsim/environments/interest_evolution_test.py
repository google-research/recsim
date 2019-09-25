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
"""Tests for recsim.environments.interest_evolution."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import numpy as np
from recsim import choice_model
from recsim.environments import interest_evolution
import tensorflow as tf


class FakeChoiceModel(choice_model.AbstractChoiceModel):
  """A fake choice model that returns fixed index and scores."""

  def __init__(self, scores, score_no_click, select_index):
    self._scores = scores
    self._score_no_click = score_no_click
    self._select_index = select_index

  def score_documents(self, user_obs, doc_obs):
    """Skip set user and docs features."""
    pass

  def choose_item(self):
    return self._select_index


class InterestEvolutionTest(tf.test.TestCase):

  def setUp(self):
    super(InterestEvolutionTest, self).setUp()
    self._user_model = interest_evolution.IEvUserModel(
        slate_size=1,
        choice_model_ctor=choice_model.MultinomialLogitChoiceModel,
        seed=0,
        no_click_mass=0)
    self._user_model.choice_model = FakeChoiceModel(
        scores=[2], score_no_click=0, select_index=0)

  def test_user_model_simulate_response(self):
    """Test the simulate_response function."""
    self._user_model._user_state.time_budget = 0.5
    cluster_id = 3
    quality = 2.0
    document = interest_evolution.IEvVideo(
        doc_id=1,
        features=np.ones((20,)),
        cluster_id=cluster_id,
        video_length=1,
        quality=quality)
    responses = self._user_model.simulate_response([document])

    self.assertEqual(responses[0].cluster_id, 3)
    self.assertEqual(responses[0].quality, quality)
    # The clicked is true since our choice model wil select the first document.
    self.assertEqual(responses[0].clicked, True)
    # The watch time is 0.5 because time_budget < video_length and
    # time_budget = 0.5.
    self.assertEqual(responses[0].watch_time, 0.5)

  def test_user_model_update_state(self):
    """Test the update_state function."""
    self._user_model._user_state.time_budget = 0.5
    self._user_model._user_state.user_quality_factor = 0.3
    self._user_model._user_state.document_quality_factor = 0.7
    self._user_model._user_state.user_update_alpha = 1

    cluster_id = 3
    quality = 3.0
    document = interest_evolution.IEvVideo(
        doc_id=1,
        features=np.ones((20,)),
        cluster_id=cluster_id,
        video_length=1,
        quality=quality)
    response = interest_evolution.IEvResponse(clicked=True, watch_time=0.3)
    self._user_model.update_state([document], [response])

    # The expected_utility is 2 (the score of the choice model), the document
    # quality is 3.0, the user_quality_factor = 0.3 and document_quality_factor
    # = 0.7, so received_utility = 0.3 * 2 * 0.7 * 3 = 2.7. Besides,
    # user_update_alpha = 1 so the final time budget is
    # 0.5 - 0.3 + 1 * 0.3 * 2.7 = 1.01.
    self.assertAlmostEqual(self._user_model._user_state.time_budget, 1.01)

  def test_user_model_is_terminal(self):
    # is_terminal is False is time_budget is > 0.
    self._user_model._user_state.time_budget = 0.5
    self.assertFalse(self._user_model.is_terminal())

    # is_terminal is True is time_budget is > 0.
    self._user_model._user_state.time_budget = 0
    self.assertTrue(self._user_model.is_terminal())


if __name__ == '__main__':
  tf.test.main()
