"""
Runs the monte carlo simulation for specified number of times
"""

from monte_carlo_tictactoe import mc_move
from tictactoe_board import (PLAYERO, PLAYERX, switch_player, TicTacToeBoard)

BOARD = TicTacToeBoard(3, False, None)
NUM_TRIALS = 500

player = PLAYERX
win = None

while not win:
    move = mc_move(BOARD, player, NUM_TRIALS)
    BOARD.move(move[0], move[1], player)
    player = switch_player(player)
    print BOARD.__str__() + '\n'
    win = BOARD.evaluate_win_status()

print "win: " + str(win)
