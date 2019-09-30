<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.slate_decomp_q_agent.compute_target_greedy_q" />
<meta itemprop="path" content="Stable" />
</div>

# recsim.agents.slate_decomp_q_agent.compute_target_greedy_q

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/agents/slate_decomp_q_agent.py">View
source</a>

Computes the optimal target Q value with the adaptive greedy algorithm.

```python
recsim.agents.slate_decomp_q_agent.compute_target_greedy_q(
    reward,
    gamma,
    next_actions,
    next_q_values,
    next_states,
    terminals
)
```

<!-- Placeholder for "Used in" -->

This algorithm corresponds to the method "GT" in Ie et al.
https://arxiv.org/abs/1905.12767..

#### Args:

*   <b>`reward`</b>: [batch_size] tensor, the immediate reward.
*   <b>`gamma`</b>: float, discount factor with the usual RL meaning.
*   <b>`next_actions`</b>: [batch_size, slate_size] tensor, the next slate.
*   <b>`next_q_values`</b>: [batch_size, num_of_documents] tensor, the q values
    of the documents in the next step.
*   <b>`next_states`</b>: [batch_size, 1 + num_of_documents] tensor, the
    features for the user and the docuemnts in the next step.
*   <b>`terminals`</b>: [batch_size] tensor, indicating if this is a terminal
    step.

#### Returns:

[batch_size] tensor, the target q values.
