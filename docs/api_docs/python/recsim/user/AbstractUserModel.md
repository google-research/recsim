<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.user.AbstractUserModel" />
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

# recsim.user.AbstractUserModel

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//user.py">View
source</a>

## Class `AbstractUserModel`

Abstract class to represent an encoding of a user's dynamics.

<!-- Placeholder for "Used in" -->

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//user.py">View
source</a>

```python
__init__(
    response_model_ctor,
    user_sampler,
    slate_size
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

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//user.py">View
source</a>

```python
is_terminal()
```

Returns a boolean indicating whether this session is over.

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

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//user.py">View
source</a>

```python
simulate_response(documents)
```

Simulates the user's response to a slate of documents.

This could involve simulating models of attention, as well as random sampling
for selection from scored documents.

#### Args:

*   <b>`documents`</b>: a list of AbstractDocuments

#### Returns:

(response) a list of AbstractResponse objects for each slate item

<h3 id="update_state"><code>update_state</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//user.py">View
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
