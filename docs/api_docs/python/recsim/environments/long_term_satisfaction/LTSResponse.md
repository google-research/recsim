<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.long_term_satisfaction.LTSResponse" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_observation"/>
<meta itemprop="property" content="response_space"/>
<meta itemprop="property" content="MAX_ENGAGEMENT_MAGNITUDE"/>
</div>

# recsim.environments.long_term_satisfaction.LTSResponse

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/environments/long_term_satisfaction.py">View
source</a>

## Class `LTSResponse`

Class to represent a user's response to a document.

Inherits From: [`AbstractResponse`](../../../recsim/user/AbstractResponse.md)

<!-- Placeholder for "Used in" -->

#### Attributes:

*   <b>`engagement`</b>: real number representing the degree of engagement with
    a document (e.g. watch time).
*   <b>`clicked`</b>: boolean indicating whether the item was clicked or not.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/environments/long_term_satisfaction.py">View
source</a>

```python
__init__(
    clicked=False,
    engagement=0.0
)
```

Creates a new user response for a document.

#### Args:

*   <b>`clicked`</b>: boolean indicating whether the item was clicked or not.
*   <b>`engagement`</b>: real number representing the degree of engagement with
    a document (e.g. watch time).

## Methods

<h3 id="create_observation"><code>create_observation</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/environments/long_term_satisfaction.py">View
source</a>

```python
create_observation()
```

Creates a tensor observation of this response.

<h3 id="response_space"><code>response_space</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/environments/long_term_satisfaction.py">View
source</a>

```python
@classmethod
response_space(cls)
```

ArraySpec that defines how a single response is represented.

## Class Members

*   `MAX_ENGAGEMENT_MAGNITUDE = 100.0` <a id="MAX_ENGAGEMENT_MAGNITUDE"></a>
