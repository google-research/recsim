<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.choice_model.CascadeChoiceModel" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="score_no_click"/>
<meta itemprop="property" content="scores"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="choose_item"/>
<meta itemprop="property" content="score_documents"/>
</div>

# recsim.choice_model.CascadeChoiceModel

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//choice_model.py">View
source</a>

## Class `CascadeChoiceModel`

The base class for cascade choice models.

Inherits From:
[`NormalizableChoiceModel`](../../recsim/choice_model/NormalizableChoiceModel.md)

<!-- Placeholder for "Used in" -->

#### Attributes:

*   <b>`attention_prob`</b>: The probability of examining a document i given
    document i - 1 not clicked.
*   <b>`score_scaling`</b>: A multiplicative factor to convert score of document
    i to the click probability of examined document i.

#### Raises:

*   <b>`ValueError`</b>: if either attention_prob or base_attention_prob is
    invalid.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//choice_model.py">View
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

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//choice_model.py">View
source</a>

```python
choose_item()
```

Returns selected index of document in the slate.

#### Returns:

*   <b>`selected_index`</b>: a integer indicating which item was chosen, or None
    if none were selected.

<h3 id="score_documents"><code>score_documents</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim//choice_model.py">View
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
