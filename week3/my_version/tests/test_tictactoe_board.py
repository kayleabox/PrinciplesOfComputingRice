import unittest

from tictactoe_board import (DRAW, EMPTY, PLAYERO, PLAYERX,
                             evaluate_diagonal_win, evaluate_grid_win,
                             switch_player, TicTacToeBoard)

class SwitchPlayerTest(unittest.TestCase):
    def test(self):
        self.assertEqual(switch_player(PLAYERO), PLAYERX)
        self.assertEqual(switch_player(PLAYERX), PLAYERO)

class TicTacToeBoardStrTest(unittest.TestCase):
    def test(self):
        tictactoe_board = TicTacToeBoard(3, False, None)
        self.assertEqual(tictactoe_board.__str__(), "   |   |  \n-----------\n   |   |  \n-----------\n   |   |  ")

class TicTacToeBoardTest(unittest.TestCase):
    def test(self):
        tictactoe_board = TicTacToeBoard(3, False, None)
        self.assertEqual(tictactoe_board.board, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

        tictactoe_board = TicTacToeBoard(5, False, None)
        self.assertEqual(tictactoe_board.board, [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

class TicTacToeBoardCloneTest(unittest.TestCase):
    def test(self):
        board = TicTacToeBoard(5, False, None)
        clone = board.clone()
        self.assertNotEqual(clone, board)

class TicTacToeBoardNewBoardTest(unittest.TestCase):
    def test(self):
        tictactoe_board = TicTacToeBoard(5, False, None)
        tictactoe_board.dimension = 3
        new_board = tictactoe_board.new_board()
        self.assertEqual(new_board, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

class TicTacToeBoardSquareTest(unittest.TestCase):
    def test(self):
        tictactoe_board = TicTacToeBoard(4, False, None)
        tictactoe_board.board[0][0] = 1
        tictactoe_board.board[1][2] = 2

        self.assertEqual(tictactoe_board.square(0, 0), PLAYERX)
        self.assertEqual(tictactoe_board.square(1, 2), PLAYERO)
        self.assertEqual(tictactoe_board.square(0, 1), EMPTY)

class TicTacToeBoardGetEmptySquaresTest(unittest.TestCase):
    def test_empty_board(self):
        tictactoe_board = TicTacToeBoard(2, False, None)

        self.assertEqual(tictactoe_board.get_empty_squares(), [(0, 0), (0, 1), (1, 0), (1, 1)])

    def test_nonempty_board(self):
        tictactoe_board = TicTacToeBoard(4, False, None)
        tictactoe_board.board[0][0] = 1
        tictactoe_board.board[1][2] = 2
        tictactoe_board.board[2][1] = 1

        self.assertEqual(tictactoe_board.get_empty_squares(), [(0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 3), (2, 0), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)])

        tictactoe_board.board[1][3] = 2
        tictactoe_board.board[3][0] = 2
        tictactoe_board.board[2][3] = 1

        self.assertEqual(tictactoe_board.get_empty_squares(), [(0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (2, 0), (2, 2), (3, 1), (3, 2), (3, 3)])

class TicTacToeBoardMoveTest(unittest.TestCase):
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

class TicTacToeBoardDiagonalGridTest(unittest.TestCase):
    def test(self):
        tictactoe_board = TicTacToeBoard(4, False, None)
        tictactoe_board.board[0][0] = 1
        tictactoe_board.board[1][2] = 2
        tictactoe_board.board[0][1] = 1
        tictactoe_board.board[2][2] = 2
        tictactoe_board.board[3][1] = 1
        tictactoe_board.board[2][3] = 2

        self.assertEqual(tictactoe_board.uleft_bright_diagonal(), [1, 0, 2, 0])
        self.assertEqual(tictactoe_board.bleft_uright_diagonal(), [0, 0, 2, 0])

class TicTacToeBoardColumnGridTest(unittest.TestCase):
    def test(self):
        tictactoe_board = TicTacToeBoard(4, False, None)
        tictactoe_board.board[0][0] = 1
        tictactoe_board.board[1][2] = 2
        tictactoe_board.board[0][1] = 1
        tictactoe_board.board[2][2] = 2
        tictactoe_board.board[3][1] = 1
        tictactoe_board.board[2][3] = 2

        self.assertEqual(tictactoe_board.column_grid(), [[1, 0, 0, 0], [1, 0, 0, 1], [0, 2, 2, 0], [0, 0, 2, 0]])

class TicTacToeBoardCheckGridTest(unittest.TestCase):
    def test(self):
        tictactoe_board = TicTacToeBoard(4, False, None)
        tictactoe_board.board[0][0] = 1
        tictactoe_board.board[1][2] = 2
        tictactoe_board.board[0][1] = 1
        
        column_grid = tictactoe_board.column_grid()
        row_grid = tictactoe_board.board

        self.assertEqual(evaluate_grid_win(column_grid), [])
        self.assertEqual(evaluate_grid_win(row_grid), [])

        tictactoe_board.board[1][1] = 1
        tictactoe_board.board[2][1] = 1
        tictactoe_board.board[2][2] = 2
        tictactoe_board.board[3][1] = 1
        tictactoe_board.board[2][3] = 2

        column_grid = tictactoe_board.column_grid()

        self.assertEqual(evaluate_grid_win(column_grid), [PLAYERX])

        tictactoe_board.board[2][1] = 2
        tictactoe_board.board[2][0] = 2

        row_grid = tictactoe_board.board

        self.assertEqual(evaluate_grid_win(row_grid), [PLAYERO])

class TicTacToeBoardCheckDiagonalTest(unittest.TestCase):
    def test(self):
        tictactoe_board = TicTacToeBoard(4, False, None)
        tictactoe_board.board[0][0] = 1
        tictactoe_board.board[1][2] = 2
        tictactoe_board.board[0][1] = 1
      
        uleft_bright = tictactoe_board.uleft_bright_diagonal()
        bleft_uright = tictactoe_board.bleft_uright_diagonal()

        self.assertEqual(evaluate_diagonal_win(uleft_bright), [])
        self.assertEqual(evaluate_diagonal_win(bleft_uright), [])

        tictactoe_board.board[1][1] = 1
        tictactoe_board.board[2][1] = 1
        tictactoe_board.board[2][2] = 1
        tictactoe_board.board[3][3] = 1

        uleft_bright = tictactoe_board.uleft_bright_diagonal()

        self.assertEqual(evaluate_diagonal_win(uleft_bright), [PLAYERX])

        tictactoe_board.board[2][1] = 2
        tictactoe_board.board[3][0] = 2
        tictactoe_board.board[0][3] = 2

        bleft_uright = tictactoe_board.bleft_uright_diagonal()

        self.assertEqual(evaluate_diagonal_win(bleft_uright), [PLAYERO])

class TicTacToeBoardCheckWinTest(unittest.TestCase):
    def test_empty_board(self):
        tictactoe_board = TicTacToeBoard(3, False, None)
        tictactoe_board.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.assertEqual(tictactoe_board.evaluate_win_status(), None)

    def test_winning_row(self):
        tictactoe_board = TicTacToeBoard(3, False, None)
        tictactoe_board.board = [[0, 0, 2],
                                [0, 2, 0],
                                [1, 1, 1]]

        self.assertEqual(tictactoe_board.evaluate_win_status(), PLAYERX)

    def test_winning_column(self):
        tictactoe_board = TicTacToeBoard(3, False, None)
        tictactoe_board.board = [[2, 0, 2],
                                [2, 1, 0],
                                [2, 1, 1]]

        self.assertEqual(tictactoe_board.evaluate_win_status(), PLAYERO)

    def test_winning_uleft_diagonal(self):
        tictactoe_board = TicTacToeBoard(3, False, None)
        tictactoe_board.board = [[1, 0, 2],
                                [0, 1, 2],
                                [2, 1, 1]]
        
        self.assertEqual(tictactoe_board.evaluate_win_status(), PLAYERX)

    def test_winning_bleft_diagonal(self):
        tictactoe_board = TicTacToeBoard(3, False, None)    
        tictactoe_board.board = [[0, 0, 2],
                                [0, 2, 0],
                                [2, 1, 1]]
        
        self.assertEqual(tictactoe_board.evaluate_win_status(), PLAYERO)

    def test_tie(self):
        tictactoe_board = TicTacToeBoard(3, False, None)
        tictactoe_board.board = [[1, 1, 2], 
                                [2, 2, 1], 
                                [1, 2, 1]]

        self.assertEqual(tictactoe_board.evaluate_win_status(), DRAW)
