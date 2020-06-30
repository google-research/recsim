<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.interest_exploration.IEResponse" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_observation"/>
<meta itemprop="property" content="response_space"/>
<meta itemprop="property" content="NUM_CLUSTERS"/>
</div>

# recsim.environments.interest_exploration.IEResponse

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_exploration.py">View
source</a>

Class to represent a user's response to a document.

Inherits From: [`AbstractResponse`](../../../recsim/user/AbstractResponse.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.environments.interest_exploration.IEResponse(
    clicked=False, quality=0.0, cluster_id=0
)
</code></pre>

<!-- Placeholder for "Used in" -->

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`clicked`
</td>
<td>
boolean indicating whether the item was clicked or not.
</td>
</tr><tr>
<td>
`quality`
</td>
<td>
a float indicating the quality of the document.
</td>
</tr><tr>
<td>
`cluster_id`
</td>
<td>
an integer representing the topic ID of the document.
</td>
</tr>
</table>

## Methods

<h3 id="create_observation"><code>create_observation</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_exploration.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>create_observation()
</code></pre>

Creates a tensor observation of this response.

<h3 id="response_space"><code>response_space</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_exploration.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>response_space()
</code></pre>

ArraySpec that defines how a single response is represented.

## Class Variables

*   `NUM_CLUSTERS = 0` <a id="NUM_CLUSTERS"></a>
