<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.tabular_q_agent.TabularQAgent" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="begin_episode"/>
<meta itemprop="property" content="bundle_and_checkpoint"/>
<meta itemprop="property" content="end_episode"/>
<meta itemprop="property" content="step"/>
<meta itemprop="property" content="unbundle"/>
</div>

# recsim.agents.tabular_q_agent.TabularQAgent

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/tabular_q_agent.py">View
source</a>

Tabular Q-learning agent with universal function approximation.

Inherits From:
[`AbstractEpisodicRecommenderAgent`](../../../recsim/agent/AbstractEpisodicRecommenderAgent.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.agents.tabular_q_agent.TabularQAgent(
    observation_space, action_space, eval_mode=False, ignore_response=True,
    discretization_bounds=(0.0, 10.0), number_bins=100,
    exploration_policy='epsilon_greedy', exploration_temperature=0.99,
    learning_rate=0.1, gamma=0.99, ordinal_slates=False, **kwargs
)
</code></pre>

<!-- Placeholder for "Used in" -->

This agent provides a tabular implementation of the Q-learning algorithm. To
construct a tabular representation of the state-action space, the agent does the
following: 1. the action space consists of all ordered k-tuples of document
features available in observation['doc']; 2. the state space consists of
observation['user'] and observation['response']; 3. the observation and action
space are joined and flattened; 4. all continuoius values in the flattened
state-action vector are discretized into a predefined number of bins. In the
tabularized state-action space, the agent applies the standard Q-learning update
of Q_{t+1}(s,a) = (1-a) * Q_t(s,a) + a * (R(s,a) + g * max_a(Q_t(s', a))).
Assuming that the discretization of countinous attributes is fine enough, and
the problem itself is Markovian given the observations, the output of this agent
can be assumed to converge to a close approximation of the ground truth
Q-function. Producing ground truth Q-functions is the main intended use of this
agent, since discretization is prohibitively expensive in high-dimensional
environments.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`observation_space`
</td>
<td>
a gym.spaces object specifying the format of
observations.
</td>
</tr><tr>
<td>
`action_space`
</td>
<td>
a gym.spaces object that specifies the format of actions.
</td>
</tr><tr>
<td>
`eval_mode`
</td>
<td>
Boolean indicating whether the agent is in training or eval
mode.
</td>
</tr><tr>
<td>
`ignore_response`
</td>
<td>
Boolean indicating whether the agent should ignore the
response part of the observation.
</td>
</tr><tr>
<td>
`discretization_bounds`
</td>
<td>
pair of real numbers indicating the min and max
value for continuous attributes discretization. Values below the min
will all be grouped in the first bin, while values above the max will
all be grouped in the last bin. See the documentation of numpy.digitize
for further details.
</td>
</tr><tr>
<td>
`number_bins`
</td>
<td>
positive integer number of bins used to discretize continuous
attributes.
</td>
</tr><tr>
<td>
`exploration_policy`
</td>
<td>
either one of ['epsilon_greedy', 'min_count'] or a
custom function.
function.
</td>
</tr><tr>
<td>
`exploration_temperature`
</td>
<td>
a real number passed as parameter to the
exploration policy.
</td>
</tr><tr>
<td>
`learning_rate`
</td>
<td>
a real number between 0 and 1 indicating how much to update
Q-values, i.e. Q_t+1(s,a) = (1 - learning_rate) * Q_t(s, a)
+ learning_rate * (R(s,a) + ...).
</td>
</tr><tr>
<td>
`gamma`
</td>
<td>
real value between 0 and 1 indicating the discount factor of the
MDP.
</td>
</tr><tr>
<td>
`ordinal_slates`
</td>
<td>
boolean indicating whether slate ordering matters, e.g.
whether the slates (1, 2) and (2, 1) should be considered different
actions. Using ordinal slates increases complexity factorially.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
additional arguments like eval_mode.
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`multi_user`
</td>
<td>
Returns boolean indicating whether this agent serves multiple users.
</td>
</tr>
</table>

## Methods

<h3 id="begin_episode"><code>begin_episode</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agent.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>begin_episode(
    observation=None
)
</code></pre>

Returns the agent's first action for this episode.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`observation`
</td>
<td>
numpy array, the environment's initial observation.
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`slate`
</td>
<td>
An integer array of size _slate_size, where each element is an
index into the list of doc_obs
</td>
</tr>
</table>

<h3 id="bundle_and_checkpoint"><code>bundle_and_checkpoint</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/tabular_q_agent.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>bundle_and_checkpoint(
    checkpoint_dir, iteration_number
)
</code></pre>

Returns a self-contained bundle of the agent's state.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`checkpoint_dir`
</td>
<td>
A string for the directory where objects will be saved.
</td>
</tr><tr>
<td>
`iteration_number`
</td>
<td>
An integer of iteration number to use for naming the
checkpoint file.
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A dictionary containing additional Python objects to be checkpointed by
the experiment. Each key is a string for the object name and the value
is actual object. If the checkpoint directory does not exist, returns
empty dictionary.
</td>
</tr>

</table>

<h3 id="end_episode"><code>end_episode</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/tabular_q_agent.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>end_episode(
    reward, observation
)
</code></pre>

Signals the end of the episode to the agent.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`reward`
</td>
<td>
An float that is the last reward from the environment.
</td>
</tr><tr>
<td>
`observation`
</td>
<td>
numpy array that represents the last observation of the
episode.
</td>
</tr>
</table>

<h3 id="step"><code>step</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/tabular_q_agent.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>step(
    reward, observation
)
</code></pre>

Records the most recent transition and returns the agent's next action.

We store the observation of the last time step since we want to store it with
the reward.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`reward`
</td>
<td>
The reward received from the agent's most recent action as a
float.
</td>
</tr><tr>
<td>
`observation`
</td>
<td>
A dictionary that includes the most recent observations and
should have the following fields:
- user: A NumPy array representing user's observed state. Assumes it is
a concatenation of topic pull counts and topic click counts.
- doc: A NumPy array representing observations of document features.
Assumes it is a concatenation of one-hot encoding of topic_id and
document quality.
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`slate`
</td>
<td>
An integer array of size _slate_size, where each element is an
index into the list of doc_obs
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if reward is not in [0, 1].
</td>
</tr>
</table>

<h3 id="unbundle"><code>unbundle</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/tabular_q_agent.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>unbundle(
    checkpoint_dir, iteration_number, bundle_dict
)
</code></pre>

Restores the agent from a checkpoint.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`checkpoint_dir`
</td>
<td>
A string that represents the path to the checkpoint saved
by tf.Save.
</td>
</tr><tr>
<td>
`iteration_number`
</td>
<td>
An integer that represents the checkpoint version and is
used when restoring replay buffer.
</td>
</tr><tr>
<td>
`bundle_dict`
</td>
<td>
A dict containing additional Python objects owned by the
agent. Each key is an object name and the value is the actual object.
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
bool, True if unbundling was successful.
</td>
</tr>

</table>
