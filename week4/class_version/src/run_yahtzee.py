from itertools import chain, combinations, combinations_with_replacement

from yahtzee import strategy
from yahtzee_itertools import strategy as yi_strategy
from yahtzee_with_recursion import strategy as ywr_strategy

def run_example(strategy, run_text):
    """
    Compute the dice to hold and expected score for an example hand
    """
    print run_text
    num_die_sides = 3
    hand = (1, 2, 1)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score

run_example(strategy, "running yahtzee.py")
run_example(yi_strategy, "running yahtzee_itertools.py")
run_example(ywr_strategy, "running yahtzee_with_recursion.py")
