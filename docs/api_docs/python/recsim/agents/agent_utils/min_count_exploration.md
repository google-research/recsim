<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.agent_utils.min_count_exploration" />
<meta itemprop="path" content="Stable" />
</div>

# recsim.agents.agent_utils.min_count_exploration

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/agent_utils.py">View
source</a>

Minimum count exploration.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.agents.agent_utils.min_count_exploration(
    state_action_iterator, counts_function
)
</code></pre>

<!-- Placeholder for "Used in" -->

Picks the state-action pair with minimum counts. Args: state_action_iterator: an
iterator over slate, state_action_index tuples. counts_function: a container
holding the number of times a state-action pair has been executed so far.
Returns: slate: the picked slate. sa_index: the index of the picked slate in the
counts table.
