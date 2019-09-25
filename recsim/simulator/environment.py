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
"""Class to represent the environment in the recommender system setting.

   Thus, it models things such as (1) the user's state, for example his/her
   interests and circumstances, (2) the documents available to suggest from and
   their properties, (3) simulates the selection of an item in the slate (or a
   no-op/quit), and (4) models the change in a user's state based on the slate
   presented and the document selected.

   The agent interacting with the environment is the recommender system.  The
   agent receives the state, which is an observation of the user's state and
   observations of the candidate documents. The agent then provides an action,
   which is a slate (an array of indices into the candidate set).

   The goal of the agent is to learn a recommendation policy: a policy that
   serves the user a slate (action) based on user and document features (state)
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
from recsim import document


class Environment(object):
  """Class to represent the environment in the recommender system simulator.

  Attributes:
    user_model: An instantiation of AbstractUserModel that represents a user.
    document_sampler: An instantiation of AbstractDocumentSampler.
    num_candidates: An integer representing the size of the candidate_set.
    slate_size: An integer representing the slate size.
    candidate_set: An instantiation of CandidateSet.
    num_clusters: An integer representing the number of document clusters.
  """

  def __init__(self,
               user_model,
               document_sampler,
               num_candidates,
               slate_size,
               resample_documents=True):
    """Initializes a new simulation environment.

    Args:
      user_model: An instantiation of AbstractUserModel
      document_sampler: An instantiation of AbstractDocumentSampler
      num_candidates: An integer representing the size of the candidate_set
      slate_size: An integer representing the slate size
      resample_documents: A boolean indicating whether to resample the candidate
        set every step
    """
    self._user_model = user_model
    self._document_sampler = document_sampler
    self._slate_size = slate_size
    self._num_candidates = num_candidates
    self._resample_documents = resample_documents

    # Create a candidate set.
    self._do_resample_documents()
    assert (slate_size <= num_candidates
           ), 'Slate size %d cannot be larger than number of candidates %d' % (
               slate_size, num_candidates)

  def _do_resample_documents(self):
    # TODO(sanmit): eventually model this creation with content creators.
    self._candidate_set = document.CandidateSet()
    for _ in range(self._num_candidates):
      self._candidate_set.add_document(self._document_sampler.sample_document())

  def reset(self):
    """Resets the environment and return the first observation.

    Returns:
      user_obs: An array of floats representing observations of the user's
        current state
      doc_obs: An OrderedDict of document observations keyed by document ids
    """
    self._user_model.reset()
    user_obs = self._user_model.create_observation()
    if self._resample_documents:
      self._do_resample_documents()
    self._current_documents = collections.OrderedDict(
        self._candidate_set.create_observation())
    return (user_obs, self._current_documents)

  def reset_sampler(self):
    self._document_sampler.reset_sampler()
    self._user_model.reset_sampler()

  @property
  def num_candidates(self):
    return self._num_candidates

  @property
  def slate_size(self):
    return self._slate_size

  @property
  def candidate_set(self):
    return self._candidate_set

  @property
  def user_model(self):
    return self._user_model

  def step(self, slate):
    """Executes the action, returns next state observation and reward.

    Args:
      slate: An integer array of size slate_size, where each element is an index
        into the set of current_documents presented

    Returns:
      user_obs: A gym observation representing the user's next state
      doc_obs: A list of observations of the documents
      responses: A list of AbstractResponse objects for each item in the slate
      done: A boolean indicating whether the episode has terminated
    """

    assert (len(slate) == self._slate_size
           ), 'Received unexpected slate size: expecting %s, got %s' % (
               self._slate_size, len(slate))

    # Get the documents associated with the slate
    doc_ids = list(self._current_documents)
    mapped_slate = [doc_ids[x] for x in slate]
    documents = self._candidate_set.get_documents(mapped_slate)
    # Simulate the user's response
    responses = self._user_model.simulate_response(documents)

    # Update the user's state.
    self._user_model.update_state(documents, responses)

    # Obtain next user state observation.
    user_obs = self._user_model.create_observation()

    # Check if reaches a terminal state and return.
    done = self._user_model.is_terminal()

    # Optionally, recreate the candidate set to simulate candidate
    # generators for the next query.
    if self._resample_documents:
      self._do_resample_documents()

    # Create observation of candidate set.
    self._current_documents = self._candidate_set.create_observation()

    return (user_obs, self._current_documents, responses, done)
