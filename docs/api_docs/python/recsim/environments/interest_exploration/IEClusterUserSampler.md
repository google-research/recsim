<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.interest_exploration.IEClusterUserSampler" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="avg_affinity_given_topic"/>
<meta itemprop="property" content="get_user_ctor"/>
<meta itemprop="property" content="reset_sampler"/>
<meta itemprop="property" content="sample_user"/>
</div>

# recsim.environments.interest_exploration.IEClusterUserSampler

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//environments/interest_exploration.py">View
source</a>

## Class `IEClusterUserSampler`

Samples users from predetermined types with type-specific parameters.

Inherits From:
[`AbstractUserSampler`](../../../recsim/user/AbstractUserSampler.md)

<!-- Placeholder for "Used in" -->

This sampler consumes a distribution over user types and type-specific
parameters for the user's affinity towards content types. It first samples a
user type, then using that user type generates affinities according to the
type-specific parameters. In this case, these are the mean and scale of a
lognormal distribution, i.e. the affinity of user u of type U towards an
document of type D is drawn according to lognormal(mean(U,D), scale(U,D)).

#### Args:

*   <b>`user_type_distribution`</b>: a non-negative array of dimension equal to
    the number of user types, whose entries sum to one.
*   <b>`user_document_mean_affinity_matrix`</b>: a non-negative two-dimensional
    array with dimensions number of user types by number of document topics.
    Represents the mean of the affinity score of a user type to a topic.
*   <b>`user_document_stddev_affinity_matrix`</b>: a non-negative
    two-dimensional array with dimensions number of user types by number of
    document topics. Represents the scale of the affinity score of a user type
    to a topic.
*   <b>`user_ctor`</b>: constructor for a user state.

<h2 id="__init__"><code>__init__</code></h2>

```python
__init__(
    *args,
    **kwargs
)
```

Creates a new user state sampler.

User states of the type user_ctor are sampled.

#### Args:

*   <b>`user_ctor`</b>: A class/constructor for the type of user states that
    will be sampled.
*   <b>`seed`</b>: An integer for a random seed.

## Methods

<h3 id="avg_affinity_given_topic"><code>avg_affinity_given_topic</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//environments/interest_exploration.py">View
source</a>

```python
avg_affinity_given_topic()
```

<h3 id="get_user_ctor"><code>get_user_ctor</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//user.py">View
source</a>

```python
get_user_ctor()
```

Returns the constructor/class of the user states that will be sampled.

<h3 id="reset_sampler"><code>reset_sampler</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//user.py">View
source</a>

```python
reset_sampler()
```

<h3 id="sample_user"><code>sample_user</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//environments/interest_exploration.py">View
source</a>

```python
sample_user()
```

Creates a new instantiation of this user's hidden state parameters.
