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
"""Agent that picks items with highest pCTR given the true user choice model."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from absl import logging

import numpy as np

from recsim import agent
from recsim import choice_model as cm


class GreedyPCTRAgent(agent.AbstractEpisodicRecommenderAgent):
  """An agent that recommends slates with the highest pCTR items.

  This agent assumes knowledge of the true underlying choice model. Note that
  this implicitly means it receives observations of the true user and document
  states. This agent myopically creates slates with items that have the highest
  probability of being clicked under the given choice model.
  """

  def __init__(self,
               action_space,
               belief_state,
               choice_model=cm.MultinomialLogitChoiceModel({'no_click_mass': 5
                                                           })):
    """Initializes a new greedy pCTR agent.

    Args:
      action_space: A gym.spaces object that specifies the format of actions
      belief_state: An instantiation of AbstractUserState assumed by the agent
      choice_model: An instantiation of AbstractChoiceModel assumed by the agent
        Default to a multinomial logit choice model with no_click_mass = 5.
    """

    super(GreedyPCTRAgent, self).__init__(action_space)
    self._choice_model = choice_model
    self._belief_state = belief_state

  def step(self, reward, observation):
    """Records the most recent transition and returns the agent's next action.

    We store the observation of the last time step since we want to store it
    with the reward.

    Args:
      reward: Unused.
      observation: A dictionary that includes the most recent observations and
        should have the following fields:
        - user: A list of floats representing the user's observed state
        - doc: A list of observations of document features

    Returns:
      slate: An integer array of size _slate_size, where each element is an
        index into the list of doc_obs
    """
    del reward  # Unused argument.
    doc_obs = observation['doc']

    # Score the documents without knowing the latent user state.
    self._choice_model.score_documents(self._belief_state, doc_obs.values())

    # Find the indices of the top scoring documents
    slate = self.findBestDocuments(self._choice_model.scores)

    # Return the slate of those documents
    logging.debug('Recommended slate: %s', slate)
    return slate

  def findBestDocuments(self, scores):
    """Returns the indices of the highest scores in sorted order.

    Args:
      scores: A list of floats representing unnormalized document scores

    Returns:
      sorted_indices: A list of integers indexing the highest scores, in sorted
      order
    """
    # Chose the k = slate_size best ones
    scores = np.array(scores)
    indices = np.argpartition(scores, -self._slate_size)[-self._slate_size:]

    # Sort them so the best appear first
    sorted_indices = indices[np.argsort(-scores[indices])]
    return sorted_indices
