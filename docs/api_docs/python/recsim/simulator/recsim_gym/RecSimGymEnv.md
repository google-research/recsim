<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.simulator.recsim_gym.RecSimGymEnv" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__enter__"/>
<meta itemprop="property" content="__exit__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="close"/>
<meta itemprop="property" content="extract_env_info"/>
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
<meta itemprop="property" content="spec"/>
</div>

# recsim.simulator.recsim_gym.RecSimGymEnv

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/simulator/recsim_gym.py">View
source</a>

Class to wrap recommender system environment to gym.Env.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.simulator.recsim_gym.RecSimGymEnv(
    raw_environment, reward_aggregator,
    metrics_aggregator=_dummy_metrics_aggregator,
    metrics_writer=_dummy_metrics_writer
)
</code></pre>

<!-- Placeholder for "Used in" -->
<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`raw_environment`
</td>
<td>
A recsim recommender system environment.
</td>
</tr><tr>
<td>
`reward_aggregator`
</td>
<td>
A function mapping a list of responses to a number.
</td>
</tr><tr>
<td>
`metrics_aggregator`
</td>
<td>
A function aggregating metrics over all steps given
responses and response_names.
</td>
</tr><tr>
<td>
`metrics_writer`
</td>
<td>
A function writing final metrics to TensorBoard.
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`game_over`
</td>
<td>
A boolean indicating whether the current game has finished
</td>
</tr><tr>
<td>
`action_space`
</td>
<td>
A gym.spaces object that specifies the space for possible
actions.
</td>
</tr><tr>
<td>
`observation_space`
</td>
<td>
A gym.spaces object that specifies the space for possible
observations.
</td>
</tr><tr>
<td>
`environment`
</td>
<td>
Returns the recsim recommender system environment.
</td>
</tr><tr>
<td>
`unwrapped`
</td>
<td>
Completely unwrap this env.
</td>
</tr>
</table>

## Methods

<h3 id="close"><code>close</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/simulator/recsim_gym.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>close()
</code></pre>

Override close in your subclass to perform any necessary cleanup.

Environments will automatically close() themselves when garbage collected or
when the program exits.

<h3 id="extract_env_info"><code>extract_env_info</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/simulator/recsim_gym.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>extract_env_info()
</code></pre>

<h3 id="render"><code>render</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/simulator/recsim_gym.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>render(
    mode='human'
)
</code></pre>

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

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>
<tr class="alt">
<td colspan="2">
mode (str): the mode to render with
</td>
</tr>

</table>

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

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/simulator/recsim_gym.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset()
</code></pre>

Resets the state of the environment and returns an initial observation.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
observation (object): the initial observation.
</td>
</tr>

</table>

<h3 id="reset_metrics"><code>reset_metrics</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/simulator/recsim_gym.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset_metrics()
</code></pre>

Resets every metric to zero.

We reset metrics for every iteration but not every episode. On the other hand,
reset() gets called for every episode.

<h3 id="reset_sampler"><code>reset_sampler</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/simulator/recsim_gym.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset_sampler()
</code></pre>

<h3 id="seed"><code>seed</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/simulator/recsim_gym.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>seed(
    seed=None
)
</code></pre>

Sets the seed for this env's random number generator(s).

#### Note:

Some environments use multiple pseudorandom number generators. We want to
capture all such seeds used in order to ensure that there aren't accidental
correlations between multiple generators.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
list<bigint>: Returns the list of seeds used in this env's random
number generators. The first value in the list should be the
"main" seed, or the value which a reproducer should pass to
'seed'. Often, the main seed equals the provided 'seed', but
this won't be true if seed=None, for example.
</td>
</tr>

</table>

<h3 id="step"><code>step</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/simulator/recsim_gym.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>step(
    action
)
</code></pre>

Runs one timestep of the environment's dynamics.

When end of episode is reached, you are responsible for calling `reset()` to
reset this environment's state. Accepts an action and returns a tuple
(observation, reward, done, info).

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>
<tr class="alt">
<td colspan="2">
action (object): An action provided by the environment
</td>
</tr>

</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A four-tuple of (observation, reward, done, info) where:
observation (object): agent's observation that include
1. User's state features
2. Document's observation
3. Observation about user's slate responses.
reward (float) : The amount of reward returned after previous action
done (boolean): Whether the episode has ended, in which case further
step() calls will return undefined results
info (dict): Contains responses for the full slate for
debugging/learning.
</td>
</tr>

</table>

<h3 id="update_metrics"><code>update_metrics</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/simulator/recsim_gym.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>update_metrics(
    responses, info=None
)
</code></pre>

Updates metrics with one step responses.

<h3 id="write_metrics"><code>write_metrics</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/simulator/recsim_gym.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>write_metrics(
    add_summary_fn
)
</code></pre>

Writes metrics to TensorBoard by calling add_summary_fn.

<h3 id="__enter__"><code>__enter__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__enter__()
</code></pre>

<h3 id="__exit__"><code>__exit__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__exit__(
    *args
)
</code></pre>

## Class Variables

*   `metadata` <a id="metadata"></a>
*   `reward_range` <a id="reward_range"></a>
*   `spec = None` <a id="spec"></a>
