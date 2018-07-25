from tictactoe_board import TicTacToeBoard

# TICTACTOE_BOARD = TicTacToeBoard(3, False, None)
# print TICTACTOE_BOARD.dimension
# #TICTACTOE_BOARD.dimension = 4
# print TICTACTOE_BOARD.dimension
# #print tictactoe_board.new_board()
# TICTACTOE_BOARD.board[0][0] = 1
# TICTACTOE_BOARD.board[1][2] = 1
# TICTACTOE_BOARD.board[2][1] = 1

# print "   |   |   \n-----------\n   |   |   \n-----------\n   |   |   "
# print TICTACTOE_BOARD.get_empty_squares()
# CLONE = TICTACTOE_BOARD.clone()
# print 'clone ' + str(CLONE)

# #print TICTACTOE_BOARD.row_index()
# #print TICTACTOE_BOARD.column_index()
# print TICTACTOE_BOARD.column_grid()
# print TICTACTOE_BOARD.check_rows()
# print TICTACTOE_BOARD.check_columns()
# print TICTACTOE_BOARD.__str__()

# TICTACTOE_BOARD.board[0][1] = 2
# TICTACTOE_BOARD.board[0][2] = 2
# TICTACTOE_BOARD.board[2][2] = 1
# TICTACTOE_BOARD.board[1][1] = 1
# print TICTACTOE_BOARD.__str__()


# print TICTACTOE_BOARD.check_rows()
# print TICTACTOE_BOARD.check_grid(TICTACTOE_BOARD.board)
# print TICTACTOE_BOARD.check_columns()
# print TICTACTOE_BOARD.check_grid(TICTACTOE_BOARD.column_grid())
# print TICTACTOE_BOARD.uleft_bright()
# print TICTACTOE_BOARD.check_diagonal(TICTACTOE_BOARD.uleft_bright())
# print TICTACTOE_BOARD.bleft_uright()
# print TICTACTOE_BOARD.column_grid()
# print TICTACTOE_BOARD.board
# TICTACTOE_BOARD.check_win()

from tictactoe_board import switch_player
from tictactoe_board import TicTacToeBoard
from tictactoe_board import PLAYERO
from tictactoe_board import PLAYERX
from monte_carlo_tictactoe import mc_move
from monte_carlo_tictactoe import get_best_move

#number_trails_to_run = int(input ("how many trials would you like to run?"))

board = TicTacToeBoard(3, False, None)
player = PLAYERX
win = None

while win == None:
  move = mc_move(board, player, 500)
  board.move(move[0], move[1], player)
  player = switch_player(player)
  print board.__str__()
  print('\n')
  win = board.check_win()

print "win: " + str(win)


scores =  [[1, 2, 3], [7, 8, 9], [4, 5, 6]]
board.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print get_best_move(board,scores)