<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.interest_exploration.IEDocument" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_observation"/>
<meta itemprop="property" content="doc_id"/>
<meta itemprop="property" content="observation_space"/>
<meta itemprop="property" content="NUM_CLUSTERS"/>
<meta itemprop="property" content="NUM_FEATURES"/>
</div>

# recsim.environments.interest_exploration.IEDocument

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_exploration.py">View
source</a>

Class to represent an IE Document.

Inherits From:
[`AbstractDocument`](../../../recsim/document/AbstractDocument.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.environments.interest_exploration.IEDocument(
    doc_id, cluster_id, quality
)
</code></pre>

<!-- Placeholder for "Used in" -->

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`cluster_id`
</td>
<td>
an integer representing the document cluster.
</td>
</tr><tr>
<td>
`quality`
</td>
<td>
non-negative real number representing the quality of the document.
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

Returns observable properties of this document as a float array.

<h3 id="doc_id"><code>doc_id</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>doc_id()
</code></pre>

Returns the document ID.

<h3 id="observation_space"><code>observation_space</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_exploration.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>observation_space()
</code></pre>

Gym space that defines how documents are represented.

## Class Variables

*   `NUM_CLUSTERS = 0` <a id="NUM_CLUSTERS"></a>
*   `NUM_FEATURES = None` <a id="NUM_FEATURES"></a>
