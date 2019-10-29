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
"""Classes to represent and interface with documents."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc
from gym import spaces
import numpy as np

# Some notes:
#
#   These represent properties of the documents. Presumably we can add more or
#   remove documents from the candidate set. But these do not include features
#   that depend on both the user and the document.
#


class CandidateSet(object):
  """Class to represent a collection of AbstractDocuments.

     The candidate set is represented as a hashmap (dictionary), with documents
     indexed by their document ID.
  """

  def __init__(self):
    """Initializes a document candidate set with 0 documents."""
    self._documents = {}

  def size(self):
    """Returns an integer, the number of documents in this candidate set."""
    return len(self._documents)

  def get_all_documents(self):
    """Returns all documents."""
    return self.get_documents(self._documents.keys())

  def get_documents(self, document_ids):
    """Gets the documents associated with the specified document IDs.

    Args:
      document_ids: an array representing indices into the candidate set.
        Indices can be integers or string-encoded integers.

    Returns:
      (documents) an ordered list of AbstractDocuments associated with the
        document ids.
    """
    return [self._documents[int(k)] for k in document_ids]

  def add_document(self, document):
    """Adds a document to the candidate set."""
    self._documents[document.doc_id()] = document

  def remove_document(self, document):
    """Removes a document from the set (to simulate a changing corpus)."""
    del self._documents[document.doc_id()]

  def create_observation(self):
    """Returns a dictionary of observable features of documents."""
    return {
        str(k): self._documents[k].create_observation()
        for k in self._documents.keys()
    }

  def observation_space(self):
    return spaces.Dict({
        str(k): self._documents[k].observation_space()
        for k in self._documents.keys()
    })


class AbstractDocumentSampler(object):  # pytype: disable=ignored-metaclass
  """Abstract class to sample documents."""

  __metaclass__ = abc.ABCMeta

  def __init__(self, doc_ctor, seed=0):
    self._doc_ctor = doc_ctor
    self._seed = seed
    self.reset_sampler()

  def reset_sampler(self):
    self._rng = np.random.RandomState(self._seed)

  @abc.abstractmethod
  def sample_document(self):
    """Samples and return an instantiation of AbstractDocument."""

  def get_doc_ctor(self):
    """Returns the constructor/class of the documents that will be sampled."""
    return self._doc_ctor

  @property
  def num_clusters(self):
    """Returns the number of document clusters. Returns 0 if not applicable."""
    return 0


class AbstractDocument(object):  # pytype: disable=ignored-metaclass
  """Abstract class to represent a document and its properties."""

  __metaclass__ = abc.ABCMeta

  # Number of features to represent the document.
  NUM_FEATURES = None

  def __init__(self, doc_id):
    self._doc_id = doc_id  # Unique identifier for the document

  def doc_id(self):
    """Returns the document ID."""
    return self._doc_id

  @abc.abstractmethod
  def create_observation(self):
    """Returns observable properties of this document as a float array."""

  @classmethod
  @abc.abstractmethod
  def observation_space(cls):
    """Gym space that defines how documents are represented."""
