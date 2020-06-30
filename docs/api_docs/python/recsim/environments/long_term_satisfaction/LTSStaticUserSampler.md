<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.long_term_satisfaction.LTSStaticUserSampler" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="get_user_ctor"/>
<meta itemprop="property" content="reset_sampler"/>
<meta itemprop="property" content="sample_user"/>
</div>

# recsim.environments.long_term_satisfaction.LTSStaticUserSampler

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/long_term_satisfaction.py">View
source</a>

Generates user with identical predetermined parameters.

Inherits From:
[`AbstractUserSampler`](../../../recsim/user/AbstractUserSampler.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.environments.long_term_satisfaction.LTSStaticUserSampler(
    user_ctor=recsim.environments.long_term_satisfaction.LTSUserState,
    memory_discount=0.7, sensitivity=0.01, innovation_stddev=0.05, choc_mean=5.0,
    choc_stddev=1.0, kale_mean=4.0, kale_stddev=1.0, time_budget=60, **kwargs
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

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/long_term_satisfaction.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>sample_user()
</code></pre>

Creates a new instantiation of this user's hidden state parameters.
