<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.slate_decomp_q_agent.score_documents" />
<meta itemprop="path" content="Stable" />
</div>

# recsim.agents.slate_decomp_q_agent.score_documents

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/slate_decomp_q_agent.py">View
source</a>

Computes unnormalized scores given both user and document observations.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.agents.slate_decomp_q_agent.score_documents(
    user_obs, doc_obs, no_click_mass=1.0, is_mnl=False, min_normalizer=-1.0
)
</code></pre>

<!-- Placeholder for "Used in" -->

Similar to score_documents_tf but works on NumPy objects.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`user_obs`
</td>
<td>
An instance of AbstractUserState.
</td>
</tr><tr>
<td>
`doc_obs`
</td>
<td>
A numpy array that represents the observation of all documents in
the candidate set.
</td>
</tr><tr>
<td>
`no_click_mass`
</td>
<td>
a float indicating the mass given to a no click option
</td>
</tr><tr>
<td>
`is_mnl`
</td>
<td>
whether to use a multinomial logit model instead of a multinomial
proportional model.
</td>
</tr><tr>
<td>
`min_normalizer`
</td>
<td>
A float (<= 0) used to offset the scores to be positive when
using multinomial proportional model.
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A float array that stores unnormalzied scores of documents and a float
number that represents the score for the action of picking no document.
</td>
</tr>

</table>
