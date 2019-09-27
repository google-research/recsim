<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.cluster_bandit_agent" />
<meta itemprop="path" content="Stable" />
</div>

# Module: recsim.agents.cluster_bandit_agent

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/agents/cluster_bandit_agent.py">View
source</a>

Agent that picks topics based on the UCB1 algorithm given past responses.

<!-- Placeholder for "Used in" -->

## Classes

[`class ClusterBanditAgent`](../../recsim/agents/cluster_bandit_agent/ClusterBanditAgent.md):
An agent that recommends items with the highest UCBs of topic affinities.

[`class GreedyClusterAgent`](../../recsim/agents/cluster_bandit_agent/GreedyClusterAgent.md):
Simple agent sorting all documents of a topic according to quality.
