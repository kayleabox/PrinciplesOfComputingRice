from cv_tictactoe_board import (PLAYERO, PLAYERX, switch_player, TicTacToeBoard)
from monte_carlo_tictactoe import (get_best_move, mc_move)

board = TicTacToeBoard(3, False, None)
player = PLAYERX
win = None

while not win:
  move = mc_move(board, player, 500)
  board.move(move[0], move[1], player)
  player = switch_player(player)
  print board.__str__() + '\n'
  win = board.evaluate_win_status()

print "win: " + str(win)
