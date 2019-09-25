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
"""Tests for recsim.utils."""

import collections
import numpy as np
from recsim import utils
import tensorflow as tf


class UtilsTest(tf.test.TestCase):

  def test_aggregate_video_cluster_metrics(self):
    metrics = collections.defaultdict(float)
    metrics['impression'] = 10
    metrics['cluster_watch_count_cluster_0'] = 1
    metrics['cluster_watch_count_no_click'] = 9
    metrics['quality'] = 0.7
    metrics['click'] = 1
    responses = ({
        'click': 1,
        'quality': np.array(0.5),
        'cluster_id': np.array(1)
    }, {
        'click': 0,
        'quality': np.array(0.8),
        'cluster_id': np.array(2)
    })
    metrics = utils.aggregate_video_cluster_metrics(responses, metrics)
    self.assertEqual(
        metrics, {
            'impression': 11.0,
            'cluster_watch_count_cluster_0': 1.0,
            'cluster_watch_count_cluster_1': 1.0,
            'cluster_watch_count_no_click': 9.0,
            'quality': 1.2,
            'click': 2.0
        })


if __name__ == '__main__':
  tf.test.main()
