<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.interest_exploration.IEUserState" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_observation"/>
<meta itemprop="property" content="observation_space"/>
<meta itemprop="property" content="score_document"/>
</div>

# recsim.environments.interest_exploration.IEUserState

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_exploration.py">View
source</a>

## Class `IEUserState`

Class to represent users.

Inherits From: [`AbstractUserState`](../../../recsim/user/AbstractUserState.md)

<!-- Placeholder for "Used in" -->

#### Attributes:

*   <b>`topic_affinity`</b>: a nonnegative vector holds document type affinities
    which are not temporal dynamics and hidden.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_exploration.py">View
source</a>

```python
__init__(topic_affinity)
```

Initializes a new user.

## Methods

<h3 id="create_observation"><code>create_observation</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_exploration.py">View
source</a>

```python
create_observation()
```

User's topic_affinity is not observable.

<h3 id="observation_space"><code>observation_space</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_exploration.py">View
source</a>

```python
@staticmethod
observation_space()
```

Gym.spaces object that defines how user states are represented.

<h3 id="score_document"><code>score_document</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_exploration.py">View
source</a>

```python
score_document(doc_obs)
```

Returns user document affinity plus document quality.
