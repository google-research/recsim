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
"""Agent that implements the Slate-Q algorithms."""
import gin.tf
import numpy as np
from recsim import agent as abstract_agent
from recsim import choice_model
from recsim.agents.dopamine import dqn_agent
import tensorflow as tf


def compute_probs_tf(slate, scores_tf, score_no_click_tf):
  """Computes the selection probability and returns selected index.

  This assumes scores are normalizable, e.g., scores cannot be negative.

  Args:
    slate: a list of integers that represents the video slate.
    scores_tf: a float tensor that stores the scores of all documents.
    score_no_click_tf: a float tensor that represents the score for the action
      of picking no document.

  Returns:
    A float tensor that represents the probabilities of selecting each document
      in the slate.
  """
  all_scores = tf.concat([
      tf.gather(scores_tf, slate),
      tf.reshape(score_no_click_tf, (1, 1))
  ], axis=0)  # pyformat: disable
  all_probs = all_scores / tf.reduce_sum(input_tensor=all_scores)
  return all_probs[:-1]


def score_documents_tf(user_obs,
                       doc_obs,
                       no_click_mass=1.0,
                       is_mnl=False,
                       min_normalizer=-1.0):
  """Computes unnormalized scores given both user and document observations.

  This implements both multinomial proportional model and multinormial logit
    model given some parameters. We also assume scores are based on inner
    products of user_obs and doc_obs.

  Args:
    user_obs: An instance of AbstractUserState.
    doc_obs: A numpy array that represents the observation of all documents in
      the candidate set.
    no_click_mass: a float indicating the mass given to a no click option
    is_mnl: whether to use a multinomial logit model instead of a multinomial
      proportional model.
    min_normalizer: A float (<= 0) used to offset the scores to be positive when
      using multinomial proportional model.

  Returns:
    A float tensor that stores unnormalzied scores of documents and a float
      tensor that represents the score for the action of picking no document.
  """
  user_obs = tf.reshape(user_obs, [1, -1])
  scores = tf.reduce_sum(input_tensor=tf.multiply(user_obs, doc_obs), axis=1)
  all_scores = tf.concat([scores, tf.constant([no_click_mass])], axis=0)
  if is_mnl:
    all_scores = tf.nn.softmax(all_scores)
  else:
    all_scores = all_scores - min_normalizer
  return all_scores[:-1], all_scores[-1]


def score_documents(user_obs,
                    doc_obs,
                    no_click_mass=1.0,
                    is_mnl=False,
                    min_normalizer=-1.0):
  """Computes unnormalized scores given both user and document observations.

  Similar to score_documents_tf but works on NumPy objects.

  Args:
    user_obs: An instance of AbstractUserState.
    doc_obs: A numpy array that represents the observation of all documents in
      the candidate set.
    no_click_mass: a float indicating the mass given to a no click option
    is_mnl: whether to use a multinomial logit model instead of a multinomial
      proportional model.
    min_normalizer: A float (<= 0) used to offset the scores to be positive when
      using multinomial proportional model.

  Returns:
    A float array that stores unnormalzied scores of documents and a float
      number that represents the score for the action of picking no document.
  """
  scores = np.array([])
  for doc in doc_obs:
    scores = np.append(scores, np.dot(user_obs, doc))

  all_scores = np.append(scores, no_click_mass)
  if is_mnl:
    all_scores = choice_model.softmax(all_scores)
  else:
    all_scores = all_scores - min_normalizer
  assert not all_scores[
      all_scores < 0.0], 'Normalized scores have non-positive elements.'
  return all_scores[:-1], all_scores[-1]


def select_slate_topk(slate_size, s_no_click, s, q):
  """Selects the slate using the top-K algorithm.

  This algorithm corresponds to the method "TS" in
  Ie et al. https://arxiv.org/abs/1905.12767.

  Args:
    slate_size: int, the size of the recommendation slate.
    s_no_click: float tensor, the score for not clicking any document.
    s: [num_of_documents] tensor, the scores for clicking documents.
    q: [num_of_documents] tensor, the predicted q values for documents.

  Returns:
    [slate_size] tensor, the selected slate.
  """
  del s_no_click  # Unused argument.
  _, output_slate = tf.math.top_k(s * q, k=slate_size)
  return output_slate


def select_slate_greedy(slate_size, s_no_click, s, q):
  """Selects the slate using the adaptive greedy algorithm.

  This algorithm corresponds to the method "GS" in
  Ie et al. https://arxiv.org/abs/1905.12767.

  Args:
    slate_size: int, the size of the recommendation slate.
    s_no_click: float tensor, the score for not clicking any document.
    s: [num_of_documents] tensor, the scores for clicking documents.
    q: [num_of_documents] tensor, the predicted q values for documents.

  Returns:
    [slate_size] tensor, the selected slate.
  """

  def argmax(v, mask):
    return tf.argmax(
        input=(v - tf.reduce_min(input_tensor=v) + 1) * mask, axis=0)

  numerator = tf.constant(0.)
  denominator = tf.constant(0.) + s_no_click
  mask = tf.ones(tf.shape(input=q)[0])

  def set_element(v, i, x):
    mask = tf.one_hot(i, tf.shape(input=v)[0])
    v_new = tf.ones_like(v) * x
    return tf.compat.v1.where(tf.equal(mask, 1), v_new, v)

  for _ in range(slate_size):
    k = argmax((numerator + s * q) / (denominator + s), mask)
    mask = set_element(mask, k, 0)
    numerator = numerator + tf.gather(s * q, k)
    denominator = denominator + tf.gather(s, k)

  output_slate = tf.compat.v1.where(tf.equal(mask, 0))
  return output_slate


def select_slate_optimal(slate_size, s_no_click, s, q):
  """Selects the slate using exhaustive search.

  This algorithm corresponds to the method "OS" in
  Ie et al. https://arxiv.org/abs/1905.12767.

  Args:
    slate_size: int, the size of the recommendation slate.
    s_no_click: float tensor, the score for not clicking any document.
    s: [num_of_documents] tensor, the scores for clicking documents.
    q: [num_of_documents] tensor, the predicted q values for documents.

  Returns:
    [slate_size] tensor, the selected slate.
  """

  num_candidates = s.shape.as_list()[0]

  # Obtain all possible slates given current docs in the candidate set.
  mesh_args = [list(range(num_candidates))] * slate_size
  slates = tf.stack(tf.meshgrid(*mesh_args), axis=-1)
  slates = tf.reshape(slates, shape=(-1, slate_size))

  # Filter slates that include duplicates to ensure each document is picked
  # at most once.
  unique_mask = tf.map_fn(
      lambda x: tf.equal(tf.size(input=x), tf.size(input=tf.unique(x)[0])),
      slates,
      dtype=tf.bool)
  slates = tf.boolean_mask(tensor=slates, mask=unique_mask)

  slate_q_values = tf.gather(s * q, slates)
  slate_scores = tf.gather(s, slates)
  slate_normalizer = tf.reduce_sum(
      input_tensor=slate_scores, axis=1) + s_no_click

  slate_q_values = slate_q_values / tf.expand_dims(slate_normalizer, 1)
  slate_sum_q_values = tf.reduce_sum(input_tensor=slate_q_values, axis=1)
  max_q_slate_index = tf.argmax(input=slate_sum_q_values)
  return tf.gather(slates, max_q_slate_index, axis=0)


def compute_target_sarsa(reward, gamma, next_actions, next_q_values,
                         next_states, terminals):
  """Computes the SARSA target Q value.

  Args:
    reward: [batch_size] tensor, the immediate reward.
    gamma: float, discount factor with the usual RL meaning.
    next_actions: [batch_size, slate_size] tensor, the next slate.
    next_q_values: [batch_size, num_of_documents] tensor, the q values of the
      documents in the next step.
    next_states: [batch_size, 1 + num_of_documents] tensor, the features for the
      user and the docuemnts in the next step.
    terminals: [batch_size] tensor, indicating if this is a terminal step.

  Returns:
    [batch_size] tensor, the target q values.
  """
  stack_number = -1
  user_obs = next_states[:, 0, :, stack_number]
  doc_obs = next_states[:, 1:, :, stack_number]

  batch_size = next_q_values.get_shape().as_list()[0]
  next_sarsa_q_list = []
  for i in range(batch_size):
    s, s_no_click = score_documents_tf(user_obs[i], doc_obs[i])
    q = next_q_values[i]

    slate = tf.expand_dims(next_actions[i], 1)
    p_selected = compute_probs_tf(slate, s, s_no_click)
    q_selected = tf.gather(q, slate)
    next_sarsa_q_list.append(
        tf.reduce_sum(input_tensor=p_selected * q_selected))

  next_sarsa_q_values = tf.stack(next_sarsa_q_list)

  return reward + gamma * next_sarsa_q_values * (1. -
                                                 tf.cast(terminals, tf.float32))


# The top-K and greedy algorithms rely on the fact that the
# probs[slate] = normalize(scores[slate], score_no_click)
def compute_target_greedy_q(reward, gamma, next_actions, next_q_values,
                            next_states, terminals):
  """Computes the optimal target Q value with the adaptive greedy algorithm.

  This algorithm corresponds to the method "GT" in
  Ie et al. https://arxiv.org/abs/1905.12767..

  Args:
    reward: [batch_size] tensor, the immediate reward.
    gamma: float, discount factor with the usual RL meaning.
    next_actions: [batch_size, slate_size] tensor, the next slate.
    next_q_values: [batch_size, num_of_documents] tensor, the q values of the
      documents in the next step.
    next_states: [batch_size, 1 + num_of_documents] tensor, the features for the
      user and the docuemnts in the next step.
    terminals: [batch_size] tensor, indicating if this is a terminal step.

  Returns:
    [batch_size] tensor, the target q values.
  """
  slate_size = next_actions.get_shape().as_list()[1]
  stack_number = -1
  user_obs = next_states[:, 0, :, stack_number]
  doc_obs = next_states[:, 1:, :, stack_number]

  batch_size = next_q_values.get_shape().as_list()[0]
  next_greedy_q_list = []
  for i in range(batch_size):
    s, s_no_click = score_documents_tf(user_obs[i], doc_obs[i])
    q = next_q_values[i]

    slate = select_slate_greedy(slate_size, s_no_click, s, q)
    p_selected = compute_probs_tf(slate, s, s_no_click)
    q_selected = tf.gather(q, slate)
    next_greedy_q_list.append(
        tf.reduce_sum(input_tensor=p_selected * q_selected))

  next_greedy_q_values = tf.stack(next_greedy_q_list)

  return reward + gamma * next_greedy_q_values * (
      1. - tf.cast(terminals, tf.float32))


def _get_unnormalized_scores(states):
  """Computes the unnormalized scores for the docs."""
  stack_number = -1
  user_obs = states[:, 0, :, stack_number]
  doc_obs = states[:, 1:, :, stack_number]

  batch_size = states.get_shape().as_list()[0]
  scores_list = []
  score_no_click_list = []
  for i in range(batch_size):
    scores_tf, score_no_click_tf = score_documents_tf(user_obs[i], doc_obs[i])
    scores_list.append(scores_tf)
    score_no_click_list.append(score_no_click_tf)
  scores = tf.stack(scores_list)
  score_no_click = tf.stack(score_no_click_list)

  return scores, score_no_click


def compute_target_topk_q(reward, gamma, next_actions, next_q_values,
                          next_states, terminals):
  """Computes the optimal target Q value with the greedy algorithm.

  This algorithm corresponds to the method "TT" in
  Ie et al. https://arxiv.org/abs/1905.12767.

  Args:
    reward: [batch_size] tensor, the immediate reward.
    gamma: float, discount factor with the usual RL meaning.
    next_actions: [batch_size, slate_size] tensor, the next slate.
    next_q_values: [batch_size, num_of_documents] tensor, the q values of the
      documents in the next step.
    next_states: [batch_size, 1 + num_of_documents] tensor, the features for the
      user and the docuemnts in the next step.
    terminals: [batch_size] tensor, indicating if this is a terminal step.

  Returns:
    [batch_size] tensor, the target q values.
  """
  slate_size = next_actions.get_shape().as_list()[1]
  scores, score_no_click = _get_unnormalized_scores(next_states)

  # Choose the documents with top affinity_scores * Q values to fill a slate and
  # treat it as if it is the optimal slate.
  unnormalized_next_q_target = next_q_values * scores
  _, topk_optimal_slate = tf.math.top_k(
      unnormalized_next_q_target, k=slate_size)

  # Get the expected Q-value of the slate containing top-K items.
  # [batch_size, slate_size]
  next_q_values_selected = tf.compat.v1.batch_gather(
      next_q_values, tf.cast(topk_optimal_slate, dtype=tf.int32))

  # Get normalized affinity scores on the slate.
  # [batch_size, slate_size]
  scores_selected = tf.compat.v1.batch_gather(
      scores, tf.cast(topk_optimal_slate, dtype=tf.int32))

  next_q_target_topk = tf.reduce_sum(
      input_tensor=next_q_values_selected * scores_selected, axis=1) / (
          tf.reduce_sum(input_tensor=scores_selected, axis=1) + score_no_click)

  return reward + gamma * next_q_target_topk * (
      1. - tf.cast(terminals, tf.float32))


def compute_target_optimal_q(reward, gamma, next_actions, next_q_values,
                             next_states, terminals):
  """Builds an op used as a target for the Q-value.

  This algorithm corresponds to the method "OT" in
  Ie et al. https://arxiv.org/abs/1905.12767..

  Args:
    reward: [batch_size] tensor, the immediate reward.
    gamma: float, discount factor with the usual RL meaning.
    next_actions: [batch_size, slate_size] tensor, the next slate.
    next_q_values: [batch_size, num_of_documents] tensor, the q values of the
      documents in the next step.
    next_states: [batch_size, 1 + num_of_documents] tensor, the features for the
      user and the docuemnts in the next step.
    terminals: [batch_size] tensor, indicating if this is a terminal step.

  Returns:
    [batch_size] tensor, the target q values.
  """
  scores, score_no_click = _get_unnormalized_scores(next_states)

  # Obtain all possible slates given current docs in the candidate set.
  slate_size = next_actions.get_shape().as_list()[1]
  num_candidates = next_q_values.get_shape().as_list()[1]
  mesh_args = [list(range(num_candidates))] * slate_size
  slates = tf.stack(tf.meshgrid(*mesh_args), axis=-1)
  slates = tf.reshape(slates, shape=(-1, slate_size))
  # Filter slates that include duplicates to ensure each document is picked
  # at most once.
  unique_mask = tf.map_fn(
      lambda x: tf.equal(tf.size(input=x), tf.size(input=tf.unique(x)[0])),
      slates,
      dtype=tf.bool)
  # [num_of_slates, slate_size]
  slates = tf.boolean_mask(tensor=slates, mask=unique_mask)

  # [batch_size, num_of_slates, slate_size]
  next_q_values_slate = tf.gather(next_q_values, slates, axis=1)
  # [batch_size, num_of_slates, slate_size]
  scores_slate = tf.gather(scores, slates, axis=1)
  # [batch_size, num_of_slates]
  batch_size = next_states.get_shape().as_list()[0]
  score_no_click_slate = tf.reshape(
      tf.tile(score_no_click,
              tf.shape(input=slates)[:1]), [batch_size, -1])

  # [batch_size, num_of_slates]
  next_q_target_slate = tf.reduce_sum(
      input_tensor=next_q_values_slate * scores_slate, axis=2) / (
          tf.reduce_sum(input_tensor=scores_slate, axis=2) +
          score_no_click_slate)

  next_q_target_max = tf.reduce_max(input_tensor=next_q_target_slate, axis=1)

  return reward + gamma * next_q_target_max * (1. -
                                               tf.cast(terminals, tf.float32))


@gin.configurable
class SlateDecompQAgent(dqn_agent.DQNAgentRecSim,
                        abstract_agent.AbstractEpisodicRecommenderAgent):
  """A recommender agent implements DQN using slate decomposition techniques."""

  def __init__(self,
               sess,
               observation_space,
               action_space,
               optimizer_name='',
               select_slate_fn=None,
               compute_target_fn=None,
               stack_size=1,
               eval_mode=False,
               **kwargs):
    """Initializes SlateDecompQAgent.

    Args:
      sess: a Tensorflow session.
      observation_space: A gym.spaces object that specifies the format of
        observations.
      action_space: A gym.spaces object that specifies the format of actions.
      optimizer_name: The name of the optimizer.
      select_slate_fn: A function that selects the slate.
      compute_target_fn: A function that omputes the target q value.
      stack_size: The stack size for the replay buffer.
      eval_mode: A bool for whether the agent is in training or evaluation mode.
      **kwargs: Keyword arguments to the DQNAgent.
    """
    self._response_adapter = dqn_agent.ResponseAdapter(
        observation_space.spaces['response'])
    response_names = self._response_adapter.response_names
    expected_response_names = ['click', 'watch_time']
    if not all(key in response_names for key in expected_response_names):
      raise ValueError(
          "Couldn't find all fields needed for the decomposition: %r" %
          expected_response_names)

    self._click_response_index = response_names.index('click')
    self._reward_response_index = response_names.index('watch_time')
    self._quality_response_index = response_names.index('quality')
    self._cluster_id_response_index = response_names.index('cluster_id')

    self._env_action_space = action_space
    self._num_candidates = int(action_space.nvec[0])
    abstract_agent.AbstractEpisodicRecommenderAgent.__init__(self, action_space)

    # The doc score is a [num_candidates] vector.
    self._doc_affinity_scores_ph = tf.compat.v1.placeholder(
        tf.float32, (self._num_candidates,), name='doc_affinity_scores_ph')
    self._prob_no_click_ph = tf.compat.v1.placeholder(
        tf.float32, (), name='prob_no_click_ph')

    self._select_slate_fn = select_slate_fn
    self._compute_target_fn = compute_target_fn

    dqn_agent.DQNAgentRecSim.__init__(
        self,
        sess,
        observation_space,
        num_actions=0,  # Unused.
        stack_size=1,
        optimizer_name=optimizer_name,
        eval_mode=eval_mode,
        **kwargs)

  def _network_adapter(self, states, scope):
    self._validate_states(states)

    with tf.compat.v1.name_scope('network'):
      # Since we decompose the slate optimization into an item-level
      # optimization problem, the observation space is the user state
      # observation plus all documents' observations. In the Dopamine DQN agent
      # implementation, there is one head for each possible action value, which
      # is designed for computing the argmax operation in the action space.
      # In our implementation, we generate one output for each document.
      q_value_list = []
      for i in range(self._num_candidates):
        user = tf.squeeze(states[:, 0, :, :], axis=2)
        doc = tf.squeeze(states[:, i + 1, :, :], axis=2)
        q_value_list.append(self.network(user, doc, scope))
      q_values = tf.concat(q_value_list, axis=1)

    return dqn_agent.DQNNetworkType(q_values)

  def _build_networks(self):
    with tf.compat.v1.name_scope('networks'):
      self._replay_net_outputs = self._network_adapter(self._replay.states,
                                                       'Online')
      self._replay_next_target_net_outputs = self._network_adapter(
          self._replay.states, 'Target')
      self._net_outputs = self._network_adapter(self.state_ph, 'Online')
      self._build_select_slate_op()

  def _build_train_op(self):
    """Builds a training op.

    Returns:
      An op performing one step of training from replay data.
    """
    # click_indicator: [B, S]
    # q_values: [B, A]
    # actions: [B, S]
    # slate_q_values: [B, S]
    # replay_click_q: [B]
    click_indicator = self._replay.rewards[:, :, self._click_response_index]
    slate_q_values = tf.compat.v1.batch_gather(
        self._replay_net_outputs.q_values,
        tf.cast(self._replay.actions, dtype=tf.int32))
    # Only get the Q from the clicked document.
    replay_click_q = tf.reduce_sum(
        input_tensor=slate_q_values * click_indicator,
        axis=1,
        name='replay_click_q')

    target = tf.stop_gradient(self._build_target_q_op())

    clicked = tf.reduce_sum(input_tensor=click_indicator, axis=1)
    clicked_indices = tf.squeeze(
        tf.compat.v1.where(tf.equal(clicked, 1)), axis=1)
    # clicked_indices is a vector and tf.gather selects the batch dimension.
    q_clicked = tf.gather(replay_click_q, clicked_indices)
    target_clicked = tf.gather(target, clicked_indices)

    def get_train_op():
      loss = tf.reduce_mean(input_tensor=tf.square(q_clicked - target_clicked))
      if self.summary_writer is not None:
        with tf.compat.v1.variable_scope('Losses'):
          tf.compat.v1.summary.scalar('Loss', loss)

      return loss

    loss = tf.cond(
        pred=tf.greater(tf.reduce_sum(input_tensor=clicked), 0),
        true_fn=get_train_op,
        false_fn=lambda: tf.constant(0.),
        name='')

    return self.optimizer.minimize(loss)

  def _build_target_q_op(self):
    """Builds an op used as a target for the Q-value.

    Returns:
      An op calculating the Q-value.
    """
    item_reward = self._replay.rewards[:, :, self._reward_response_index]
    click_indicator = self._replay.rewards[:, :, self._click_response_index]
    # Only compute the watch time reward of the clicked item.
    reward = tf.reduce_sum(input_tensor=item_reward * click_indicator, axis=1)

    return self._compute_target_fn(
        reward=reward,
        gamma=self.gamma,
        next_actions=self._replay.next_actions,
        next_q_values=self._replay_next_target_net_outputs.q_values,
        next_states=self._replay.next_states,
        terminals=self._replay.terminals)

  # The following functions defines how the agent takes actions.
  def step(self, reward, observation):
    """Records the transition and returns the agent's next action.

    It uses document-level user response instead of overral reward as the reward
    of the problem.

    Args:
      reward: unused.
      observation: a space.Dict that includes observation of the user state
        observation, documents and user responses.

    Returns:
      Array, the selected action.
    """
    del reward  # Unused argument.

    responses = observation['response']
    self._raw_observation = observation
    return super(SlateDecompQAgent,
                 self).step(self._response_adapter.encode(responses),
                            self._obs_adapter.encode(observation))

  def _build_select_slate_op(self):
    p_no_click = self._prob_no_click_ph
    p = self._doc_affinity_scores_ph
    q = self._net_outputs.q_values[0]
    with tf.compat.v1.name_scope('select_slate'):
      self._output_slate = self._select_slate_fn(self._slate_size, p_no_click,
                                                 p, q)

    self._output_slate = tf.compat.v1.Print(
        self._output_slate, [tf.constant('cp 1'), self._output_slate, p, q],
        summarize=10000)
    self._output_slate = tf.reshape(self._output_slate, (self._slate_size,))

    self._action_counts = tf.compat.v1.get_variable(
        'action_counts',
        shape=[self._num_candidates],
        initializer=tf.compat.v1.zeros_initializer())
    output_slate = tf.reshape(self._output_slate, [-1])
    output_one_hot = tf.one_hot(output_slate, self._num_candidates)
    update_ops = []
    for i in range(self._slate_size):
      update_ops.append(
          tf.compat.v1.assign_add(self._action_counts, output_one_hot[i]))
    self._select_action_update_op = tf.group(*update_ops)

  def _select_action(self):
    """Selects an slate based on the trained model.

    Chooses an action randomly with probability self._calculate_epsilon(), and
    otherwise acts greedily according to the current Q-value estimates. It will
    pick the top slate_size documents with highest Q values and return them as a
    slate.

    Returns:
       Array, the selected action.
    """
    if self.eval_mode:
      epsilon = self.epsilon_eval
    else:
      epsilon = self.epsilon_fn(self.epsilon_decay_period, self.training_steps,
                                self.min_replay_history, self.epsilon_train)
      self._add_summary('epsilon', epsilon)

    if np.random.random() <= epsilon:
      # Sample without replacement.
      return np.random.choice(
          self._num_candidates, self._slate_size, replace=False)
    else:
      observation = self._raw_observation
      user_obs = observation['user']
      doc_obs = np.array(list(observation['doc'].values()))
      tf.compat.v1.logging.debug('cp 1: %s, %s', doc_obs, observation)
      # TODO(cwhsu): Use score_documents_tf() and remove score_documents().
      scores, score_no_click = score_documents(user_obs, doc_obs)
      output_slate, _ = self._sess.run(
          [self._output_slate, self._select_action_update_op], {
              self.state_ph: self.state,
              self._doc_affinity_scores_ph: scores,
              self._prob_no_click_ph: score_no_click,
          })

      return output_slate

  # Other functions.
  def _build_replay_buffer(self, use_staging):
    """Creates the replay buffer used by the agent.

    Args:
      use_staging: bool, if True, uses a staging area to prefetch data for
        faster training.

    Returns:
      A WrapperReplayBuffer object.
    """
    return dqn_agent.wrapped_replay_buffer(
        observation_shape=self.observation_shape,
        stack_size=self.stack_size,
        use_staging=use_staging,
        update_horizon=self.update_horizon,
        gamma=self.gamma,
        observation_dtype=self.observation_dtype,
        action_shape=self._env_action_space.shape,
        action_dtype=self._env_action_space.dtype,
        reward_shape=self._response_adapter.response_shape,
        reward_dtype=self._response_adapter.response_dtype)

  def _add_summary(self, tag, value):
    if self.summary_writer:
      summary = tf.compat.v1.Summary(
          value=[tf.compat.v1.Summary.Value(tag=tag, simple_value=value)])
      self.summary_writer.add_summary(summary, self.training_steps)

  def begin_episode(self, observation):
    """Returns the agent's first action for this episode.

    Args:
      observation: numpy array, the environment's initial observation.

    Returns:
      An integer array of size _slate_size, the selected slated, each
      element of which is an index in the list of doc_obs.
    """
    self._raw_observation = observation
    return super(SlateDecompQAgent,
                 self).begin_episode(self._obs_adapter.encode(observation))

  def end_episode(self, reward, observation):
    """Signals the end of the episode to the agent.

    We store the observation of the current time step, which is the last
    observation of the episode.

    Args:
      reward: float, the last reward from the environment.
      observation: numpy array, the environment's initial observation.
    """
    del reward  # Unused argument.
    super(SlateDecompQAgent, self).end_episode(
        self._response_adapter.encode(observation['response']))


def create_agent(agent_name, sess, **kwargs):
  """Creates a slate decomposition agent given agent name."""
  if agent_name == 'dp_random':
    return SlateDecompQAgent(
        sess,
        epsilon_train=1.0,
        epsilon_eval=1.0,
        select_slate_fn=select_slate_greedy,
        compute_target_fn=compute_target_sarsa,
        **kwargs)
  elif agent_name == 'slate_topk_sarsa':
    return SlateDecompQAgent(
        sess,
        select_slate_fn=select_slate_topk,
        compute_target_fn=compute_target_sarsa,
        **kwargs)
  elif agent_name == 'myopic_slate_topk_sarsa':
    return SlateDecompQAgent(
        sess,
        gamma=0,
        select_slate_fn=select_slate_topk,
        compute_target_fn=compute_target_sarsa,
        **kwargs)
  elif agent_name == 'slate_greedy_sarsa':
    return SlateDecompQAgent(
        sess,
        select_slate_fn=select_slate_greedy,
        compute_target_fn=compute_target_sarsa,
        **kwargs)
  elif agent_name == 'myopic_slate_greedy_sarsa':
    return SlateDecompQAgent(
        sess,
        gamma=0,
        select_slate_fn=select_slate_greedy,
        compute_target_fn=compute_target_sarsa,
        **kwargs)
  elif agent_name == 'slate_greedy_optimal_q':
    return SlateDecompQAgent(
        sess,
        select_slate_fn=select_slate_greedy,
        compute_target_fn=compute_target_optimal_q,
        **kwargs)
  elif agent_name == 'slate_topk_topk_q':
    return SlateDecompQAgent(
        sess,
        select_slate_fn=select_slate_topk,
        compute_target_fn=compute_target_topk_q,
        **kwargs)
  elif agent_name == 'slate_topk_optimal_q':
    return SlateDecompQAgent(
        sess,
        select_slate_fn=select_slate_topk,
        compute_target_fn=compute_target_optimal_q,
        **kwargs)
  elif agent_name == 'slate_optimal_optimal_q':
    return SlateDecompQAgent(
        sess,
        select_slate_fn=select_slate_optimal,
        compute_target_fn=compute_target_optimal_q,
        **kwargs)
  elif agent_name == 'slate_greedy_greedy_q':
    return SlateDecompQAgent(
        sess,
        select_slate_fn=select_slate_greedy,
        compute_target_fn=compute_target_greedy_q,
        **kwargs)
  else:
    raise ValueError('Unknown agent: {}'.format(agent_name))
