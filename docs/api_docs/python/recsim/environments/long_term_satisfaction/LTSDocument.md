<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.long_term_satisfaction.LTSDocument" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_observation"/>
<meta itemprop="property" content="doc_id"/>
<meta itemprop="property" content="observation_space"/>
</div>

# recsim.environments.long_term_satisfaction.LTSDocument

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/environments/long_term_satisfaction.py">View
source</a>

## Class `LTSDocument`

Class to represent an LTS Document.

Inherits From:
[`AbstractDocument`](../../../recsim/document/AbstractDocument.md)

<!-- Placeholder for "Used in" -->

#### Attributes:

*   <b>`clickbait_score`</b>: real number in [0,1] representing the
    clickbaitiness of a document.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/environments/long_term_satisfaction.py">View
source</a>

```python
__init__(
    doc_id,
    clickbait_score
)
```

Initialize self. See help(type(self)) for accurate signature.

## Methods

<h3 id="create_observation"><code>create_observation</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/environments/long_term_satisfaction.py">View
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

<a target="_blank" href="https://github.com/google-research/recsim/recsim/environments/long_term_satisfaction.py">View
source</a>

```python
@staticmethod
observation_space()
```

Gym space that defines how documents are represented.
