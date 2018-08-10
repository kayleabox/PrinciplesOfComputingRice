"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

from itertools import chain, combinations, product

def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score
    """
    return max([hand.count(number) * number for number in hand])


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    dice_sides = range(1, num_die_sides+1)
    all_rolls = list(gen_all_sequences(dice_sides, num_free_dice))
    summed_scores = sum([score(held_dice + roll) for roll in all_rolls])
    num_rolls = float(len(all_rolls))
    return round(summed_scores/num_rolls, 11)

def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    possible_holds = list(gen_all_holds(hand))
    return max([(expected_value(hold, num_die_sides, len(hand)-len(hold)), hold)
                for hold in possible_holds])

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    return set(generate_powerset(hand))

def generate_powerset(hand):
    """
    Returns an iterable with the powerset of
    the array hand
    """
    return chain.from_iterable(combinations(hand, number)
                               for number in range(len(hand)+1))

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    return set(product(outcomes, repeat=length))
