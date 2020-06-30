<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.long_term_satisfaction.LTSResponse" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_observation"/>
<meta itemprop="property" content="response_space"/>
<meta itemprop="property" content="MAX_ENGAGEMENT_MAGNITUDE"/>
</div>

# recsim.environments.long_term_satisfaction.LTSResponse

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/long_term_satisfaction.py">View
source</a>

Class to represent a user's response to a document.

Inherits From: [`AbstractResponse`](../../../recsim/user/AbstractResponse.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.environments.long_term_satisfaction.LTSResponse(
    clicked=False, engagement=0.0
)
</code></pre>

<!-- Placeholder for "Used in" -->

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`clicked`
</td>
<td>
boolean indicating whether the item was clicked or not.
</td>
</tr><tr>
<td>
`engagement`
</td>
<td>
real number representing the degree of engagement with a
document (e.g. watch time).
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`engagement`
</td>
<td>
real number representing the degree of engagement with a
document (e.g. watch time).
</td>
</tr><tr>
<td>
`clicked`
</td>
<td>
boolean indicating whether the item was clicked or not.
</td>
</tr>
</table>

## Methods

<h3 id="create_observation"><code>create_observation</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/long_term_satisfaction.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>create_observation()
</code></pre>

Creates a tensor observation of this response.

<h3 id="response_space"><code>response_space</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/long_term_satisfaction.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>response_space()
</code></pre>

ArraySpec that defines how a single response is represented.

## Class Variables

*   `MAX_ENGAGEMENT_MAGNITUDE = 100.0` <a id="MAX_ENGAGEMENT_MAGNITUDE"></a>
