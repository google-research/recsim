<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.slate_decomp_q_agent.compute_target_topk_q" />
<meta itemprop="path" content="Stable" />
</div>

# recsim.agents.slate_decomp_q_agent.compute_target_topk_q

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/slate_decomp_q_agent.py">View
source</a>

Computes the optimal target Q value with the greedy algorithm.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.agents.slate_decomp_q_agent.compute_target_topk_q(
    reward, gamma, next_actions, next_q_values, next_states, terminals
)
</code></pre>

<!-- Placeholder for "Used in" -->

This algorithm corresponds to the method "TT" in Ie et al.
https://arxiv.org/abs/1905.12767.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`reward`
</td>
<td>
[batch_size] tensor, the immediate reward.
</td>
</tr><tr>
<td>
`gamma`
</td>
<td>
float, discount factor with the usual RL meaning.
</td>
</tr><tr>
<td>
`next_actions`
</td>
<td>
[batch_size, slate_size] tensor, the next slate.
</td>
</tr><tr>
<td>
`next_q_values`
</td>
<td>
[batch_size, num_of_documents] tensor, the q values of the
documents in the next step.
</td>
</tr><tr>
<td>
`next_states`
</td>
<td>
[batch_size, 1 + num_of_documents] tensor, the features for the
user and the docuemnts in the next step.
</td>
</tr><tr>
<td>
`terminals`
</td>
<td>
[batch_size] tensor, indicating if this is a terminal step.
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
[batch_size] tensor, the target q values.
</td>
</tr>

</table>
