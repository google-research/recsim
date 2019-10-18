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
"""Tests for recsim.agents.tabular_q_agent."""

from gym import spaces
import numpy as np
from recsim.agents import tabular_q_agent
from recsim.testing import test_environment as te
import tensorflow as tf


class TabularQAgentTest(tf.test.TestCase):

  def init_agent_and_env(self,
                         slate_size=1,
                         num_candidates=10,
                         learning_rate=0.8,
                         gamma=0.0,
                         policy='epsilon_greedy',
                         starting_probs=(1.0, 0.0, 0.0, 0.0, 0.0, 0.0)):
    env_config = {
        'num_candidates': num_candidates,
        'slate_size': slate_size,
        'resample_documents': False,
        'seed': 42,
        'starting_probs': starting_probs
    }
    te_sim = te.create_environment(env_config)
    agent = tabular_q_agent.TabularQAgent(
        te_sim.observation_space,
        te_sim.action_space,
        gamma=gamma,
        exploration_policy=policy,
        learning_rate=learning_rate)
    return te_sim, agent

  def test_step(self):
    te_sim, agent = self.init_agent_and_env()
    observation0 = te_sim.reset()
    slate1 = agent.step(0, observation0)
    selected_doc0 = list(observation0['doc'].values())[slate1[0]]
    # Environment always starts at state 0.
    self.assertEqual(agent._previous_state_action_index, (selected_doc0, 0))
    observation1, reward1, _, _ = te_sim.step(slate1)
    slate2 = agent.step(reward1, observation1)
    selected_doc1 = list(observation1['doc'].values())[slate2[0]]
    observed_state = observation1['user']
    self.assertEqual(agent._previous_state_action_index,
                     (selected_doc1, observed_state))
    self.assertEqual(agent._q_value_table,
                     {(selected_doc0, 0): agent._learning_rate * -10.0})
    self.assertEqual(agent._state_action_counts, {(selected_doc0, 0): 1})

  def test_myopic_value_estimation(self):
    te_sim, agent = self.init_agent_and_env()
    observation0 = te_sim.reset()
    slate = agent.step(0, observation0)
    for _ in range(5000):
      observation, reward, _, _ = te_sim.step(slate)
      slate = agent.step(reward, observation)
    for state in range(6):
      for action in range(4):
        self.assertAlmostEqual(agent._q_value_table[(action, state)],
                               te.QVALUES0[state][action])

  def test_gamma05_value_estimation(self):
    # TODO(mmladenov): tune further to improve speed of this test
    te_sim, agent = self.init_agent_and_env(gamma=0.5)
    observation = te_sim.reset()
    reward = 0
    for i in range(100, 100100):
      slate = agent.step(reward, observation)
      observation, reward, _, _ = te_sim.step(slate)
      agent._learning_rate = 100.0 / float(i)
    for state in range(6):
      for action in range(4):
        self.assertAlmostEqual(
            agent._q_value_table[(action, state)],
            te.QVALUES05[state][action],
            delta=0.2)

  def test_dicretize_gym_leaf(self):
    _, agent = self.init_agent_and_env()
    self.assertEqual(
        agent._discretize_gym_leaf(spaces.Discrete(5), [
            4,
        ]), [
            4,
        ])
    box = spaces.Box(
        low=agent._discretization_bins[0],
        high=agent._discretization_bins[-1],
        shape=(1, 1),
        dtype=np.float32)
    # Some corner cases in 1d and 2x2d.
    self.assertEqual(
        agent._discretize_gym_leaf(box, [
            agent._discretization_bins[0] - 10E-5,
        ]), [
            0,
        ])
    self.assertEqual(
        agent._discretize_gym_leaf(box, [
            agent._discretization_bins[0],
        ]), [
            1,
        ])
    self.assertEqual(
        agent._discretize_gym_leaf(box, [
            agent._discretization_bins[-1] - 10E-5,
        ]), [
            len(agent._discretization_bins) - 1,
        ])
    self.assertEqual(
        agent._discretize_gym_leaf(box, [
            agent._discretization_bins[-1] + 1.0,
        ]), [
            len(agent._discretization_bins),
        ])
    box2x2 = spaces.Box(
        low=agent._discretization_bins[0],
        high=agent._discretization_bins[-1],
        shape=(2, 2),
        dtype=np.float32)
    self.assertEqual(
        agent._discretize_gym_leaf(box2x2, [
            np.array([[
                agent._discretization_bins[0] - 10E-6,
                agent._discretization_bins[-1] - 10E-6
            ],
                      [
                          agent._discretization_bins[-1] + 1.0,
                          agent._discretization_bins[0]
                      ]]),
        ]), [0, 99, 100, 1])

  def test_slate_enumeration(self):
    te_sim, agent = self.init_agent_and_env(slate_size=2, num_candidates=4)
    observation0 = te_sim.reset()
    slates = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    enumerated_slates = [
        slate for slate, _ in agent._enumerate_slates(observation0['doc'])
    ]
    self.assertCountEqual(slates, enumerated_slates)

  def test_bundle_and_unbundle(self):
    te_sim, agent = self.init_agent_and_env(
        slate_size=1, num_candidates=4, policy='min_count')
    # Make a few steps to populate counts and Q-table.
    observation0 = te_sim.reset()
    slate1 = agent.step(0, observation0)
    observation1, reward1, _, _ = te_sim.step(slate1)
    agent.step(reward1, observation1)
    bundle_dict = {
        'q_value_table': agent._q_value_table,
        'sa_count': agent._state_action_counts
    }
    self.assertEqual(bundle_dict, agent.bundle_and_checkpoint('', 0))
    _, new_agent = self.init_agent_and_env(slate_size=1, num_candidates=4)
    self.assertTrue(new_agent.unbundle('', 0, bundle_dict))
    self.assertEqual(bundle_dict['q_value_table'], new_agent._q_value_table)
    self.assertEqual(bundle_dict['sa_count'], new_agent._state_action_counts)


if __name__ == '__main__':
  tf.test.main()
