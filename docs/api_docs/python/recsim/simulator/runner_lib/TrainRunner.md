<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.simulator.runner_lib.TrainRunner" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="run_experiment"/>
</div>

# recsim.simulator.runner_lib.TrainRunner

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/simulator/runner_lib.py">View
source</a>

Object that handles running the training.

Inherits From: [`Runner`](../../../recsim/simulator/runner_lib/Runner.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.simulator.runner_lib.TrainRunner(
    max_training_steps=250000, num_iterations=100, checkpoint_frequency=1, **kwargs
)
</code></pre>

<!-- Placeholder for "Used in" -->

See main.py for a simple example to train an agent.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`base_dir`
</td>
<td>
str, the base directory to host all required sub-directories.
</td>
</tr><tr>
<td>
`create_agent_fn`
</td>
<td>
A function that takes as args a Tensorflow session and an
environment, and returns an agent.
</td>
</tr><tr>
<td>
`env`
</td>
<td>
A Gym environment for running the experiments.
</td>
</tr><tr>
<td>
`episode_log_file`
</td>
<td>
Path to output simulated episodes in tf.SequenceExample.
Disable logging if episode_log_file is an empty string.
</td>
</tr><tr>
<td>
`checkpoint_file_prefix`
</td>
<td>
str, the prefix to use for checkpoint files.
</td>
</tr><tr>
<td>
`max_steps_per_episode`
</td>
<td>
int, maximum number of steps after which an episode
terminates.
</td>
</tr>
</table>

## Methods

<h3 id="run_experiment"><code>run_experiment</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/simulator/runner_lib.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>run_experiment()
</code></pre>

Runs a full experiment, spread over multiple iterations.
