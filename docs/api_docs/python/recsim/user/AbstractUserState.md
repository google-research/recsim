<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.user.AbstractUserState" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="create_observation"/>
<meta itemprop="property" content="observation_space"/>
<meta itemprop="property" content="NUM_FEATURES"/>
</div>

# recsim.user.AbstractUserState

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/user.py">View
source</a>

Abstract class to represent a user's state.

<!-- Placeholder for "Used in" -->

## Methods

<h3 id="create_observation"><code>create_observation</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/user.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>create_observation()
</code></pre>

Generates obs of underlying state to simulate partial observability.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`obs`
</td>
<td>
A float array of the observed user features.
</td>
</tr>
</table>

<h3 id="observation_space"><code>observation_space</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/user.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@staticmethod</code>
<code>@abc.abstractmethod</code>
<code>observation_space()
</code></pre>

Gym.spaces object that defines how user states are represented.

## Class Variables

*   `NUM_FEATURES = None` <a id="NUM_FEATURES"></a>
