<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.slate_decomp_q_agent.compute_probs_tf" />
<meta itemprop="path" content="Stable" />
</div>

# recsim.agents.slate_decomp_q_agent.compute_probs_tf

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/slate_decomp_q_agent.py">View
source</a>

Computes the selection probability and returns selected index.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.agents.slate_decomp_q_agent.compute_probs_tf(
    slate, scores_tf, score_no_click_tf
)
</code></pre>

<!-- Placeholder for "Used in" -->

This assumes scores are normalizable, e.g., scores cannot be negative.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`slate`
</td>
<td>
a list of integers that represents the video slate.
</td>
</tr><tr>
<td>
`scores_tf`
</td>
<td>
a float tensor that stores the scores of all documents.
</td>
</tr><tr>
<td>
`score_no_click_tf`
</td>
<td>
a float tensor that represents the score for the action
of picking no document.
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A float tensor that represents the probabilities of selecting each document
in the slate.
</td>
</tr>

</table>
