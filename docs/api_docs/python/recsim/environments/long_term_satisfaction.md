<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.long_term_satisfaction" />
<meta itemprop="path" content="Stable" />
</div>

# Module: recsim.environments.long_term_satisfaction

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/long_term_satisfaction.py">View
source</a>

Long term satisfaction (Choc/Kale) environment.

This environment depicts a situation in which a user of an online service
interacts with items of content, which are characterized by their level of
clickbaitiness (on a scale of 0 to 1). In particular, clickbaity items (choc)
generate engagement, but lead to decrease in long-term satisfaction.
Non-clickbaity items (kale) increase satisfaction but do not generate as much
engagement. The challenge is to balance the two in order to achieve some long-
term optimal trade-off. The dynamics of this system are partially observable, as
satisfaction is a latent variable. It has to be inferred through the
increase/decrease in engagement.

## Classes

[`class LTSDocument`](../../recsim/environments/long_term_satisfaction/LTSDocument.md):
Class to represent an LTS Document.

[`class LTSDocumentSampler`](../../recsim/environments/long_term_satisfaction/LTSDocumentSampler.md):
Class to sample LTSDocument documents.

[`class LTSResponse`](../../recsim/environments/long_term_satisfaction/LTSResponse.md):
Class to represent a user's response to a document.

[`class LTSStaticUserSampler`](../../recsim/environments/long_term_satisfaction/LTSStaticUserSampler.md):
Generates user with identical predetermined parameters.

[`class LTSUserModel`](../../recsim/environments/long_term_satisfaction/LTSUserModel.md):
Class to model a user with long-term satisfaction dynamics.

[`class LTSUserState`](../../recsim/environments/long_term_satisfaction/LTSUserState.md):
Class to represent users.

## Functions

[`FLAGS(...)`](../../recsim/environments/interest_evolution/FLAGS.md): Registry
of 'Flag' objects.

[`clicked_engagement_reward(...)`](../../recsim/environments/long_term_satisfaction/clicked_engagement_reward.md):
Calculates the total clicked watchtime from a list of responses.

[`create_environment(...)`](../../recsim/environments/long_term_satisfaction/create_environment.md):
Creates a long-term satisfaction environment.
