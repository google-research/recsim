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
"""Tests for recsim.choice_model."""

import numpy as np
from recsim import choice_model
from recsim.environments import interest_evolution as evolution
import tensorflow as tf


class SoftmaxTest(tf.test.TestCase):

  def test_softmax_single_int(self):
    self.assertAllClose(choice_model.softmax([0]), [1.0])

  def test_softmax_equal_ints(self):
    self.assertAllClose(
        choice_model.softmax(np.ones(4)), np.array([0.25, 0.25, 0.25, 0.25]))

  def test_softmax_positive_floats(self):
    self.assertAllClose(
        choice_model.softmax(np.log(np.arange(1, 5))),
        np.array([0.1, 0.2, 0.3, 0.4]))

  def test_softmax_negative_floats(self):
    self.assertAllClose(
        choice_model.softmax(-1.0 * np.log(np.arange(1, 5))),
        np.array([0.48, 0.24, 0.16, 0.12]))


class MultinomialChoiceModelTest(tf.test.TestCase):

  def setUp(self):
    super(MultinomialChoiceModelTest, self).setUp()
    np.random.seed(0)
    self._user_state = evolution.IEvUserState(np.array([0.8, 0.6]))

  def test_multinomial_logit_default(self):
    mnl_model = choice_model.MultinomialLogitChoiceModel(choice_features={})
    mnl_model.score_documents(
        self._user_state, np.array([[0.8, 0.6], [0.6, 0.8]]))
    # The logits for two documents are 1 and 0.96 respectively. When computing
    # softmax logits, we subtract the largest value, which is 1 here. So the
    # score is softmax([0, -0.04]) = [0.51, 0.49]
    self.assertAlmostEqual(mnl_model._scores[0], 0.510, delta=0.001)
    self.assertAlmostEqual(mnl_model._scores[1], 0.490, delta=0.001)
    self.assertEqual(mnl_model._score_no_click, 0)

  def test_multinomial_logit_no_click_mass(self):
    choice_features = dict(no_click_mass=1.0)
    mnl_model = choice_model.MultinomialLogitChoiceModel(
        choice_features=choice_features)
    # The logits for two documents are 1 and 0.96 respectively. No click mass
    # is 1.0. When computing
    # softmax logits, we subtract the largest value, which is 1 here. So the
    # score is softmax([0, -0.04, 0]) = [0.337, 0.325, 0.338]
    mnl_model.score_documents(
        self._user_state, np.array([[0.8, 0.6], [0.6, 0.8]]))
    self.assertAlmostEqual(mnl_model._scores[0], 0.338, delta=0.001)
    self.assertAlmostEqual(mnl_model._scores[1], 0.325, delta=0.001)
    self.assertAlmostEqual(mnl_model._score_no_click, 0.338, delta=0.001)

  def test_multinomial_proportion_choice_model_default(self):
    choice_features = dict(min_normalizer=0)
    mnp_model = choice_model.MultinomialProportionalChoiceModel(
        choice_features=choice_features)
    mnp_model.score_documents(
        self._user_state, np.array([[0.8, 0.6], [0.6, 0.8]]))
    # The scores are the dot product between user features and doc features.
    self.assertAlmostEqual(mnp_model._scores[0], 1, delta=0.001)
    self.assertAlmostEqual(mnp_model._scores[1], 0.96, delta=0.001)
    self.assertEqual(mnp_model._score_no_click, 0)

  def test_multinomial_proportion_min_normalizer(self):
    choice_features = dict(min_normalizer=0.5, no_click_mass=0.5)
    mnp_model = choice_model.MultinomialProportionalChoiceModel(
        choice_features=choice_features)
    mnp_model.score_documents(
        self._user_state, np.array([[0.8, 0.6], [0.6, 0.8]]))
    # The scores the dot product user features and doc features minus the
    # min_normalizer.
    self.assertAlmostEqual(mnp_model._scores[0], 0.5, delta=0.001)
    self.assertAlmostEqual(mnp_model._scores[1], 0.46, delta=0.001)
    self.assertAlmostEqual(mnp_model._score_no_click, 0, delta=0.001)


class CascadeChoiceModelTest(tf.test.TestCase):

  def setUp(self):
    super(CascadeChoiceModelTest, self).setUp()
    np.random.seed(0)
    self._user_state = evolution.IEvUserState(np.array([1.0]))

  def test_exponential_cascade_invalid_score_scaling(self):
    with self.assertRaises(ValueError):
      choice_features = {'attention_prob': 0.8, 'score_scaling': -1.0}
      choice_model.ExponentialCascadeChoiceModel(choice_features)

  def test_exponential_cascade_invalid_attenion_prob(self):
    with self.assertRaises(ValueError):
      choice_features = {'attention_prob': 2.0}
      choice_model.ExponentialCascadeChoiceModel(choice_features)

  def test_exponential_cascade(self):
    choice_features = {'score_scaling': 0.04}
    model = choice_model.ExponentialCascadeChoiceModel(choice_features)
    model.score_documents(self._user_state, np.array([[3.0], [2.0], [1.0]]))
    self.assertEqual(model.choose_item(), 0)

  def test_exponential_cascade_with_no_click(self):
    choice_features = {'attention_prob': 1.0, 'score_scaling': 0.0}
    model = choice_model.ExponentialCascadeChoiceModel(choice_features)
    model.score_documents(self._user_state, np.array([[3.0], [2.0], [1.0]]))
    self.assertEqual(model.choose_item(), None)

  def test_proportional_cascade_invalid_attenion_prob(self):
    with self.assertRaises(ValueError):
      choice_features = {
          'attention_prob': 2.0,
          'min_normalizer': -2.0,
          'score_scaling': 0.1
      }
      choice_model.ProportionalCascadeChoiceModel(choice_features)

  def test_proportional_cascade_invalid_score_scaling(self):
    with self.assertRaises(ValueError):
      choice_features = {
          'attention_prob': 0.5,
          'min_normalizer': -2.0,
          'score_scaling': -1.0
      }
      choice_model.ProportionalCascadeChoiceModel(choice_features)

  def test_proportional_cascade(self):
    choice_features = {
        'attention_prob': 1.0,
        'min_normalizer': -4.0,
        'score_scaling': 0.07
    }
    model = choice_model.ProportionalCascadeChoiceModel(choice_features)
    model.score_documents(self._user_state,
                          np.array([[-3.0], [-3.0], [10.0], [1.0], [-4.0]]))
    self.assertEqual(model.choose_item(), 2)

  def test_proportional_cascade_with_no_click(self):
    choice_features = {
        'attention_prob': 0.5,
        'min_normalizer': -1.0,
        'score_scaling': 0.1
    }
    model = choice_model.ProportionalCascadeChoiceModel(choice_features)
    model.score_documents(self._user_state, np.array([[0.0], [0.0], [0.0]]))
    self.assertEqual(model.choose_item(), None)


if __name__ == '__main__':
  tf.test.main()
