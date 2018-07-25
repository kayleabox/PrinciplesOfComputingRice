import unittest

from cv_tictactoe_board import switch_player

from cv_tictactoe_board import TicTacToeBoard

from cv_tictactoe_board import PLAYERO
from cv_tictactoe_board import PLAYERX

from monte_carlo_tictactoe import mc_move
from monte_carlo_tictactoe import mc_trial
from monte_carlo_tictactoe import mc_update_scores
from monte_carlo_tictactoe import get_best_move
from monte_carlo_tictactoe import get_score_values

class TrialTest(unittest.TestCase):
  def test(self):
    board = TicTacToeBoard(3, False, None)
    #original_state = board.board[:]
    #original_state = list(board.board)
    #original_state = [row for row in board.board]
    original_state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    self.assertEqual(board.board, original_state)

    #print id(original_state) #these have different ids for all of the cases :( I don't understand why original_state is changing
    #print id(board.board)
    mc_trial(board, PLAYERX)
    self.assertNotEqual(board.board, original_state)
    self.assertNotEqual(board.check_win(), None)

class UpdateScoresTest(unittest.TestCase):
  def test(self):
    scores = [[3, -3, 5], [-2, 7, 0], [4, -1, 3]]
    board = TicTacToeBoard(3, False, None)
    board.board = [[0, 2, 1], [0, 1, 2], [1, 2, 1]]
    mc_update_scores(scores, board, PLAYERX)

    self.assertEqual(scores, [[3, -4, 6], [-2, 8, -1], [5, -2, 4]])
    
    scores = [[4, -3, 5], [-2, 7, -3], [4, -1, 3]]
    board = TicTacToeBoard(3, False, None)
    board.board = [[2, 2, 1], [2, 1, 2], [2, 1, 1]]
    mc_update_scores(scores, board, PLAYERO)

    self.assertEqual(scores, [[5, -2, 4], [-1, 6, -2], [5, -2, 2]])


class GetScoreValuesTest(unittest.TestCase):
  def test(self):
    board = TicTacToeBoard(3, False, None)
    board.board = [[2, 2, 1], [2, 1, 2], [2, 1, 1]]

    self.assertEqual(get_score_values(board, PLAYERO), (1, -1))
    self.assertEqual(get_score_values(board, PLAYERX), (-1, 1))

class BestMoveTest(unittest.TestCase):
  def test(self):
    scores = [[3, -3, 5], [-2, 7, 0], [4, -1, 3]]
    board = TicTacToeBoard(3, False, None)
    board.board = [[0, 2, 1], [0, 1, 2], [1, 2, 1]]

    self.assertEqual(get_best_move(board,scores), (0,0))

    board.board = [[0, 2, 1], [0, 0, 2], [1, 2, 1]]

    self.assertEqual(get_best_move(board,scores), (1,1))

    board.board = [[2, 0, 1], [2, 1, 2], [1, 0, 1]]

    self.assertEqual(get_best_move(board,scores), (2,1))

    board.board = [[0, 2, 1], [0, 1, 2], [1, 0, 0]]

    self.assertIn(get_best_move(board,scores), ((0,0), (2,2)))

    board.board = [[1, 2, 1], [2, 1, 2], [1, 2, 1]]

    self.assertEqual(get_best_move(board,scores), None)

    scores =  [[1, 2, 3], [7, 8, 9], [4, 5, 6]]
    board.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    self.assertEqual(get_best_move(board,scores), (1, 2))

class MoveTest(unittest.TestCase):
  """
  This function takes a current board, which player the machine
  player is, and the number of trials to run. The function
  should use the Monte Carlo simulation described above to return 
  a move for the machine player in the form of a (row,column) tuple.
  Be sure to use the other functions you have written!
  """
  def test(self):
    board = TicTacToeBoard(3, False, None)

    index_grid = [[(row, col) for col in range(board.dimension)] for row in range(board.dimension)]
    index_list = []
    for l_list in index_grid:
      index_list += l_list

    self.assertIsInstance(mc_move(board, PLAYERO, 30), tuple)
    self.assertIn(mc_move(board, PLAYERO, 30), index_list)