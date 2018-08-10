import unittest

from cv_tictactoe_board import (PLAYERO, PLAYERX, switch_player, TicTacToeBoard)
from monte_carlo_tictactoe import (get_best_move, get_score_values,
                                   mc_move, mc_trial, mc_update_scores)

class TrialTest(unittest.TestCase):
  def test(self):
    board = TicTacToeBoard(3, False, None)
    original_state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    self.assertEqual(board.board, original_state)

    mc_trial(board, PLAYERX)
    self.assertNotEqual(board.board, original_state)
    self.assertNotEqual(board.evaluate_win_status(), None)

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

    scores =  [[1, 2, 10], [7, 8, 9], [4, 5, 6]]
    board.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    self.assertEqual(get_best_move(board,scores), (0, 2))

    board2 = TicTacToeBoard(2, False, None)
    scores =  [[1, 2], [7, 8]]
    board2.board = [[0, 0], [0, 0]]

    self.assertEqual(get_best_move(board2,scores), (1, 1))

class MoveTest(unittest.TestCase):
  def test(self):
    board = TicTacToeBoard(3, False, None)

    index_grid = [[(row, col) for col in range(board.dimension)] for row in range(board.dimension)]
    index_list = []
    for l_list in index_grid:
      index_list += l_list

    self.assertIsInstance(mc_move(board, PLAYERO, 30), tuple)
    self.assertIn(mc_move(board, PLAYERO, 30), index_list)