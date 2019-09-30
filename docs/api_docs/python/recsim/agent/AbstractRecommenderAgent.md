<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agent.AbstractRecommenderAgent" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="bundle_and_checkpoint"/>
<meta itemprop="property" content="step"/>
<meta itemprop="property" content="unbundle"/>
</div>

# recsim.agent.AbstractRecommenderAgent

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/agent.py">View
source</a>

## Class `AbstractRecommenderAgent`

Abstract class to model a recommender system agent.

<!-- Placeholder for "Used in" -->

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/agent.py">View
source</a>

```python
__init__(action_space)
```

Initializes AbstractRecommenderAgent.

#### Args:

*   <b>`action_space`</b>: A gym.spaces object that specifies the format of
    actions.

## Methods

<h3 id="bundle_and_checkpoint"><code>bundle_and_checkpoint</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/agent.py">View
source</a>

```python
bundle_and_checkpoint(
    checkpoint_dir,
    iteration_number
)
```

Returns a self-contained bundle of the agent's state.

This is used for checkpointing. It will return a dictionary containing all
non-TensorFlow objects (to be saved into a file by the caller), and it saves all
TensorFlow objects into a checkpoint file.

#### Args:

*   <b>`checkpoint_dir`</b>: A string for the directory where objects will be
    saved.
*   <b>`iteration_number`</b>: An integer of iteration number to use for naming
    the checkpoint file.

#### Returns:

A dictionary containing additional Python objects to be checkpointed by the
experiment. Each key is a string for the object name and the value is actual
object. If the checkpoint directory does not exist, returns empty dictionary.

<h3 id="step"><code>step</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/agent.py">View
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

<a target="_blank" href="https://github.com/google-research/recsim/recsim/agent.py">View
source</a>

```python
unbundle(
    checkpoint_dir,
    iteration_number,
    bundle_dict
)
```

Restores the agent from a checkpoint.

Restores the agent's Python objects to those specified in bundle_dict, and
restores the TensorFlow objects to those specified in the checkpoint_dir. If the
checkpoint_dir does not exist, will not reset the agent's state.

#### Args:

*   <b>`checkpoint_dir`</b>: A string that represents the path to the checkpoint
    saved by tf.Save.
*   <b>`iteration_number`</b>: An integer that represents the checkpoint version
    and is used when restoring replay buffer.
*   <b>`bundle_dict`</b>: A dict containing additional Python objects owned by
    the agent. Each key is an object name and the value is the actual object.

#### Returns:

bool, True if unbundling was successful.
