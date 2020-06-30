<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.interest_evolution.IEvUserState" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_observation"/>
<meta itemprop="property" content="observation_space"/>
<meta itemprop="property" content="score_document"/>
<meta itemprop="property" content="NUM_FEATURES"/>
</div>

# recsim.environments.interest_evolution.IEvUserState

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_evolution.py">View
source</a>

Class to represent interest evolution users.

Inherits From: [`AbstractUserState`](../../../recsim/user/AbstractUserState.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.environments.interest_evolution.IEvUserState(
    user_interests, time_budget=None, score_scaling=None, attention_prob=None,
    no_click_mass=None, keep_interact_prob=None, min_doc_utility=None,
    user_update_alpha=None, watched_videos=None, impressed_videos=None,
    liked_videos=None, step_penalty=None, min_normalizer=None,
    user_quality_factor=None, document_quality_factor=None
)
</code></pre>

<!-- Placeholder for "Used in" -->

## Methods

<h3 id="create_observation"><code>create_observation</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_evolution.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>create_observation()
</code></pre>

Return an observation of this user's observable state.

<h3 id="observation_space"><code>observation_space</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_evolution.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>observation_space()
</code></pre>

Gym.spaces object that defines how user states are represented.

<h3 id="score_document"><code>score_document</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_evolution.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>score_document(
    doc_obs
)
</code></pre>

## Class Variables

*   `NUM_FEATURES = 20` <a id="NUM_FEATURES"></a>
