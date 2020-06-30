<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.interest_exploration.IETopicDocumentSampler" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="get_doc_ctor"/>
<meta itemprop="property" content="reset_sampler"/>
<meta itemprop="property" content="sample_document"/>
<meta itemprop="property" content="update_state"/>
</div>

# recsim.environments.interest_exploration.IETopicDocumentSampler

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_exploration.py">View
source</a>

Samples documents with topic-specific quality distribution.

Inherits From:
[`AbstractDocumentSampler`](../../../recsim/document/AbstractDocumentSampler.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.environments.interest_exploration.IETopicDocumentSampler(
    topic_distribution=(0.2, 0.8), topic_quality_mean=(0.8, 0.2),
    topic_quality_stddev=(0.1, 0.1),
    doc_ctor=recsim.environments.interest_exploration.IEDocument, **kwargs
)
</code></pre>

<!-- Placeholder for "Used in" -->

Consumes a distribution over document topics and topic-specific parameters for
generating a quality score (according to a lognormal distribution).

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`topic_distribution`
</td>
<td>
a non-negative array of dimension equal to the
number of topics, whose entries sum to one.
</td>
</tr><tr>
<td>
`topic_quality_mean`
</td>
<td>
a non-negative array of dimension equal to the
number of topics, representing the mean of the topic quality score.
</td>
</tr><tr>
<td>
`topic_quality_stddev`
</td>
<td>
a non-negative array of dimension equal to the
number of topics, representing the scale of the topic quality score.
</td>
</tr><tr>
<td>
`doc_ctor`
</td>
<td>
A class/constructor for the type of videos that will be sampled
by this sampler.
</td>
</tr>
</table>

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

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_exploration.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>sample_document()
</code></pre>

Samples the topic and then samples document features given the topic.

<h3 id="update_state"><code>update_state</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>update_state(
    documents, responses
)
</code></pre>

Update document state (if needed) given user's (or users') responses.
