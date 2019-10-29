# coding=utf-8
# coding=utf-8
# Copyright 2019 The RecSim Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Utility functions for RecSim environment."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def aggregate_video_cluster_metrics(responses, metrics, info=None):
  """Aggregates the video cluster metrics with one step responses.

  Args:
    responses: a dictionary of names, observed responses.
    metrics: A dictionary mapping from metric_name to its value in float.
    info: Additional info for computing metrics (ignored here)

  Returns:
    A dictionary storing metrics after aggregation.
  """
  del info  # Unused.
  is_clicked = False
  metrics['impression'] += 1

  for response in responses:
    if not response['click']:
      continue
    is_clicked = True
    metrics['click'] += 1
    metrics['quality'] += response['quality']
    cluster_id = response['cluster_id']
    metrics['cluster_watch_count_cluster_%d' % cluster_id] += 1

  if not is_clicked:
    metrics['cluster_watch_count_no_click'] += 1
  return metrics


def write_video_cluster_metrics(metrics, add_summary_fn):
  """Writes average video cluster metrics using add_summary_fn."""
  add_summary_fn('CTR', metrics['click'] / metrics['impression'])
  if metrics['click'] > 0:
    add_summary_fn('AverageQuality', metrics['quality'] / metrics['click'])
  for k in metrics:
    prefix = 'cluster_watch_count_cluster_'
    if k.startswith(prefix):
      add_summary_fn('cluster_watch_count_frac/cluster_%s' % k[len(prefix):],
                     metrics[k] / metrics['impression'])
  add_summary_fn(
      'cluster_watch_count_frac/no_click',
      metrics['cluster_watch_count_no_click'] / metrics['impression'])
