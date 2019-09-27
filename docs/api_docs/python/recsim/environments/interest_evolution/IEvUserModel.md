<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.interest_evolution.IEvUserModel" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_observation"/>
<meta itemprop="property" content="get_response_model_ctor"/>
<meta itemprop="property" content="is_terminal"/>
<meta itemprop="property" content="observation_space"/>
<meta itemprop="property" content="reset"/>
<meta itemprop="property" content="reset_sampler"/>
<meta itemprop="property" content="response_space"/>
<meta itemprop="property" content="simulate_response"/>
<meta itemprop="property" content="update_state"/>
</div>

# recsim.environments.interest_evolution.IEvUserModel

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/environments/interest_evolution.py">View
source</a>

## Class `IEvUserModel`

Class to model an interest evolution user.

Inherits From: [`AbstractUserModel`](../../../recsim/user/AbstractUserModel.md)

<!-- Placeholder for "Used in" -->

Assumes the user state contains: - user_interests - time_budget - no_click_mass

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/environments/interest_evolution.py">View
source</a>

```python
__init__(
    slate_size,
    choice_model_ctor=None,
    response_model_ctor=recsim.environments.interest_evolution.IEvResponse,
    user_state_ctor=recsim.environments.interest_evolution.IEvUserState,
    no_click_mass=1.0,
    seed=0,
    alpha_x_intercept=1.0,
    alpha_y_intercept=0.3
)
```

Initializes a new user model.

#### Args:

*   <b>`slate_size`</b>: An integer representing the size of the slate
*   <b>`choice_model_ctor`</b>: A contructor function to create user choice
    model.
*   <b>`response_model_ctor`</b>: A constructor function to create response. The
    function should take a string of doc ID as input and returns a IEvResponse
    object.
*   <b>`user_state_ctor`</b>: A constructor to create user state
*   <b>`no_click_mass`</b>: A float that will be passed to compute probability
    of no click.
*   <b>`seed`</b>: A integer used as the seed of the choice model.
*   <b>`alpha_x_intercept`</b>: A float for the x intercept of the line used to
    compute interests update factor.
*   <b>`alpha_y_intercept`</b>: A float for the y intercept of the line used to
    compute interests update factor.

#### Raises:

*   <b>`Exception`</b>: if choice_model_ctor is not specified.

## Methods

<h3 id="create_observation"><code>create_observation</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/user.py">View
source</a>

```python
create_observation()
```

Emits obesrvation about user's state.

<h3 id="get_response_model_ctor"><code>get_response_model_ctor</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/user.py">View
source</a>

```python
get_response_model_ctor()
```

Returns a constructor for the type of response this model will create.

<h3 id="is_terminal"><code>is_terminal</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/environments/interest_evolution.py">View
source</a>

```python
is_terminal()
```

Returns a boolean indicating if the session is over.

<h3 id="observation_space"><code>observation_space</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/user.py">View
source</a>

```python
observation_space()
```

A Gym.spaces object that describes possible user observations.

<h3 id="reset"><code>reset</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/user.py">View
source</a>

```python
reset()
```

Resets the user.

<h3 id="reset_sampler"><code>reset_sampler</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/user.py">View
source</a>

```python
reset_sampler()
```

Resets the sampler.

<h3 id="response_space"><code>response_space</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/user.py">View
source</a>

```python
response_space()
```

<h3 id="simulate_response"><code>simulate_response</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/environments/interest_evolution.py">View
source</a>

```python
simulate_response(documents)
```

Simulates the user's response to a slate of documents with choice model.

#### Args:

*   <b>`documents`</b>: a list of IEvVideo objects

#### Returns:

*   <b>`responses`</b>: a list of IEvResponse objects, one for each document

<h3 id="update_state"><code>update_state</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/environments/interest_evolution.py">View
source</a>

```python
update_state(
    slate_documents,
    responses
)
```

Updates the user state based on responses to the slate.

This function assumes only 1 response per slate. If a video is watched, we
update the user's interests some small step size alpha based on the user's
interest in that topic. The update is either towards the video's features or
away, and is determined stochastically by the user's interest in that document.

#### Args:

*   <b>`slate_documents`</b>: a list of IEvVideos representing the slate
*   <b>`responses`</b>: a list of IEvResponses representing the user's response
    to each video in the slate.
