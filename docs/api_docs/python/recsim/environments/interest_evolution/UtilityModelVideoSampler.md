<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.interest_evolution.UtilityModelVideoSampler" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="num_clusters"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="get_doc_ctor"/>
<meta itemprop="property" content="reset_sampler"/>
<meta itemprop="property" content="sample_document"/>
<meta itemprop="property" content="update_state"/>
</div>

# recsim.environments.interest_evolution.UtilityModelVideoSampler

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_evolution.py">View
source</a>

## Class `UtilityModelVideoSampler`

<!-- Start diff -->
Class that samples videos for utility model experiment.

Inherits From:
[`AbstractDocumentSampler`](../../../recsim/document/AbstractDocumentSampler.md)

<!-- Placeholder for "Used in" -->

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_evolution.py">View
source</a>

```python
__init__(
    doc_ctor=recsim.environments.interest_evolution.IEvVideo,
    min_utility=-3.0,
    max_utility=3.0,
    video_length=4.0,
    **kwargs
)
```

Creates a new utility model video sampler.

#### Args:

*   <b>`doc_ctor`</b>: A class/constructor for the type of videos that will be
    sampled by this sampler.
*   <b>`min_utility`</b>: A float for the min utility score.
*   <b>`max_utility`</b>: A float for the max utility score.
*   <b>`video_length`</b>: A float for the video_length in minutes.
*   <b>`**kwargs`</b>: other keyword parameters for the video sampler.

## Properties

<h3 id="num_clusters"><code>num_clusters</code></h3>

Returns the number of document clusters. Returns 0 if not applicable.

## Methods

<h3 id="get_doc_ctor"><code>get_doc_ctor</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

```python
get_doc_ctor()
```

Returns the constructor/class of the documents that will be sampled.

<h3 id="reset_sampler"><code>reset_sampler</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

```python
reset_sampler()
```

<h3 id="sample_document"><code>sample_document</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_evolution.py">View
source</a>

```python
sample_document()
```

Samples and return an instantiation of AbstractDocument.

<h3 id="update_state"><code>update_state</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

```python
update_state(
    documents,
    responses
)
```

Update document state (if needed) given user's (or users') responses.
