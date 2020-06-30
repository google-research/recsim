<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.simulator.runner_lib.Runner" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# recsim.simulator.runner_lib.Runner

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/simulator/runner_lib.py">View
source</a>

Object that handles running experiments.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.simulator.runner_lib.Runner(
    base_dir, create_agent_fn, env, episode_log_file='',
    checkpoint_file_prefix='ckpt', max_steps_per_episode=27000
)
</code></pre>

<!-- Placeholder for "Used in" -->

Here we use the term 'experiment' to mean simulating interactions between the
agent and the environment and reporting some statistics pertaining to these
interactions.

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
