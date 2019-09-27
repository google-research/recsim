<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.dopamine.dqn_agent.ResponseAdapter" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="response_dtype"/>
<meta itemprop="property" content="response_names"/>
<meta itemprop="property" content="response_shape"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="encode"/>
</div>

# recsim.agents.dopamine.dqn_agent.ResponseAdapter

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/agents/dopamine/dqn_agent.py">View
source</a>

## Class `ResponseAdapter`

Custom flattening of responses to accommodate dopamine replay buffer.

<!-- Placeholder for "Used in" -->

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/agents/dopamine/dqn_agent.py">View
source</a>

```python
__init__(input_response_space)
```

Init function for ResponseAdapter.

#### Args:

*   <b>`input_response_space`</b>: this is assumed to be an instance of
    gym.spaces.Tuple; each element of the tuple is has to be an instance of
    gym.spaces.Dict consisting of feature_name: 0-d gym.spaces.Box (single
    float) key-value pairs.

## Properties

<h3 id="response_dtype"><code>response_dtype</code></h3>

<h3 id="response_names"><code>response_names</code></h3>

<h3 id="response_shape"><code>response_shape</code></h3>

## Methods

<h3 id="encode"><code>encode</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/agents/dopamine/dqn_agent.py">View
source</a>

```python
encode(responses)
```
