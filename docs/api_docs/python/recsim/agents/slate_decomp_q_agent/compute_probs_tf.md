<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.slate_decomp_q_agent.compute_probs_tf" />
<meta itemprop="path" content="Stable" />
</div>

# recsim.agents.slate_decomp_q_agent.compute_probs_tf

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//agents/slate_decomp_q_agent.py">View
source</a>

Computes the selection probability and returns selected index.

```python
recsim.agents.slate_decomp_q_agent.compute_probs_tf(
    slate,
    scores_tf,
    score_no_click_tf
)
```

<!-- Placeholder for "Used in" -->

This assumes scores are normalizable, e.g., scores cannot be negative.

#### Args:

*   <b>`slate`</b>: a list of integers that represents the video slate.
*   <b>`scores_tf`</b>: a float tensor that stores the scores of all documents.
*   <b>`score_no_click_tf`</b>: a float tensor that represents the score for the
    action of picking no document.

#### Returns:

A float tensor that represents the probabilities of selecting each document in
the slate.
