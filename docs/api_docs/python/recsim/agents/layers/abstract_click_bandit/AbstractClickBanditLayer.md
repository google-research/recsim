<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.layers.abstract_click_bandit.AbstractClickBanditLayer" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="begin_episode"/>
<meta itemprop="property" content="bundle_and_checkpoint"/>
<meta itemprop="property" content="end_episode"/>
<meta itemprop="property" content="step"/>
<meta itemprop="property" content="unbundle"/>
</div>

# recsim.agents.layers.abstract_click_bandit.AbstractClickBanditLayer

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/layers/abstract_click_bandit.py">View source</a>



A hierarchical bandit layer which treats a set of base agents as arms.

Inherits From: [`AbstractHierarchicalAgentLayer`](../../../../recsim/agent/AbstractHierarchicalAgentLayer.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.agents.layers.abstract_click_bandit.AbstractClickBanditLayer(
    observation_space, action_space, arm_base_agent_ctors,
    alg_ctor=recsim.agents.bandits.algorithms.UCB1, ci_scaling=1.0, random_seed=0,
    **kwargs
)
</code></pre>

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

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`observation_space`
</td>
<td>
Instance of a gym space corresponding to the
observation format.
</td>
</tr><tr>
<td>
`action_space`
</td>
<td>
A gym.spaces object that specifies the format of actions.
</td>
</tr><tr>
<td>
`arm_base_agent_ctors`
</td>
<td>
a list of agent constructors, each agent corresponds
to a bandit arm.
</td>
</tr><tr>
<td>
`alg_ctor`
</td>
<td>
A class of an MABAlgorithm for exploration, default to UCB1.
</td>
</tr><tr>
<td>
`ci_scaling`
</td>
<td>
A floating number specifying the scaling of confidence bound.
</td>
</tr><tr>
<td>
`random_seed`
</td>
<td>
An integer for random seed.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
arguments for base agents.
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`multi_user`
</td>
<td>
Returns boolean indicating whether this agent serves multiple users.
</td>
</tr>
</table>

## Methods

<h3 id="begin_episode"><code>begin_episode</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agent.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>begin_episode(
    observation=None
)
</code></pre>

<h3 id="bundle_and_checkpoint"><code>bundle_and_checkpoint</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agent.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>bundle_and_checkpoint(
    checkpoint_dir, iteration_number
)
</code></pre>

Returns a self-contained bundle of the agent's state.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`checkpoint_dir`
</td>
<td>
A string for the directory where objects will be saved.
</td>
</tr><tr>
<td>
`iteration_number`
</td>
<td>
An integer of iteration number to use for naming the
checkpoint file.
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A dictionary containing additional Python objects to be checkpointed by
the experiment. Each key is a string for the object name and the value
is actual object. If the checkpoint directory does not exist, returns
empty dictionary.
</td>
</tr>

</table>

<h3 id="end_episode"><code>end_episode</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agent.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>end_episode(
    reward, observation
)
</code></pre>

<h3 id="step"><code>step</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/layers/abstract_click_bandit.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>step(
    reward, observation
)
</code></pre>

Records the most recent transition and returns the agent's next action.

We store the observation of the last time step since we want to store it
with the reward.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`reward`
</td>
<td>
Unused.
</td>
</tr><tr>
<td>
`observation`
</td>
<td>
A dictionary that includes the most recent observations and
should have the following fields:
- user: A dictionary representing user's observed state. Assumes
observation['user']['sufficient_statics'] is a dictionary containing
base agent impression counts and base agent click counts.
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`slate`
</td>
<td>
An integer array of size _slate_size, where each element is an
index into the list of doc_obs
</td>
</tr>
</table>

<h3 id="unbundle"><code>unbundle</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agent.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>unbundle(
    checkpoint_dir, iteration_number, bundle_dict
)
</code></pre>

Restores the agent from a checkpoint.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`checkpoint_dir`
</td>
<td>
A string that represents the path to the checkpoint saved
by tf.Save.
</td>
</tr><tr>
<td>
`iteration_number`
</td>
<td>
An integer that represents the checkpoint version and is
used when restoring replay buffer.
</td>
</tr><tr>
<td>
`bundle_dict`
</td>
<td>
A dict containing additional Python objects owned by the
agent. Each key is an object name and the value is the actual object.
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
bool, True if unbundling was successful.
</td>
</tr>

</table>
