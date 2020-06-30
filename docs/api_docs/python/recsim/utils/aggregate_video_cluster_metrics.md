<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.utils.aggregate_video_cluster_metrics" />
<meta itemprop="path" content="Stable" />
</div>

# recsim.utils.aggregate_video_cluster_metrics

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">

</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/utils.py">View
source</a>

Aggregates the video cluster metrics with one step responses.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recsim.utils.aggregate_video_cluster_metrics(
    responses, metrics, info=None
)
</code></pre>

<!-- Placeholder for "Used in" -->

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`responses`
</td>
<td>
a dictionary of names, observed responses.
</td>
</tr><tr>
<td>
`metrics`
</td>
<td>
A dictionary mapping from metric_name to its value in float.
</td>
</tr><tr>
<td>
`info`
</td>
<td>
Additional info for computing metrics (ignored here)
</td>
</tr>
</table>

<!-- Tabular view -->

 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A dictionary storing metrics after aggregation.
</td>
</tr>

</table>
