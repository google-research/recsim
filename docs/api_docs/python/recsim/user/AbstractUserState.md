<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.user.AbstractUserState" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="create_observation"/>
<meta itemprop="property" content="observation_space"/>
</div>

# recsim.user.AbstractUserState

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/user.py">View
source</a>

## Class `AbstractUserState`

<!-- Start diff -->
Abstract class to represent a user's state.

<!-- Placeholder for "Used in" -->

## Methods

<h3 id="create_observation"><code>create_observation</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/user.py">View
source</a>

```python
create_observation()
```

Generates obs of underlying state to simulate partial observability.

#### Returns:

*   <b>`obs`</b>: A float array of the observed user features.

<h3 id="observation_space"><code>observation_space</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/user.py">View
source</a>

```python
@staticmethod
observation_space()
```

Gym.spaces object that defines how user states are represented.




