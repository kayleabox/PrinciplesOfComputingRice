"""
Runs the monte carlo simulation for specified number of times
"""

from monte_carlo_tictactoe import mc_move
from tictactoe_board import (PLAYERX, switch_player, TicTacToeBoard)

BOARD = TicTacToeBoard(3, False, None)
NUM_TRIALS = 500

PLAYER = PLAYERX
win = None

while not win:
    MOVE = mc_move(BOARD, PLAYER, NUM_TRIALS)
    BOARD.move(MOVE[0], MOVE[1], PLAYER)
    PLAYER = switch_player(PLAYER)
    print BOARD.__str__() + '\n'
    win = BOARD.evaluate_win_status()

print "win: " + str(win)
