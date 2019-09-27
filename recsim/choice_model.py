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
"""Abstract classes that encode a user's state and dynamics."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc
import numpy as np


def softmax(vector):
  """Computes the softmax of a vector."""
  normalized_vector = np.array(vector) - np.max(
      vector)  # For numerical stability
  return np.exp(normalized_vector) / np.sum(np.exp(normalized_vector))


class AbstractChoiceModel(object):  # pytype: disable=ignored-metaclass
  """Abstract class to represent the user choice model.

  Each user has a choice model.
  """
  __metaclass__ = abc.ABCMeta
  _scores = None
  _score_no_click = None

  @abc.abstractmethod
  def score_documents(self, user_state, doc_obs):
    """Computes unnormalized scores of documents in the slate given user state.

    Args:
      user_state: An instance of AbstractUserState.
      doc_obs: A numpy array that represents the observation of all documents in
        the slate.
    Attributes:
      scores: A numpy array that stores the scores of all documents.
      score_no_click: A float that represents the score for the action of
        picking no document.
    """

  @property
  def scores(self):
    return self._scores

  @property
  def score_no_click(self):
    return self._score_no_click

  @abc.abstractmethod
  def choose_item(self):
    """Returns selected index of document in the slate.

    Returns:
      selected_index: a integer indicating which item was chosen, or None if
        none were selected.
    """


class NormalizableChoiceModel(AbstractChoiceModel):
  """A normalizable choice model."""

  @staticmethod
  def _score_documents_helper(user_state, doc_obs):
    scores = np.array([])
    for doc in doc_obs:
      scores = np.append(scores, user_state.score_document(doc))
    return scores

  def choose_item(self):
    all_scores = np.append(self._scores, self._score_no_click)
    all_probs = all_scores / np.sum(all_scores)
    selected_index = np.random.choice(len(all_probs), p=all_probs)
    if selected_index == len(all_probs) - 1:
      selected_index = None
    return selected_index


class MultinomialLogitChoiceModel(NormalizableChoiceModel):
  """A multinomial logit choice model.

   Samples item x in scores according to
     p(x) = exp(x) / Sum_{y in scores} exp(y)

   Args:
     choice_features: a dict that stores the features used in choice model:
       `no_click_mass`: a float indicating the mass given to a no click option.
  """

  def __init__(self, choice_features):
    self._no_click_mass = choice_features.get('no_click_mass', -float('Inf'))

  def score_documents(self, user_state, doc_obs):
    logits = self._score_documents_helper(user_state, doc_obs)
    logits = np.append(logits, self._no_click_mass)
    # Use softmax scores instead of exponential scores to avoid overflow.
    all_scores = softmax(logits)
    self._scores = all_scores[:-1]
    self._score_no_click = all_scores[-1]


class MultinomialProportionalChoiceModel(NormalizableChoiceModel):
  """A multinomial proportional choice function.

  Samples item x in scores according to
    p(x) = x - min_normalizer / sum(x - min_normalizer)

  Attributes:
    min_normalizer: A float (<= 0) used to offset the scores to be positive.
      Specifically, if the scores have negative elements, then they do not
      form a valid probability distribution for sampling. Subtracting the
      least expected element is one heuristic for normalization.
    no_click_mass: An optional float indicating the mass given to a no click
      option
  """

  def __init__(self, choice_features):
    self._min_normalizer = choice_features.get('min_normalizer')
    self._no_click_mass = choice_features.get('no_click_mass', 0)

  def score_documents(self, user_state, doc_obs):
    scores = self._score_documents_helper(user_state, doc_obs)
    all_scores = np.append(scores, self._no_click_mass)
    all_scores = all_scores - self._min_normalizer
    assert all_scores[
        all_scores <
        0.0].size == 0, 'Normalized scores have non-positive elements.'
    self._scores = all_scores[:-1]
    self._score_no_click = all_scores[-1]


class CascadeChoiceModel(NormalizableChoiceModel):
  """The base class for cascade choice models.

  Attributes:
    attention_prob: The probability of examining a document i given document i -
      1 not clicked.
    score_scaling: A multiplicative factor to convert score of document i to the
      click probability of examined document i.

  Raises:
    ValueError: if either attention_prob or base_attention_prob is invalid.
  """

  def __init__(self, choice_features):
    self._attention_prob = choice_features.get('attention_prob', 1.0)
    self._score_scaling = choice_features.get('score_scaling')
    if self._attention_prob < 0.0 or self._attention_prob > 1.0:
      raise ValueError('attention_prob must be in [0,1].')
    if self._score_scaling < 0.0:
      raise ValueError('score_scaling must be positive.')

  def _positional_normalization(self, scores):
    """Computes the click probability of each document in _scores.

    The probability to click item i conditioned on unclicked item i - 1 is:
      attention_prob * score_scaling * score(i)
    We also compute the probability of not clicking any items in _score_no_click
    Because they are already probabilities, the normlaization in choose_item
    is no-op but we utilize random choice there.

    Args:
      scores: normalizable scores.
    """
    self._score_no_click = 1.0
    for i in range(len(scores)):
      s = self._score_scaling * scores[i]
      assert s <= 1.0, ('score_scaling cannot convert score %f into a '
                        'probability') % scores[i]
      scores[i] = self._score_no_click * self._attention_prob * s
      self._score_no_click *= (1.0 - self._attention_prob * s)
    self._scores = scores


class ExponentialCascadeChoiceModel(CascadeChoiceModel):
  """An exponential cascade choice model.

  Clicks the item at position i according to
    p(i) = attention_prob * score_scaling * exp(score(i))
  by going through the slate in order, and stopping once an item has been
  clicked.
  """

  def score_documents(self, user_state, doc_obs):
    scores = self._score_documents_helper(user_state, doc_obs)
    scores = np.exp(scores)
    self._positional_normalization(scores)


class ProportionalCascadeChoiceModel(CascadeChoiceModel):
  """A proportional cascade choice model.

  Clicks the item at position i according to
    attention_prob * score_scaling * (score(i) - min_normalizer)
  by going through the slate in order, and stopping once an item has been
  clicked.
  """

  def __init__(self, choice_features):
    self._min_normalizer = choice_features.get('min_normalizer')
    super(ProportionalCascadeChoiceModel, self).__init__(choice_features)

  def score_documents(self, user_state, doc_obs):
    scores = self._score_documents_helper(user_state, doc_obs)
    scores = scores - self._min_normalizer
    assert not scores[
        scores < 0.0], 'Normalized scores have non-positive elements.'
    self._positional_normalization(scores)
