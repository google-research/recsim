<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.layers.fixed_length_history.FixedLengthHistoryLayer" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="begin_episode"/>
<meta itemprop="property" content="bundle_and_checkpoint"/>
<meta itemprop="property" content="end_episode"/>
<meta itemprop="property" content="step"/>
<meta itemprop="property" content="unbundle"/>
</div>

# recsim.agents.layers.fixed_length_history.FixedLengthHistoryLayer

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/layers/fixed_length_history.py">View
source</a>

Creates a buffer of the last k rewards and observations.

Inherits From:
[`SufficientStatisticsLayer`](../../../../recsim/agents/layers/sufficient_statistics/SufficientStatisticsLayer.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.agents.layers.fixed_length_history.FixedLengthHistoryLayer(
    base_agent_ctor, observation_space, action_space, history_length,
    remember_user=True, remember_response=True, remember_doc=False, **kwargs
)
</code></pre>

<!-- Placeholder for "Used in" -->

This module introduces sufficient statistics in the form of a buffer holding the
last k (specified by history_length) observations. This buffer is injected into
observation_space[\'user\'][\'sufficient_statistics\'] in the form of a
gym.spaces.Tuple of length up to k . In the first k-1 steps of the episode there
are not enough observations to fill the buffer, so they will be filled with
None. Each non-vacuous element of the tuple is an instance of (a subset of)
observation_space.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`base_agent_ctor`
</td>
<td>
a constructor for the base agent.
</td>
</tr><tr>
<td>
`observation_space`
</td>
<td>
a gym.spaces object specifying the format of
observations.
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
`history_length`
</td>
<td>
positive integer number of observations to remember.
</td>
</tr><tr>
<td>
`remember_user`
</td>
<td>
boolean, indicates whether to track
observation_space[\'user\'].
</td>
</tr><tr>
<td>
`remember_response`
</td>
<td>
boolean, indicates whether to track
observation_space[\'response\'].
</td>
</tr><tr>
<td>
`remember_doc`
</td>
<td>
boolean, indicates whether to track
observation_space[\'doc\'].
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
arguments to pass to the downstream agent at construction time.
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr> <td> `multi_user` </td> <td> Returns boolean indicating whether this agent
serves multiple users. </td> </tr><tr> <td> `observation_space` </td> <td>

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

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/layers/sufficient_statistics.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>end_episode(
    reward, observation
)
</code></pre>

<h3 id="step"><code>step</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/layers/sufficient_statistics.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
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
