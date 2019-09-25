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
"""Long term satisfaction (Choc/Kale) environment.

This environment depicts a situation in which a user of an online service
interacts with items of content, which are characterized by their level of
clickbaitiness (on a scale of 0 to 1). In particular, clickbaity items (choc)
generate engagement, but lead to decrease in long-term satisfaction.
Non-clickbaity items (kale) increase satisfaction but do not generate as much
engagement. The challenge is to balance the two in order to achieve some long-
term optimal trade-off.
The dynamics of this system are partially observable, as satisfaction is a
latent variable. It has to be inferred through the increase/decrease in
engagement.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl import flags
from absl import logging
import gin.tf
from gym import spaces
import numpy as np
from recsim import document
from recsim import user
from recsim.simulator import environment
from recsim.simulator import recsim_gym

FLAGS = flags.FLAGS


class LTSUserModel(user.AbstractUserModel):
  """Class to model a user with long-term satisfaction dynamics.

  Implements a controlled continuous Hidden Markov Model of the user having
  the following components.
    * State space: one dimensional real number, termed net_positive_exposure
      (abbreviated NPE);
    * controls: one dimensional control signal in [0, 1], representing the
      clickbait score of the item of content;
    * transition dynamics: net_positive_exposure is updated according to:
      NPE_(t+1) := memory_discount * NPE_t
                   + 2 * (clickbait_score - .5)
                   + N(0, innovation_stddev);
    * observation space: a nonnegative real number, representing the degree of
      engagement, e.g. econds watched from a recommended video. An observation
      is drawn from a log-normal distribution with mean

      (clickbait_score * choc_mean
                      + (1 - clickbait_score) * kale_mean) * SAT_t,

      where SAT_t = sigmoid(sensitivity * NPE_t). The observation standard
      standard deviation is similarly given by

      (clickbait_score * choc_stddev + ((1 - clickbait_score) * kale_stddev)).

      An individual user is thus represented by the combination of parameters
      (memory_discount, innovation_stddev, choc_mean, choc_stddev, kale_mean,
      kale_stddev, sensitivity), which are encapsulated in LTSUserState.

    Args:
      slate_size: An integer representing the size of the slate
      user_state_ctor: A constructor to create user state.
      response_model_ctor: A constructor function to create response. The
        function should take a string of doc ID as input and returns a
        LTSResponse object.
      seed: an integer as the seed in random sampling.
  """

  def __init__(self,
               slate_size,
               user_state_ctor=None,
               response_model_ctor=None,
               seed=0):
    if not response_model_ctor:
      raise TypeError('response_model_ctor is a required callable.')

    super(LTSUserModel, self).__init__(
        response_model_ctor,
        LTSStaticUserSampler(user_ctor=user_state_ctor, seed=seed), slate_size)

  def is_terminal(self):
    """Returns a boolean indicating if the session is over."""
    return self._user_state.time_budget <= 0

  def update_state(self, slate_documents, responses):
    """Updates the user's latent state based on responses to the slate.

    Args:
      slate_documents: a list of LTSDocuments representing the slate
      responses: a list of LTSResponses representing the user's response to each
        document in the slate.
    """

    for doc, response in zip(slate_documents, responses):
      if response.clicked:
        innovation = np.random.normal(scale=self._user_state.innovation_stddev)
        net_positive_exposure = (self._user_state.memory_discount
                                 * self._user_state.net_positive_exposure
                                 - 2.0 * (doc.clickbait_score - 0.5)
                                 + innovation
                                )
        self._user_state.net_positive_exposure = net_positive_exposure
        satisfaction = 1 / (1.0 + np.exp(-self._user_state.sensitivity
                                         * net_positive_exposure)
                           )
        self._user_state.satisfaction = satisfaction
        self._user_state.time_budget -= 1
        return

  def simulate_response(self, documents):
    """Simulates the user's response to a slate of documents with choice model.

    Args:
      documents: a list of LTSDocument objects.

    Returns:
      responses: a list of LTSResponse objects, one for each document.
    """
    # List of empty responses
    responses = [self._response_model_ctor() for _ in documents]
    # User always clicks the first item.
    selected_index = 0
    self.generate_response(documents[selected_index], responses[selected_index])
    return responses

  def generate_response(self, doc, response):
    """Generates a response to a clicked document.

    Args:
      doc: an LTSDocument object.
      response: an LTSResponse for the document.
    Updates: response, with whether the document was clicked, liked, and how
      much of it was watched.
    """
    response.clicked = True
    # linear interpolation between choc and kale.
    engagement_loc = (doc.clickbait_score * self._user_state.choc_mean
                      + (1 - doc.clickbait_score) * self._user_state.kale_mean)
    engagement_loc *= self._user_state.satisfaction
    engagement_scale = (doc.clickbait_score * self._user_state.choc_stddev
                        + ((1 - doc.clickbait_score)
                           * self._user_state.kale_stddev))
    log_engagement = np.random.normal(loc=engagement_loc,
                                      scale=engagement_scale)
    response.engagement = np.exp(log_engagement)


class LTSUserState(user.AbstractUserState):
  """Class to represent users.

  See the LTSUserModel class documentation for precise information about how the
  parameters influence user dynamics.
  Attributes:
    memory_discount: rate of forgetting of latent state.
    sensitivity: magnitude of the dependence between latent state and
      engagement.
    innovation_stddev: noise standard deviation in latent state transitions.
    choc_mean: mean of engagement with clickbaity content.
    choc_stddev: standard deviation of engagement with clickbaity content.
    kale_mean: mean of engagement with non-clickbaity content.
    kale_stddev: standard deviation of engagement with non-clickbaity content.
    net_positive_exposure: starting value for NPE (NPE_0).
    time_budget: length of a user session.
  """

  def __init__(self, memory_discount, sensitivity, innovation_stddev,
               choc_mean, choc_stddev, kale_mean, kale_stddev,
               net_positive_exposure, time_budget
              ):
    """Initializes a new user."""
    ## Transition model parameters
    ##############################
    self.memory_discount = memory_discount
    self.sensitivity = sensitivity
    self.innovation_stddev = innovation_stddev

    ## Engagement parameters
    self.choc_mean = choc_mean
    self.choc_stddev = choc_stddev
    self.kale_mean = kale_mean
    self.kale_stddev = kale_stddev

    ## State variables
    ##############################
    self.net_positive_exposure = net_positive_exposure
    self.satisfaction = 1 / (1 + np.exp(-sensitivity * net_positive_exposure))
    self.time_budget = time_budget

  def create_observation(self):
    """User's state is not observable."""
    return np.array([])

  # No choice model.
  def score_document(self, doc_obs):
    return 1

  @staticmethod
  def observation_space():
    return spaces.Box(shape=(0,), dtype=np.float32, low=0.0, high=np.inf)


@gin.configurable
class LTSStaticUserSampler(user.AbstractUserSampler):
  """Generates user with identical predetermined parameters."""
  _state_parameters = None

  def __init__(self,
               user_ctor=LTSUserState,
               memory_discount=0.7,
               sensitivity=0.01,
               innovation_stddev=0.05,
               choc_mean=5.0,
               choc_stddev=1.0,
               kale_mean=4.0,
               kale_stddev=1.0,
               time_budget=60,
               **kwargs):
    """Creates a new user state sampler."""
    logging.debug('Initialized LTSStaticUserSampler')
    self._state_parameters = {'memory_discount': memory_discount,
                              'sensitivity': sensitivity,
                              'innovation_stddev': innovation_stddev,
                              'choc_mean': choc_mean,
                              'choc_stddev': choc_stddev,
                              'kale_mean': kale_mean,
                              'kale_stddev': kale_stddev,
                              'time_budget': time_budget
                             }
    super(LTSStaticUserSampler, self).__init__(user_ctor, **kwargs)

  def sample_user(self):
    starting_npe = ((self._rng.random_sample() - .5) *
                    (1 / (1.0 - self._state_parameters['memory_discount'])))
    self._state_parameters['net_positive_exposure'] = starting_npe
    return self._user_ctor(**self._state_parameters)


class LTSResponse(user.AbstractResponse):
  """Class to represent a user's response to a document.

  Attributes:
    engagement: real number representing the degree of engagement with a
      document (e.g. watch time).
    clicked: boolean indicating whether the item was clicked or not.
  """

  # The maximum degree of engagement.
  MAX_ENGAGEMENT_MAGNITUDE = 100.0

  def __init__(self, clicked=False, engagement=0.0):
    """Creates a new user response for a document.

    Args:
      clicked: boolean indicating whether the item was clicked or not.
      engagement: real number representing the degree of engagement with a
        document (e.g. watch time).
    """
    self.clicked = clicked
    self.engagement = engagement

  def __str__(self):
    return '[' + self.engagement + ']'

  def __repr__(self):
    return self.__str__()

  def create_observation(self):
    return {'click': int(self.clicked), 'engagement': self.engagement}

  @classmethod
  def response_space(cls):
    # `engagement` feature range is [0, MAX_ENGAGEMENT_MAGNITUDE]
    return spaces.Dict({
        'click':
            spaces.Discrete(2),
        'engagement':
            spaces.Box(
                low=0.0,
                high=LTSResponse.MAX_ENGAGEMENT_MAGNITUDE,
                shape=tuple(),
                dtype=np.float32)
    })


class LTSDocument(document.AbstractDocument):
  """Class to represent an LTS Document.

  Attributes:
    clickbait_score: real number in [0,1] representing the clickbaitiness of a
      document.
  """

  def __init__(self, doc_id, clickbait_score):
    self.clickbait_score = clickbait_score
    # doc_id is an integer representing the unique ID of this document
    super(LTSDocument, self).__init__(doc_id)

  def create_observation(self):
    return np.array([self.clickbait_score])

  @staticmethod
  def observation_space():
    return spaces.Box(shape=(1,), dtype=np.float32, low=0.0, high=1.0)


class LTSDocumentSampler(document.AbstractDocumentSampler):
  """Class to sample LTSDocument documents.

    Args:
    doc_ctor: A class/constructor for the type of documents that will be sampled
      by this sampler.
  """

  def __init__(self, doc_ctor=LTSDocument, **kwargs):
    super(LTSDocumentSampler, self).__init__(doc_ctor, **kwargs)
    self._doc_count = 0

  def sample_document(self):
    doc_features = {}
    doc_features['doc_id'] = self._doc_count
    doc_features['clickbait_score'] = self._rng.random_sample()
    self._doc_count += 1
    return self._doc_ctor(**doc_features)


def clicked_engagement_reward(responses):
  """Calculates the total clicked watchtime from a list of responses.

  Args:
    responses: A list of LTSResponse objects

  Returns:
    reward: A float representing the total watch time from the responses
  """
  reward = 0.0
  for response in responses:
    if response.clicked:
      reward += response.engagement
  return reward


def create_environment(env_config):
  """Creates a long-term satisfaction environment."""

  user_model = LTSUserModel(
      env_config['slate_size'],
      user_state_ctor=LTSUserState,
      response_model_ctor=LTSResponse)

  document_sampler = LTSDocumentSampler()

  ltsenv = environment.Environment(
      user_model,
      document_sampler,
      env_config['num_candidates'],
      env_config['slate_size'],
      resample_documents=env_config['resample_documents'])

  return recsim_gym.RecSimGymEnv(ltsenv, clicked_engagement_reward)
