<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.interest_evolution.IEvVideo" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_observation"/>
<meta itemprop="property" content="doc_id"/>
<meta itemprop="property" content="observation_space"/>
<meta itemprop="property" content="MAX_VIDEO_LENGTH"/>
<meta itemprop="property" content="NUM_FEATURES"/>
</div>

# recsim.environments.interest_evolution.IEvVideo

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/environments/interest_evolution.py">View
source</a>

## Class `IEvVideo`

Class to represent a interest evolution Video.

Inherits From:
[`AbstractDocument`](../../../recsim/document/AbstractDocument.md)

<!-- Placeholder for "Used in" -->

#### Attributes:

*   <b>`features`</b>: A numpy array that stores video features.
*   <b>`cluster_id`</b>: An integer that represents.
*   <b>`video_length`</b>: A float for video length.
*   <b>`quality`</b>: a float the represents document quality.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/environments/interest_evolution.py">View
source</a>

```python
__init__(
    doc_id,
    features,
    cluster_id=None,
    video_length=None,
    quality=None
)
```

Generates a random set of features for this interest evolution Video.

## Methods

<h3 id="create_observation"><code>create_observation</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/environments/interest_evolution.py">View
source</a>

```python
create_observation()
```

Returns observable properties of this document as a float array.

<h3 id="doc_id"><code>doc_id</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/document.py">View
source</a>

```python
doc_id()
```

Returns the document ID.

<h3 id="observation_space"><code>observation_space</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/environments/interest_evolution.py">View
source</a>

```python
@classmethod
observation_space(cls)
```

Gym space that defines how documents are represented.

## Class Members

*   `MAX_VIDEO_LENGTH = 100.0` <a id="MAX_VIDEO_LENGTH"></a>
*   `NUM_FEATURES = 20` <a id="NUM_FEATURES"></a>
