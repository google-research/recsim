<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.bandits.algorithms.MABAlgorithm" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="set_state"/>
<meta itemprop="property" content="update"/>
</div>

# recsim.agents.bandits.algorithms.MABAlgorithm

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/agents/bandits/algorithms.py">View
source</a>

## Class `MABAlgorithm`

Base class for Multi-armed bandit (MAB) algorithms.

<!-- Placeholder for "Used in" -->

We implement multi-armed bandit algorithms with confidence width tuning proposed
in Hsu et al. https://arxiv.org/abs/1904.02664.

#### Attributes:

*   <b>`pulls`</b>: A numpy array which counts number of pulls of each arm
*   <b>`reward`</b>: A numpy array which sums up reward of each arm
*   <b>`optimism_scaling`</b>: A float specifying the confidence level. Default
    value (1.0) corresponds to the exploration strategy presented in the
    literature. A smaller number means less exploration and more exploitation.
*   <b>`_rng`</b>: An instance of random.RandomState for random number
    generation

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/agents/bandits/algorithms.py">View
source</a>

```python
__init__(
    num_arms,
    params,
    seed=0
)
```

Initializes MABAlgorithm.

#### Args:

*   <b>`num_arms`</b>: Number of arms. Must be greater than one.
*   <b>`params`</b>: A dictionary which includes additional parameters like
    optimism_scaling. Default is an empty dictionary.
*   <b>`seed`</b>: Random seed for this object. Default is zero.

## Methods

<h3 id="set_state"><code>set_state</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/agents/bandits/algorithms.py">View
source</a>

```python
set_state(
    pulls,
    reward
)
```

<h3 id="update"><code>update</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/agents/bandits/algorithms.py">View
source</a>

```python
update(
    arm,
    reward
)
```
