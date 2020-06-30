<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.long_term_satisfaction.LTSDocumentSampler" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="get_doc_ctor"/>
<meta itemprop="property" content="reset_sampler"/>
<meta itemprop="property" content="sample_document"/>
<meta itemprop="property" content="update_state"/>
</div>

# recsim.environments.long_term_satisfaction.LTSDocumentSampler

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/long_term_satisfaction.py">View
source</a>

Class to sample LTSDocument documents.

Inherits From:
[`AbstractDocumentSampler`](../../../recsim/document/AbstractDocumentSampler.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.environments.long_term_satisfaction.LTSDocumentSampler(
    doc_ctor=recsim.environments.long_term_satisfaction.LTSDocument, **kwargs
)
</code></pre>

<!-- Placeholder for "Used in" -->

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

</table>

doc_ctor: A class/constructor for the type of documents that will be sampled by
this sampler.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`num_clusters`
</td>
<td>
Returns the number of document clusters. Returns 0 if not applicable.
</td>
</tr>
</table>

## Methods

<h3 id="get_doc_ctor"><code>get_doc_ctor</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_doc_ctor()
</code></pre>

Returns the constructor/class of the documents that will be sampled.

<h3 id="reset_sampler"><code>reset_sampler</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset_sampler()
</code></pre>

<h3 id="sample_document"><code>sample_document</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/long_term_satisfaction.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>sample_document()
</code></pre>

Samples and return an instantiation of AbstractDocument.

<h3 id="update_state"><code>update_state</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>update_state(
    documents, responses
)
</code></pre>

Update document state (if needed) given user's (or users') responses.
