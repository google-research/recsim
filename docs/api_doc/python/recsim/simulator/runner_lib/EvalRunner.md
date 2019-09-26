<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.simulator.runner_lib.EvalRunner" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="run_experiment"/>
</div>

# recsim.simulator.runner_lib.EvalRunner

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/simulator/runner_lib.py">View
source</a>

## Class `EvalRunner`

Object that handles running the evaluation.

Inherits From: [`Runner`](../../../recsim/simulator/runner_lib/Runner.md)

<!-- Placeholder for "Used in" -->

See main.py for a simple example to evaluate an agent.

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

## Methods

<h3 id="run_experiment"><code>run_experiment</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/simulator/runner_lib.py">View
source</a>

```python
run_experiment()
```

Runs a full experiment, spread over multiple iterations.
