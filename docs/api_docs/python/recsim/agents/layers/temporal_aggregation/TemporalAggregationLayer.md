<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.layers.temporal_aggregation.TemporalAggregationLayer" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="begin_episode"/>
<meta itemprop="property" content="bundle_and_checkpoint"/>
<meta itemprop="property" content="end_episode"/>
<meta itemprop="property" content="step"/>
<meta itemprop="property" content="unbundle"/>
</div>

# recsim.agents.layers.temporal_aggregation.TemporalAggregationLayer

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/layers/temporal_aggregation.py">View
source</a>

Temporally aggregated reinforcement learning agent.

Inherits From:
[`AbstractHierarchicalAgentLayer`](../../../../recsim/agent/AbstractHierarchicalAgentLayer.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.agents.layers.temporal_aggregation.TemporalAggregationLayer(
    base_agent_ctor, observation_space, action_space, gamma=0.0,
    aggregation_period=1, switching_cost=1.0, document_comparison_fcn=None, **kwargs
)
</code></pre>

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
`gamma`
</td>
<td>
geometric discounting factor between [0, 1) for the event-level
objective.
</td>
</tr><tr>
<td>
`aggregation_period`
</td>
<td>
number of time steps to hold an action fixed.
</td>
</tr><tr>
<td>
`switching_cost`
</td>
<td>
a non-negative penalty for switching an action.
</td>
</tr><tr>
<td>
`document_comparison_fcn`
</td>
<td>
a function taking two document observations and
returning a Boolean value that indicates if they are considered
equivalent. This is useful for making decisions at a higher abstraction
level (e.g. comparing only document topics). If not provided, this will
default to direct observation equality.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
base_agent initialization args.
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

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/layers/temporal_aggregation.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>step(
    reward, observation
)
</code></pre>

Preprocesses the reward and observation and calls base agent.

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
A dictionary that includes the most recent observations and
should have the following fields:
- user: A NumPy array representing user's observed state. Assumes it is
a concatenation of topic pull counts and topic click counts.
- doc: A NumPy array representing observations of document features.
Assumes it is a concatenation of one-hot encoding of topic_id and
document quality.
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
index into the list of doc_obs.
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`RuntimeError`
</td>
<td>
if the agent has to hold a slate with given features fixed
for k steps but the documents needed to reconstruct that slate
become unavailable.
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
