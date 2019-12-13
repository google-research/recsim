<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.tabular_q_agent.TabularQAgent" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="multi_user"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="begin_episode"/>
<meta itemprop="property" content="bundle_and_checkpoint"/>
<meta itemprop="property" content="end_episode"/>
<meta itemprop="property" content="step"/>
<meta itemprop="property" content="unbundle"/>
</div>

# recsim.agents.tabular_q_agent.TabularQAgent

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/tabular_q_agent.py">View
source</a>

## Class `TabularQAgent`

<!-- Start diff -->
Tabular Q-learning agent with universal function approximation.

Inherits From:
[`AbstractEpisodicRecommenderAgent`](../../../recsim/agent/AbstractEpisodicRecommenderAgent.md)

<!-- Placeholder for "Used in" -->

This agent provides a tabular implementation of the Q-learning algorithm. To
construct a tabular representation of the state-action space, the agent does the
following: 1. the action space consists of all ordered k-tuples of document
features available in observation['doc']; 2. the state space consists of
observation['user'] and observation['response']; 3. the observation and action
space are joined and flattened; 4. all continuoius values in the flattened
state-action vector are discretized into a predefined number of bins. In the
tabularized state-action space, the agent applies the standard Q-learning update
of Q_{t+1}(s,a) = (1-a) * Q_t(s,a) + a * (R(s,a) + g * max_a(Q_t(s', a))).
Assuming that the discretization of countinous attributes is fine enough, and
the problem itself is Markovian given the observations, the output of this agent
can be assumed to converge to a close approximation of the ground truth
Q-function. Producing ground truth Q-functions is the main intended use of this
agent, since discretization is prohibitively expensive in high-dimensional
environments.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/tabular_q_agent.py">View
source</a>

```python
__init__(
    observation_space,
    action_space,
    eval_mode=False,
    ignore_response=True,
    discretization_bounds=(0.0, 10.0),
    number_bins=100,
    exploration_policy='epsilon_greedy',
    exploration_temperature=0.99,
    learning_rate=0.1,
    gamma=0.99,
    **kwargs
)
```

TabularQAgent init.

#### Args:

*   <b>`observation_space`</b>: a gym.spaces object specifying the format of
    observations.
*   <b>`action_space`</b>: a gym.spaces object that specifies the format of
    actions.
*   <b>`eval_mode`</b>: Boolean indicating whether the agent is in training or
    eval mode.
*   <b>`ignore_response`</b>: Boolean indicating whether the agent should ignore
    the response part of the observation.
*   <b>`discretization_bounds`</b>: pair of real numbers indicating the min and
    max value for continuous attributes discretization. Values below the min
    will all be grouped in the first bin, while values above the max will all be
    grouped in the last bin. See the documentation of numpy.digitize for further
    details.
*   <b>`number_bins`</b>: positive integer number of bins used to discretize
    continuous attributes.
*   <b>`exploration_policy`</b>: either one of ['epsilon_greedy', 'min_count']
    or a custom function. TODO(mmladenov): formalize requirements of this
    function.
*   <b>`exploration_temperature`</b>: a real number passed as parameter to the
    exploration policy.
*   <b>`learning_rate`</b>: a real number between 0 and 1 indicating how much to
    update Q-values, i.e. Q_t+1(s,a) = (1 - learning_rate) * Q_t(s, a) +
    learning_rate * (R(s,a) + ...).
*   <b>`gamma`</b>: real value between 0 and 1 indicating the discount factor of
    the MDP.
*   <b>`**kwargs`</b>: additional arguments like eval_mode.

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

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/tabular_q_agent.py">View
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

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/tabular_q_agent.py">View
source</a>

```python
end_episode(
    reward,
    observation
)
```

Signals the end of the episode to the agent.

#### Args:

*   <b>`reward`</b>: An float that is the last reward from the environment.
*   <b>`observation`</b>: numpy array that represents the last observation of
    the episode.

<h3 id="step"><code>step</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/tabular_q_agent.py">View
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
    observations and should have the following fields:
    -   user: A NumPy array representing user's observed state. Assumes it is a
        concatenation of topic pull counts and topic click counts.
    -   doc: A NumPy array representing observations of document features.
        Assumes it is a concatenation of one-hot encoding of topic_id and
        document quality.

#### Returns:

*   <b>`slate`</b>: An integer array of size _slate_size, where each element is
    an index into the list of doc_obs

#### Raises:

*   <b>`ValueError`</b>: if reward is not in [0, 1].

<h3 id="unbundle"><code>unbundle</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/tabular_q_agent.py">View
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
