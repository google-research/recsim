<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.document.AbstractDocumentSampler" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="num_clusters"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="get_doc_ctor"/>
<meta itemprop="property" content="reset_sampler"/>
<meta itemprop="property" content="sample_document"/>
</div>

# recsim.document.AbstractDocumentSampler

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//document.py">View
source</a>

## Class `AbstractDocumentSampler`

Abstract class to sample documents.

<!-- Placeholder for "Used in" -->

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//document.py">View
source</a>

```python
__init__(
    doc_ctor,
    seed=0
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

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//document.py">View
source</a>

```python
sample_document()
```

Samples and return an instantiation of AbstractDocument.
