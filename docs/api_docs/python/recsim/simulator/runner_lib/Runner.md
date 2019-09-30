<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.simulator.runner_lib.Runner" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# recsim.simulator.runner_lib.Runner

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/simulator/runner_lib.py">View
source</a>

## Class `Runner`

Object that handles running experiments.

<!-- Placeholder for "Used in" -->

Here we use the term 'experiment' to mean simulating interactions between the
agent and the environment and reporting some statistics pertaining to these
interactions.

<h2 id="__init__"><code>__init__</code></h2>

```python
__init__(
    *args,
    **kwargs
)
```

Initializes the Runner object in charge of running a full experiment.

#### Args:

*   <b>`base_dir`</b>: str, the base directory to host all required
    sub-directories.
*   <b>`create_agent_fn`</b>: A function that takes as args a Tensorflow session
    and an environment, and returns an agent.
*   <b>`env`</b>: A Gym environment for running the experiments.
*   <b>`episode_log_file`</b>: Path to output simulated episodes in
    tf.SequenceExample. Disable logging if episode_log_file is an empty string.
*   <b>`checkpoint_file_prefix`</b>: str, the prefix to use for checkpoint
    files.
*   <b>`max_steps_per_episode`</b>: int, maximum number of steps after which an
    episode terminates.
