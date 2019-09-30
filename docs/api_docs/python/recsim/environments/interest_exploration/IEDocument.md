<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.interest_exploration.IEDocument" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_observation"/>
<meta itemprop="property" content="doc_id"/>
<meta itemprop="property" content="observation_space"/>
<meta itemprop="property" content="NUM_CLUSTERS"/>
</div>

# recsim.environments.interest_exploration.IEDocument

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_exploration.py">View
source</a>

## Class `IEDocument`

Class to represent an IE Document.

Inherits From:
[`AbstractDocument`](../../../recsim/document/AbstractDocument.md)

<!-- Placeholder for "Used in" -->

#### Attributes:

*   <b>`cluster_id`</b>: an integer representing the document cluster.
*   <b>`quality`</b>: non-negative real number representing the quality of the
    document.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_exploration.py">View
source</a>

```python
__init__(
    doc_id,
    cluster_id,
    quality
)
```

Initialize self. See help(type(self)) for accurate signature.

## Methods

<h3 id="create_observation"><code>create_observation</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_exploration.py">View
source</a>

```python
create_observation()
```

Returns observable properties of this document as a float array.

<h3 id="doc_id"><code>doc_id</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/document.py">View
source</a>

```python
doc_id()
```

Returns the document ID.

<h3 id="observation_space"><code>observation_space</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_exploration.py">View
source</a>

```python
@classmethod
observation_space(cls)
```

Gym space that defines how documents are represented.

## Class Members

*   `NUM_CLUSTERS = 0` <a id="NUM_CLUSTERS"></a>
