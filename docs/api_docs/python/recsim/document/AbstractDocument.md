<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.document.AbstractDocument" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_observation"/>
<meta itemprop="property" content="doc_id"/>
<meta itemprop="property" content="observation_space"/>
<meta itemprop="property" content="NUM_FEATURES"/>
</div>

# recsim.document.AbstractDocument

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

Abstract class to represent a document and its properties.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.document.AbstractDocument(
    doc_id
)
</code></pre>

<!-- Placeholder for "Used in" -->

## Methods

<h3 id="create_observation"><code>create_observation</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
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

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>@abc.abstractmethod</code>
<code>observation_space()
</code></pre>

Gym space that defines how documents are represented.

## Class Variables

*   `NUM_FEATURES = None` <a id="NUM_FEATURES"></a>
