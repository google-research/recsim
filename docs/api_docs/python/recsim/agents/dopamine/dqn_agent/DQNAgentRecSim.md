<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.agents.dopamine.dqn_agent.DQNAgentRecSim" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="begin_episode"/>
<meta itemprop="property" content="bundle_and_checkpoint"/>
<meta itemprop="property" content="end_episode"/>
<meta itemprop="property" content="step"/>
<meta itemprop="property" content="unbundle"/>
</div>

# recsim.agents.dopamine.dqn_agent.DQNAgentRecSim

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/dopamine/dqn_agent.py">View
source</a>

RecSim-specific Dopamine DQN agent that converts the observation space.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.agents.dopamine.dqn_agent.DQNAgentRecSim(
    sess, observation_space, num_actions, stack_size, optimizer_name, eval_mode,
    **kwargs
)
</code></pre>

<!-- Placeholder for "Used in" -->
<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`sess`
</td>
<td>
`tf.compat.v1.Session`, for executing ops.
</td>
</tr><tr>
<td>
`num_actions`
</td>
<td>
int, number of actions the agent can take at any state.
</td>
</tr><tr>
<td>
`observation_shape`
</td>
<td>
tuple of ints describing the observation shape.
</td>
</tr><tr>
<td>
`observation_dtype`
</td>
<td>
tf.DType, specifies the type of the observations. Note
that if your inputs are continuous, you should set this to tf.float32.
</td>
</tr><tr>
<td>
`stack_size`
</td>
<td>
int, number of frames to use in state stack.
</td>
</tr><tr>
<td>
`network`
</td>
<td>
tf.Keras.Model, expecting 2 parameters: num_actions,
network_type. A call to this object will return an instantiation of the
network provided. The network returned can be run with different inputs
to create different outputs. See
dopamine.discrete_domains.atari_lib.NatureDQNNetwork as an example.
</td>
</tr><tr>
<td>
`gamma`
</td>
<td>
float, discount factor with the usual RL meaning.
</td>
</tr><tr>
<td>
`update_horizon`
</td>
<td>
int, horizon at which updates are performed, the 'n' in
n-step update.
</td>
</tr><tr>
<td>
`min_replay_history`
</td>
<td>
int, number of transitions that should be experienced
before the agent begins training its value function.
</td>
</tr><tr>
<td>
`update_period`
</td>
<td>
int, period between DQN updates.
</td>
</tr><tr>
<td>
`target_update_period`
</td>
<td>
int, update period for the target network.
</td>
</tr><tr>
<td>
`epsilon_fn`
</td>
<td>
function expecting 4 parameters:
(decay_period, step, warmup_steps, epsilon). This function should return
the epsilon value used for exploration during training.
</td>
</tr><tr>
<td>
`epsilon_train`
</td>
<td>
float, the value to which the agent's epsilon is eventually
decayed during training.
</td>
</tr><tr>
<td>
`epsilon_eval`
</td>
<td>
float, epsilon used when evaluating the agent.
</td>
</tr><tr>
<td>
`epsilon_decay_period`
</td>
<td>
int, length of the epsilon decay schedule.
</td>
</tr><tr>
<td>
`tf_device`
</td>
<td>
str, Tensorflow device on which the agent's graph is executed.
</td>
</tr><tr>
<td>
`eval_mode`
</td>
<td>
bool, True for evaluation and False for training.
</td>
</tr><tr>
<td>
`use_staging`
</td>
<td>
bool, when True use a staging area to prefetch the next
training batch, speeding training up by about 30%.
</td>
</tr><tr>
<td>
`max_tf_checkpoints_to_keep`
</td>
<td>
int, the number of TensorFlow checkpoints to
keep.
</td>
</tr><tr>
<td>
`optimizer`
</td>
<td>
`tf.compat.v1.train.Optimizer`, for training the value
function.
</td>
</tr><tr>
<td>
`summary_writer`
</td>
<td>
SummaryWriter object for outputting training statistics.
Summary writing disabled if set to None.
</td>
</tr><tr>
<td>
`summary_writing_frequency`
</td>
<td>
int, frequency with which summaries will be
written. Lower values will result in slower training.
</td>
</tr><tr>
<td>
`allow_partial_reload`
</td>
<td>
bool, whether we allow reloading a partial agent
(for instance, only the network parameters).
</td>
</tr>
</table>

## Methods

<h3 id="begin_episode"><code>begin_episode</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>begin_episode(
    observation
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
<tr class="alt">
<td colspan="2">
int, the selected action.
</td>
</tr>

</table>

<h3 id="bundle_and_checkpoint"><code>bundle_and_checkpoint</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>bundle_and_checkpoint(
    checkpoint_dir, iteration_number
)
</code></pre>

Returns a self-contained bundle of the agent's state.

This is used for checkpointing. It will return a dictionary containing all
non-TensorFlow objects (to be saved into a file by the caller), and it saves all
TensorFlow objects into a checkpoint file.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`checkpoint_dir`
</td>
<td>
str, directory where TensorFlow objects will be saved.
</td>
</tr><tr>
<td>
`iteration_number`
</td>
<td>
int, iteration number to use for naming the checkpoint
file.
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A dict containing additional Python objects to be checkpointed by the
experiment. If the checkpoint directory does not exist, returns None.
</td>
</tr>

</table>

<h3 id="end_episode"><code>end_episode</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>end_episode(
    reward
)
</code></pre>

Signals the end of the episode to the agent.

We store the observation of the current time step, which is the last observation
of the episode.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`reward`
</td>
<td>
float, the last reward from the environment.
</td>
</tr>
</table>

<h3 id="step"><code>step</code></h3>

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
float, the reward received from the agent's most recent action.
</td>
</tr><tr>
<td>
`observation`
</td>
<td>
numpy array, the most recent observation.
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
int, the selected action.
</td>
</tr>

</table>

<h3 id="unbundle"><code>unbundle</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>unbundle(
    checkpoint_dir, iteration_number, bundle_dictionary
)
</code></pre>

Restores the agent from a checkpoint.

Restores the agent's Python objects to those specified in bundle_dictionary, and
restores the TensorFlow objects to those specified in the checkpoint_dir. If the
checkpoint_dir does not exist, will not reset the agent's state.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`checkpoint_dir`
</td>
<td>
str, path to the checkpoint saved by tf.Save.
</td>
</tr><tr>
<td>
`iteration_number`
</td>
<td>
int, checkpoint version, used when restoring the replay
buffer.
</td>
</tr><tr>
<td>
`bundle_dictionary`
</td>
<td>
dict, containing additional Python objects owned by
the agent.
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
