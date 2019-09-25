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
"""Temporally aggregated reinforcement learning agent."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from gym import spaces
import numpy as np

from recsim import agent
from recsim.agents import agent_utils


class TemporalAggregationLayer(agent.AbstractHierarchicalAgentLayer):
  """Temporally aggregated reinforcement learning agent.

  A reinforcement learning agent that implements learns a temporally aggregated
  policy. This is achieved in two ways:
    * making a decision only every k-steps;
    * introducing a switching cost penalty whenever the policy executes two
      different consequitve actions.
  See "Advantage Amplification in Slowly Evolving Latent-State Environments"
  Martin Mladenov, Ofer Meshi, Jayden Ooi, Dale Schuurmans, Craig Boutilier
  https://arxiv.org/abs/1905.13559
  for details.
  Implementation-wise, this agent relies on an event-level (base) agent suited
  for the domain.
  Aggregation is implemented as a preprocessing step for the base agent:
  in the first case only calling the agent every k steps (and adjusting the
  discount (gamma) accordingly to keep the objective consistent), in the second
  case subtracting a penalty from the environment reward whenever the base agent
  switches actions. For switching cost, it is also necessary to append the last
  executed action to the
  state representation, otherwise the learning problem becomes non-Markovian.

  The two methods are not mutually exclusive and may be used in conjunction by
  specifying a non-unit aggregation_period and a non-zero switching_cost.
  """

  def __init__(self,
               base_agent_ctor,
               observation_space,
               action_space,
               gamma=0.0,
               aggregation_period=1,
               switching_cost=1.0,
               document_comparison_fcn=None,
               **kwargs):
    """TemporallyAggregatedAgent init.

    Args:
      base_agent_ctor: a constructor for the base agent.
      observation_space: a gym.spaces object specifying the format of
        observations.
      action_space: A gym.spaces object that specifies the format of actions.
      gamma: geometric discounting factor between [0, 1) for the event-level
        objective.
      aggregation_period: number of time steps to hold an action fixed.
      switching_cost: a non-negative penalty for switching an action.
      document_comparison_fcn: a function taking two document observations and
        returning a Boolean value that indicates if they are considered
        equivalent. This is useful for making decisions at a higher abstraction
        level (e.g. comparing only document topics). If not provided, this will
        default to direct observation equality.
      **kwargs: base_agent initialization args.
    """
    super(TemporalAggregationLayer, self).__init__(action_space,
                                                   base_agent_ctor)
    self._step_count = 0
    self._observation_space = observation_space
    self._aggregation_period = aggregation_period
    self._gamma_accumulator = 1.0
    self._reward_accumulator = 0.0
    self._switching_cost = switching_cost
    self._gamma = gamma
    single_doc_space = list(observation_space.spaces['doc'].spaces.values())[0]
    if document_comparison_fcn is None:
      self._doc_equality_walker = agent_utils.GymSpaceWalker(
          single_doc_space, self._spaces_equal).apply_and_flatten
      self._doc_comparator = self._default_doc_comparator
    else:
      self._doc_comparator = document_comparison_fcn
    self._slate_comparator = self._default_slate_comparator
    if aggregation_period > 1:
      base_agent_gamma = gamma**aggregation_period
    else:
      base_agent_gamma = gamma
    if switching_cost > 0.0:
      # Attach documents in the last slate as a user observation.
      slate_tuple = tuple([single_doc_space] * self._slate_size)
      last_slate_space = spaces.Tuple(slate_tuple)
      augmented_observation_space = {
          'user':
              spaces.Dict({
                  'original_observation': observation_space.spaces['user'],
                  'last_slate': last_slate_space
              }),
          'response':
              observation_space.spaces['response'],
          'doc':
              observation_space.spaces['doc']
      }
      base_observation_space = spaces.Dict(augmented_observation_space)
    else:
      base_observation_space = observation_space
    self._base_observation_space = base_observation_space
    kwargs['observation_space'] = base_observation_space
    kwargs['gamma'] = base_agent_gamma
    kwargs['action_space'] = action_space
    self._base_agents = [
        base_agent_ctor(**kwargs),
    ]
    self._last_slate = None
    self._previous_last_slate = None

  def _default_doc_comparator(self, doc1, doc2):
    return all(self._doc_equality_walker([doc1, doc2]))

  def _default_slate_comparator(self, slate1, slate2):
    return all([
        self._doc_comparator(doc1_obs, doc2_obs)
        for doc1_obs, doc2_obs in zip(slate1, slate2)
    ])

  def _spaces_equal(self, gym_space, gym_observations, abs_tolerance=10E-5):
    if isinstance(gym_space, spaces.box.Box):
      all_equal = [
          True,
      ]
      gym_observation0 = np.array(gym_observations[0])
      for gym_observation in gym_observations[1:]:
        gym_observation = np.array(gym_observations)
        if not np.allclose(
            gym_observation0, gym_observation, atol=abs_tolerance):
          all_equal = [
              False,
          ]
    elif isinstance(gym_space, spaces.discrete.Discrete):
      all_equal = [
          not gym_observations or
          gym_observations.count(gym_observations[0]) == len(gym_observations),
      ]
    else:
      raise NotImplementedError('Gym space type ' + str(type(gym_space)) +
                                ' not implemented yet.')
    return list(all_equal)

  def _preprocess_reward_observation(self, reward, observation):
    # Aggregate reward and adjust discount.
    if self._switching_cost > 0.0:
      if self._last_slate is None:
        # Invent some fake first slate for consistency.
        self._last_slate = tuple(observation['doc'].values())[:self._slate_size]
        self._previous_last_slate = self._last_slate
      # Augment state space if switching cost is nonzero.
      observation['user'] = {
          'original_observation': observation['user'],
          'last_slate': self._last_slate
      }
      # Penalize action switch.
      if not self._slate_comparator(self._last_slate,
                                    self._previous_last_slate):
        reward -= self._switching_cost
    self._reward_accumulator += self._gamma_accumulator * reward
    self._gamma_accumulator *= self._gamma
    return self._reward_accumulator, observation

  def _postprocess_actions(self, action_list):
    # Does not modify the action of the base agent.
    return action_list[0]

  def step(self, reward, observation):
    """Preprocesses the reward and observation and calls base agent.

    Args:
      reward: The reward received from the agent's most recent action as a
        float.
      observation: A dictionary that includes the most recent observations and
        should have the following fields:
        - user: A NumPy array representing user's observed state. Assumes it is
          a concatenation of topic pull counts and topic click counts.
        - doc: A NumPy array representing observations of document features.
          Assumes it is a concatenation of one-hot encoding of topic_id and
          document quality.

    Returns:
      slate: An integer array of size _slate_size, where each element is an
        index into the list of doc_obs.
    Raises:
      RuntimeError: if the agent has to hold a slate with given features fixed
        for k steps but the documents needed to reconstruct that slate
        become unavailable.
    """
    reward, observation = self._preprocess_reward_observation(
        reward, observation)
    # Is this a decision period?
    if not self._step_count % self._aggregation_period:
      new_slate_index = self._base_agents[0].step(reward,
                                                  observation)
      new_slate_features = [
          tuple(observation['doc'].values())[i] for i in new_slate_index
      ]
      self._previous_last_slate = self._last_slate
      self._last_slate = new_slate_features
      slate = new_slate_index
      self._gamma_accumulator = 1.0
      self._reward_accumulator = 0.0
    else:
      # Not a decision period, we need to recreate the fixed slate by finding
      # docs with the same features.
      documents_to_find = list(range(self._slate_size))
      slate = [None] * self._slate_size
      for i, doc_features in enumerate(observation['doc'].values()):
        for missing_doc_position, missing_doc in enumerate(documents_to_find):
          if not self._doc_comparator(doc_features,
                                      self._last_slate[missing_doc]):
            slate[missing_doc] = i
            documents_to_find.pop(missing_doc_position)
            break
        if not documents_to_find:
          break
      if documents_to_find:
        raise RuntimeError(('Temporal aggregation could not recreate previous '
                            'slate because items became unavailable.'))

    return slate
