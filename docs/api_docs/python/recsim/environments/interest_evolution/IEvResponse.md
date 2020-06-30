<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.interest_evolution.IEvResponse" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_observation"/>
<meta itemprop="property" content="response_space"/>
<meta itemprop="property" content="MAX_QUALITY_SCORE"/>
<meta itemprop="property" content="MIN_QUALITY_SCORE"/>
</div>

# recsim.environments.interest_evolution.IEvResponse

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_evolution.py">View
source</a>

Class to represent a user's response to a video.

Inherits From: [`AbstractResponse`](../../../recsim/user/AbstractResponse.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.environments.interest_evolution.IEvResponse(
    clicked=False, watch_time=0.0, liked=False, quality=0.0, cluster_id=0.0
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
A boolean indicating whether the video was clicked
</td>
</tr><tr>
<td>
`watch_time`
</td>
<td>
A float for fraction of the video watched
</td>
</tr><tr>
<td>
`liked`
</td>
<td>
A boolean indicating whether the video was liked
</td>
</tr><tr>
<td>
`quality`
</td>
<td>
A float for document quality
</td>
</tr><tr>
<td>
`cluster_id`
</td>
<td>
a integer for the cluster ID of the document.
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`clicked`
</td>
<td>
A boolean indicating whether the video was clicked.
</td>
</tr><tr>
<td>
`watch_time`
</td>
<td>
A float for fraction of the video watched.
</td>
</tr><tr>
<td>
`liked`
</td>
<td>
A boolean indicating whether the video was liked.
</td>
</tr><tr>
<td>
`quality`
</td>
<td>
A float indicating the quality of the video.
</td>
</tr><tr>
<td>
`cluster_id`
</td>
<td>
A integer representing the cluster ID of the video.
</td>
</tr>
</table>

## Methods

<h3 id="create_observation"><code>create_observation</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_evolution.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>create_observation()
</code></pre>

Creates a tensor observation of this response.

<h3 id="response_space"><code>response_space</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_evolution.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>response_space()
</code></pre>

ArraySpec that defines how a single response is represented.

## Class Variables

*   `MAX_QUALITY_SCORE = 100` <a id="MAX_QUALITY_SCORE"></a>
*   `MIN_QUALITY_SCORE = -100` <a id="MIN_QUALITY_SCORE"></a>
