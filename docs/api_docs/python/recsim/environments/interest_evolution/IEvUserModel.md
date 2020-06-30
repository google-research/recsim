<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.interest_evolution.IEvUserModel" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_observation"/>
<meta itemprop="property" content="get_response_model_ctor"/>
<meta itemprop="property" content="is_terminal"/>
<meta itemprop="property" content="observation_space"/>
<meta itemprop="property" content="reset"/>
<meta itemprop="property" content="reset_sampler"/>
<meta itemprop="property" content="response_space"/>
<meta itemprop="property" content="simulate_response"/>
<meta itemprop="property" content="update_state"/>
</div>

# recsim.environments.interest_evolution.IEvUserModel

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_evolution.py">View
source</a>

Class to model an interest evolution user.

Inherits From: [`AbstractUserModel`](../../../recsim/user/AbstractUserModel.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.environments.interest_evolution.IEvUserModel(
    slate_size, choice_model_ctor=None,
    response_model_ctor=recsim.environments.interest_evolution.IEvResponse,
    user_state_ctor=recsim.environments.interest_evolution.IEvUserState,
    no_click_mass=1.0, seed=0, alpha_x_intercept=1.0, alpha_y_intercept=0.3
)
</code></pre>

<!-- Placeholder for "Used in" -->

Assumes the user state contains: - user_interests - time_budget - no_click_mass

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`slate_size`
</td>
<td>
An integer representing the size of the slate
</td>
</tr><tr>
<td>
`choice_model_ctor`
</td>
<td>
A contructor function to create user choice model.
</td>
</tr><tr>
<td>
`response_model_ctor`
</td>
<td>
A constructor function to create response. The
function should take a string of doc ID as input and returns a
IEvResponse object.
</td>
</tr><tr>
<td>
`user_state_ctor`
</td>
<td>
A constructor to create user state
</td>
</tr><tr>
<td>
`no_click_mass`
</td>
<td>
A float that will be passed to compute probability of no
click.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
A integer used as the seed of the choice model.
</td>
</tr><tr>
<td>
`alpha_x_intercept`
</td>
<td>
A float for the x intercept of the line used to compute
interests update factor.
</td>
</tr><tr>
<td>
`alpha_y_intercept`
</td>
<td>
A float for the y intercept of the line used to compute
interests update factor.
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`Exception`
</td>
<td>
if choice_model_ctor is not specified.
</td>
</tr>
</table>

## Methods

<h3 id="create_observation"><code>create_observation</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/user.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>create_observation()
</code></pre>

Emits obesrvation about user's state.

<h3 id="get_response_model_ctor"><code>get_response_model_ctor</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/user.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_response_model_ctor()
</code></pre>

Returns a constructor for the type of response this model will create.

<h3 id="is_terminal"><code>is_terminal</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_evolution.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>is_terminal()
</code></pre>

Returns a boolean indicating if the session is over.

<h3 id="observation_space"><code>observation_space</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/user.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>observation_space()
</code></pre>

A Gym.spaces object that describes possible user observations.

<h3 id="reset"><code>reset</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/user.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset()
</code></pre>

Resets the user.

<h3 id="reset_sampler"><code>reset_sampler</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/user.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset_sampler()
</code></pre>

Resets the sampler.

<h3 id="response_space"><code>response_space</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/user.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>response_space()
</code></pre>

<h3 id="simulate_response"><code>simulate_response</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_evolution.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>simulate_response(
    documents
)
</code></pre>

Simulates the user's response to a slate of documents with choice model.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`documents`
</td>
<td>
a list of IEvVideo objects
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`responses`
</td>
<td>
a list of IEvResponse objects, one for each document
</td>
</tr>
</table>

<h3 id="update_state"><code>update_state</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_evolution.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>update_state(
    slate_documents, responses
)
</code></pre>

Updates the user state based on responses to the slate.

This function assumes only 1 response per slate. If a video is watched, we
update the user's interests some small step size alpha based on the user's
interest in that topic. The update is either towards the video's features or
away, and is determined stochastically by the user's interest in that document.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`slate_documents`
</td>
<td>
a list of IEvVideos representing the slate
</td>
</tr><tr>
<td>
`responses`
</td>
<td>
a list of IEvResponses representing the user's response to each
video in the slate.
</td>
</tr>
</table>
