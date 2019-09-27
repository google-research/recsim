<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.interest_exploration.IEResponse" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_observation"/>
<meta itemprop="property" content="response_space"/>
<meta itemprop="property" content="NUM_CLUSTERS"/>
</div>

# recsim.environments.interest_exploration.IEResponse

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/environments/interest_exploration.py">View
source</a>

## Class `IEResponse`

Class to represent a user's response to a document.

Inherits From: [`AbstractResponse`](../../../recsim/user/AbstractResponse.md)

<!-- Placeholder for "Used in" -->

#### Attributes:

*   <b>`clicked`</b>: boolean indicating whether the item was clicked or not.
*   <b>`quality`</b>: a float indicating the quality of the document.
*   <b>`cluster_id`</b>: an integer representing the topic ID of the document.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/environments/interest_exploration.py">View
source</a>

```python
__init__(
    clicked=False,
    quality=0.0,
    cluster_id=0
)
```

Initialize self. See help(type(self)) for accurate signature.

## Methods

<h3 id="create_observation"><code>create_observation</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/environments/interest_exploration.py">View
source</a>

```python
create_observation()
```

Creates a tensor observation of this response.

<h3 id="response_space"><code>response_space</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/environments/interest_exploration.py">View
source</a>

```python
@classmethod
response_space(cls)
```

ArraySpec that defines how a single response is represented.

## Class Members

*   `NUM_CLUSTERS = 0` <a id="NUM_CLUSTERS"></a>
