<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.long_term_satisfaction.LTSUserState" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_observation"/>
<meta itemprop="property" content="observation_space"/>
<meta itemprop="property" content="score_document"/>
<meta itemprop="property" content="NUM_FEATURES"/>
</div>

# recsim.environments.long_term_satisfaction.LTSUserState

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/long_term_satisfaction.py">View
source</a>

Class to represent users.

Inherits From: [`AbstractUserState`](../../../recsim/user/AbstractUserState.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.environments.long_term_satisfaction.LTSUserState(
    memory_discount, sensitivity, innovation_stddev, choc_mean, choc_stddev,
    kale_mean, kale_stddev, net_positive_exposure, time_budget
)
</code></pre>

<!-- Placeholder for "Used in" -->

See the LTSUserModel class documentation for precise information about how the
parameters influence user dynamics. Attributes: memory_discount: rate of
forgetting of latent state. sensitivity: magnitude of the dependence between
latent state and engagement. innovation_stddev: noise standard deviation in
latent state transitions. choc_mean: mean of engagement with clickbaity content.
choc_stddev: standard deviation of engagement with clickbaity content.
kale_mean: mean of engagement with non-clickbaity content. kale_stddev: standard
deviation of engagement with non-clickbaity content. net_positive_exposure:
starting value for NPE (NPE_0). time_budget: length of a user session.

## Methods

<h3 id="create_observation"><code>create_observation</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/long_term_satisfaction.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>create_observation()
</code></pre>

User's state is not observable.

<h3 id="observation_space"><code>observation_space</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/long_term_satisfaction.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@staticmethod</code>
<code>observation_space()
</code></pre>

Gym.spaces object that defines how user states are represented.

<h3 id="score_document"><code>score_document</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/long_term_satisfaction.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>score_document(
    doc_obs
)
</code></pre>

## Class Variables

*   `NUM_FEATURES = None` <a id="NUM_FEATURES"></a>
