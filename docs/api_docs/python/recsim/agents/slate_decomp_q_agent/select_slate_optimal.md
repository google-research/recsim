<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.slate_decomp_q_agent.select_slate_optimal" />
<meta itemprop="path" content="Stable" />
</div>

# recsim.agents.slate_decomp_q_agent.select_slate_optimal

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//agents/slate_decomp_q_agent.py">View
source</a>

Selects the slate using exhaustive search.

```python
recsim.agents.slate_decomp_q_agent.select_slate_optimal(
    slate_size,
    s_no_click,
    s,
    q
)
```

<!-- Placeholder for "Used in" -->

This algorithm corresponds to the method "OS" in Ie et al.
https://arxiv.org/abs/1905.12767.

#### Args:

*   <b>`slate_size`</b>: int, the size of the recommendation slate.
*   <b>`s_no_click`</b>: float tensor, the score for not clicking any document.
*   <b>`s`</b>: [num_of_documents] tensor, the scores for clicking documents.
*   <b>`q`</b>: [num_of_documents] tensor, the predicted q values for documents.

#### Returns:

[slate_size] tensor, the selected slate.
