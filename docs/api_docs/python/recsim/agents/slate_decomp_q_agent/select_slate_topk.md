<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.slate_decomp_q_agent.select_slate_topk" />
<meta itemprop="path" content="Stable" />
</div>

# recsim.agents.slate_decomp_q_agent.select_slate_topk

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/slate_decomp_q_agent.py">View
source</a>

Selects the slate using the top-K algorithm.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.agents.slate_decomp_q_agent.select_slate_topk(
    slate_size, s_no_click, s, q
)
</code></pre>

<!-- Placeholder for "Used in" -->

This algorithm corresponds to the method "TS" in Ie et al.
https://arxiv.org/abs/1905.12767.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`slate_size`
</td>
<td>
int, the size of the recommendation slate.
</td>
</tr><tr>
<td>
`s_no_click`
</td>
<td>
float tensor, the score for not clicking any document.
</td>
</tr><tr>
<td>
`s`
</td>
<td>
[num_of_documents] tensor, the scores for clicking documents.
</td>
</tr><tr>
<td>
`q`
</td>
<td>
[num_of_documents] tensor, the predicted q values for documents.
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
[slate_size] tensor, the selected slate.
</td>
</tr>

</table>
