<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.greedy_pctr_agent.GreedyPCTRAgent" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="multi_user"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="begin_episode"/>
<meta itemprop="property" content="bundle_and_checkpoint"/>
<meta itemprop="property" content="end_episode"/>
<meta itemprop="property" content="findBestDocuments"/>
<meta itemprop="property" content="step"/>
<meta itemprop="property" content="unbundle"/>
</div>

# recsim.agents.greedy_pctr_agent.GreedyPCTRAgent

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/greedy_pctr_agent.py">View
source</a>

## Class `GreedyPCTRAgent`

<!-- Start diff -->
An agent that recommends slates with the highest pCTR items.

Inherits From:
[`AbstractEpisodicRecommenderAgent`](../../../recsim/agent/AbstractEpisodicRecommenderAgent.md)

<!-- Placeholder for "Used in" -->

This agent assumes knowledge of the true underlying choice model. Note that this
implicitly means it receives observations of the true user and document states.
This agent myopically creates slates with items that have the highest
probability of being clicked under the given choice model.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/greedy_pctr_agent.py">View
source</a>

```python
__init__(
    action_space,
    belief_state,
    choice_model=cm.MultinomialLogitChoiceModel({'no_click_mass': 5})
)
```

Initializes a new greedy pCTR agent.

#### Args:

*   <b>`action_space`</b>: A gym.spaces object that specifies the format of
    actions
*   <b>`belief_state`</b>: An instantiation of AbstractUserState assumed by the
    agent
*   <b>`choice_model`</b>: An instantiation of AbstractChoiceModel assumed by
    the agent Default to a multinomial logit choice model with
    no_click_mass = 5.

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

Returns the agent's first action for this episode.

#### Args:

*   <b>`observation`</b>: numpy array, the environment's initial observation.

#### Returns:

*   <b>`slate`</b>: An integer array of size _slate_size, where each element is
    an index into the list of doc_obs

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

*   <b>`checkpoint_dir`</b>: A string that represents the path to the checkpoint
    and is used when we save TensorFlow objects by tf.Save.
*   <b>`iteration_number`</b>: An integer that represents the checkpoint version
    and is used when restoring replay buffer.

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
    observation=None
)
```

Signals the end of the episode to the agent.

#### Args:

*   <b>`reward`</b>: An float that is the last reward from the environment.
*   <b>`observation`</b>: numpy array that represents the last observation of
    the episode.

<h3 id="findBestDocuments"><code>findBestDocuments</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/greedy_pctr_agent.py">View
source</a>

```python
findBestDocuments(scores)
```

Returns the indices of the highest scores in sorted order.

#### Args:

*   <b>`scores`</b>: A list of floats representing unnormalized document scores

#### Returns:

*   <b>`sorted_indices`</b>: A list of integers indexing the highest scores, in
    sorted order

<h3 id="step"><code>step</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/greedy_pctr_agent.py">View
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

*   <b>`reward`</b>: Unused.
*   <b>`observation`</b>: A dictionary that includes the most recent
    observations and should have the following fields:
    -   user: A list of floats representing the user's observed state
    -   doc: A list of observations of document features

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
    and is used when we save TensorFlow objects by tf.Save.
*   <b>`iteration_number`</b>: An integer that represents the checkpoint version
    and is used when restoring replay buffer.
*   <b>`bundle_dict`</b>: A dict containing additional Python objects owned by
    the agent. Each key is an object name and the value is the actual object.

#### Returns:

bool, True if unbundling was successful.
