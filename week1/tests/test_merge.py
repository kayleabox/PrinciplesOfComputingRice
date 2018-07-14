import unittest

from merge import append_to_line_if_not_merged
from merge import merge
from merge import merge_if_not_merged_with_previous
from merge import try_merge

class MergeTest1(unittest.TestCase):
  def test(self):
    self.assertEqual(merge([2, 4, 4, 8, 8, 8, 2, 2, 4, 8, 2, 2, 2, 4, 4]),
      [2, 8, 16, 8, 4, 4, 8, 4, 2, 8, 0, 0, 0, 0, 0])

class MergeTest2(unittest.TestCase):
  def test(self):
    self.assertEqual(merge(merge([2, 4, 4, 8, 8, 8, 2, 2, 4, 8, 2, 2, 2, 4, 4])),
      [2, 8, 16, 8, 8, 8, 4, 2, 8, 0, 0, 0, 0, 0, 0])

class MergeTest3(unittest.TestCase):
  def test(self):
    self.assertEqual(merge(merge(merge([2, 4, 4, 8, 8, 8, 2, 2, 4, 8, 2, 2, 2, 4, 4]))),
      [2, 8, 16, 16, 8, 4, 2, 8, 0, 0, 0, 0, 0, 0, 0])

class MergeTest4(unittest.TestCase):
  def test(self):
    self.assertEqual(merge(merge(merge(merge([2, 4, 4, 8, 8, 8, 2, 2, 4, 8, 2, 2, 2, 4, 4])))),
      [2, 8, 32, 8, 4, 2, 8, 0, 0, 0, 0, 0, 0, 0, 0])
    self.assertEqual(merge(merge(merge(merge(merge([2, 4, 4, 8, 8, 8, 2, 2, 4, 8, 2, 2, 2, 4, 4]))))),
      [2, 8, 32, 8, 4, 2, 8, 0, 0, 0, 0, 0, 0, 0, 0])

class MergeTest5(unittest.TestCase):
  def test(self):
    self.assertEqual(merge([2, 4, 8]), [2, 4, 8])

class MergeTest6(unittest.TestCase):
  def test(self):
    self.assertEqual(merge([2, 2, 2, 2, 2, 2]), [4, 4, 4, 0, 0, 0])

class MergeTest7(unittest.TestCase):
  def test(self):
    self.assertEqual(merge(merge([2, 2, 2, 2, 2, 2])), [8, 4, 0, 0, 0, 0])

class MergeTest8(unittest.TestCase):
  def test(self):
    new_array = merge(merge([2, 2, 2, 2, 2, 2]))
    new_array.append(4)
    self.assertEqual(merge(new_array), [8, 8, 0, 0, 0, 0, 0])

class MergeTest9(unittest.TestCase):
  def test(self):
    self.assertEqual(merge([8,8]), [16, 0])
    self.assertEqual(merge([2,0]), [2, 0])
    self.assertEqual(merge([0,2]), [2, 0])

class TryMergeTest(unittest.TestCase):
  def test(self):
    merged_line = []
    try_merge([8,8], merged_line)
    self.assertEqual(merged_line, [16])
    merged_line = []
    try_merge([2,4], merged_line)
    self.assertEqual(merged_line, [2, 4])
    merged_line = []
    try_merge([2, 2, 4, 8], merged_line)
    self.assertEqual(merged_line, [4, 4, 8])


class MergeIfNotMergedTest(unittest.TestCase):
  def test(self):
    merged_with_previous = True
    merged_line = [4]
    line_without_zeros = [4, 4, 8]
    merged_with_previous = merge_if_not_merged_with_previous(merged_with_previous, merged_line, line_without_zeros, 0)
    self.assertEqual(merged_with_previous, False)
    merged_with_previous = merge_if_not_merged_with_previous(merged_with_previous, merged_line, line_without_zeros, 0)
    self.assertEqual(merged_with_previous, True)


class AppendIfNotMergedTest(unittest.TestCase):
  def test(self):
    merged_with_previous = True
    merged_line = [4]
    line_without_zeros = [4, 4, 8]
    merged_with_previous = append_to_line_if_not_merged(merged_with_previous, merged_line, line_without_zeros, 0)
    self.assertEqual(merged_with_previous, False)
    self.assertEqual(merged_line, [4])
    merged_with_previous = append_to_line_if_not_merged(merged_with_previous, merged_line, line_without_zeros, 2)
    self.assertEqual(merged_with_previous, False)
    self.assertEqual(merged_line, [4, 8])