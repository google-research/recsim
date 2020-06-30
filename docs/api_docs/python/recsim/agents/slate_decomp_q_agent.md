<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.slate_decomp_q_agent" />
<meta itemprop="path" content="Stable" />
</div>

# Module: recsim.agents.slate_decomp_q_agent

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/slate_decomp_q_agent.py">View
source</a>

Agent that implements the Slate-Q algorithms.

## Classes

[`class SlateDecompQAgent`](../../recsim/agents/slate_decomp_q_agent/SlateDecompQAgent.md):
A recommender agent implements DQN using slate decomposition techniques.

## Functions

[`compute_probs_tf(...)`](../../recsim/agents/slate_decomp_q_agent/compute_probs_tf.md):
Computes the selection probability and returns selected index.

[`compute_target_greedy_q(...)`](../../recsim/agents/slate_decomp_q_agent/compute_target_greedy_q.md):
Computes the optimal target Q value with the adaptive greedy algorithm.

[`compute_target_optimal_q(...)`](../../recsim/agents/slate_decomp_q_agent/compute_target_optimal_q.md):
Builds an op used as a target for the Q-value.

[`compute_target_sarsa(...)`](../../recsim/agents/slate_decomp_q_agent/compute_target_sarsa.md):
Computes the SARSA target Q value.

[`compute_target_topk_q(...)`](../../recsim/agents/slate_decomp_q_agent/compute_target_topk_q.md):
Computes the optimal target Q value with the greedy algorithm.

[`create_agent(...)`](../../recsim/agents/slate_decomp_q_agent/create_agent.md):
Creates a slate decomposition agent given agent name.

[`score_documents(...)`](../../recsim/agents/slate_decomp_q_agent/score_documents.md):
Computes unnormalized scores given both user and document observations.

[`score_documents_tf(...)`](../../recsim/agents/slate_decomp_q_agent/score_documents_tf.md):
Computes unnormalized scores given both user and document observations.

[`select_slate_greedy(...)`](../../recsim/agents/slate_decomp_q_agent/select_slate_greedy.md):
Selects the slate using the adaptive greedy algorithm.

[`select_slate_optimal(...)`](../../recsim/agents/slate_decomp_q_agent/select_slate_optimal.md):
Selects the slate using exhaustive search.

[`select_slate_topk(...)`](../../recsim/agents/slate_decomp_q_agent/select_slate_topk.md):
Selects the slate using the top-K algorithm.
