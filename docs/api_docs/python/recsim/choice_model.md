<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.choice_model" />
<meta itemprop="path" content="Stable" />
</div>

# Module: recsim.choice_model

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/choice_model.py">View
source</a>

Abstract classes that encode a user's state and dynamics.

## Classes

[`class AbstractChoiceModel`](../recsim/choice_model/AbstractChoiceModel.md):
Abstract class to represent the user choice model.

[`class CascadeChoiceModel`](../recsim/choice_model/CascadeChoiceModel.md): The
base class for cascade choice models.

[`class ExponentialCascadeChoiceModel`](../recsim/choice_model/ExponentialCascadeChoiceModel.md):
An exponential cascade choice model.

[`class MultinomialLogitChoiceModel`](../recsim/choice_model/MultinomialLogitChoiceModel.md):
A multinomial logit choice model.

[`class MultinomialProportionalChoiceModel`](../recsim/choice_model/MultinomialProportionalChoiceModel.md):
A multinomial proportional choice function.

[`class NormalizableChoiceModel`](../recsim/choice_model/NormalizableChoiceModel.md):
A normalizable choice model.

[`class ProportionalCascadeChoiceModel`](../recsim/choice_model/ProportionalCascadeChoiceModel.md):
A proportional cascade choice model.

## Functions

[`softmax(...)`](../recsim/choice_model/softmax.md): Computes the softmax of a
vector.
