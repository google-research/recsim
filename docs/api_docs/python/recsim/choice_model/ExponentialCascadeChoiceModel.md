<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.choice_model.ExponentialCascadeChoiceModel" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="score_no_click"/>
<meta itemprop="property" content="scores"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="choose_item"/>
<meta itemprop="property" content="score_documents"/>
</div>

# recsim.choice_model.ExponentialCascadeChoiceModel

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/choice_model.py">View
source</a>

## Class `ExponentialCascadeChoiceModel`

An exponential cascade choice model.

Inherits From:
[`CascadeChoiceModel`](../../recsim/choice_model/CascadeChoiceModel.md)

<!-- Placeholder for "Used in" -->

Clicks the item at position i according to p(i) = attention_prob * score_scaling
* exp(score(i)) by going through the slate in order, and stopping once an item
has been clicked.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/choice_model.py">View
source</a>

```python
__init__(choice_features)
```

Initialize self. See help(type(self)) for accurate signature.

## Properties

<h3 id="score_no_click"><code>score_no_click</code></h3>

<h3 id="scores"><code>scores</code></h3>

## Methods

<h3 id="choose_item"><code>choose_item</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/choice_model.py">View
source</a>

```python
choose_item()
```

Returns selected index of document in the slate.

#### Returns:

*   <b>`selected_index`</b>: a integer indicating which item was chosen, or None
    if none were selected.

<h3 id="score_documents"><code>score_documents</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/choice_model.py">View
source</a>

```python
score_documents(
    user_state,
    doc_obs
)
```

Computes unnormalized scores of documents in the slate given user state.

#### Args:

*   <b>`user_state`</b>: An instance of AbstractUserState.
*   <b>`doc_obs`</b>: A numpy array that represents the observation of all
    documents in the slate.

#### Attributes:

*   <b>`scores`</b>: A numpy array that stores the scores of all documents.
*   <b>`score_no_click`</b>: A float that represents the score for the action of
    picking no document.
