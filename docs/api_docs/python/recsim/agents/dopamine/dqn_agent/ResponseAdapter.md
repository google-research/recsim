<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.dopamine.dqn_agent.ResponseAdapter" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="encode"/>
</div>

# recsim.agents.dopamine.dqn_agent.ResponseAdapter

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/dopamine/dqn_agent.py">View
source</a>

Custom flattening of responses to accommodate dopamine replay buffer.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.agents.dopamine.dqn_agent.ResponseAdapter(
    input_response_space
)
</code></pre>

<!-- Placeholder for "Used in" -->

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_response_space`
</td>
<td>
this is assumed to be an instance of
gym.spaces.Tuple; each element of the tuple is has to be an instance
of gym.spaces.Dict consisting of feature_name: 0-d gym.spaces.Box
(single float) key-value pairs.
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr> <td> `response_dtype` </td> <td>

</td> </tr><tr> <td> `response_names` </td> <td>

</td> </tr><tr> <td> `response_shape` </td> <td>

</td>
</tr>
</table>

## Methods

<h3 id="encode"><code>encode</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/dopamine/dqn_agent.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>encode(
    responses
)
</code></pre>
