<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agent.AbstractHierarchicalAgentLayer" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="begin_episode"/>
<meta itemprop="property" content="bundle_and_checkpoint"/>
<meta itemprop="property" content="end_episode"/>
<meta itemprop="property" content="step"/>
<meta itemprop="property" content="unbundle"/>
</div>

# recsim.agent.AbstractHierarchicalAgentLayer

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agent.py">View
source</a>

Parent class for stackable agent layers.

Inherits From:
[`AbstractRecommenderAgent`](../../recsim/agent/AbstractRecommenderAgent.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.agent.AbstractHierarchicalAgentLayer(
    action_space, *base_agent_ctors
)
</code></pre>

<!-- Placeholder for "Used in" -->

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`action_space`
</td>
<td>
A gym.spaces object that specifies the format of actions.
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

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agent.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>begin_episode(
    observation=None
)
</code></pre>

<h3 id="bundle_and_checkpoint"><code>bundle_and_checkpoint</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agent.py">View
source</a>

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

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agent.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>end_episode(
    reward, observation
)
</code></pre>

<h3 id="step"><code>step</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agent.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>step(
    reward, observation
)
</code></pre>

Records the most recent transition and returns the agent's next action.

We store the observation of the last time step since we want to store it with
the reward.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`reward`
</td>
<td>
The reward received from the agent's most recent action as a
float.
</td>
</tr><tr>
<td>
`observation`
</td>
<td>
A dictionary that includes the most recent observations.
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

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agent.py">View
source</a>

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
