import unittest

from cv_tictactoe_board import (DRAW, EMPTY, PLAYERO, PLAYERX,
                                switch_player, TicTacToeBoard)

class SwitchPlayerTest(unittest.TestCase):
  def test(self):
    self.assertEqual(switch_player(PLAYERO), PLAYERX)
    self.assertEqual(switch_player(PLAYERX), PLAYERO)

class TicTacToeBoardStrTest1(unittest.TestCase):
  def test(self):
    tictactoe_board = TicTacToeBoard(3, False, None)
    self.assertEqual(tictactoe_board.__str__(), "   |   |  \n-----------\n   |   |  \n-----------\n   |   |  ")

class TicTacToeBoardTest1(unittest.TestCase):
  def test(self):
    tictactoe_board = TicTacToeBoard(3, False, None)
    self.assertEqual(tictactoe_board.board, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    tictactoe_board = TicTacToeBoard(5, False, None)
    self.assertEqual(tictactoe_board.board, [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

class TicTacToeBoardGetDimTest(unittest.TestCase):
  def test(self):
    board = TicTacToeBoard(5, False, None)
    self.assertEqual(board.get_dim(), 5)

class TicTacToeBoardCloneTest(unittest.TestCase):
  def test(self):
    board = TicTacToeBoard(5, False, None)
    clone = board.clone()
    self.assertNotEqual(clone, board)

class TicTacToeBoardNewBoardTest1(unittest.TestCase):
  def test(self):
    tictactoe_board = TicTacToeBoard(5, False, None)
    tictactoe_board.dimension = 3
    new_board = tictactoe_board.new_board()
    self.assertEqual(new_board, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

class TicTacToeBoardSquareTest1(unittest.TestCase):
  def test(self):
    tictactoe_board = TicTacToeBoard(4, False, None)
    tictactoe_board.board[0][0] = 1
    tictactoe_board.board[1][2] = 2

    self.assertEqual(tictactoe_board.square(0, 0), PLAYERX)
    self.assertEqual(tictactoe_board.square(1, 2), PLAYERO)
    self.assertEqual(tictactoe_board.square(0, 1), EMPTY)

class TicTacToeBoardGetEmptySquaresTest1(unittest.TestCase):
  def test(self):
    tictactoe_board = TicTacToeBoard(2, False, None)

    self.assertEqual(tictactoe_board.get_empty_squares(), [(0, 0), (0, 1), (1, 0), (1, 1)])

    tictactoe_board = TicTacToeBoard(4, False, None)
    tictactoe_board.board[0][0] = 1
    tictactoe_board.board[1][2] = 2
    tictactoe_board.board[2][1] = 1

    self.assertEqual(tictactoe_board.get_empty_squares(), [(0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 3), (2, 0), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)])

    tictactoe_board.board[1][3] = 2
    tictactoe_board.board[3][0] = 2
    tictactoe_board.board[2][3] = 1

    self.assertEqual(tictactoe_board.get_empty_squares(), [(0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (2, 0), (2, 2), (3, 1), (3, 2), (3, 3)])

class TicTacToeBoardMoveTest1(unittest.TestCase):
  def test(self):
    tictactoe_board = TicTacToeBoard(4, False, None)
    tictactoe_board.move(0, 0, PLAYERX)
    tictactoe_board.move(3, 0, PLAYERX)
    tictactoe_board.move(1, 2, PLAYERO)
    tictactoe_board.move(1, 3, PLAYERO)
    tictactoe_board.move(1, 3, PLAYERX)

    self.assertEqual(tictactoe_board.square(0, 0), PLAYERX)
    self.assertEqual(tictactoe_board.square(3, 0), PLAYERX)
    self.assertEqual(tictactoe_board.square(1, 2), PLAYERO)
    self.assertEqual(tictactoe_board.square(1, 3), PLAYERO)

class TicTacToeBoardDiagonalGridTest1(unittest.TestCase):
  def test(self):
    tictactoe_board = TicTacToeBoard(4, False, None)
    tictactoe_board.board[0][0] = 1
    tictactoe_board.board[1][2] = 2
    tictactoe_board.board[0][1] = 1
    tictactoe_board.board[2][2] = 2
    tictactoe_board.board[3][1] = 1
    tictactoe_board.board[2][3] = 2

    self.assertEqual(tictactoe_board.uleft_bright(), [1, 0, 2, 0])
    self.assertEqual(tictactoe_board.bleft_uright(), [0, 0, 2, 0])

class TicTacToeBoardColumnGridTest1(unittest.TestCase):
  def test(self):
    tictactoe_board = TicTacToeBoard(4, False, None)
    tictactoe_board.board[0][0] = 1
    tictactoe_board.board[1][2] = 2
    tictactoe_board.board[0][1] = 1
    tictactoe_board.board[2][2] = 2
    tictactoe_board.board[3][1] = 1
    tictactoe_board.board[2][3] = 2

    self.assertEqual(tictactoe_board.column_grid(), [[1, 0, 0, 0], [1, 0, 0, 1], [0, 2, 2, 0], [0, 0, 2, 0]])

class TicTacToeBoardCheckGridTest1(unittest.TestCase):
  def test(self):
    tictactoe_board = TicTacToeBoard(4, False, None)
    tictactoe_board.board[0][0] = 1
    tictactoe_board.board[1][2] = 2
    tictactoe_board.board[0][1] = 1
    
    column_grid = tictactoe_board.column_grid()
    row_grid = tictactoe_board.board

    self.assertEqual(tictactoe_board.evaluate_grid_win(column_grid), [])
    self.assertEqual(tictactoe_board.evaluate_grid_win(row_grid), [])

    tictactoe_board.board[1][1] = 1
    tictactoe_board.board[2][1] = 1
    tictactoe_board.board[2][2] = 2
    tictactoe_board.board[3][1] = 1
    tictactoe_board.board[2][3] = 2

    column_grid = tictactoe_board.column_grid()

    self.assertEqual(tictactoe_board.evaluate_grid_win(column_grid), [PLAYERX])

    tictactoe_board.board[2][1] = 2
    tictactoe_board.board[2][0] = 2

    row_grid = tictactoe_board.board

    self.assertEqual(tictactoe_board.evaluate_grid_win(row_grid), [PLAYERO])

class TicTacToeBoardCheckDiagonalTest1(unittest.TestCase):
  def test(self):
    tictactoe_board = TicTacToeBoard(4, False, None)
    tictactoe_board.board[0][0] = 1
    tictactoe_board.board[1][2] = 2
    tictactoe_board.board[0][1] = 1
  
    uleft_bright = tictactoe_board.uleft_bright()
    bleft_uright = tictactoe_board.bleft_uright()

    self.assertEqual(tictactoe_board.evaluate_diagonal_win(uleft_bright), [])
    self.assertEqual(tictactoe_board.evaluate_diagonal_win(bleft_uright), [])

    tictactoe_board.board[1][1] = 1
    tictactoe_board.board[2][1] = 1
    tictactoe_board.board[2][2] = 1
    tictactoe_board.board[3][3] = 1

    uleft_bright = tictactoe_board.uleft_bright()

    self.assertEqual(tictactoe_board.evaluate_diagonal_win(uleft_bright), [PLAYERX])

    tictactoe_board.board[2][1] = 2
    tictactoe_board.board[3][0] = 2
    tictactoe_board.board[0][3] = 2

    bleft_uright = tictactoe_board.bleft_uright()

    self.assertEqual(tictactoe_board.evaluate_diagonal_win(bleft_uright), [PLAYERO])

class TicTacToeBoardCheckWinTest1(unittest.TestCase):
  def test(self):
    tictactoe_board = TicTacToeBoard(3, False, None)
    tictactoe_board.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    self.assertEqual(tictactoe_board.evaluate_win_status(), None)


    tictactoe_board.board = [[0, 0, 2],
                             [0, 2, 0],
                             [1, 1, 1]]

    self.assertEqual(tictactoe_board.evaluate_win_status(), PLAYERX)

    tictactoe_board.board = [[2, 0, 2],
                             [2, 1, 0],
                             [2, 1, 1]]

    self.assertEqual(tictactoe_board.evaluate_win_status(), PLAYERO)

    tictactoe_board.board = [[1, 0, 2],
                             [0, 1, 2],
                             [2, 1, 1]]
    
    self.assertEqual(tictactoe_board.evaluate_win_status(), PLAYERX)
    
    tictactoe_board.board = [[0, 0, 2],
                             [0, 2, 0],
                             [2, 1, 1]]
    
    self.assertEqual(tictactoe_board.evaluate_win_status(), PLAYERO)

    tictactoe_board.board = [[1, 1, 2], 
                             [2, 2, 1], 
                             [1, 2, 1]]

    self.assertEqual(tictactoe_board.evaluate_win_status(), DRAW)
