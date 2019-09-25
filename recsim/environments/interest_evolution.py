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
"""Classes to represent the interest evolution documents and users."""

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


class IEvResponse(user.AbstractResponse):
  """Class to represent a user's response to a video.

  Attributes:
    clicked: A boolean indicating whether the video was clicked.
    watch_time: A float for fraction of the video watched.
    liked: A boolean indicating whether the video was liked.
    quality: A float indicating the quality of the video.
    cluster_id: A integer representing the cluster ID of the video.
  """

  # The min quality score.
  MIN_QUALITY_SCORE = -100
  # The max quality score.
  MAX_QUALITY_SCORE = 100

  def __init__(self,
               clicked=False,
               watch_time=0.0,
               liked=False,
               quality=0.0,
               cluster_id=0.0):
    """Creates a new user response for a video.

    Args:
      clicked: A boolean indicating whether the video was clicked
      watch_time: A float for fraction of the video watched
      liked: A boolean indicating whether the video was liked
      quality: A float for document quality
      cluster_id: a integer for the cluster ID of the document.
    """
    self.clicked = clicked
    self.watch_time = watch_time
    self.liked = liked
    self.quality = quality
    self.cluster_id = cluster_id

  def create_observation(self):
    return {
        'click': int(self.clicked),
        'watch_time': self.watch_time,
        'liked': int(self.liked),
        'quality': self.quality,
        'cluster_id': int(self.cluster_id)
    }

  @classmethod
  def response_space(cls):
    # `clicked` feature range is [0, 1]
    # `watch_time` feature range is [0, MAX_VIDEO_LENGTH]
    # `liked` feature range is [0, 1]
    # `quality`: the quality of the document and range is specified by
    #    [MIN_QUALITY_SCORE, MAX_QUALITY_SCORE].
    # `cluster_id`: the cluster the document belongs to and its range is
    # .  [0, IEvVideo.NUM_FEATURES].
    return spaces.Dict({
        'click':
            spaces.Discrete(2),
        'watch_time':
            spaces.Box(
                low=0.0,
                high=IEvVideo.MAX_VIDEO_LENGTH,
                shape=tuple(),
                dtype=np.float32),
        'liked':
            spaces.Discrete(2),
        'quality':
            spaces.Box(
                low=cls.MIN_QUALITY_SCORE,
                high=cls.MAX_QUALITY_SCORE,
                shape=tuple(),
                dtype=np.float32),
        'cluster_id':
            spaces.Discrete(IEvVideo.NUM_FEATURES)
    })


class IEvVideo(document.AbstractDocument):
  """Class to represent a interest evolution Video.

  Attributes:
    features: A numpy array that stores video features.
    cluster_id: An integer that represents.
    video_length : A float for video length.
    quality: a float the represents document quality.
  """

  # The maximum length of videos.
  MAX_VIDEO_LENGTH = 100.0

  # The number of features to represent each video.
  NUM_FEATURES = 20

  def __init__(self,
               doc_id,
               features,
               cluster_id=None,
               video_length=None,
               quality=None):
    """Generates a random set of features for this interest evolution Video."""

    # Document features (i.e. distribution over topics)
    self.features = features

    # Cluster ID
    self.cluster_id = cluster_id

    # Length of video
    self.video_length = video_length

    # Document quality (i.e. trashiness/nutritiousness)
    self.quality = quality

    # doc_id is an integer representing the unique ID of this document
    super(IEvVideo, self).__init__(doc_id)

  def create_observation(self):
    """Returns observable properties of this document as a float array."""
    return self.features

  @classmethod
  def observation_space(cls):
    return spaces.Box(
        shape=(cls.NUM_FEATURES,), dtype=np.float32, low=-1.0, high=1.0)


class IEvVideoSampler(document.AbstractDocumentSampler):
  """Class to sample interest_evolution videos."""

  def __init__(self,
               doc_ctor=IEvVideo,
               min_feature_value=-1.0,
               max_feature_value=1.0,
               video_length_mean=4.3,
               video_length_std=1.0,
               **kwargs):
    """Creates a new interest evolution video sampler.

    Args:
      doc_ctor: A class/constructor for the type of videos that will be sampled
        by this sampler.
      min_feature_value: A float for the min feature value.
      max_feature_value: A float for the max feature value.
      video_length_mean: A float for the mean of the video length.
      video_length_std: A float for the std deviation of video length.
      **kwargs: other keyword parameters for the video sampler.
    """
    super(IEvVideoSampler, self).__init__(doc_ctor, **kwargs)
    self._doc_count = 0
    self._min_feature_value = min_feature_value
    self._max_feature_value = max_feature_value
    self._video_length_mean = video_length_mean
    self._video_length_std = video_length_std

  def sample_document(self):
    doc_features = {}
    doc_features['doc_id'] = self._doc_count
    # For now, assume the document properties are uniform random.
    # It will probably make more sense to concentrate the interests around a few
    # (e.g. 5?) categories or have a more sophisticated generative process?
    doc_features['features'] = self._rng.uniform(
        self._min_feature_value, self._max_feature_value,
        self.get_doc_ctor().NUM_FEATURES)
    doc_features['video_length'] = min(
        self._rng.normal(self._video_length_mean, self._video_length_std),
        self.get_doc_ctor().MAX_VIDEO_LENGTH)
    doc_features['quality'] = 1.0
    self._doc_count += 1
    return self._doc_ctor(**doc_features)


class UtilityModelVideoSampler(document.AbstractDocumentSampler):
  """Class that samples videos for utility model experiment."""

  def __init__(self,
               doc_ctor=IEvVideo,
               min_utility=-3.0,
               max_utility=3.0,
               video_length=4.0,
               **kwargs):
    """Creates a new utility model video sampler.

    Args:
      doc_ctor: A class/constructor for the type of videos that will be sampled
        by this sampler.
      min_utility: A float for the min utility score.
      max_utility: A float for the max utility score.
      video_length: A float for the video_length in minutes.
      **kwargs: other keyword parameters for the video sampler.
    """
    super(UtilityModelVideoSampler, self).__init__(doc_ctor, **kwargs)
    self._doc_count = 0
    self._num_clusters = self.get_doc_ctor().NUM_FEATURES
    self._min_utility = min_utility
    self._max_utility = max_utility
    self._video_length = video_length

    # Linearly space utility according to cluster ID
    # cluster 0 will get min_utility. cluster
    # NUM_FEATURES - 1 will get max_utility
    # In between will be spaced as follows
    trashy = np.linspace(self._min_utility, 0, int(self._num_clusters * 0.7))
    nutritious = np.linspace(0, self._max_utility,
                             int(self._num_clusters * 0.3))
    self.cluster_means = np.concatenate((trashy, nutritious))

  def sample_document(self):
    doc_features = {}
    doc_features['doc_id'] = self._doc_count

    # Sample a cluster_id. Assumes there are NUM_FEATURE clusters.
    cluster_id = self._rng.randint(0, self._num_clusters)
    doc_features['cluster_id'] = cluster_id

    # Features are a 1-hot encoding of cluster id
    features = np.zeros(self._num_clusters)
    features[cluster_id] = 1.0
    doc_features['features'] = features

    # Fixed video lengths (in minutes)
    doc_features['video_length'] = self._video_length

    # Quality
    quality_mean = self.cluster_means[cluster_id]

    # Variance fixed
    quality_variance = 0.1
    doc_features['quality'] = self._rng.normal(quality_mean, quality_variance)

    self._doc_count += 1
    return self._doc_ctor(**doc_features)


class IEvUserState(user.AbstractUserState):
  """Class to represent interest evolution users."""

  # Number of features in the user state representation.
  NUM_FEATURES = 20

  def __init__(self,
               user_interests,
               time_budget=None,
               score_scaling=None,
               attention_prob=None,
               no_click_mass=None,
               keep_interact_prob=None,
               min_doc_utility=None,
               user_update_alpha=None,
               watched_videos=None,
               impressed_videos=None,
               liked_videos=None,
               step_penalty=None,
               min_normalizer=None,
               user_quality_factor=None,
               document_quality_factor=None):
    """Initializes a new user."""

    # Only user_interests is required, since it is needed to create an
    # observation. It is the responsibility of the designer to make sure any
    # other variables that are needed in the user choice/transition model are
    # also provided.

    ## User features
    #######################

    # The user's interests (1 = very interested, -1 = disgust)
    # Another option could be to represent in [0,1] e.g. by dirichlet
    self.user_interests = user_interests

    # Amount of time in minutes this user has left in session.
    self.time_budget = time_budget

    # Probability of interacting with another element on the same slate
    self.keep_interact_prob = keep_interact_prob

    # Min utility to interact with a document
    self.min_doc_utility = min_doc_utility

    # Convenience wrapper
    self.choice_features = {
        'score_scaling': score_scaling,
        # Factor of attention to give for subsequent items on slate
        # Item i on a slate will get attention (attention_prob)^i
        'attention_prob': attention_prob,
        # Mass that user does not click on any item in the slate
        'no_click_mass': no_click_mass,
        # If using the multinomial proportion model with negative scores, this
        # negative value will be subtracted from all scores to make a valid
        # distribution for sampling.
        'min_normalizer': min_normalizer
    }

    ## Transition model parameters
    ##############################

    # Step size for updating user interests based on watched videos (small!)
    # We may want to have different values for different interests
    # to represent how malleable those interests are (e.g. strong dislikes may
    # be less malleable).
    self.user_update_alpha = user_update_alpha

    # A step penalty applied when no item is selected (e.g. the time wasted
    # looking through a slate but not clicking, and any loss of interest)
    self.step_penalty = step_penalty

    # How much to weigh the user quality when updating budget
    self.user_quality_factor = user_quality_factor
    # How much to weigh the document quality when updating budget
    self.document_quality_factor = document_quality_factor

    # Observable user features (these are just examples for now)
    ###########################

    # Video IDs of videos that have been watched
    self.watched_videos = watched_videos

    # Video IDs of videos that have been impressed
    self.impressed_videos = impressed_videos

    # Video IDs of liked videos
    self.liked_videos = liked_videos

  def score_document(self, doc_obs):
    if self.user_interests.shape != doc_obs.shape:
      raise ValueError('User and document feature dimension mismatch!')
    return np.dot(self.user_interests, doc_obs)

  def create_observation(self):
    """Return an observation of this user's observable state."""
    return self.user_interests

  @classmethod
  def observation_space(cls):
    return spaces.Box(
        shape=(cls.NUM_FEATURES,), dtype=np.float32, low=-1.0, high=1.0)


class IEvUserDistributionSampler(user.AbstractUserSampler):
  """Class to sample users by a hardcoded distribution."""

  def __init__(self, user_ctor=IEvUserState, **kwargs):
    """Creates a new user state sampler."""
    logging.debug('Initialized IEvUserDistributionSampler')
    super(IEvUserDistributionSampler, self).__init__(user_ctor, **kwargs)

  def sample_user(self):
    """Samples a new user, with a new set of features."""

    features = {}
    features['user_interests'] = self._rng.uniform(
        -1.0, 1.0,
        self.get_user_ctor().NUM_FEATURES)
    features['time_budget'] = 30
    features['score_scaling'] = 0.05
    features['attention_prob'] = 0.9
    features['no_click_mass'] = 1
    features['keep_interact_prob'] = self._rng.beta(1, 3, 1)
    features['min_doc_utility'] = 0.1
    features['user_update_alpha'] = 0
    features['watched_videos'] = set()
    features['impressed_videos'] = set()
    features['liked_videos'] = set()
    features['step_penalty'] = 1.0
    features['min_normalizer'] = -1.0
    features['user_quality_factor'] = 1.0
    features['document_quality_factor'] = 1.0
    return self._user_ctor(**features)


@gin.configurable
class UtilityModelUserSampler(user.AbstractUserSampler):
  """Class that samples users for utility model experiment."""

  def __init__(self,
               user_ctor=IEvUserState,
               document_quality_factor=1.0,
               no_click_mass=1.0,
               min_normalizer=-1.0,
               **kwargs):
    """Creates a new user state sampler."""
    logging.debug('Initialized UtilityModelUserSampler')
    self._no_click_mass = no_click_mass
    self._min_normalizer = min_normalizer
    self._document_quality_factor = document_quality_factor
    super(UtilityModelUserSampler, self).__init__(user_ctor, **kwargs)

  def sample_user(self):
    features = {}
    # Interests are distributed uniformly randomly
    features['user_interests'] = self._rng.uniform(
        -1.0, 1.0,
        self.get_user_ctor().NUM_FEATURES)
    # Assume all users have fixed amount of time
    features['time_budget'] = 200.0  # 120.0
    features['no_click_mass'] = self._no_click_mass
    features['step_penalty'] = 0.5
    features['score_scaling'] = 0.05
    features['attention_prob'] = 0.65
    features['min_normalizer'] = self._min_normalizer
    features['user_quality_factor'] = 0.0
    features['document_quality_factor'] = self._document_quality_factor

    # Fraction of video length we can extend (or cut) budget by
    # Maybe this should be a parameter that varies by user?
    alpha = 0.9
    # In our setup, utility is just doc_quality as user_quality_factor is 0.
    # doc_quality is distributed normally ~ N([-3,3], 0.1) for a 3 sigma range
    # of [-3.3,3.3]. Therefore, we normalize doc_quality by 3.4 (adding a little
    # extra in case) to get in [-1,1].
    utility_range = 1.0 / 3.4
    features['user_update_alpha'] = alpha * utility_range
    return self._user_ctor(**features)


class IEvUserModel(user.AbstractUserModel):
  """Class to model an interest evolution user.

  Assumes the user state contains:
    - user_interests
    - time_budget
    - no_click_mass
  """

  def __init__(self,
               slate_size,
               choice_model_ctor=None,
               response_model_ctor=IEvResponse,
               user_state_ctor=IEvUserState,
               no_click_mass=1.0,
               seed=0,
               alpha_x_intercept=1.0,
               alpha_y_intercept=0.3):
    """Initializes a new user model.

    Args:
      slate_size: An integer representing the size of the slate
      choice_model_ctor: A contructor function to create user choice model.
      response_model_ctor: A constructor function to create response. The
        function should take a string of doc ID as input and returns a
        IEvResponse object.
      user_state_ctor: A constructor to create user state
      no_click_mass: A float that will be passed to compute probability of no
        click.
      seed: A integer used as the seed of the choice model.
      alpha_x_intercept: A float for the x intercept of the line used to compute
        interests update factor.
      alpha_y_intercept: A float for the y intercept of the line used to compute
        interests update factor.

    Raises:
      Exception: if choice_model_ctor is not specified.
    """
    super(IEvUserModel, self).__init__(
        response_model_ctor,
        UtilityModelUserSampler(
            user_ctor=user_state_ctor, no_click_mass=no_click_mass, seed=seed),
        slate_size)
    if choice_model_ctor is None:
      raise Exception('A choice model needs to be specified!')
    self.choice_model = choice_model_ctor(self._user_state.choice_features)

    self._alpha_x_intercept = alpha_x_intercept
    self._alpha_y_intercept = alpha_y_intercept

  def is_terminal(self):
    """Returns a boolean indicating if the session is over."""
    return self._user_state.time_budget <= 0

  def update_state(self, slate_documents, responses):
    """Updates the user state based on responses to the slate.

    This function assumes only 1 response per slate. If a video is watched, we
    update the user's interests some small step size alpha based on the
    user's interest in that topic. The update is either towards the
    video's features or away, and is determined stochastically by the user's
    interest in that document.

    Args:
      slate_documents: a list of IEvVideos representing the slate
      responses: a list of IEvResponses representing the user's response to each
        video in the slate.
    """

    user_state = self._user_state

    # Step size should vary based on interest.
    def compute_alpha(x, x_intercept, y_intercept):
      return (-y_intercept / x_intercept) * np.absolute(x) + y_intercept

    for doc, response in zip(slate_documents, responses):
      if response.clicked:
        self.choice_model.score_documents(
            user_state, [doc.create_observation()])
        # scores is a list of length 1 since only one doc observation is set.
        expected_utility = self.choice_model.scores[0]
        ## Update interests
        target = doc.features - user_state.user_interests
        mask = doc.features
        alpha = compute_alpha(user_state.user_interests,
                              self._alpha_x_intercept, self._alpha_y_intercept)

        update = alpha * mask * target
        positive_update_prob = np.dot((user_state.user_interests + 1.0) / 2,
                                      mask)
        flip = np.random.rand(1)
        if flip < positive_update_prob:
          user_state.user_interests += update
        else:
          user_state.user_interests -= update
        user_state.user_interests = np.clip(user_state.user_interests, -1.0,
                                            1.0)
        ## Update budget
        received_utility = (
            user_state.user_quality_factor * expected_utility) + (
                user_state.document_quality_factor * doc.quality)
        user_state.time_budget -= response.watch_time
        user_state.time_budget += (
            user_state.user_update_alpha * response.watch_time *
            received_utility)
        return

    # Step penalty if no selection
    user_state.time_budget -= user_state.step_penalty

  def simulate_response(self, documents):
    """Simulates the user's response to a slate of documents with choice model.

    Args:
      documents: a list of IEvVideo objects

    Returns:
      responses: a list of IEvResponse objects, one for each document
    """
    # List of empty responses
    responses = [self._response_model_ctor() for _ in documents]

    # Sample some clicked responses using user's choice model and populate
    # responses.
    doc_obs = [doc.create_observation() for doc in documents]
    self.choice_model.score_documents(self._user_state, doc_obs)
    selected_index = self.choice_model.choose_item()

    for i, response in enumerate(responses):
      response.quality = documents[i].quality
      response.cluster_id = documents[i].cluster_id

    if selected_index is None:
      return responses
    self._generate_click_response(documents[selected_index],
                                  responses[selected_index])

    return responses

  def _generate_click_response(self, doc, response):
    """Generates a response to a clicked document.

    Right now we assume watch_time is a fixed value that is the minium value of
    time_budget and video_length. In the future, we may want to try more
    variations of watch_time definition.

    Args:
      doc: an IEvVideo object
      response: am IEvResponse for the document
    Updates: response, with whether the document was clicked, liked, and how
      much of it was watched
    """
    user_state = self._user_state
    response.clicked = True
    response.watch_time = min(user_state.time_budget, doc.video_length)


def clicked_watchtime_reward(responses):
  """Calculates the total clicked watchtime from a list of responses.

  Args:
    responses: A list of IEvResponse objects

  Returns:
    reward: A float representing the total watch time from the responses
  """
  reward = 0.0
  for response in responses:
    if response.clicked:
      reward += response.watch_time
  return reward


def total_clicks_reward(responses):
  """Calculates the total number of clicks from a list of responses.

  Args:
     responses: A list of IEvResponse objects

  Returns:
    reward: A float representing the total clicks from the responses
  """
  reward = 0.0
  for r in responses:
    reward += r.clicked
  return reward


def create_environment(env_config):
  """Creates an interest evolution environment."""

  user_model = IEvUserModel(
      env_config['slate_size'],
      choice_model_ctor=choice_model.MultinomialProportionalChoiceModel,
      response_model_ctor=IEvResponse,
      user_state_ctor=IEvUserState,
      seed=env_config['seed'])

  document_sampler = UtilityModelVideoSampler(
      doc_ctor=IEvVideo, seed=env_config['seed'])

  ievenv = environment.Environment(
      user_model,
      document_sampler,
      env_config['num_candidates'],
      env_config['slate_size'],
      resample_documents=env_config['resample_documents'])

  return recsim_gym.RecSimGymEnv(ievenv, clicked_watchtime_reward,
                                 utils.aggregate_video_cluster_metrics,
                                 utils.write_video_cluster_metrics)
