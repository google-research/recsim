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

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/dopamine/dqn_agent.py">View
source</a>

## Class `DQNAgentRecSim`

RecSim-specific Dopamine DQN agent that converts the observation space.

<!-- Placeholder for "Used in" -->

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/agents/dopamine/dqn_agent.py">View
source</a>

```python
__init__(
    sess,
    observation_space,
    num_actions,
    stack_size,
    optimizer_name,
    eval_mode,
    **kwargs
)
```

Initializes the agent and constructs the components of its graph.

#### Args:

*   <b>`sess`</b>: `tf.Session`, for executing ops.
*   <b>`num_actions`</b>: int, number of actions the agent can take at any
    state.
*   <b>`observation_shape`</b>: tuple of ints describing the observation shape.
*   <b>`observation_dtype`</b>: tf.DType, specifies the type of the
    observations. Note that if your inputs are continuous, you should set this
    to tf.float32.
*   <b>`stack_size`</b>: int, number of frames to use in state stack.
*   <b>`network`</b>: tf.Keras.Model, expecting 2 parameters: num_actions,
    network_type. A call to this object will return an instantiation of the
    network provided. The network returned can be run with different inputs to
    create different outputs. See
    dopamine.discrete_domains.atari_lib.NatureDQNNetwork as an example.
*   <b>`gamma`</b>: float, discount factor with the usual RL meaning.
*   <b>`update_horizon`</b>: int, horizon at which updates are performed, the
    'n' in n-step update.
*   <b>`min_replay_history`</b>: int, number of transitions that should be
    experienced before the agent begins training its value function.
*   <b>`update_period`</b>: int, period between DQN updates.
*   <b>`target_update_period`</b>: int, update period for the target network.
*   <b>`epsilon_fn`</b>: function expecting 4 parameters: (decay_period, step,
    warmup_steps, epsilon). This function should return the epsilon value used
    for exploration during training.
*   <b>`epsilon_train`</b>: float, the value to which the agent's epsilon is
    eventually decayed during training.
*   <b>`epsilon_eval`</b>: float, epsilon used when evaluating the agent.
*   <b>`epsilon_decay_period`</b>: int, length of the epsilon decay schedule.
*   <b>`tf_device`</b>: str, Tensorflow device on which the agent's graph is
    executed.
*   <b>`eval_mode`</b>: bool, True for evaluation and False for training.
*   <b>`use_staging`</b>: bool, when True use a staging area to prefetch the
    next training batch, speeding training up by about 30%.
*   <b>`max_tf_checkpoints_to_keep`</b>: int, the number of TensorFlow
    checkpoints to keep.
*   <b>`optimizer`</b>: `tf.train.Optimizer`, for training the value function.
*   <b>`summary_writer`</b>: SummaryWriter object for outputting training
    statistics. Summary writing disabled if set to None.
*   <b>`summary_writing_frequency`</b>: int, frequency with which summaries will
    be written. Lower values will result in slower training.
*   <b>`allow_partial_reload`</b>: bool, whether we allow reloading a partial
    agent (for instance, only the network parameters).

## Methods

<h3 id="begin_episode"><code>begin_episode</code></h3>

```python
begin_episode(observation)
```

Returns the agent's first action for this episode.

#### Args:

*   <b>`observation`</b>: numpy array, the environment's initial observation.

#### Returns:

int, the selected action.

<h3 id="bundle_and_checkpoint"><code>bundle_and_checkpoint</code></h3>

```python
bundle_and_checkpoint(
    checkpoint_dir,
    iteration_number
)
```

Returns a self-contained bundle of the agent's state.

This is used for checkpointing. It will return a dictionary containing all
non-TensorFlow objects (to be saved into a file by the caller), and it saves all
TensorFlow objects into a checkpoint file.

#### Args:

*   <b>`checkpoint_dir`</b>: str, directory where TensorFlow objects will be
    saved.
*   <b>`iteration_number`</b>: int, iteration number to use for naming the
    checkpoint file.

#### Returns:

A dict containing additional Python objects to be checkpointed by the
experiment. If the checkpoint directory does not exist, returns None.

<h3 id="end_episode"><code>end_episode</code></h3>

```python
end_episode(reward)
```

Signals the end of the episode to the agent.

We store the observation of the current time step, which is the last observation
of the episode.

#### Args:

*   <b>`reward`</b>: float, the last reward from the environment.

<h3 id="step"><code>step</code></h3>

```python
step(
    reward,
    observation
)
```

Records the most recent transition and returns the agent's next action.

We store the observation of the last time step since we want to store it with
the reward.

#### Args:

*   <b>`reward`</b>: float, the reward received from the agent's most recent
    action.
*   <b>`observation`</b>: numpy array, the most recent observation.

#### Returns:

int, the selected action.

<h3 id="unbundle"><code>unbundle</code></h3>

```python
unbundle(
    checkpoint_dir,
    iteration_number,
    bundle_dictionary
)
```

Restores the agent from a checkpoint.

Restores the agent's Python objects to those specified in bundle_dictionary, and
restores the TensorFlow objects to those specified in the checkpoint_dir. If the
checkpoint_dir does not exist, will not reset the agent's state.

#### Args:

*   <b>`checkpoint_dir`</b>: str, path to the checkpoint saved by tf.Save.
*   <b>`iteration_number`</b>: int, checkpoint version, used when restoring the
    replay buffer.
*   <b>`bundle_dictionary`</b>: dict, containing additional Python objects owned
    by the agent.

#### Returns:

bool, True if unbundling was successful.
