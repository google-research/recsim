<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.dopamine.dqn_agent.ObservationAdapter" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="output_observation_space"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="encode"/>
</div>

# recsim.agents.dopamine.dqn_agent.ObservationAdapter

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/dopamine/dqn_agent.py">View
source</a>

## Class `ObservationAdapter`

<!-- Start diff -->
An adapter to convert between user/doc observation and images.

<!-- Placeholder for "Used in" -->

<h2 id="__init__"><code>__init__</code></h2>

```python
__init__(
    *args,
    **kwargs
)
```

Initialize self. See help(type(self)) for accurate signature.

## Properties

<h3 id="output_observation_space"><code>output_observation_space</code></h3>

The output observation space of the adapter.

## Methods

<h3 id="encode"><code>encode</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/dopamine/dqn_agent.py">View
source</a>

```python
encode(observation)
```

Encode user observation and document observations to an image.
