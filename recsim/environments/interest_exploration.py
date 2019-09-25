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
"""Correlated interest exploration environment.

This environment models the problem of active exploration of user interests. It
is meant to illustrate popularity bias in recommender systems, where myopic
maximization of engagement leads to bias towards documents that have wider
appeal, whereas niche user interests remain unexplored.

In this setting, documents are generated from M topics (types) such that each
document belongs to exactly one topic. Furthermore, there are N types (types)
of users. Each document d has a production quality f_D(d) score drawn from a
distribution associated with its type D (e.g. more mass-appeal types tend
to have higher production values). On the other hand, each user u has an
affinity score g_U(u,d) towards each document type (drawn from a distribution
associated with the user's type). The final affinity of user u to document
d is thus g_U(u,d) + f_D(d). When faced with a slate of documents, the user
clicks on a document based on a multinomial logistic choice model with the
affinity scores as parameters.

A myopic agent will favor types with high production value, as they have
a high apriori probability of getting clicked across all user types. This leads
the agent to ignore niche interests, producing a suboptimal policy. This
scenario can be seen as a correlated arms bandit problem.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl import flags
from absl import logging
import gin.tf
from gym import spaces
import numpy as np
from recsim import choice_model
from recsim import document
from recsim import user
from recsim import utils
from recsim.simulator import environment
from recsim.simulator import recsim_gym

FLAGS = flags.FLAGS


class IEUserModel(user.AbstractUserModel):
  """Class to model a user.

  The user in this scenario is completely characterized by a vector g
  of affinity scores of dimension |D| (the number of document topics). When
  presented with a slate of documents, the user scores each document as g(d) +
  f(d), where f(d) is the document's quality score, and then chooses according
  to a choice model based on these scores.

  The state space consists of a vector of affinity scores which is unique to the
  user and static but not observable.

  Args:
  slate_size: An integer representing the size of the slate.
  no_click_mass: A float indicating the mass given to a no-click option.
    Must be positive, otherwise CTR is always 1.
  choice_model_ctor: A contructor function to create user choice model.
  user_state_ctor: A constructor to create user state.
  response_model_ctor: A constructor function to create response. The
    function should take a string of doc ID as input and returns a
    IEResponse object.
  seed: an integer used as the seed in random sampling.
  """

  def __init__(self,
               slate_size,
               no_click_mass=5,
               choice_model_ctor=choice_model.MultinomialLogitChoiceModel,
               user_state_ctor=None,
               response_model_ctor=None,
               seed=0):
    if no_click_mass < 0:
      raise ValueError('no_click_mass must be positive.')

    super(IEUserModel, self).__init__(response_model_ctor, IEClusterUserSampler(
        user_ctor=user_state_ctor, seed=seed), slate_size)
    self._user_state_ctor = user_state_ctor
    if choice_model_ctor is None:
      raise Exception('A choice model needs to be specified!')
    self.choice_model = choice_model_ctor({
        'no_click_mass': no_click_mass,
    })

  @property
  def avg_user_state(self):
    """Returns the prior of user state."""
    return self._user_state_ctor(self._user_sampler.avg_affinity_given_topic())

  def is_terminal(self):
    """Returns a boolean indicating if the session is over."""
    return False

  # No state transitions.
  def update_state(self, slate_documents, responses):
    del slate_documents  # Unused
    del responses  # Unused
    return

  def simulate_response(self, documents):
    """Simulates the user's response to a slate of documents with choice model.

    Args:
      documents: a list of IEDocument objects in the slate.

    Returns:
      responses: a list of IEResponse objects, one for each document.
    """
    # List of empty responses
    responses = [self._response_model_ctor() for _ in documents]

    # Sample the response for selected slate items.

    self.choice_model.score_documents(
        self._user_state, [doc.create_observation() for doc in documents])
    selected_index = self.choice_model.choose_item()
    for i, response in enumerate(responses):
      response.quality = documents[i].quality
      response.cluster_id = documents[i].cluster_id
    if selected_index is None:
      return responses
    self._generate_response(documents[selected_index],
                            responses[selected_index])
    return responses

  def _generate_response(self, doc, response):
    """Trivial response: sets the clicked property of a clicked document.

    Args:
      doc: a IEDocument object.
      response: a IEResponse for the document.
    Updates: response, with whether the document was clicked.
    """
    response.clicked = True


class IEUserState(user.AbstractUserState):
  """Class to represent users.

  Attributes:
    topic_affinity: a nonnegative vector holds document type affinities which
      are not temporal dynamics and hidden.
  """

  def __init__(self, topic_affinity):
    """Initializes a new user."""
    self.topic_affinity = topic_affinity

  def score_document(self, doc_obs):
    """Returns user document affinity plus document quality."""
    return self.topic_affinity[doc_obs['cluster_id']] + doc_obs['quality']

  def create_observation(self):
    """User's topic_affinity is not observable."""
    return np.array([])

  @staticmethod
  def observation_space():
    return spaces.Box(shape=(0,), dtype=np.float32, low=0.0, high=np.inf)


@gin.configurable
class IEClusterUserSampler(user.AbstractUserSampler):
  """Samples users from predetermined types with type-specific parameters.

    This sampler consumes a distribution over user types and type-specific
    parameters for the user's affinity towards content types. It first samples
    a user type, then using that user type generates affinities according to
    the type-specific parameters. In this case, these are the mean and scale
    of a lognormal distribution, i.e. the affinity of user u of type U towards
    an document of type D is drawn according to
    lognormal(mean(U,D), scale(U,D)).

    Args:
      user_type_distribution: a non-negative array of dimension equal to the
        number of user types, whose entries sum to one.
      user_document_mean_affinity_matrix: a non-negative two-dimensional array
        with dimensions number of user types by number of document topics.
        Represents the mean of the affinity score of a user type to a topic.
      user_document_stddev_affinity_matrix: a non-negative two-dimensional array
        with dimensions number of user types by number of document topics.
        Represents the scale of the affinity score of a user type to a topic.
      user_ctor: constructor for a user state.
  """

  def __init__(self,
               user_type_distribution=(0.3, 0.7),
               user_document_mean_affinity_matrix=((.1, .7), (.7, .1)),
               user_document_stddev_affinity_matrix=((.1, .1), (.1, .1)),
               user_ctor=IEUserState,
               **kwargs):
    self._number_of_user_types = len(user_type_distribution)
    self._user_type_dist = user_type_distribution
    if len(user_document_mean_affinity_matrix) != len(user_type_distribution):
      raise ValueError('The dimensions of user_type_distribution and '
                       'user_document_mean_affinity_matrix do not match.')
    if len(user_document_stddev_affinity_matrix) != len(user_type_distribution):
      raise ValueError('The dimensions of user_type_distribution and '
                       'user_document_stddev_affinity_matrix do not match.')
    self._user_doc_means = user_document_mean_affinity_matrix
    self._user_doc_stddev = user_document_stddev_affinity_matrix
    logging.debug('Initialized IEClusterUserSampler')
    super(IEClusterUserSampler, self).__init__(user_ctor, **kwargs)

  def sample_user(self):
    # 1. Pick user type.
    user_type = self._rng.choice(
        self._number_of_user_types, p=self._user_type_dist)
    # 2. Sample user-document affinity given type.
    user_doc_affinity = (
        self._rng.lognormal(
            mean=self._user_doc_means[user_type],
            sigma=self._user_doc_stddev[user_type]))
    return self._user_ctor(user_doc_affinity)

  def avg_affinity_given_topic(self):
    # Returns the prior of document affinity.
    return np.matmul(self._user_type_dist, self._user_doc_means)


class IEResponse(user.AbstractResponse):
  """Class to represent a user's response to a document.

  Attributes:
    clicked: boolean indicating whether the item was clicked or not.
    quality: a float indicating the quality of the document.
    cluster_id: an integer representing the topic ID of the document.
  """

  NUM_CLUSTERS = 0

  def __init__(self,
               clicked=False,
               quality=0.0,
               cluster_id=0):
    self.clicked = clicked
    self.quality = quality
    self.cluster_id = cluster_id

  def __str__(self):
    return str(self.clicked)

  def __repr__(self):
    return self.__str__()

  def create_observation(self):
    return {'click': int(self.clicked),
            'quality': self.quality,
            'cluster_id': self.cluster_id}

  @classmethod
  def response_space(cls):
    return spaces.Dict({
        'click':
            spaces.Discrete(2),
        'quality':
            spaces.Box(
                low=0.0, high=np.inf, shape=tuple(), dtype=np.float32),
        'cluster_id':
            spaces.Discrete(cls.NUM_CLUSTERS)
    })


class IEDocument(document.AbstractDocument):
  """Class to represent an IE Document.

  Attributes:
    cluster_id: an integer representing the document cluster.
    quality: non-negative real number representing the quality of the document.
  """

  NUM_CLUSTERS = 0

  def __init__(self, doc_id, cluster_id, quality):
    self.cluster_id = cluster_id
    self.quality = quality
    # doc_id is an integer representing the unique ID of this document
    super(IEDocument, self).__init__(doc_id)

  def create_observation(self):
    return {'quality': self.quality,
            'cluster_id': self.cluster_id}

  @classmethod
  def observation_space(cls):
    return spaces.Dict({
        'quality':
            spaces.Box(
                low=0.0, high=np.inf, shape=tuple(), dtype=np.float32),
        'cluster_id':
            spaces.Discrete(cls.NUM_CLUSTERS)
    })


@gin.configurable
class IETopicDocumentSampler(document.AbstractDocumentSampler):
  """Samples documents with topic-specific quality distribution.

     Consumes a distribution over document topics and topic-specific parameters
     for generating a quality score (according to a lognormal distribution).

     Args:
       topic_distribution: a non-negative array of dimension equal to the
         number of topics, whose entries sum to one.
       topic_quality_mean: a non-negative array of dimension equal to the
         number of topics, representing the mean of the topic quality score.
       topic_quality_stddev: a non-negative array of dimension equal to the
         number of topics, representing the scale of the topic quality score.
       doc_ctor: A class/constructor for the type of videos that will be sampled
        by this sampler.
  """

  def __init__(self,
               topic_distribution=(.2, .8),
               topic_quality_mean=(.8, .2),
               topic_quality_stddev=(.1, .1),
               doc_ctor=IEDocument,
               **kwargs):
    self._number_of_topics = len(topic_distribution)
    self._topic_dist = topic_distribution
    if len(topic_quality_mean) != len(topic_distribution):
      raise ValueError('The dimensions of topic_quality_mean and '
                       'topic_distribution do not match.')
    if len(topic_quality_stddev) != len(topic_distribution):
      raise ValueError('The dimensions of topic_quality_stddev and '
                       'topic_distribution do not match.')
    self._topic_quality_mean = topic_quality_mean
    self._topic_quality_stddev = topic_quality_stddev
    super(IETopicDocumentSampler, self).__init__(doc_ctor, **kwargs)
    self._doc_count = 0

  @property
  def num_clusters(self):
    return self._number_of_topics

  def sample_document(self):
    """Samples the topic and then samples document features given the topic."""
    doc_features = {}
    doc_features['doc_id'] = self._doc_count
    self._doc_count += 1
    topic_id = self._rng.choice(self._number_of_topics, p=self._topic_dist)
    doc_quality = (
        self._rng.lognormal(
            mean=self._topic_quality_mean[topic_id],
            sigma=self._topic_quality_stddev[topic_id]))
    doc_features['cluster_id'] = topic_id
    doc_features['quality'] = doc_quality
    return self._doc_ctor(**doc_features)


def total_clicks_reward(responses):
  """Calculates the total number of clicks from a list of responses.

  Args:
     responses: A list of IEResponse objects

  Returns:
    reward: A float representing the total clicks from the responses
  """
  reward = 0.0
  for r in responses:
    reward += r.clicked
  return reward


def create_environment(env_config):
  """Creates an interest exploration environment."""

  document_sampler = IETopicDocumentSampler(seed=env_config['seed'])
  IEDocument.NUM_CLUSTERS = document_sampler.num_clusters
  IEResponse.NUM_CLUSTERS = document_sampler.num_clusters

  user_model = IEUserModel(
      env_config['slate_size'],
      user_state_ctor=IEUserState,
      response_model_ctor=IEResponse,
      seed=env_config['seed'])

  ieenv = environment.Environment(
      user_model,
      document_sampler,
      env_config['num_candidates'],
      env_config['slate_size'],
      resample_documents=env_config['resample_documents'])

  return recsim_gym.RecSimGymEnv(ieenv, total_clicks_reward,
                                 utils.aggregate_video_cluster_metrics,
                                 utils.write_video_cluster_metrics)
