<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.interest_evolution.UtilityModelVideoSampler" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="get_doc_ctor"/>
<meta itemprop="property" content="reset_sampler"/>
<meta itemprop="property" content="sample_document"/>
<meta itemprop="property" content="update_state"/>
</div>

# recsim.environments.interest_evolution.UtilityModelVideoSampler

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_evolution.py">View
source</a>

Class that samples videos for utility model experiment.

Inherits From:
[`AbstractDocumentSampler`](../../../recsim/document/AbstractDocumentSampler.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.environments.interest_evolution.UtilityModelVideoSampler(
    doc_ctor=recsim.environments.interest_evolution.IEvVideo, min_utility=-3.0,
    max_utility=3.0, video_length=4.0, **kwargs
)
</code></pre>

<!-- Placeholder for "Used in" -->

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`doc_ctor`
</td>
<td>
A class/constructor for the type of videos that will be sampled
by this sampler.
</td>
</tr><tr>
<td>
`min_utility`
</td>
<td>
A float for the min utility score.
</td>
</tr><tr>
<td>
`max_utility`
</td>
<td>
A float for the max utility score.
</td>
</tr><tr>
<td>
`video_length`
</td>
<td>
A float for the video_length in minutes.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
other keyword parameters for the video sampler.
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

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_evolution.py">View
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
