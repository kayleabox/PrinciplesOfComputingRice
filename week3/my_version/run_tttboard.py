"""
Runs the monte carlo simulation for specified number of times
"""

from monte_carlo_tictactoe import mc_move
from tictactoe_board import PLAYERO
from tictactoe_board import PLAYERX
from tictactoe_board import switch_player
from tictactoe_board import TicTacToeBoard

#number_trails_to_run = int(input ("how many trials would you like to run?"))

BOARD = TicTacToeBoard(3, False, None)
NUM_TRIALS = 500

player = PLAYERX
win = None

while not win:
    move = mc_move(BOARD, player, NUM_TRIALS)
    BOARD.move(move[0], move[1], player)
    player = switch_player(player)
    print BOARD.__str__() + '\n'
    win = BOARD.check_win()

print "win: " + str(win)
