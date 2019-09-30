<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.full_slate_q_agent.FullSlateQAgent" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="begin_episode"/>
<meta itemprop="property" content="bundle_and_checkpoint"/>
<meta itemprop="property" content="end_episode"/>
<meta itemprop="property" content="step"/>
<meta itemprop="property" content="unbundle"/>
</div>

# recsim.agents.full_slate_q_agent.FullSlateQAgent

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/agents/full_slate_q_agent.py">View
source</a>

## Class `FullSlateQAgent`

A recommender agent implements full slate Q-learning based on DQN agent.

Inherits From:
[`DQNAgentRecSim`](../../../recsim/agents/dopamine/dqn_agent/DQNAgentRecSim.md),
[`AbstractEpisodicRecommenderAgent`](../../../recsim/agent/AbstractEpisodicRecommenderAgent.md)

<!-- Placeholder for "Used in" -->

This is a standard, nondecomposed Q-learning method that treats each slate
atomically (i.e., holistically) as a single action.

<h2 id="__init__"><code>__init__</code></h2>

```python
__init__(
    *args,
    **kwargs
)
```

Initializes a FullSlateQAgent.

#### Args:

*   <b>`sess`</b>: a Tensorflow session.
*   <b>`observation_space`</b>: A gym.spaces object that specifies the format of
    observations.
*   <b>`action_space`</b>: A gym.spaces object that specifies the format of
    actions.
*   <b>`optimizer_name`</b>: The name of the optimizer.
*   <b>`eval_mode`</b>: A bool for whether the agent is in training or
    evaluation mode.
*   <b>`**kwargs`</b>: Keyword arguments to the DQNAgent.

## Methods

<h3 id="begin_episode"><code>begin_episode</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/agents/full_slate_q_agent.py">View
source</a>

```python
begin_episode(observation)
```

Returns the agent's first action for this episode.

#### Args:

*   <b>`observation`</b>: numpy array, the environment's initial observation.

#### Returns:

An integer array of size _slate_size, the selected slated, each element of which
is an index in the list of doc_obs.

<h3 id="bundle_and_checkpoint"><code>bundle_and_checkpoint</code></h3>

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

*   <b>`checkpoint_dir`</b>: str, directory where TensorFlow objects will be
    saved.
*   <b>`iteration_number`</b>: int, iteration number to use for naming the
    checkpoint file.

#### Returns:

A dict containing additional Python objects to be checkpointed by the
experiment. If the checkpoint directory does not exist, returns None.

<h3 id="end_episode"><code>end_episode</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/agents/full_slate_q_agent.py">View
source</a>

```python
end_episode(
    reward,
    observation
)
```

Signals the end of the episode to the agent.

We store the observation of the current time step, which is the last observation
of the episode.

#### Args:

*   <b>`reward`</b>: float, the last reward from the environment.
*   <b>`observation`</b>: numpy array, the environment's initial observation.

<h3 id="step"><code>step</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/agents/full_slate_q_agent.py">View
source</a>

```python
step(
    reward,
    observation
)
```

Receives observations of environment and returns a slate.

#### Args:

*   <b>`reward`</b>: A double representing the overall reward to the recommended
    slate.
*   <b>`observation`</b>: A dictionary that stores all the observations
    including:
    -   user: A list of floats representing the user's observed state
    -   doc: A list of observations of document features
    -   response: A vector valued response signal that represent user's response
        to each document

#### Returns:

*   <b>`slate`</b>: An integer array of size _slate_size, where each element is
    an index in the list of document observvations.

<h3 id="unbundle"><code>unbundle</code></h3>

```python
unbundle(
    checkpoint_dir,
    iteration_number,
    bundle_dictionary
)
```

Restores the agent from a checkpoint.

Restores the agent's Python objects to those specified in bundle_dictionary, and
restores the TensorFlow objects to those specified in the checkpoint_dir. If the
checkpoint_dir does not exist, will not reset the agent's state.

#### Args:

*   <b>`checkpoint_dir`</b>: str, path to the checkpoint saved by tf.Save.
*   <b>`iteration_number`</b>: int, checkpoint version, used when restoring the
    replay buffer.
*   <b>`bundle_dictionary`</b>: dict, containing additional Python objects owned
    by the agent.

#### Returns:

bool, True if unbundling was successful.
