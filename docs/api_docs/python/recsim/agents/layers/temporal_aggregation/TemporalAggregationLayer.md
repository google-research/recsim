<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.layers.temporal_aggregation.TemporalAggregationLayer" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="multi_user"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="begin_episode"/>
<meta itemprop="property" content="bundle_and_checkpoint"/>
<meta itemprop="property" content="end_episode"/>
<meta itemprop="property" content="step"/>
<meta itemprop="property" content="unbundle"/>
</div>

# recsim.agents.layers.temporal_aggregation.TemporalAggregationLayer

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/layers/temporal_aggregation.py">View
source</a>

## Class `TemporalAggregationLayer`

<!-- Start diff -->
Temporally aggregated reinforcement learning agent.

Inherits From:
[`AbstractHierarchicalAgentLayer`](../../../../recsim/agent/AbstractHierarchicalAgentLayer.md)

<!-- Placeholder for "Used in" -->

A reinforcement learning agent that implements learns a temporally aggregated
policy. This is achieved in two ways: * making a decision only every k-steps; *
introducing a switching cost penalty whenever the policy executes two different
consequitve actions. See "Advantage Amplification in Slowly Evolving
Latent-State Environments" Martin Mladenov, Ofer Meshi, Jayden Ooi, Dale
Schuurmans, Craig Boutilier https://arxiv.org/abs/1905.13559 for details.
Implementation-wise, this agent relies on an event-level (base) agent suited for
the domain. Aggregation is implemented as a preprocessing step for the base
agent: in the first case only calling the agent every k steps (and adjusting the
discount (gamma) accordingly to keep the objective consistent), in the second
case subtracting a penalty from the environment reward whenever the base agent
switches actions. For switching cost, it is also necessary to append the last
executed action to the state representation, otherwise the learning problem
becomes non-Markovian.

The two methods are not mutually exclusive and may be used in conjunction by
specifying a non-unit aggregation_period and a non-zero switching_cost.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/layers/temporal_aggregation.py">View
source</a>

```python
__init__(
    base_agent_ctor,
    observation_space,
    action_space,
    gamma=0.0,
    aggregation_period=1,
    switching_cost=1.0,
    document_comparison_fcn=None,
    **kwargs
)
```

TemporallyAggregatedAgent init.

#### Args:

*   <b>`base_agent_ctor`</b>: a constructor for the base agent.
*   <b>`observation_space`</b>: a gym.spaces object specifying the format of
    observations.
*   <b>`action_space`</b>: A gym.spaces object that specifies the format of
    actions.
*   <b>`gamma`</b>: geometric discounting factor between [0, 1) for the
    event-level objective.
*   <b>`aggregation_period`</b>: number of time steps to hold an action fixed.
*   <b>`switching_cost`</b>: a non-negative penalty for switching an action.
*   <b>`document_comparison_fcn`</b>: a function taking two document
    observations and returning a Boolean value that indicates if they are
    considered equivalent. This is useful for making decisions at a higher
    abstraction level (e.g. comparing only document topics). If not provided,
    this will default to direct observation equality.
*   <b>`**kwargs`</b>: base_agent initialization args.

## Properties

<h3 id="multi_user"><code>multi_user</code></h3>

Returns boolean indicating whether this agent serves multiple users.

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

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agent.py">View
source</a>

```python
end_episode(
    reward,
    observation
)
```

<h3 id="step"><code>step</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/layers/temporal_aggregation.py">View
source</a>

```python
step(
    reward,
    observation
)
```

Preprocesses the reward and observation and calls base agent.

#### Args:

*   <b>`reward`</b>: The reward received from the agent's most recent action as
    a float.
*   <b>`observation`</b>: A dictionary that includes the most recent
    observations and should have the following fields:
    -   user: A NumPy array representing user's observed state. Assumes it is a
        concatenation of topic pull counts and topic click counts.
    -   doc: A NumPy array representing observations of document features.
        Assumes it is a concatenation of one-hot encoding of topic_id and
        document quality.

#### Returns:

*   <b>`slate`</b>: An integer array of size _slate_size, where each element is
    an index into the list of doc_obs.

#### Raises:

*   <b>`RuntimeError`</b>: if the agent has to hold a slate with given features
    fixed for k steps but the documents needed to reconstruct that slate become
    unavailable.

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
