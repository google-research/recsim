<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.simulator.environment.AbstractEnvironment" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="reset"/>
<meta itemprop="property" content="reset_sampler"/>
<meta itemprop="property" content="step"/>
</div>

# recsim.simulator.environment.AbstractEnvironment

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/simulator/environment.py">View
source</a>

Abstract class representing the recommender system environment.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.simulator.environment.AbstractEnvironment(
    user_model, document_sampler, num_candidates, slate_size,
    resample_documents=True
)
</code></pre>

<!-- Placeholder for "Used in" -->
<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`user_model`
</td>
<td>
An instantiation of AbstractUserModel or list of such
instantiations
</td>
</tr><tr>
<td>
`document_sampler`
</td>
<td>
An instantiation of AbstractDocumentSampler
</td>
</tr><tr>
<td>
`num_candidates`
</td>
<td>
An integer representing the size of the candidate_set
</td>
</tr><tr>
<td>
`slate_size`
</td>
<td>
An integer representing the slate size
</td>
</tr><tr>
<td>
`resample_documents`
</td>
<td>
A boolean indicating whether to resample the candidate
set every step
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`user_model`
</td>
<td>
An list or single instantiation of AbstractUserModel
representing the user/users.
</td>
</tr><tr>
<td>
`document_sampler`
</td>
<td>
An instantiation of AbstractDocumentSampler.
</td>
</tr><tr>
<td>
`num_candidates`
</td>
<td>
An integer representing the size of the candidate_set.
</td>
</tr><tr>
<td>
`slate_size`
</td>
<td>
An integer representing the slate size.
</td>
</tr><tr>
<td>
`candidate_set`
</td>
<td>
An instantiation of CandidateSet.
</td>
</tr><tr>
<td>
`num_clusters`
</td>
<td>
An integer representing the number of document clusters.
</td>
</tr>
</table>

## Methods

<h3 id="reset"><code>reset</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/simulator/environment.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>reset()
</code></pre>

Resets the environment and return the first observation.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`user_obs`
</td>
<td>
An array of floats representing observations of the user's
current state
</td>
</tr><tr>
<td>
`doc_obs`
</td>
<td>
An OrderedDict of document observations keyed by document ids
</td>
</tr>
</table>

<h3 id="reset_sampler"><code>reset_sampler</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/simulator/environment.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>reset_sampler()
</code></pre>

Resets the relevant samplers of documents and user/users.

<h3 id="step"><code>step</code></h3>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/simulator/environment.py">View
source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>step(
    slate
)
</code></pre>

Executes the action, returns next state observation and reward.

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`slate`
</td>
<td>
An integer array of size slate_size (or list of such arrays), where
each element is an index into the set of current_documents presented.
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`user_obs`
</td>
<td>
A gym observation representing the user's next state
</td>
</tr><tr>
<td>
`doc_obs`
</td>
<td>
A list of observations of the documents
</td>
</tr><tr>
<td>
`responses`
</td>
<td>
A list of AbstractResponse objects for each item in the slate
</td>
</tr><tr>
<td>
`done`
</td>
<td>
A boolean indicating whether the episode has terminated
</td>
</tr>
</table>
