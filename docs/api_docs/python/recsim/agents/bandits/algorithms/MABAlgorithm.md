<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.bandits.algorithms.MABAlgorithm" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="set_state"/>
<meta itemprop="property" content="update"/>
</div>

# recsim.agents.bandits.algorithms.MABAlgorithm

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/bandits/algorithms.py">View
source</a>

Base class for Multi-armed bandit (MAB) algorithms.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.agents.bandits.algorithms.MABAlgorithm(
    num_arms, params, seed=0
)
</code></pre>

<!-- Placeholder for "Used in" -->

We implement multi-armed bandit algorithms with confidence width tuning proposed
in Hsu et al. https://arxiv.org/abs/1904.02664.

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

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`pulls`
</td>
<td>
A numpy array which counts number of pulls of each arm
</td>
</tr><tr>
<td>
`reward`
</td>
<td>
A numpy array which sums up reward of each arm
</td>
</tr><tr>
<td>
`optimism_scaling`
</td>
<td>
A float specifying the confidence level. Default value
(1.0) corresponds to the exploration strategy presented in the literature.
A smaller number means less exploration and more exploitation.
</td>
</tr><tr>
<td>
`_rng`
</td>
<td>
An instance of random.RandomState for random number generation
</td>
</tr>
</table>

## Methods

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
