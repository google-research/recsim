<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.layers.fixed_length_history.FixedLengthHistoryLayer" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="multi_user"/>
<meta itemprop="property" content="observation_space"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="begin_episode"/>
<meta itemprop="property" content="bundle_and_checkpoint"/>
<meta itemprop="property" content="end_episode"/>
<meta itemprop="property" content="step"/>
<meta itemprop="property" content="unbundle"/>
</div>

# recsim.agents.layers.fixed_length_history.FixedLengthHistoryLayer

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/layers/fixed_length_history.py">View
source</a>

## Class `FixedLengthHistoryLayer`

<!-- Start diff -->
Creates a buffer of the last k rewards and observations.

Inherits From:
[`SufficientStatisticsLayer`](../../../../recsim/agents/layers/sufficient_statistics/SufficientStatisticsLayer.md)

<!-- Placeholder for "Used in" -->

This module introduces sufficient statistics in the form of a buffer holding the
last k (specified by history_length) observations. This buffer is injected into
observation_space[\'user\'][\'sufficient_statistics\'] in the form of a
gym.spaces.Tuple of length up to k . In the first k-1 steps of the episode there
are not enough observations to fill the buffer, so they will be filled with
None. Each non-vacuous element of the tuple is an instance of (a subset of)
observation_space.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/layers/fixed_length_history.py">View
source</a>

```python
__init__(
    base_agent_ctor,
    observation_space,
    action_space,
    history_length,
    remember_user=True,
    remember_response=True,
    remember_doc=False,
    **kwargs
)
```

Initializes a FixedLengthHistoryLayer object.

#### Args:

*   <b>`base_agent_ctor`</b>: a constructor for the base agent.
*   <b>`observation_space`</b>: a gym.spaces object specifying the format of
    observations.
*   <b>`action_space`</b>: A gym.spaces object that specifies the format of
    actions.
*   <b>`history_length`</b>: positive integer number of observations to
    remember.
*   <b>`remember_user`</b>: boolean, indicates whether to track
    observation_space[\'user\'].
*   <b>`remember_response`</b>: boolean, indicates whether to track
    observation_space[\'response\'].
*   <b>`remember_doc`</b>: boolean, indicates whether to track
    observation_space[\'doc\'].
*   <b>`**kwargs`</b>: arguments to pass to the downstream agent at construction
    time.

## Properties

<h3 id="multi_user"><code>multi_user</code></h3>

Returns boolean indicating whether this agent serves multiple users.

<h3 id="observation_space"><code>observation_space</code></h3>

## Methods

<h3 id="begin_episode"><code>begin_episode</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agent.py">View
source</a>

```python
begin_episode(observation=None)
```

<h3 id="bundle_and_checkpoint"><code>bundle_and_checkpoint</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agent.py">View
source</a>

```python
bundle_and_checkpoint(
    checkpoint_dir,
    iteration_number
)
```

Returns a self-contained bundle of the agent's state.

#### Args:

*   <b>`checkpoint_dir`</b>: A string for the directory where objects will be
    saved.
*   <b>`iteration_number`</b>: An integer of iteration number to use for naming
    the checkpoint file.

#### Returns:

A dictionary containing additional Python objects to be checkpointed by the
experiment. Each key is a string for the object name and the value is actual
object. If the checkpoint directory does not exist, returns empty dictionary.

<h3 id="end_episode"><code>end_episode</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/layers/sufficient_statistics.py">View
source</a>

```python
end_episode(
    reward,
    observation
)
```

<h3 id="step"><code>step</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/layers/sufficient_statistics.py">View
source</a>

```python
step(
    reward,
    observation
)
```

Records the most recent transition and returns the agent's next action.

We store the observation of the last time step since we want to store it with
the reward.

#### Args:

*   <b>`reward`</b>: The reward received from the agent's most recent action as
    a float.
*   <b>`observation`</b>: A dictionary that includes the most recent
    observations.

#### Returns:

*   <b>`slate`</b>: An integer array of size _slate_size, where each element is
    an index into the list of doc_obs

<h3 id="unbundle"><code>unbundle</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agent.py">View
source</a>

```python
unbundle(
    checkpoint_dir,
    iteration_number,
    bundle_dict
)
```

Restores the agent from a checkpoint.

#### Args:

*   <b>`checkpoint_dir`</b>: A string that represents the path to the checkpoint
    saved by tf.Save.
*   <b>`iteration_number`</b>: An integer that represents the checkpoint version
    and is used when restoring replay buffer.
*   <b>`bundle_dict`</b>: A dict containing additional Python objects owned by
    the agent. Each key is an object name and the value is the actual object.

#### Returns:

bool, True if unbundling was successful.
