<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.document.AbstractDocument" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_observation"/>
<meta itemprop="property" content="doc_id"/>
<meta itemprop="property" content="observation_space"/>
</div>

# recsim.document.AbstractDocument

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/document.py">View
source</a>

## Class `AbstractDocument`

Abstract class to represent a document and its properties.

<!-- Placeholder for "Used in" -->

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/document.py">View
source</a>

```python
__init__(doc_id)
```

Initialize self. See help(type(self)) for accurate signature.

## Methods

<h3 id="create_observation"><code>create_observation</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/document.py">View
source</a>

```python
create_observation()
```

Returns observable properties of this document as a float array.

<h3 id="doc_id"><code>doc_id</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/document.py">View
source</a>

```python
doc_id()
```

Returns the document ID.

<h3 id="observation_space"><code>observation_space</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/document.py">View
source</a>

```python
@classmethod
observation_space(cls)
```

Gym space that defines how documents are represented.
