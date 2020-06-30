<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.agent_utils.GymSpaceWalker" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="apply_and_flatten"/>
</div>

# recsim.agents.agent_utils.GymSpaceWalker

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/agent_utils.py">View
source</a>

Class for recursively applying a given function to a gym space.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.agents.agent_utils.GymSpaceWalker(
    gym_space, leaf_op
)
</code></pre>

<!-- Placeholder for "Used in" -->

Gym spaces have nested structure in terms of container spaces (e.g. Dict and
Tuple) containing basic spaces such as Discrete and Box. This class consumes a
gym observation definition and a leaf operator is used to produce a flat list of
the contents of the gym space, apply the leaf operator to all basic spaces in
the proces. E.g., given a gym space of the form Tuple((Box(1), Box(1)) and a
leaf operator f, this class can is used to transform an observation (a, b) to
[f(a), f(b)].

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

</table>

gym_space: An instance of an OpenAI Gym space. leaf_op: A function taking as
arguments an OpenAI Gym space and an observation conforming to that space. There
are no requirements on its output.

## Methods

<h3 id="apply_and_flatten"><code>apply_and_flatten</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/agent_utils.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>apply_and_flatten(
    gym_observations
)
</code></pre>
