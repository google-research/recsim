<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.interest_evolution.UtilityModelUserSampler" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="get_user_ctor"/>
<meta itemprop="property" content="reset_sampler"/>
<meta itemprop="property" content="sample_user"/>
</div>

# recsim.environments.interest_evolution.UtilityModelUserSampler

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_evolution.py">View
source</a>

Class that samples users for utility model experiment.

Inherits From:
[`AbstractUserSampler`](../../../recsim/user/AbstractUserSampler.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.environments.interest_evolution.UtilityModelUserSampler(
    user_ctor=recsim.environments.interest_evolution.IEvUserState,
    document_quality_factor=1.0, no_click_mass=1.0, min_normalizer=-1.0, **kwargs
)
</code></pre>

<!-- Placeholder for "Used in" -->

## Methods

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

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_evolution.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>sample_user()
</code></pre>

Creates a new instantiation of this user's hidden state parameters.
