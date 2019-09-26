<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agent.AbstractEpisodicRecommenderAgent" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="begin_episode"/>
<meta itemprop="property" content="bundle_and_checkpoint"/>
<meta itemprop="property" content="end_episode"/>
<meta itemprop="property" content="step"/>
<meta itemprop="property" content="unbundle"/>
</div>

# recsim.agent.AbstractEpisodicRecommenderAgent

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/agent.py">View
source</a>

## Class `AbstractEpisodicRecommenderAgent`

Abstract class for recommender systems that solves episodic tasks.

Inherits From:
[`AbstractRecommenderAgent`](../../recsim/agent/AbstractRecommenderAgent.md)

<!-- Placeholder for "Used in" -->

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/agent.py">View
source</a>

```python
__init__(
    action_space,
    summary_writer=None
)
```

Initializes AbstractEpisodicRecommenderAgent.

#### Args:

*   <b>`action_space`</b>: A gym.spaces object that specifies the format of
    actions.
*   <b>`summary_writer`</b>: A Tensorflow summary writer to pass to the agent
    for in-agent training statistics in Tensorboard.

## Methods

<h3 id="begin_episode"><code>begin_episode</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/agent.py">View
source</a>

```python
begin_episode(observation=None)
```

Returns the agent's first action for this episode.

#### Args:

*   <b>`observation`</b>: numpy array, the environment's initial observation.

#### Returns:

*   <b>`slate`</b>: An integer array of size _slate_size, where each element is
    an index into the list of doc_obs

<h3 id="bundle_and_checkpoint"><code>bundle_and_checkpoint</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/agent.py">View
source</a>

```python
bundle_and_checkpoint(
    checkpoint_dir,
    iteration_number
)
```

Returns a self-contained bundle of the agent's state.

#### Args:

*   <b>`checkpoint_dir`</b>: A string that represents the path to the checkpoint
    and is used when we save TensorFlow objects by tf.Save.
*   <b>`iteration_number`</b>: An integer that represents the checkpoint version
    and is used when restoring replay buffer.

#### Returns:

A dictionary containing additional Python objects to be checkpointed by the
experiment. Each key is a string for the object name and the value is actual
object. If the checkpoint directory does not exist, returns empty dictionary.

<h3 id="end_episode"><code>end_episode</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/agent.py">View
source</a>

```python
end_episode(
    reward,
    observation=None
)
```

Signals the end of the episode to the agent.

#### Args:

*   <b>`reward`</b>: An float that is the last reward from the environment.
*   <b>`observation`</b>: numpy array that represents the last observation of
    the episode.

<h3 id="step"><code>step</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/agent.py">View
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

<a target="_blank" href="https://github.com/google-research/recsim/agent.py">View
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
    and is used when we save TensorFlow objects by tf.Save.
*   <b>`iteration_number`</b>: An integer that represents the checkpoint version
    and is used when restoring replay buffer.
*   <b>`bundle_dict`</b>: A dict containing additional Python objects owned by
    the agent. Each key is an object name and the value is the actual object.

#### Returns:

bool, True if unbundling was successful.
