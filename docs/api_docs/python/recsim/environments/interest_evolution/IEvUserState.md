<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.interest_evolution.IEvUserState" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_observation"/>
<meta itemprop="property" content="observation_space"/>
<meta itemprop="property" content="score_document"/>
<meta itemprop="property" content="NUM_FEATURES"/>
</div>

# recsim.environments.interest_evolution.IEvUserState

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//environments/interest_evolution.py">View
source</a>

## Class `IEvUserState`

Class to represent interest evolution users.

Inherits From: [`AbstractUserState`](../../../recsim/user/AbstractUserState.md)

<!-- Placeholder for "Used in" -->

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//environments/interest_evolution.py">View
source</a>

```python
__init__(
    user_interests,
    time_budget=None,
    score_scaling=None,
    attention_prob=None,
    no_click_mass=None,
    keep_interact_prob=None,
    min_doc_utility=None,
    user_update_alpha=None,
    watched_videos=None,
    impressed_videos=None,
    liked_videos=None,
    step_penalty=None,
    min_normalizer=None,
    user_quality_factor=None,
    document_quality_factor=None
)
```

Initializes a new user.

## Methods

<h3 id="create_observation"><code>create_observation</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//environments/interest_evolution.py">View
source</a>

```python
create_observation()
```

Return an observation of this user's observable state.

<h3 id="observation_space"><code>observation_space</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//environments/interest_evolution.py">View
source</a>

```python
@classmethod
observation_space(cls)
```

Gym.spaces object that defines how user states are represented.

<h3 id="score_document"><code>score_document</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//environments/interest_evolution.py">View
source</a>

```python
score_document(doc_obs)
```

## Class Members

*   `NUM_FEATURES = 20` <a id="NUM_FEATURES"></a>
