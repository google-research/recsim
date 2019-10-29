<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.slate_decomp_q_agent.SlateDecompQAgent" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="begin_episode"/>
<meta itemprop="property" content="bundle_and_checkpoint"/>
<meta itemprop="property" content="end_episode"/>
<meta itemprop="property" content="step"/>
<meta itemprop="property" content="unbundle"/>
</div>

# recsim.agents.slate_decomp_q_agent.SlateDecompQAgent

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/slate_decomp_q_agent.py">View
source</a>

## Class `SlateDecompQAgent`

A recommender agent implements DQN using slate decomposition techniques.

Inherits From:
[`DQNAgentRecSim`](../../../recsim/agents/dopamine/dqn_agent/DQNAgentRecSim.md),
[`AbstractEpisodicRecommenderAgent`](../../../recsim/agent/AbstractEpisodicRecommenderAgent.md)

<!-- Placeholder for "Used in" -->

<h2 id="__init__"><code>__init__</code></h2>

```python
__init__(
    *args,
    **kwargs
)
```

Initializes SlateDecompQAgent.

#### Args:

*   <b>`sess`</b>: a Tensorflow session.
*   <b>`observation_space`</b>: A gym.spaces object that specifies the format of
    observations.
*   <b>`action_space`</b>: A gym.spaces object that specifies the format of
    actions.
*   <b>`optimizer_name`</b>: The name of the optimizer.
*   <b>`select_slate_fn`</b>: A function that selects the slate.
*   <b>`compute_target_fn`</b>: A function that omputes the target q value.
*   <b>`stack_size`</b>: The stack size for the replay buffer.
*   <b>`eval_mode`</b>: A bool for whether the agent is in training or
    evaluation mode.
*   <b>`**kwargs`</b>: Keyword arguments to the DQNAgent.

## Methods

<h3 id="begin_episode"><code>begin_episode</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/slate_decomp_q_agent.py">View
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

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/slate_decomp_q_agent.py">View
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

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/slate_decomp_q_agent.py">View
source</a>

```python
step(
    reward,
    observation
)
```

Records the transition and returns the agent's next action.

It uses document-level user response instead of overral reward as the reward of
the problem.

#### Args:

*   <b>`reward`</b>: unused.
*   <b>`observation`</b>: a space.Dict that includes observation of the user
    state observation, documents and user responses.

#### Returns:

Array, the selected action.

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
