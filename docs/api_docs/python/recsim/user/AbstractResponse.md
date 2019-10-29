<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.user.AbstractResponse" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="create_observation"/>
<meta itemprop="property" content="response_space"/>
</div>

# recsim.user.AbstractResponse

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/user.py">View
source</a>

## Class `AbstractResponse`

Abstract class to model a user response.

<!-- Placeholder for "Used in" -->

## Methods

<h3 id="create_observation"><code>create_observation</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/user.py">View
source</a>

```python
create_observation()
```

Creates a tensor observation of this response.

<h3 id="response_space"><code>response_space</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/user.py">View
source</a>

```python
@staticmethod
response_space()
```

ArraySpec that defines how a single response is represented.
