<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.long_term_satisfaction.LTSUserModel" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_observation"/>
<meta itemprop="property" content="generate_response"/>
<meta itemprop="property" content="get_response_model_ctor"/>
<meta itemprop="property" content="is_terminal"/>
<meta itemprop="property" content="observation_space"/>
<meta itemprop="property" content="reset"/>
<meta itemprop="property" content="reset_sampler"/>
<meta itemprop="property" content="response_space"/>
<meta itemprop="property" content="simulate_response"/>
<meta itemprop="property" content="update_state"/>
</div>

# recsim.environments.long_term_satisfaction.LTSUserModel

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/long_term_satisfaction.py">View
source</a>

Class to model a user with long-term satisfaction dynamics.

Inherits From: [`AbstractUserModel`](../../../recsim/user/AbstractUserModel.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.environments.long_term_satisfaction.LTSUserModel(
    slate_size, user_state_ctor=None, response_model_ctor=None, seed=0
)
</code></pre>

<!-- Placeholder for "Used in" -->

Implements a controlled continuous Hidden Markov Model of the user having the
following components. * State space: one dimensional real number, termed
net_positive_exposure (abbreviated NPE); * controls: one dimensional control
signal in [0, 1], representing the clickbait score of the item of content; *
transition dynamics: net_positive_exposure is updated according to: NPE_(t+1) :=
memory_discount * NPE_t + 2 * (clickbait_score - .5) + N(0, innovation_stddev);
* observation space: a nonnegative real number, representing the degree of
engagement, e.g. econds watched from a recommended video. An observation is
drawn from a log-normal distribution with mean

    (clickbait_score * choc_mean
                    + (1 - clickbait_score) * kale_mean) * SAT_t,

    where SAT_t = sigmoid(sensitivity * NPE_t). The observation standard
    standard deviation is similarly given by

    (clickbait_score * choc_stddev + ((1 - clickbait_score) * kale_stddev)).

    An individual user is thus represented by the combination of parameters
    (memory_discount, innovation_stddev, choc_mean, choc_stddev, kale_mean,
    kale_stddev, sensitivity), which are encapsulated in LTSUserState.

Args: slate_size: An integer representing the size of the slate user_state_ctor:
A constructor to create user state. response_model_ctor: A constructor function
to create response. The function should take a string of doc ID as input and
returns a LTSResponse object. seed: an integer as the seed in random sampling.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`response_model_ctor`
</td>
<td>
A class/constructor representing the type of
responses this model will generate.
</td>
</tr><tr>
<td>
`user_sampler`
</td>
<td>
An instance of AbstractUserSampler that can generate
initial user states from an inital state distribution.
</td>
</tr><tr>
<td>
`slate_size`
</td>
<td>
integer number of documents that can be served to the user at
any interaction.
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

<h3 id="generate_response"><code>generate_response</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/long_term_satisfaction.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>generate_response(
    doc, response
)
</code></pre>

Generates a response to a clicked document.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`doc`
</td>
<td>
an LTSDocument object.
</td>
</tr><tr>
<td>
`response`
</td>
<td>
an LTSResponse for the document.
</td>
</tr>
</table>

Updates: response, with whether the document was clicked, liked, and how much of
it was watched.

<h3 id="get_response_model_ctor"><code>get_response_model_ctor</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/user.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_response_model_ctor()
</code></pre>

Returns a constructor for the type of response this model will create.

<h3 id="is_terminal"><code>is_terminal</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/long_term_satisfaction.py">View
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

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/long_term_satisfaction.py">View
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
a list of LTSDocument objects.
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
a list of LTSResponse objects, one for each document.
</td>
</tr>
</table>

<h3 id="update_state"><code>update_state</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/long_term_satisfaction.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>update_state(
    slate_documents, responses
)
</code></pre>

Updates the user's latent state based on responses to the slate.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`slate_documents`
</td>
<td>
a list of LTSDocuments representing the slate
</td>
</tr><tr>
<td>
`responses`
</td>
<td>
a list of LTSResponses representing the user's response to each
document in the slate.
</td>
</tr>
</table>
