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
r"""An example of main function for training in RecSim.

Use the interest evolution environment and a slateQ agent for illustration.

To run locally:

python main.py --base_dir=/tmp/interest_evolution \
  --gin_bindings=simulator.runner_lib.Runner.max_steps_per_episode=50

"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl import app
from absl import flags
import numpy as np
from recsim.agents import full_slate_q_agent
from recsim.environments import interest_evolution
from recsim.simulator import runner_lib


FLAGS = flags.FLAGS


def create_agent(sess, environment, eval_mode, summary_writer=None):
  """Creates an instance of FullSlateQAgent.

  Args:
    sess: A `tf.Session` object for running associated ops.
    environment: A recsim Gym environment.
    eval_mode: A bool for whether the agent is in training or evaluation mode.
    summary_writer: A Tensorflow summary writer to pass to the agent for
      in-agent training statistics in Tensorboard.

  Returns:
    An instance of FullSlateQAgent.
  """
  kwargs = {
      'observation_space': environment.observation_space,
      'action_space': environment.action_space,
      'summary_writer': summary_writer,
      'eval_mode': eval_mode,
  }
  return full_slate_q_agent.FullSlateQAgent(sess, **kwargs)


def main(argv):
  if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')

  runner_lib.load_gin_configs(FLAGS.gin_files, FLAGS.gin_bindings)
  seed = 0
  slate_size = 2
  np.random.seed(seed)
  env_config = {
      'num_candidates': 5,
      'slate_size': slate_size,
      'resample_documents': True,
      'seed': seed,
  }

  runner = runner_lib.TrainRunner(
      base_dir=FLAGS.base_dir,
      create_agent_fn=create_agent,
      env=interest_evolution.create_environment(env_config),
      episode_log_file=FLAGS.episode_log_file,
      max_training_steps=50,
      num_iterations=10)
  runner.run_experiment()

  runner = runner_lib.EvalRunner(
      base_dir=FLAGS.base_dir,
      create_agent_fn=create_agent,
      env=interest_evolution.create_environment(env_config),
      max_eval_episodes=5,
      test_mode=True)
  runner.run_experiment()


if __name__ == '__main__':
  flags.mark_flag_as_required('base_dir')
  app.run(main)
