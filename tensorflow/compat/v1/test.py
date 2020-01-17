import numpy as np
import numpy.testing as npt
import unittest
from unittest import main

class TestCase(unittest.TestCase):
  def assertAllClose(self, actual, desired, *args, **kwargs):
    npt.assert_allclose(actual, desired, *args, **kwargs)

  def assertAllEqual(self, x, y):
    npt.assert_array_equal(x, y)

  def assertLen(self, container, expected_len):
    self.assertEqual(len(container), expected_len)

  def assertAllInSet(self, target, expected_set):
    # Elements in target that are not in expected_set.
    if not isinstance(target, np.ndarray):
      target = np.array(target)
    diff = np.setdiff1d(target.flatten(), list(expected_set))
    if np.size(diff):
      raise AssertionError("%d unique element(s) are not in the set %s: %s" %
                           (np.size(diff), expected_set, diff))

  def assertEmpty(self, container):
    self.assertEqual(len(container), 0)
