import unittest

from merge import get_new_value
from merge import merge
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
    self.assertEqual(try_merge([8,8]), [16])
    self.assertEqual(try_merge([2,4]), [2, 4])
    self.assertEqual(try_merge([2, 2, 4, 8]), [4, 4, 8])

class GetNewValueMergeTest(unittest.TestCase):
  def test(self):
    self.assertEqual(get_new_value([8, 8], 0, 8), 16)
    self.assertEqual(get_new_value([8, 8], 1, 8), 8)
    self.assertEqual(get_new_value([4, 2, 2, 8,8], 1, 2), 4)
    self.assertEqual(get_new_value([4, 2, 2, 8,8], 2, 2), 2)
