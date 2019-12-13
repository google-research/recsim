<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.interest_evolution.IEvResponse" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_observation"/>
<meta itemprop="property" content="response_space"/>
<meta itemprop="property" content="MAX_QUALITY_SCORE"/>
<meta itemprop="property" content="MIN_QUALITY_SCORE"/>
</div>

# recsim.environments.interest_evolution.IEvResponse

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_evolution.py">View
source</a>

## Class `IEvResponse`

<!-- Start diff -->
Class to represent a user's response to a video.

Inherits From: [`AbstractResponse`](../../../recsim/user/AbstractResponse.md)

<!-- Placeholder for "Used in" -->

#### Attributes:

*   <b>`clicked`</b>: A boolean indicating whether the video was clicked.
*   <b>`watch_time`</b>: A float for fraction of the video watched.
*   <b>`liked`</b>: A boolean indicating whether the video was liked.
*   <b>`quality`</b>: A float indicating the quality of the video.
*   <b>`cluster_id`</b>: A integer representing the cluster ID of the video.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_evolution.py">View
source</a>

```python
__init__(
    clicked=False,
    watch_time=0.0,
    liked=False,
    quality=0.0,
    cluster_id=0.0
)
```

Creates a new user response for a video.

#### Args:

*   <b>`clicked`</b>: A boolean indicating whether the video was clicked
*   <b>`watch_time`</b>: A float for fraction of the video watched
*   <b>`liked`</b>: A boolean indicating whether the video was liked
*   <b>`quality`</b>: A float for document quality
*   <b>`cluster_id`</b>: a integer for the cluster ID of the document.

## Methods

<h3 id="create_observation"><code>create_observation</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_evolution.py">View
source</a>

```python
create_observation()
```

Creates a tensor observation of this response.

<h3 id="response_space"><code>response_space</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_evolution.py">View
source</a>

```python
@classmethod
response_space(cls)
```

ArraySpec that defines how a single response is represented.

## Class Members

*   `MAX_QUALITY_SCORE = 100` <a id="MAX_QUALITY_SCORE"></a>
*   `MIN_QUALITY_SCORE = -100` <a id="MIN_QUALITY_SCORE"></a>
