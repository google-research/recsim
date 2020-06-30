<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.interest_exploration.IEClusterUserSampler" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="avg_affinity_given_topic"/>
<meta itemprop="property" content="get_user_ctor"/>
<meta itemprop="property" content="reset_sampler"/>
<meta itemprop="property" content="sample_user"/>
</div>

# recsim.environments.interest_exploration.IEClusterUserSampler

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_exploration.py">View
source</a>

Samples users from predetermined types with type-specific parameters.

Inherits From:
[`AbstractUserSampler`](../../../recsim/user/AbstractUserSampler.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.environments.interest_exploration.IEClusterUserSampler(
    user_type_distribution=(0.3, 0.7), user_document_mean_affinity_matrix=((0.1,
    0.7), (0.7, 0.1)), user_document_stddev_affinity_matrix=((0.1, 0.1), (0.1,
    0.1)), user_ctor=recsim.environments.interest_exploration.IEUserState, **kwargs
)
</code></pre>

<!-- Placeholder for "Used in" -->

This sampler consumes a distribution over user types and type-specific
parameters for the user's affinity towards content types. It first samples a
user type, then using that user type generates affinities according to the
type-specific parameters. In this case, these are the mean and scale of a
lognormal distribution, i.e. the affinity of user u of type U towards an
document of type D is drawn according to lognormal(mean(U,D), scale(U,D)).

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`user_type_distribution`
</td>
<td>
a non-negative array of dimension equal to the
number of user types, whose entries sum to one.
</td>
</tr><tr>
<td>
`user_document_mean_affinity_matrix`
</td>
<td>
a non-negative two-dimensional array
with dimensions number of user types by number of document topics.
Represents the mean of the affinity score of a user type to a topic.
</td>
</tr><tr>
<td>
`user_document_stddev_affinity_matrix`
</td>
<td>
a non-negative two-dimensional array
with dimensions number of user types by number of document topics.
Represents the scale of the affinity score of a user type to a topic.
</td>
</tr><tr>
<td>
`user_ctor`
</td>
<td>
constructor for a user state.
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`user_ctor`
</td>
<td>
A class/constructor for the type of user states that will be
sampled.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
An integer for a random seed.
</td>
</tr>
</table>

## Methods

<h3 id="avg_affinity_given_topic"><code>avg_affinity_given_topic</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_exploration.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>avg_affinity_given_topic()
</code></pre>

<h3 id="get_user_ctor"><code>get_user_ctor</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/user.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_user_ctor()
</code></pre>

Returns the constructor/class of the user states that will be sampled.

<h3 id="reset_sampler"><code>reset_sampler</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/user.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset_sampler()
</code></pre>

<h3 id="sample_user"><code>sample_user</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_exploration.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>sample_user()
</code></pre>

Creates a new instantiation of this user's hidden state parameters.
