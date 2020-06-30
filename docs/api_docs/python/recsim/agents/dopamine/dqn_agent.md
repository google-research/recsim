<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.dopamine.dqn_agent" />
<meta itemprop="path" content="Stable" />
</div>

# Module: recsim.agents.dopamine.dqn_agent

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/dopamine/dqn_agent.py">View
source</a>

Recsim-specific Dopamine DQN agent and related utilities.

## Classes

[`class DQNAgentRecSim`](../../../recsim/agents/dopamine/dqn_agent/DQNAgentRecSim.md):
RecSim-specific Dopamine DQN agent that converts the observation space.

[`class DQNNetworkType`](../../../recsim/agents/dopamine/dqn_agent/DQNNetworkType.md):
dqn_network(q_values,)

[`class ObservationAdapter`](../../../recsim/agents/dopamine/dqn_agent/ObservationAdapter.md):
An adapter to convert between user/doc observation and images.

[`class ResponseAdapter`](../../../recsim/agents/dopamine/dqn_agent/ResponseAdapter.md):
Custom flattening of responses to accommodate dopamine replay buffer.

## Functions

[`recsim_dqn_network(...)`](../../../recsim/agents/dopamine/dqn_agent/recsim_dqn_network.md)

[`wrapped_replay_buffer(...)`](../../../recsim/agents/dopamine/dqn_agent/wrapped_replay_buffer.md)
