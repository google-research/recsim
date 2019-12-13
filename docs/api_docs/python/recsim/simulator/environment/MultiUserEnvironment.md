<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.simulator.environment.MultiUserEnvironment" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="candidate_set"/>
<meta itemprop="property" content="num_candidates"/>
<meta itemprop="property" content="num_users"/>
<meta itemprop="property" content="slate_size"/>
<meta itemprop="property" content="user_model"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="reset"/>
<meta itemprop="property" content="reset_sampler"/>
<meta itemprop="property" content="step"/>
</div>

# recsim.simulator.environment.MultiUserEnvironment

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/simulator/environment.py">View
source</a>

## Class `MultiUserEnvironment`

<!-- Start diff -->
Class to represent environment with multiple users.

Inherits From:
[`AbstractEnvironment`](../../../recsim/simulator/environment/AbstractEnvironment.md)

<!-- Placeholder for "Used in" -->

#### Attributes:

*   <b>`user_model`</b>: A list of AbstractUserModel instances that represent
    users.
*   <b>`num_users`</b>: An integer representing the number of users.
*   <b>`document_sampler`</b>: An instantiation of AbstractDocumentSampler.
*   <b>`num_candidates`</b>: An integer representing the size of the
    candidate_set.
*   <b>`slate_size`</b>: An integer representing the slate size.
*   <b>`candidate_set`</b>: An instantiation of CandidateSet.
*   <b>`num_clusters`</b>: An integer representing the number of document
    clusters.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/simulator/environment.py">View
source</a>

```python
__init__(
    user_model,
    document_sampler,
    num_candidates,
    slate_size,
    resample_documents=True
)
```

Initializes a new simulation environment.

#### Args:

*   <b>`user_model`</b>: An instantiation of AbstractUserModel or list of such
    instantiations
*   <b>`document_sampler`</b>: An instantiation of AbstractDocumentSampler
*   <b>`num_candidates`</b>: An integer representing the size of the
    candidate_set
*   <b>`slate_size`</b>: An integer representing the slate size
*   <b>`resample_documents`</b>: A boolean indicating whether to resample the
    candidate set every step

## Properties

<h3 id="candidate_set"><code>candidate_set</code></h3>

<h3 id="num_candidates"><code>num_candidates</code></h3>

<h3 id="num_users"><code>num_users</code></h3>

<h3 id="slate_size"><code>slate_size</code></h3>

<h3 id="user_model"><code>user_model</code></h3>

## Methods

<h3 id="reset"><code>reset</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/simulator/environment.py">View
source</a>

```python
reset()
```

Resets the environment and return the first observation.

#### Returns:

*   <b>`user_obs`</b>: An array of floats representing observations of the
    user's current state
*   <b>`doc_obs`</b>: An OrderedDict of document observations keyed by document
    ids

<h3 id="reset_sampler"><code>reset_sampler</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/simulator/environment.py">View
source</a>

```python
reset_sampler()
```

Resets the relevant samplers of documents and user/users.

<h3 id="step"><code>step</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/simulator/environment.py">View
source</a>

```python
step(slates)
```

Executes the action, returns next state observation and reward.

#### Args:

*   <b>`slates`</b>: A list of slates, where each slate is an integer array of
    size slate_size, where each element is an index into the set of
    current_documents presented

#### Returns:

*   <b>`user_obs`</b>: A list of gym observation representing all users' next
    state
*   <b>`doc_obs`</b>: A list of observations of the documents
*   <b>`responses`</b>: A list of AbstractResponse objects for each item in the
    slate
*   <b>`done`</b>: A boolean indicating whether the episode has terminated
