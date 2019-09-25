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
"""Agent that picks topics based on the UCB1 algorithm given past responses."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import gin
import numpy as np

from recsim import agent
from recsim.agents.bandits import algorithms


@gin.configurable
class AbstractClickBanditLayer(agent.AbstractHierarchicalAgentLayer):
  """A hierarchical bandit layer which treats a set of base agents as arms.

  This layer consumes a list of base agents with apriori unknown mean payoffs
  and has the job of mixing them in a way that minimizes the regret relative to
  the best among them. Each agent is assumed to output a slate of size up to
  slate_size. If an agent outputs an incomplete slate, the AbstractClickBandit
  will use other agent's outputs to complete it, packing them in decreasing
  order according to the index of the bandit policy. E.g. if using the upper
  confidence bound as index, the AbstractClickBandit will put the partial slate
  of the highest-UCB base agent in first place, then the second, until the slate
  is complete.
  """

  def __init__(self,
               observation_space,
               action_space,
               arm_base_agent_ctors,
               alg_ctor=algorithms.UCB1,
               ci_scaling=1.0,
               random_seed=0,
               **kwargs):
    """Initializes a new bandit agent for clustered arm exploration.

    Args:
      observation_space: Instance of a gym space corresponding to the
        observation format.
      action_space: A gym.spaces object that specifies the format of actions.
      arm_base_agent_ctors: a list of agent constructors, each agent corresponds
        to a bandit arm.
      alg_ctor: A class of an MABAlgorithm for exploration, default to UCB1.
      ci_scaling: A floating number specifying the scaling of confidence bound.
      random_seed: An integer for random seed.
      **kwargs: arguments for base agents.
    """

    super(AbstractClickBanditLayer, self).__init__(action_space,
                                                   *arm_base_agent_ctors)
    self._alg_ctor = alg_ctor
    self._random_seed = random_seed
    self._params = {'optimism_scaling': ci_scaling}
    kwargs['observation_space'] = observation_space
    kwargs['action_space'] = action_space
    self._num_arms = len(self._base_agent_ctors)
    user_observation_space = observation_space.spaces['user'].spaces
    if 'sufficient_statistics' not in user_observation_space:
      ValueError('observation_space.spaces[\'user\'] must contain \'sufficient_'
                 'statistics\' key.')
    suffstat_observation_space = user_observation_space[
        'sufficient_statistics'].spaces
    if 'impression_count' not in suffstat_observation_space:
      ValueError('sufficient_statistics must contain \'impression_count\' key.')
    if 'click_count' not in suffstat_observation_space:
      ValueError('sufficient_statistics must contain \'click_count\' key.')
    if self._num_arms != suffstat_observation_space['impression_count'].shape[0]:
      ValueError('Dimension of impression_count must be equal to number '
                 'of arms.')
    if self._num_arms != suffstat_observation_space['click_count'].shape[0]:
      ValueError('Dimension of click_count must be equal to number ' 'of arms.')
    self._base_agents = [
        base_agent_ctor(**kwargs) for base_agent_ctor in self._base_agent_ctors
    ]

  def _postprocess_actions(self, actions):
    slate = []
    for action in actions:
      if not bool(action):
        continue
      recs_to_use = min(len(action), self._slate_size - len(slate))
      # Make sure action is not a numpy array.
      slate += list(action[:recs_to_use])
      if len(slate) == self._slate_size:
        break
    return slate

  def step(self, reward, observation):
    """Records the most recent transition and returns the agent's next action.

    We store the observation of the last time step since we want to store it
    with the reward.

    Args:
      reward: Unused.
      observation: A dictionary that includes the most recent observations and
        should have the following fields:
        - user: A dictionary representing user's observed state. Assumes
          observation['user']['sufficient_statics'] is a dictionary containing
          base agent impression counts and base agent click counts.

    Returns:
      slate: An integer array of size _slate_size, where each element is an
        index into the list of doc_obs
    """
    user_obs = observation['user']['sufficient_statistics']
    pulls = user_obs['impression_count']
    clicks = user_obs['click_count']
    mab_alg = self._alg_ctor(len(pulls), self._params, self._random_seed)
    mab_alg.set_state(pulls, clicks)
    arm_pctr_ucb = mab_alg.get_score(np.sum(pulls))
    # Use (topic_pctr_ucb, document_quality) as the criterion.
    if all(pulls):
      scores = arm_pctr_ucb
    else:
      # Pick the topics that have not beeen pulled.
      scores = -pulls
    arm_order = list(np.argsort(scores))
    docs_so_far = 0
    actions = []
    while docs_so_far < self._slate_size:
      arm = arm_order.pop()
      action = self._base_agents[arm].step(reward, observation)
      docs_so_far += len(action)
      actions.append(action)
    return self._postprocess_actions(actions)
