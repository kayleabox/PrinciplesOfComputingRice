import unittest

from game_template import TwentyFortyEight

class InitTwentyFortyEightTest(unittest.TestCase):
  def test(self):
    twenty_forty_eight = TwentyFortyEight()
    self.assertEqual(twenty_forty_eight._grid_height, 4)
    self.assertEqual(twenty_forty_eight._grid_width, 4)

    twenty_forty_eight = TwentyFortyEight(4, 5)
    self.assertEqual(twenty_forty_eight._grid_height, 4)
    self.assertEqual(twenty_forty_eight._grid_width, 5)

class SetMoveGridIndexesTwentyFortyEightTest(unittest.TestCase):
  def test(self):
    twenty_forty_eight = TwentyFortyEight()
    move_grid_indices = twenty_forty_eight.get_move_grid_indices()
    self.assertEqual(move_grid_indices[1], [(0,0), (0, 1), (0, 2), (0, 3)])
    self.assertEqual(move_grid_indices[2], [(3,0), (3, 1), (3, 2), (3, 3)])
    self.assertEqual(move_grid_indices[4], [(0,3), (1, 3), (2, 3), (3, 3)])
    self.assertEqual(move_grid_indices[3], [(0,0), (1, 0), (2, 0), (3, 0)])

class GenerateEmptyGridTwentyFortyEightTest1(unittest.TestCase):
  def test(self):
    twenty_forty_eight = TwentyFortyEight(2, 3)
    self.assertEqual(twenty_forty_eight.generate_empty_grid(), [[0, 0, 0 ], [0, 0, 0]])

class GenerateEmptyGridTwentyFortyEightTest2(unittest.TestCase):
  def test(self):
    twenty_forty_eight = TwentyFortyEight(6, 4)
    self.assertEqual(twenty_forty_eight.generate_empty_grid(), [[0, 0, 0, 0], [0, 0, 0, 0], 
                                                                [0, 0, 0, 0], [0, 0, 0, 0], 
                                                                [0, 0, 0, 0], [0, 0, 0, 0]])

class StrTwentyFortyEightTest1(unittest.TestCase):
  def test(self):
    twenty_forty_eight = TwentyFortyEight(6, 4)
    empty_grid = twenty_forty_eight.generate_empty_grid()
    twenty_forty_eight.set_grid(empty_grid)
    self.assertEqual(twenty_forty_eight.__str__(), 
    '[[0, 0, 0, 0],\n [0, 0, 0, 0],\n [0, 0, 0, 0],\n [0, 0, 0, 0],\n [0, 0, 0, 0],\n [0, 0, 0, 0]]')

twenty_forty_eight = TwentyFortyEight(6, 4)
empty_grid = twenty_forty_eight.generate_empty_grid()
twenty_forty_eight.set_grid(empty_grid)
class SelectTileIndexTwentyFortyEightTest1(unittest.TestCase):
  def test(self):
    self.assertIsInstance(twenty_forty_eight.select_tile(), tuple)
    row, col = twenty_forty_eight.select_tile()
    self.assertEquals(0 <= row < 6, True)
    self.assertEquals(0 <= col < 4, True)

class SetTileTwentyFortyEightTest1(unittest.TestCase):
  def test(self):
    twenty_forty_eight.set_tile(0, 2, 2)
    self.assertEqual(twenty_forty_eight._grid[0][2], 2)
    self.assertEqual(twenty_forty_eight.get_tile(0, 2), 2)
    self.assertEqual(twenty_forty_eight.get_tile(0, 2), twenty_forty_eight._grid[0][2])

    twenty_forty_eight.set_tile(4, 3, 4)
    self.assertEqual(twenty_forty_eight._grid[4][3], 4)
    self.assertEqual(twenty_forty_eight.get_tile(4, 3), 4)
    self.assertEqual(twenty_forty_eight.get_tile(4, 3), twenty_forty_eight._grid[4][3])

    twenty_forty_eight.set_tile(5, 0, 2)
    self.assertEqual(twenty_forty_eight._grid[5][0], 2)
    self.assertEqual(twenty_forty_eight.get_tile(5, 0), 2)
    self.assertEqual(twenty_forty_eight.get_tile(5, 0), twenty_forty_eight._grid[5][0])

    self.assertEqual(twenty_forty_eight.__str__(), 
    '[[0, 0, 2, 0],\n [0, 0, 0, 0],\n [0, 0, 0, 0],\n [0, 0, 0, 0],\n [0, 0, 0, 4],\n [2, 0, 0, 0]]')  

class CheckTileIsEmptyTileTwentyFortyEightTest1(unittest.TestCase):
  def test(self):
    twenty_forty_eight = TwentyFortyEight()
    empty_grid = twenty_forty_eight.generate_empty_grid()
    twenty_forty_eight.set_grid(empty_grid)
    twenty_forty_eight.set_tile(0, 2, 2)

    self.assertEqual(twenty_forty_eight.check_tile_is_empty(0, 2), False)
    self.assertEqual(twenty_forty_eight.check_tile_is_empty(0, 0), True)

class GetEmptyTileTwentyFortyEightTest1(unittest.TestCase):
  def check_get_empty_tile(self, twenty_forty_eight):
    row, col = twenty_forty_eight.get_empty_tile(
      twenty_forty_eight.get_random_row_index(),
      twenty_forty_eight.get_random_col_index()
    )
    self.assertEqual(twenty_forty_eight.get_tile(row, col), 0)
    self.assertNotEqual((row, col), (0, 2))
    self.assertNotEqual((row, col), (0, 3))
    self.assertNotEqual((row, col), (1, 2))

  def test(self):
    twenty_forty_eight = TwentyFortyEight()
    empty_grid = twenty_forty_eight.generate_empty_grid()
    twenty_forty_eight.set_grid(empty_grid)
    twenty_forty_eight.set_tile(0, 2, 2)
    twenty_forty_eight.set_tile(0, 3, 4)
    twenty_forty_eight.set_tile(1, 2, 2)

    [self.check_get_empty_tile(twenty_forty_eight) for dummy_num in range(5)]

class GetRandomRowWidthTwentyFortyEightTest1(unittest.TestCase):
  def test(self):
    twenty_forty_eight = TwentyFortyEight()
    empty_grid = twenty_forty_eight.generate_empty_grid()
    twenty_forty_eight.set_grid(empty_grid)

    self.assertEqual( 
      0 <= twenty_forty_eight.get_random_row_index() < twenty_forty_eight.get_grid_height(),
      True
    )
    self.assertEqual( 
      0 <= twenty_forty_eight.get_random_col_index() < twenty_forty_eight.get_grid_width(),
      True
    )


def tiles_greater_zero(grid):
  return sum(col > 0 for row in grid for col in row)

def sum_of_tiles(grid):
  return sum(col for row in grid for col in row)

class NewTileTwentyFortyEightTest1(unittest.TestCase):
  def test(self):
    twenty_forty_eight = TwentyFortyEight(6, 4)
    empty_grid = twenty_forty_eight.generate_empty_grid()
    twenty_forty_eight.set_grid(empty_grid)
    twenty_forty_eight.new_tile()
    self.assertEquals(tiles_greater_zero(twenty_forty_eight._grid), 1)
    self.assertEquals(sum_of_tiles(twenty_forty_eight._grid) > 0, True)

    twenty_forty_eight = TwentyFortyEight()
    empty_grid = twenty_forty_eight.generate_empty_grid()
    twenty_forty_eight.set_grid(empty_grid)
    twenty_forty_eight.new_tile()
    [twenty_forty_eight.new_tile() for dummy_num in range(9)]
    self.assertEquals(tiles_greater_zero(twenty_forty_eight._grid), 10)
    self.assertEquals(sum_of_tiles(twenty_forty_eight._grid) > 0, True)

class ResetTwentyFortyEightTest1(unittest.TestCase):
  def tiles_greater_zero(self, grid):
    return sum(col > 0 for row in grid for col in row)

  def sum_of_tiles(self, grid):
    return sum(col for row in grid for col in row)

  def test(self):
    twenty_forty_eight = TwentyFortyEight(6, 4)
    twenty_forty_eight.reset()
    self.assertEquals(self.tiles_greater_zero(twenty_forty_eight._grid), 2)
    self.assertEquals(self.sum_of_tiles(twenty_forty_eight._grid) > 0, True)

    twenty_forty_eight = TwentyFortyEight(7, 18)
    twenty_forty_eight.reset()
    self.assertEquals(self.tiles_greater_zero(twenty_forty_eight._grid), 2)
    self.assertEquals(self.sum_of_tiles(twenty_forty_eight._grid) > 0, True)

class MoveTilesTwentyFortyEightTest1(unittest.TestCase):
  def set_up_game(self, game, direction):
    game.set_grid([[0, 2, 2],
                   [0, 0, 0],
                   [0, 0, 2],
                   [0, 0, 2]])
    game.move(direction)

  def test(self):
    game = TwentyFortyEight(4, 3)
    self.set_up_game(game, 1) # UP
    self.assertEqual(game.get_grid(), [[0, 2, 4],
                                       [0, 0, 2],
                                       [0, 0, 0],
                                       [0, 0, 0]])

    self.set_up_game(game, 2) # DOWN
    self.assertEqual(game.get_grid(), [[0, 0, 0],
                                       [0, 0, 0],
                                       [0, 0, 2],
                                       [0, 2, 4]])

    self.set_up_game(game, 3) # LEFT
    self.assertEqual(game.get_grid(), [[4, 0, 0],
                                       [0, 0, 0],
                                       [2, 0, 0],
                                       [2, 0, 0]])

    self.set_up_game(game, 4) #RIGHT
    self.assertEqual(game.get_grid(), [[0, 0, 4],
                                       [0, 0, 0],
                                       [0, 0, 2],
                                       [0, 0, 2]])                                   
