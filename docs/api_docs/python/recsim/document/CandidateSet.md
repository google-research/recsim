<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.document.CandidateSet" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="add_document"/>
<meta itemprop="property" content="create_observation"/>
<meta itemprop="property" content="get_all_documents"/>
<meta itemprop="property" content="get_documents"/>
<meta itemprop="property" content="observation_space"/>
<meta itemprop="property" content="remove_document"/>
<meta itemprop="property" content="size"/>
</div>

# recsim.document.CandidateSet

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

Class to represent a collection of AbstractDocuments.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.document.CandidateSet()
</code></pre>

<!-- Placeholder for "Used in" -->

The candidate set is represented as a hashmap (dictionary), with documents
indexed by their document ID.

## Methods

<h3 id="add_document"><code>add_document</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_document(
    document
)
</code></pre>

Adds a document to the candidate set.

<h3 id="create_observation"><code>create_observation</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>create_observation()
</code></pre>

Returns a dictionary of observable features of documents.

<h3 id="get_all_documents"><code>get_all_documents</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_all_documents()
</code></pre>

Returns all documents.

<h3 id="get_documents"><code>get_documents</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_documents(
    document_ids
)
</code></pre>

Gets the documents associated with the specified document IDs.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`document_ids`
</td>
<td>
an array representing indices into the candidate set.
Indices can be integers or string-encoded integers.
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
(documents) an ordered list of AbstractDocuments associated with the
document ids.
</td>
</tr>

</table>

<h3 id="observation_space"><code>observation_space</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>observation_space()
</code></pre>

<h3 id="remove_document"><code>remove_document</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>remove_document(
    document
)
</code></pre>

Removes a document from the set (to simulate a changing corpus).

<h3 id="size"><code>size</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>size()
</code></pre>

Returns an integer, the number of documents in this candidate set.
