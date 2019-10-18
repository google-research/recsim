<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.bandits.algorithms.KLUCB" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="get_arm"/>
<meta itemprop="property" content="get_score"/>
<meta itemprop="property" content="print"/>
<meta itemprop="property" content="set_state"/>
<meta itemprop="property" content="update"/>
</div>

# recsim.agents.bandits.algorithms.KLUCB

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//agents/bandits/algorithms.py">View
source</a>

## Class `KLUCB`

Kullback-Leibler Upper Confidence Bounds (KL-UCB) algorithm.

Inherits From:
[`MABAlgorithm`](../../../../recsim/agents/bandits/algorithms/MABAlgorithm.md)

<!-- Placeholder for "Used in" -->

See "The KL-UCB algorithm for bounded stochastic bandits and beyond" by Garivier
and Cappe.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//agents/bandits/algorithms.py">View
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

<h3 id="get_arm"><code>get_arm</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//agents/bandits/algorithms.py">View
source</a>

```python
get_arm(t)
```

<h3 id="get_score"><code>get_score</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//agents/bandits/algorithms.py">View
source</a>

```python
get_score(t)
```

Computes upper confidence bounds of reward / pulls at round t.

<h3 id="print"><code>print</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//agents/bandits/algorithms.py">View
source</a>

```python
print()
```

<h3 id="set_state"><code>set_state</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//agents/bandits/algorithms.py">View
source</a>

```python
set_state(
    pulls,
    reward
)
```

<h3 id="update"><code>update</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//agents/bandits/algorithms.py">View
source</a>

```python
update(
    arm,
    reward
)
```
