<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.interest_evolution" />
<meta itemprop="path" content="Stable" />
</div>

# Module: recsim.environments.interest_evolution

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_evolution.py">View
source</a>

Classes to represent the interest evolution documents and users.

## Classes

[`class IEvResponse`](../../recsim/environments/interest_evolution/IEvResponse.md):
Class to represent a user's response to a video.

[`class IEvUserDistributionSampler`](../../recsim/environments/interest_evolution/IEvUserDistributionSampler.md):
Class to sample users by a hardcoded distribution.

[`class IEvUserModel`](../../recsim/environments/interest_evolution/IEvUserModel.md):
Class to model an interest evolution user.

[`class IEvUserState`](../../recsim/environments/interest_evolution/IEvUserState.md):
Class to represent interest evolution users.

[`class IEvVideo`](../../recsim/environments/interest_evolution/IEvVideo.md):
Class to represent a interest evolution Video.

[`class IEvVideoSampler`](../../recsim/environments/interest_evolution/IEvVideoSampler.md):
Class to sample interest_evolution videos.

[`class UtilityModelUserSampler`](../../recsim/environments/interest_evolution/UtilityModelUserSampler.md):
Class that samples users for utility model experiment.

[`class UtilityModelVideoSampler`](../../recsim/environments/interest_evolution/UtilityModelVideoSampler.md):
Class that samples videos for utility model experiment.

## Functions

[`FLAGS(...)`](../../recsim/environments/interest_evolution/FLAGS.md): Registry
of 'Flag' objects.

[`clicked_watchtime_reward(...)`](../../recsim/environments/interest_evolution/clicked_watchtime_reward.md):
Calculates the total clicked watchtime from a list of responses.

[`create_environment(...)`](../../recsim/environments/interest_evolution/create_environment.md):
Creates an interest evolution environment.

[`total_clicks_reward(...)`](../../recsim/environments/interest_evolution/total_clicks_reward.md):
Calculates the total number of clicks from a list of responses.
