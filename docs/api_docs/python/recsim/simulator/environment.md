<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.simulator.environment" />
<meta itemprop="path" content="Stable" />
</div>

# Module: recsim.simulator.environment

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/simulator/environment.py">View
source</a>

Class to represent the environment in the recommender system setting.


Thus, it models things such as (1) the user's state, for example his/her
interests and circumstances, (2) the documents available to suggest from and
their properties, (3) simulates the selection of an item in the slate (or a
no-op/quit), and (4) models the change in a user's state based on the slate
presented and the document selected.

The agent interacting with the environment is the recommender system. The agent
receives the state, which is an observation of the user's state and observations
of the candidate documents. The agent then provides an action, which is a slate
(an array of indices into the candidate set).

The goal of the agent is to learn a recommendation policy: a policy that serves
the user a slate (action) based on user and document features (state)

## Classes

[`class AbstractEnvironment`](../../recsim/simulator/environment/AbstractEnvironment.md):
Abstract class representing the recommender system environment.

[`class Environment`](../../recsim/simulator/environment/Environment.md): Class
to represent the environment with one user.

[`class MultiUserEnvironment`](../../recsim/simulator/environment/MultiUserEnvironment.md):
Class to represent environment with multiple users.

[`class SingleUserEnvironment`](../../recsim/simulator/environment/Environment.md):
Class to represent the environment with one user.
