<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.interest_exploration" />
<meta itemprop="path" content="Stable" />
</div>

# Module: recsim.environments.interest_exploration

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_exploration.py">View
source</a>

Correlated interest exploration environment.


This environment models the problem of active exploration of user interests. It
is meant to illustrate popularity bias in recommender systems, where myopic
maximization of engagement leads to bias towards documents that have wider
appeal, whereas niche user interests remain unexplored.

In this setting, documents are generated from M topics (types) such that each
document belongs to exactly one topic. Furthermore, there are N types (types) of
users. Each document d has a production quality f_D(d) score drawn from a
distribution associated with its type D (e.g. more mass-appeal types tend to
have higher production values). On the other hand, each user u has an affinity
score g_U(u,d) towards each document type (drawn from a distribution associated
with the user's type). The final affinity of user u to document d is thus
g_U(u,d) + f_D(d). When faced with a slate of documents, the user clicks on a
document based on a multinomial logistic choice model with the affinity scores
as parameters.

A myopic agent will favor types with high production value, as they have a high
apriori probability of getting clicked across all user types. This leads the
agent to ignore niche interests, producing a suboptimal policy. This scenario
can be seen as a correlated arms bandit problem.

## Classes

[`class IEClusterUserSampler`](../../recsim/environments/interest_exploration/IEClusterUserSampler.md):
Samples users from predetermined types with type-specific parameters.

[`class IEDocument`](../../recsim/environments/interest_exploration/IEDocument.md):
Class to represent an IE Document.

[`class IEResponse`](../../recsim/environments/interest_exploration/IEResponse.md):
Class to represent a user's response to a document.

[`class IETopicDocumentSampler`](../../recsim/environments/interest_exploration/IETopicDocumentSampler.md):
Samples documents with topic-specific quality distribution.

[`class IEUserModel`](../../recsim/environments/interest_exploration/IEUserModel.md):
Class to model a user.

[`class IEUserState`](../../recsim/environments/interest_exploration/IEUserState.md):
Class to represent users.

## Functions

[`FLAGS(...)`](../../recsim/environments/interest_evolution/FLAGS.md): Registry
of 'Flag' objects.

[`create_environment(...)`](../../recsim/environments/interest_exploration/create_environment.md):
Creates an interest exploration environment.

[`total_clicks_reward(...)`](../../recsim/environments/interest_exploration/total_clicks_reward.md):
Calculates the total number of clicks from a list of responses.
