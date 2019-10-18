<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.interest_exploration.IEUserModel" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="avg_user_state"/>
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

# recsim.environments.interest_exploration.IEUserModel

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//environments/interest_exploration.py">View
source</a>

## Class `IEUserModel`

Class to model a user.

Inherits From: [`AbstractUserModel`](../../../recsim/user/AbstractUserModel.md)

<!-- Placeholder for "Used in" -->

The user in this scenario is completely characterized by a vector g of affinity
scores of dimension |D| (the number of document topics). When presented with a
slate of documents, the user scores each document as g(d) + f(d), where f(d) is
the document's quality score, and then chooses according to a choice model based
on these scores.

The state space consists of a vector of affinity scores which is unique to the
user and static but not observable.

#### Args:

slate_size: An integer representing the size of the slate. no_click_mass: A
float indicating the mass given to a no-click option. Must be positive,
otherwise CTR is always 1. choice_model_ctor: A contructor function to create
user choice model. user_state_ctor: A constructor to create user state.
response_model_ctor: A constructor function to create response. The function
should take a string of doc ID as input and returns a IEResponse object. seed:
an integer used as the seed in random sampling.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//environments/interest_exploration.py">View
source</a>

```python
__init__(
    slate_size,
    no_click_mass=5,
    choice_model_ctor=recsim.choice_model.MultinomialLogitChoiceModel,
    user_state_ctor=None,
    response_model_ctor=None,
    seed=0
)
```

Initializes a new user model.

#### Args:

*   <b>`response_model_ctor`</b>: A class/constructor representing the type of
    responses this model will generate.
*   <b>`user_sampler`</b>: An instance of AbstractUserSampler that can generate
    initial user states from an inital state distribution.
*   <b>`slate_size`</b>: integer number of documents that can be served to the
    user at any interaction.

## Properties

<h3 id="avg_user_state"><code>avg_user_state</code></h3>

Returns the prior of user state.

## Methods

<h3 id="create_observation"><code>create_observation</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//user.py">View
source</a>

```python
create_observation()
```

Emits obesrvation about user's state.

<h3 id="get_response_model_ctor"><code>get_response_model_ctor</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//user.py">View
source</a>

```python
get_response_model_ctor()
```

Returns a constructor for the type of response this model will create.

<h3 id="is_terminal"><code>is_terminal</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//environments/interest_exploration.py">View
source</a>

```python
is_terminal()
```

Returns a boolean indicating if the session is over.

<h3 id="observation_space"><code>observation_space</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//user.py">View
source</a>

```python
observation_space()
```

A Gym.spaces object that describes possible user observations.

<h3 id="reset"><code>reset</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//user.py">View
source</a>

```python
reset()
```

Resets the user.

<h3 id="reset_sampler"><code>reset_sampler</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//user.py">View
source</a>

```python
reset_sampler()
```

Resets the sampler.

<h3 id="response_space"><code>response_space</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//user.py">View
source</a>

```python
response_space()
```

<h3 id="simulate_response"><code>simulate_response</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//environments/interest_exploration.py">View
source</a>

```python
simulate_response(documents)
```

Simulates the user's response to a slate of documents with choice model.

#### Args:

*   <b>`documents`</b>: a list of IEDocument objects in the slate.

#### Returns:

*   <b>`responses`</b>: a list of IEResponse objects, one for each document.

<h3 id="update_state"><code>update_state</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//environments/interest_exploration.py">View
source</a>

```python
update_state(
    slate_documents,
    responses
)
```

Updates the user's state based on the slate and document selected.

#### Args:

*   <b>`slate_documents`</b>: A list of AbstractDocuments for items in the
    slate.
*   <b>`responses`</b>: A list of AbstractResponses for each item in the slate.
    Updates: The user's hidden state.
