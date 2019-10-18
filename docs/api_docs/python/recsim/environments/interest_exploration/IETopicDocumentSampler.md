<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.interest_exploration.IETopicDocumentSampler" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="num_clusters"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="get_doc_ctor"/>
<meta itemprop="property" content="reset_sampler"/>
<meta itemprop="property" content="sample_document"/>
</div>

# recsim.environments.interest_exploration.IETopicDocumentSampler

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//environments/interest_exploration.py">View
source</a>

## Class `IETopicDocumentSampler`

Samples documents with topic-specific quality distribution.

Inherits From:
[`AbstractDocumentSampler`](../../../recsim/document/AbstractDocumentSampler.md)

<!-- Placeholder for "Used in" -->

Consumes a distribution over document topics and topic-specific parameters for
generating a quality score (according to a lognormal distribution).

#### Args:

*   <b>`topic_distribution`</b>: a non-negative array of dimension equal to the
    number of topics, whose entries sum to one.
*   <b>`topic_quality_mean`</b>: a non-negative array of dimension equal to the
    number of topics, representing the mean of the topic quality score.
*   <b>`topic_quality_stddev`</b>: a non-negative array of dimension equal to
    the number of topics, representing the scale of the topic quality score.
*   <b>`doc_ctor`</b>: A class/constructor for the type of videos that will be
    sampled by this sampler.

<h2 id="__init__"><code>__init__</code></h2>

```python
__init__(
    *args,
    **kwargs
)
```

Initialize self. See help(type(self)) for accurate signature.

## Properties

<h3 id="num_clusters"><code>num_clusters</code></h3>

Returns the number of document clusters. Returns 0 if not applicable.

## Methods

<h3 id="get_doc_ctor"><code>get_doc_ctor</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//document.py">View
source</a>

```python
get_doc_ctor()
```

Returns the constructor/class of the documents that will be sampled.

<h3 id="reset_sampler"><code>reset_sampler</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//document.py">View
source</a>

```python
reset_sampler()
```

<h3 id="sample_document"><code>sample_document</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//environments/interest_exploration.py">View
source</a>

```python
sample_document()
```

Samples the topic and then samples document features given the topic.
