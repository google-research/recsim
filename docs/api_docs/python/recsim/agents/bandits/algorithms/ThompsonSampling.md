<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.bandits.algorithms.ThompsonSampling" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="get_arm"/>
<meta itemprop="property" content="get_score"/>
<meta itemprop="property" content="print"/>
<meta itemprop="property" content="set_state"/>
<meta itemprop="property" content="update"/>
</div>

# recsim.agents.bandits.algorithms.ThompsonSampling

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/bandits/algorithms.py">View
source</a>

Thompson Sampling algorithm for the Bernoulli bandit.

Inherits From:
[`MABAlgorithm`](../../../../recsim/agents/bandits/algorithms/MABAlgorithm.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.agents.bandits.algorithms.ThompsonSampling(
    num_arms, params, seed=0
)
</code></pre>

<!-- Placeholder for "Used in" -->

See "Further Optimal Regret Bounds for Thompson Sampling" by Agrawal and Goyal.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`num_arms`
</td>
<td>
Number of arms. Must be greater than one.
</td>
</tr><tr>
<td>
`params`
</td>
<td>
A dictionary which includes additional parameters like
optimism_scaling. Default is an empty dictionary.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
Random seed for this object. Default is zero.
</td>
</tr>
</table>

## Methods

<h3 id="get_arm"><code>get_arm</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/bandits/algorithms.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_arm(
    t
)
</code></pre>

<h3 id="get_score"><code>get_score</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/bandits/algorithms.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_score(
    t
)
</code></pre>

Samples scores from the posterior distribution.

<h3 id="print"><code>print</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/bandits/algorithms.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@staticmethod</code>
<code>print()
</code></pre>

<h3 id="set_state"><code>set_state</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/bandits/algorithms.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_state(
    pulls, reward
)
</code></pre>

<h3 id="update"><code>update</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/bandits/algorithms.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>update(
    arm, reward
)
</code></pre>
