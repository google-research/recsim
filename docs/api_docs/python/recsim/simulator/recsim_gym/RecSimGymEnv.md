<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.simulator.recsim_gym.RecSimGymEnv" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="action_space"/>
<meta itemprop="property" content="environment"/>
<meta itemprop="property" content="game_over"/>
<meta itemprop="property" content="observation_space"/>
<meta itemprop="property" content="unwrapped"/>
<meta itemprop="property" content="__enter__"/>
<meta itemprop="property" content="__exit__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="close"/>
<meta itemprop="property" content="render"/>
<meta itemprop="property" content="reset"/>
<meta itemprop="property" content="reset_metrics"/>
<meta itemprop="property" content="reset_sampler"/>
<meta itemprop="property" content="seed"/>
<meta itemprop="property" content="step"/>
<meta itemprop="property" content="update_metrics"/>
<meta itemprop="property" content="write_metrics"/>
<meta itemprop="property" content="metadata"/>
<meta itemprop="property" content="reward_range"/>
</div>

# recsim.simulator.recsim_gym.RecSimGymEnv

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/simulator/recsim_gym.py">View
source</a>

## Class `RecSimGymEnv`

Class to wrap recommender system environment to gym.Env.

<!-- Placeholder for "Used in" -->

#### Attributes:

*   <b>`game_over`</b>: A boolean indicating whether the current game has
    finished
*   <b>`action_space`</b>: A gym.spaces object that specifies the space for
    possible actions.
*   <b>`observation_space`</b>: A gym.spaces object that specifies the space for
    possible observations.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/simulator/recsim_gym.py">View
source</a>

```python
__init__(
    raw_environment,
    reward_aggregator,
    metrics_aggregator=_dummy_metrics_aggregator,
    metrics_writer=_dummy_metrics_writer
)
```

Initializes a RecSim environment conforming to gym.Env.

#### Args:

*   <b>`raw_environment`</b>: A recsim recommender system environment.
*   <b>`reward_aggregator`</b>: A function mapping a list of responses to a
    number.
*   <b>`metrics_aggregator`</b>: A function aggregating metrics over all steps
    given responses and response_names.
*   <b>`metrics_writer`</b>: A function writing final metrics to TensorBoard.

## Properties

<h3 id="action_space"><code>action_space</code></h3>

Returns the action space of the environment.

Each action is a vector that specified document slate. Each element in the
vector corresponds to the index of the document in the candidate set.

<h3 id="environment"><code>environment</code></h3>

Returns the recsim recommender system environment.

<h3 id="game_over"><code>game_over</code></h3>

<h3 id="observation_space"><code>observation_space</code></h3>

Returns the observation space of the environment.

Each observation is a dictionary with three keys `user`, `doc` and `response`
that includes observation about user state, document and user response,
respectively.

<h3 id="unwrapped"><code>unwrapped</code></h3>

Completely unwrap this env.

#### Returns:

*   <b>`gym.Env`</b>: The base non-wrapped gym.Env instance

## Methods

<h3 id="__enter__"><code>__enter__</code></h3>

```python
__enter__()
```

<h3 id="__exit__"><code>__exit__</code></h3>

```python
__exit__(*args)
```

<h3 id="close"><code>close</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/simulator/recsim_gym.py">View
source</a>

```python
close()
```

Override close in your subclass to perform any necessary cleanup.

Environments will automatically close() themselves when garbage collected or
when the program exits.

<h3 id="render"><code>render</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/simulator/recsim_gym.py">View
source</a>

```python
render(mode='human')
```

Renders the environment.

The set of supported modes varies per environment. (And some environments do not
support rendering at all.) By convention, if mode is:

-   human: render to the current display or terminal and return nothing. Usually
    for human consumption.
-   rgb_array: Return an numpy.ndarray with shape (x, y, 3), representing RGB
    values for an x-by-y pixel image, suitable for turning into a video.
-   ansi: Return a string (str) or StringIO.StringIO containing a terminal-style
    text representation. The text can include newlines and ANSI escape sequences
    (e.g. for colors).

#### Note:

Make sure that your class's metadata 'render.modes' key includes the list of
supported modes. It's recommended to call super() in implementations to use the
functionality of this method.

#### Args:

mode (str): the mode to render with

#### Example:

class MyEnv(Env): metadata = {'render.modes': ['human', 'rgb_array']}

    def render(self, mode='human'):
        if mode == 'rgb_array':
            return np.array(...) # return RGB frame suitable for video
        elif mode == 'human':
            ... # pop up a window and render
        else:
            super(MyEnv, self).render(mode=mode) # just raise an exception

<h3 id="reset"><code>reset</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/simulator/recsim_gym.py">View
source</a>

```python
reset()
```

Resets the state of the environment and returns an initial observation.

#### Returns:

observation (object): the initial observation.

<h3 id="reset_metrics"><code>reset_metrics</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/simulator/recsim_gym.py">View
source</a>

```python
reset_metrics()
```

Resets every metric to zero.

We reset metrics for every iteration but not every episode. On the other hand,
reset() gets called for every episode.

<h3 id="reset_sampler"><code>reset_sampler</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/simulator/recsim_gym.py">View
source</a>

```python
reset_sampler()
```

<h3 id="seed"><code>seed</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/simulator/recsim_gym.py">View
source</a>

```python
seed(seed=None)
```

Sets the seed for this env's random number generator(s).

#### Note:

Some environments use multiple pseudorandom number generators. We want to
capture all such seeds used in order to ensure that there aren't accidental
correlations between multiple generators.

#### Returns:

list<bigint>: Returns the list of seeds used in this env's random number
generators. The first value in the list should be the "main" seed, or the value
which a reproducer should pass to 'seed'. Often, the main seed equals the
provided 'seed', but this won't be true if seed=None, for example.

<h3 id="step"><code>step</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/simulator/recsim_gym.py">View
source</a>

```python
step(action)
```

Runs one timestep of the environment's dynamics.

When end of episode is reached, you are responsible for calling `reset()` to
reset this environment's state. Accepts an action and returns a tuple
(observation, reward, done, info).

#### Args:

action (object): An action provided by the environment

#### Returns:

A four-tuple of (observation, reward, done, info) where: observation (object):
agent's observation that include 1. User's state features 2. Document's
observation 3. Observation about user's slate responses. reward (float) : The
amount of reward returned after previous action done (boolean): Whether the
episode has ended, in which case further step() calls will return undefined
results info (dict): Contains responses for the full slate for
debugging/learning.

<h3 id="update_metrics"><code>update_metrics</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/simulator/recsim_gym.py">View
source</a>

```python
update_metrics(responses)
```

Updates metrics with one step responses.

<h3 id="write_metrics"><code>write_metrics</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/recsim/simulator/recsim_gym.py">View
source</a>

```python
write_metrics(add_summary_fn)
```

Writes metrics to TensorBoard by calling add_summary_fn.

## Class Members

*   `metadata` <a id="metadata"></a>
*   `reward_range` <a id="reward_range"></a>
