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
"""Simple sequential environment with known Q-function for testing purposes.

The user dynamics in this environment follow a 6 state x 4  action MDP with
the following specification:

0  # action
0 (1 0.1) (2 0.1) (3 0.8)
1 (2 0.1) (3 0.1) (4 0.8)
2 (3 0.1) (4 0.1) (5 0.8)
3 (4 0.1) (5 0.1) (0 0.8)
4 (5 1.0)
5 (0 1.0)
reward (0 -10.0) (1 0.0) (2 0.0) (3 4.0) (4 0.0) (5 5.0)

1  # action
0 (2 0.1) (3 0.1) (4 0.8)
1 (3 0.1) (4 0.1) (5 0.8)
2 (4 0.1) (5 0.1) (0 0.8)
3 (5 0.1) (0 0.1) (1 0.8)
4 (0 1.0)
5 (1 1.0)
reward (0 -10.0) (1 0.0) (2 1.0) (3 0.0) (4 0.0) (5 0.0)

2  # action
0 (3 0.1) (4 0.1) (5 0.8)
1 (4 0.1) (5 0.1) (0 0.8)
2 (5 0.1) (0 0.1) (1 0.8)
3 (0 0.1) (1 0.1) (2 0.8)
4 (1 1.0)
5 (2 1.0)
reward (0 -10.0) (1 1.0) (2 0.0) (3 2.0) (4 0.0) (5 2.0)

3  # action
0 (4 0.1) (5 0.1) (0 0.8)
1 (5 0.1) (0 0.1) (1 0.8)
2 (0 0.1) (1 0.1) (2 0.8)
3 (1 0.1) (2 0.1) (3 0.8)
4 (2 1.0)
5 (3 1.0)
reward (0 -10.0) (1 0.0) (2 0.0) (3 0.0) (4 0.0) (5 5.0)

Known Q and value functions for:

* gamma = 0
  Q-function:
            Action
  State        0          1          2          3
    0         -10        -10        -10        -10
    1                                1
    2                     1
    3          4                     2
    4
    5          5                     2          5

  Value function:
  V[0] = -10, V[1] = 1, V[2] = 1, V[3] = 4, V[4] = 0, V[5] = 5

* gamma = 0.5
  Q-function:
            Action
  State        0          1          2          3
    0         -8.53022   -8.41259   -7.10072   -12.3547
    1          1.58741    2.89928   -1.35468    1.12842
    2          2.89928   -1.35468    1.12842    0.94964
    3          1.64532    1.12842    2.94964    1.46978
    4          3.23741   -3.55036    1.44964    1.44964
    5          1.44964    1.44964    3.44964    6.47482

  Value function:
  V[0] = -7.10072, V[1] = 2.89928, V[2] = 2.89928, V[3] = 2.94964,
  V[4] = 3.23741, V[5] = 6.47482

* gamma = 0.9
  Q-function:
            Action
  State        0          1          2          3
    0          5.79888    6.59282    8.12425   -0.615864
    1          16.5928    18.1242    10.3841    15.641
    2          18.1242    10.3841    15.641     15.4118
    3          13.3841    15.641     17.4118    15.7989
    4          18.6036    7.31182    16.3118    16.3118
    5          12.3118    16.3118    18.3118    20.6706

  Value function:
  V[0] = 8.12425, V[1] = 18.1242, V[2] = 18.1242, V[3] = 17.4118,
  V[4] = 18.6036, V[5] = 20.6706
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl import flags
import gin.tf
from gym import spaces
import numpy as np

from recsim import document
from recsim import user
from recsim.simulator import environment
from recsim.simulator import recsim_gym

FLAGS = flags.FLAGS
QVALUES0 = [[-10.0, -10.0, -10.0, -10.0], [0.0, 0.0, 1.0, 0.0],
            [0.0, 1.0, 0.0, 0.0], [4.0, 0.0, 2.0, 0.0], [0.0, 0.0, 0.0, 0.0],
            [5.0, 0.0, 2.0, 5.0]]
QVALUES05 = [[-8.53022, -8.41259, -7.10072, -12.3547],
             [1.58741, 2.89928, -1.35468, 1.12842],
             [2.89928, -1.35468, 1.12842, 0.94964],
             [1.64532, 1.12842, 2.94964, 1.46978],
             [3.23741, -3.55036, 1.44964, 1.44964],
             [1.44964, 1.44964, 3.44964, 6.47482]]
QVALUES09 = [[5.79888, 6.59282, 8.12425, -0.615864],
             [16.5928, 18.1242, 10.3841, 15.641],
             [18.1242, 10.3841, 15.641, 15.4118],
             [13.3841, 15.641, 17.4118, 15.7989],
             [18.6036, 7.31182, 16.3118, 16.3118],
             [12.3118, 16.3118, 18.3118, 20.6706]]


class SimpleSequentialUserModel(user.AbstractUserModel):
  """Class to model a simple sequential user for testing.

  This is a 6-state user with dynamics described above. It can consume one of 4
  document types and transition according to a fixed transition matrix. To
  facilitate testing of Q-estimation, the entire state is emitted, i.e. the
  environment is fully observed.

  Args:
  seed: random seed.
  """

  def __init__(self,
               slate_size,
               seed=0,
               starting_probs=(1.0, 0.0, 0.0, 0.0, 0.0, 0.0)):
    super(SimpleSequentialUserModel, self).__init__(
        SimpleSequentialResponse,
        SimpleSequentialUserSampler(seed=seed, starting_probs=starting_probs),
        slate_size)
    self._transition_matrix = np.zeros((4, 6, 6))
    self._transition_matrix[0, :, :] = np.array([[0, .1, .1, .8, 0, 0],
                                                 [0, 0, .1, .1, .8, 0],
                                                 [0, 0, 0, .1, .1, .8],
                                                 [.8, 0, 0, 0, .1, .1],
                                                 [0, 0, 0, 0, 0, 1.0],
                                                 [1.0, 0, 0, 0, 0, 0]])
    self._transition_matrix[1, :, :] = np.array([[0, 0, .1, .1, .8, 0],
                                                 [0, 0, 0, .1, .1, .8],
                                                 [.8, 0, 0, 0, .1, .1],
                                                 [.1, .8, 0, 0, 0, .1],
                                                 [1.0, 0, 0, 0, 0, 0],
                                                 [0, 1.0, 0, 0, 0, 0]])
    self._transition_matrix[2, :, :] = np.array([[0, 0, 0, .1, .1, .8],
                                                 [.8, 0, 0, 0, .1, .1],
                                                 [.1, .8, 0, 0, 0, .1],
                                                 [.1, .1, .8, 0, 0, 0],
                                                 [0, 1.0, 0, 0, 0, 0],
                                                 [0, 0, 1.0, 0, 0, 0]])
    self._transition_matrix[3, :, :] = np.array([[.8, 0, 0, 0, .1, .1],
                                                 [.1, .8, 0, 0, 0, .1],
                                                 [.1, .1, .8, 0, 0, 0],
                                                 [0, .1, .1, .8, 0, 0],
                                                 [0, 0, 1.0, 0, 0, 0],
                                                 [0, 0, 0, 1.0, 0, 0]])
    self._reward_vector = np.zeros((4, 6))
    self._reward_vector[0, :] = np.array([-10.0, 0.0, 0.0, 4.0, 0.0, 5.0])
    self._reward_vector[1, :] = np.array([-10.0, 0.0, 1.0, 0.0, 0.0, 0.0])
    self._reward_vector[2, :] = np.array([-10.0, 1.0, 0.0, 2.0, 0.0, 2.0])
    self._reward_vector[3, :] = np.array([-10.0, 0.0, 0.0, 0.0, 0.0, 5.0])

  def is_terminal(self):
    """Returns a boolean indicating if the session is over."""
    return False

  def update_state(self, slate_documents, responses):
    doc = slate_documents[0]
    next_state = np.random.choice(
        6, p=self._transition_matrix[doc.action_id, self._user_state.state])
    self._user_state = SimpleSequentialUserState(next_state)
    return

  def simulate_response(self, documents):
    """Simulates the user's response to a slate of documents with choice model.

    Args:
      documents: a list of SimpleSequentialDocument objects in the slate.

    Returns:
      responses: a list of SimpleSequentialResponse objects,
        one for each document.
    """
    # List of empty responses
    responses = [self._response_model_ctor() for _ in documents]
    # Always pick the first document in the slate
    selected_index = 0
    self._generate_response(documents[selected_index],
                            responses[selected_index])
    return responses

  def _generate_response(self, doc, response):
    """Trivial response: sets the clicked property of a clicked document.

    Args:
      doc: a SimpleSequentialDocument object.
      response: a SimpleSequentialResponse for the document.
    Updates: response, with whether the document was clicked.
    """
    response.reward = self._reward_vector[doc.action_id, self._user_state.state]


class SimpleSequentialUserState(user.AbstractUserState):
  """Class to represent user state for testing. Fully observed.

  Attributes:
    state: integer in [0...5] representing the state of the user Markov Chain.
  """

  def __init__(self, state):
    """Initializes a new user."""
    self.state = state

  def create_observation(self):
    return self.state

  def observation_space(self):
    return spaces.Discrete(6)

  def score_document(self, doc_obs):
    del doc_obs  # unused
    return 1.0


@gin.configurable
class SimpleSequentialUserSampler(user.AbstractUserSampler):
  """Samples initial user state from a multinomial distribution.


    Args:
      probs: 6-outcome probability mass function for sampling initial state.
  """

  def __init__(self, starting_probs=(1.0, 0, 0, 0, 0, 0), **kwargs):
    self._probs = starting_probs
    super(SimpleSequentialUserSampler, self).__init__(SimpleSequentialUserState,
                                                      **kwargs)

  def sample_user(self):
    starting_state = np.random.choice(6, p=self._probs)
    return SimpleSequentialUserState(starting_state)


class SimpleSequentialResponse(user.AbstractResponse):
  """Class to represent a user's response to a document.

  Attributes:
    reward: a real number representing the state reward of the action executed
      by the document.
  """

  # The max possible doc ID. We assume the doc ID is in range [0, MAX_DOC_ID].
  MAX_DOC_ID = None

  def __init__(self, reward=0.0):
    self.reward = reward

  def __str__(self):
    return str(self.reward)

  def __repr__(self):
    return self.__str__()

  def create_observation(self):
    return {'reward': np.array(self.reward)}

  @classmethod
  def response_space(cls):
    return spaces.Dict({
        'reward':
            spaces.Box(low=-10.0, high=5.0, shape=tuple(), dtype=np.float32)
    })


class SimpleSequentialDocument(document.AbstractDocument):
  """Class to represent an Simple Sequential Document.

  Attributes:
    doc_id: integer represents the document id.
    action_id: integer represents one of the 4 available actions.
  """

  def __init__(self, doc_id, action_id):
    self.action_id = action_id
    super(SimpleSequentialDocument, self).__init__(doc_id)

  def create_observation(self):
    return self.action_id

  def observation_space(self):
    return spaces.Discrete(4)


@gin.configurable
class SimpleSequentialDocumentSampler(document.AbstractDocumentSampler):
  """Round robin a selection of all 4 actions.

  As long as the number of candidates is more than 4, this guarantees that all
  actions will be available.
  """

  def __init__(self, **kwargs):
    self._last_action_id = -1
    self._doc_count = 0

    super(SimpleSequentialDocumentSampler,
          self).__init__(SimpleSequentialDocument, **kwargs)

  def sample_document(self):
    self._last_action_id += 1
    self._last_action_id %= 4
    self._doc_count += 1
    return self._doc_ctor(self._doc_count, self._last_action_id)


def total_reward(responses):
  """Calculates the total reward from a list of responses.

  Args:
     responses: A list of SimpleSequentialResponse objects

  Returns:
    reward: A float representing the total clicks from the responses
  """
  reward = 0.0
  for r in responses:
    reward += r.reward
  return reward


def create_environment(env_config):
  """Creates an simple sequential testing environment."""
  if env_config['num_candidates'] < 4:
    raise ValueError('num_candidates must be at least 4.')

  SimpleSequentialResponse.MAX_DOC_ID = env_config['num_candidates'] - 1
  user_model = SimpleSequentialUserModel(
      env_config['slate_size'],
      seed=env_config['seed'],
      starting_probs=env_config['starting_probs'])
  document_sampler = SimpleSequentialDocumentSampler(seed=env_config['seed'])
  simple_seq_env = environment.Environment(
      user_model,
      document_sampler,
      env_config['num_candidates'],
      env_config['slate_size'],
      resample_documents=env_config['resample_documents'])

  return recsim_gym.RecSimGymEnv(simple_seq_env, total_reward,
                                 lambda _, __, ___: None, lambda _, __: None)
