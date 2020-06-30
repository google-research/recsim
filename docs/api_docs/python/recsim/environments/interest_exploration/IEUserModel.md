<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.environments.interest_exploration.IEUserModel" />
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

# recsim.environments.interest_exploration.IEUserModel

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_exploration.py">View
source</a>

Class to model a user.

Inherits From: [`AbstractUserModel`](../../../recsim/user/AbstractUserModel.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.environments.interest_exploration.IEUserModel(
    slate_size, no_click_mass=5,
    choice_model_ctor=recsim.choice_model.MultinomialLogitChoiceModel,
    user_state_ctor=None, response_model_ctor=None, seed=0
)
</code></pre>

<!-- Placeholder for "Used in" -->

The user in this scenario is completely characterized by a vector g of affinity
scores of dimension |D| (the number of document topics). When presented with a
slate of documents, the user scores each document as g(d) + f(d), where f(d) is
the document's quality score, and then chooses according to a choice model based
on these scores.

The state space consists of a vector of affinity scores which is unique to the
user and static but not observable.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

</table>

slate_size: An integer representing the size of the slate. no_click_mass: A
float indicating the mass given to a no-click option. choice_model_ctor: A
contructor function to create user choice model. user_state_ctor: A constructor
to create user state. response_model_ctor: A constructor function to create
response. The function should take a string of doc ID as input and returns a
IEResponse object. seed: an integer used as the seed in random sampling.

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

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`avg_user_state`
</td>
<td>
Returns the prior of user state.
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

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_exploration.py">View
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

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_exploration.py">View
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
a list of IEDocument objects in the slate.
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
a list of IEResponse objects, one for each document.
</td>
</tr>
</table>

<h3 id="update_state"><code>update_state</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/environments/interest_exploration.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>update_state(
    slate_documents, responses
)
</code></pre>

Updates the user's state based on the slate and document selected.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`slate_documents`
</td>
<td>
A list of AbstractDocuments for items in the slate.
</td>
</tr><tr>
<td>
`responses`
</td>
<td>
A list of AbstractResponses for each item in the slate.
</td>
</tr>
</table>

Updates: The user's hidden state.
