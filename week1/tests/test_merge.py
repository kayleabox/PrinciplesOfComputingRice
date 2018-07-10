import unittest

from merge import merge

class Merge1(unittest.TestCase):
  def test(self):
    self.assertEqual(merge([2, 4, 4, 8, 8, 8, 2, 2, 4, 8, 2, 2, 2, 4, 4]),
      [2, 8, 16, 8, 4, 4, 8, 4, 2, 8, 0, 0, 0, 0, 0])

class Merge2(unittest.TestCase):
  def test(self):
    self.assertEqual(merge(merge([2, 4, 4, 8, 8, 8, 2, 2, 4, 8, 2, 2, 2, 4, 4])),
      [2, 8, 16, 8, 8, 8, 4, 2, 8, 0, 0, 0, 0, 0, 0])

class Merge3(unittest.TestCase):
  def test(self):
    self.assertEqual(merge(merge(merge([2, 4, 4, 8, 8, 8, 2, 2, 4, 8, 2, 2, 2, 4, 4]))),
      [2, 8, 16, 16, 8, 4, 2, 8, 0, 0, 0, 0, 0, 0, 0])

class Merge4(unittest.TestCase):
  def test(self):
    self.assertEqual(merge(merge(merge(merge([2, 4, 4, 8, 8, 8, 2, 2, 4, 8, 2, 2, 2, 4, 4])))),
      [2, 8, 32, 8, 4, 2, 8, 0, 0, 0, 0, 0, 0, 0, 0])
    self.assertEqual(merge(merge(merge(merge(merge([2, 4, 4, 8, 8, 8, 2, 2, 4, 8, 2, 2, 2, 4, 4]))))),
      [2, 8, 32, 8, 4, 2, 8, 0, 0, 0, 0, 0, 0, 0, 0])

class Merge5(unittest.TestCase):
  def test(self):
    self.assertEqual(merge([2, 4, 8]), [2, 4, 8])

class Merge6(unittest.TestCase):
  def test(self):
    self.assertEqual(merge([2, 2, 2, 2, 2, 2]), [4, 4, 4, 0, 0, 0])

class Merge7(unittest.TestCase):
  def test(self):
    self.assertEqual(merge(merge([2, 2, 2, 2, 2, 2])), [8, 4, 0, 0, 0, 0])

class Merge8(unittest.TestCase):
  def test(self):
    new_array = merge(merge([2, 2, 2, 2, 2, 2]))
    new_array.append(4)
    self.assertEqual(merge(new_array), [8, 8, 0, 0, 0, 0, 0])

class Merge9(unittest.TestCase):
  def test(self):
    self.assertEqual(merge([8,8]), [16, 0])
    self.assertEqual(merge([2,0]), [2, 0])
    self.assertEqual(merge([0,2]), [2, 0])