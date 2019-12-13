<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.layers.abstract_click_bandit.AbstractClickBanditLayer" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="multi_user"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="begin_episode"/>
<meta itemprop="property" content="bundle_and_checkpoint"/>
<meta itemprop="property" content="end_episode"/>
<meta itemprop="property" content="step"/>
<meta itemprop="property" content="unbundle"/>
</div>

# recsim.agents.layers.abstract_click_bandit.AbstractClickBanditLayer

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/layers/abstract_click_bandit.py">View source</a>



## Class `AbstractClickBanditLayer`

<!-- Start diff -->
A hierarchical bandit layer which treats a set of base agents as arms.

Inherits From: [`AbstractHierarchicalAgentLayer`](../../../../recsim/agent/AbstractHierarchicalAgentLayer.md)

<!-- Placeholder for "Used in" -->

This layer consumes a list of base agents with apriori unknown mean payoffs
and has the job of mixing them in a way that minimizes the regret relative to
the best among them. Each agent is assumed to output a slate of size up to
slate_size. If an agent outputs an incomplete slate, the AbstractClickBandit
will use other agent's outputs to complete it, packing them in decreasing
order according to the index of the bandit policy. E.g. if using the upper
confidence bound as index, the AbstractClickBandit will put the partial slate
of the highest-UCB base agent in first place, then the second, until the slate
is complete.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    *args,
    **kwargs
)
```

Initializes a new bandit agent for clustered arm exploration.


#### Args:


* <b>`observation_space`</b>: Instance of a gym space corresponding to the
  observation format.
* <b>`action_space`</b>: A gym.spaces object that specifies the format of actions.
* <b>`arm_base_agent_ctors`</b>: a list of agent constructors, each agent corresponds
  to a bandit arm.
* <b>`alg_ctor`</b>: A class of an MABAlgorithm for exploration, default to UCB1.
* <b>`ci_scaling`</b>: A floating number specifying the scaling of confidence bound.
* <b>`random_seed`</b>: An integer for random seed.
* <b>`**kwargs`</b>: arguments for base agents.

## Properties

<h3 id="multi_user"><code>multi_user</code></h3>

Returns boolean indicating whether this agent serves multiple users.

## Methods

<h3 id="begin_episode"><code>begin_episode</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agent.py">View source</a>

``` python
begin_episode(observation=None)
```




<h3 id="bundle_and_checkpoint"><code>bundle_and_checkpoint</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agent.py">View source</a>

``` python
bundle_and_checkpoint(
    checkpoint_dir,
    iteration_number
)
```

Returns a self-contained bundle of the agent's state.


#### Args:


* <b>`checkpoint_dir`</b>: A string for the directory where objects will be saved.
* <b>`iteration_number`</b>: An integer of iteration number to use for naming the
  checkpoint file.


#### Returns:

A dictionary containing additional Python objects to be checkpointed by
  the experiment. Each key is a string for the object name and the value
  is actual object. If the checkpoint directory does not exist, returns
  empty dictionary.


<h3 id="end_episode"><code>end_episode</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agent.py">View source</a>

``` python
end_episode(
    reward,
    observation
)
```




<h3 id="step"><code>step</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/layers/abstract_click_bandit.py">View source</a>

``` python
step(
    reward,
    observation
)
```

Records the most recent transition and returns the agent's next action.

We store the observation of the last time step since we want to store it
with the reward.

#### Args:


* <b>`reward`</b>: Unused.
* <b>`observation`</b>: A dictionary that includes the most recent observations and
  should have the following fields:
  - user: A dictionary representing user's observed state. Assumes
    observation['user']['sufficient_statics'] is a dictionary containing
    base agent impression counts and base agent click counts.


#### Returns:


* <b>`slate`</b>: An integer array of size _slate_size, where each element is an
  index into the list of doc_obs

<h3 id="unbundle"><code>unbundle</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agent.py">View source</a>

``` python
unbundle(
    checkpoint_dir,
    iteration_number,
    bundle_dict
)
```

Restores the agent from a checkpoint.


#### Args:


* <b>`checkpoint_dir`</b>: A string that represents the path to the checkpoint saved
  by tf.Save.
* <b>`iteration_number`</b>: An integer that represents the checkpoint version and is
  used when restoring replay buffer.
* <b>`bundle_dict`</b>: A dict containing additional Python objects owned by the
  agent. Each key is an object name and the value is the actual object.


#### Returns:

bool, True if unbundling was successful.




