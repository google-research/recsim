# coding=utf-8
# Lint as: python3
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
"""Tests for recsim.agent."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import functools
import os

from absl.testing import parameterized
import gym
import numpy as np
from recsim import agent
from recsim.simulator import environment
from recsim.simulator import recsim_gym
from recsim.simulator import runner_lib
import tensorflow.compat.v1 as tf


class DummySingleUserAgent(agent.AbstractEpisodicRecommenderAgent):

  def step(self, reward, observation):
    pass

  def bundle_and_checkpoint(self, checkpoint_dir, iteration_number):
    pass

  def unbundle(self, checkpoint_dir, iteration_number, bundle_dict):
    pass


class DummyMultiUserAgent(agent.AbstractMultiUserEpisodicRecommenderAgent):

  def step(self, reward, observation):
    pass

  def bundle_and_checkpoint(self, checkpoint_dir, iteration_number):
    pass

  def unbundle(self, checkpoint_dir, iteration_number, bundle_dict):
    pass


class DummySingleUserEnvironment(environment.SingleUserEnvironment):

  def __init__(self):
    pass


class DummyMultiUserEnvironment(environment.MultiUserEnvironment):

  def __init__(self):
    pass


def create_environment(env_config):
  if env_config['multiuser_env']:
    env = DummyMultiUserEnvironment()
  else:
    env = DummySingleUserEnvironment()
  reward_aggregator = lambda x: x
  return recsim_gym.RecSimGymEnv(env, reward_aggregator)


class AgentTest(parameterized.TestCase):
  num_users = 100
  num_candidates = 10
  slate_size = 8

  @parameterized.named_parameters(
      ('multiuser_env_multiuser_agent', True, True, True),
      ('singleuser_env_multiuser_agent', False, True, False),
      ('multiuser_env_singleuser_agent', True, False, False),
      ('singleuser_env_singleuser_agent', False, False, True),
  )
  def test_multi_and_single_user_consistency(
      self, multiuser_env, multiuser_agent, should_succeed):

    def create_agent(
        sess, env, summary_writer, eval_mode, multiuser_agent=True):
      del sess, env, summary_writer, eval_mode  # unused
      action_space = gym.spaces.MultiDiscrete(np.ones((self.slate_size,)))
      if multiuser_agent:
        action_space = gym.spaces.Tuple([action_space] * self.num_users)
        AgentClass = DummyMultiUserAgent  # pylint:disable=invalid-name
      else:
        AgentClass = DummySingleUserAgent  # pylint:disable=invalid-name
      return AgentClass(action_space)

    env_config = dict(multiuser_env=multiuser_env)
    base_dir = '/tmp/Env%sAgent%s' % (multiuser_env, multiuser_agent)
    create_agent_fn = functools.partial(create_agent,
                                        multiuser_agent=multiuser_agent)
    if not os.path.exists(base_dir):
      os.makedirs(base_dir)
    if should_succeed:  # constructors should work
      _ = runner_lib.TrainRunner(
          base_dir=base_dir,
          create_agent_fn=create_agent_fn,
          env=create_environment(env_config),
          max_training_steps=1,
          max_steps_per_episode=1,
          num_iterations=1)
    else:  # agent constructor should raise error
      with self.assertRaises(ValueError):
        _ = runner_lib.TrainRunner(
            base_dir=base_dir,
            create_agent_fn=create_agent_fn,
            env=create_environment(env_config),
            max_training_steps=1,
            max_steps_per_episode=1,
            num_iterations=1)


if __name__ == '__main__':
  tf.test.main()
