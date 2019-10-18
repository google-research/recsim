<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.long_term_satisfaction.LTSUserState" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_observation"/>
<meta itemprop="property" content="observation_space"/>
<meta itemprop="property" content="score_document"/>
</div>

# recsim.environments.long_term_satisfaction.LTSUserState

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//environments/long_term_satisfaction.py">View
source</a>

## Class `LTSUserState`

Class to represent users.

Inherits From: [`AbstractUserState`](../../../recsim/user/AbstractUserState.md)

<!-- Placeholder for "Used in" -->

See the LTSUserModel class documentation for precise information about how the
parameters influence user dynamics. Attributes: memory_discount: rate of
forgetting of latent state. sensitivity: magnitude of the dependence between
latent state and engagement. innovation_stddev: noise standard deviation in
latent state transitions. choc_mean: mean of engagement with clickbaity content.
choc_stddev: standard deviation of engagement with clickbaity content.
kale_mean: mean of engagement with non-clickbaity content. kale_stddev: standard
deviation of engagement with non-clickbaity content. net_positive_exposure:
starting value for NPE (NPE_0). time_budget: length of a user session.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//environments/long_term_satisfaction.py">View
source</a>

```python
__init__(
    memory_discount,
    sensitivity,
    innovation_stddev,
    choc_mean,
    choc_stddev,
    kale_mean,
    kale_stddev,
    net_positive_exposure,
    time_budget
)
```

Initializes a new user.

## Methods

<h3 id="create_observation"><code>create_observation</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//environments/long_term_satisfaction.py">View
source</a>

```python
create_observation()
```

User's state is not observable.

<h3 id="observation_space"><code>observation_space</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//environments/long_term_satisfaction.py">View
source</a>

```python
@staticmethod
observation_space()
```

Gym.spaces object that defines how user states are represented.

<h3 id="score_document"><code>score_document</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//environments/long_term_satisfaction.py">View
source</a>

```python
score_document(doc_obs)
```
