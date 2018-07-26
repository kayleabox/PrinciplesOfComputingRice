from cv_tictactoe_board import PLAYERO
from cv_tictactoe_board import PLAYERX
from cv_tictactoe_board import switch_player
from cv_tictactoe_board import TicTacToeBoard
from monte_carlo_tictactoe import get_best_move
from monte_carlo_tictactoe import mc_move

#number_trails_to_run = int(input ("how many trials would you like to run?"))

board = TicTacToeBoard(3, False, None)
player = PLAYERX
win = None

while win == None:
  move = mc_move(board, player, 500)
  board.move(move[0], move[1], player)
  player = switch_player(player)
  print board.__str__() + '\n'
  win = board.check_win()

print "win: " + str(win)
