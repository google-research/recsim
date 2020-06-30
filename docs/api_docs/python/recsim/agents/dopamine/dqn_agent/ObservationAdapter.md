<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.dopamine.dqn_agent.ObservationAdapter" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="encode"/>
</div>

# recsim.agents.dopamine.dqn_agent.ObservationAdapter

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/dopamine/dqn_agent.py">View
source</a>

An adapter to convert between user/doc observation and images.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.agents.dopamine.dqn_agent.ObservationAdapter(
    input_observation_space, stack_size=1
)
</code></pre>

<!-- Placeholder for "Used in" -->
<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`output_observation_space`
</td>
<td>
The output observation space of the adapter.
</td>
</tr>
</table>

## Methods

<h3 id="encode"><code>encode</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/dopamine/dqn_agent.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>encode(
    observation
)
</code></pre>

Encode user observation and document observations to an image.
