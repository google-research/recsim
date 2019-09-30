<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="recsim.utils.aggregate_video_cluster_metrics" />
<meta itemprop="path" content="Stable" />
</div>

# recsim.utils.aggregate_video_cluster_metrics

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google-research/recsim/tree/master/recsim/utils.py">View
source</a>

Aggregates the video cluster metrics with one step responses.

```python
recsim.utils.aggregate_video_cluster_metrics(
    responses,
    metrics
)
```

<!-- Placeholder for "Used in" -->

#### Args:

*   <b>`responses`</b>: a dictionary of names, observed responses.
*   <b>`metrics`</b>: A dictionary mapping from metric_name to its value in
    float.

#### Returns:

A dictionary storing metrics after aggregation.
