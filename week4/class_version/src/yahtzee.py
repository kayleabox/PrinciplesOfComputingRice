"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

from copy import copy

# Used to increase the timeout, if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)

def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score
    """
    possible_scores = [hand.count(number) * number for number in hand]
    return max(possible_scores)


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    dice = [number for number in range(1, num_die_sides+1)]
    all_rolls = list(gen_all_sequences(dice, num_free_dice))
    return round(sum([score(held_dice + roll) for roll in all_rolls])/float(len(all_rolls)), 11)

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    holds = set([()])
    return recursive_gen_holds(hand, len(hand), holds)

def recursive_gen_holds(hand, length, holds):
    """
    Recursively generate all possible holds
    """
    if length:
        holds = recursive_gen_holds(hand, length-1, add_partial_holds_to_temp(hand, holds))
    return holds

def add_partial_holds_to_temp(hand, holds):
    """
    Add a partial hold to the set of holds
    """
    temp = set()
    return [create_new_partial_hold(temp, partial_sequence, hand) for partial_sequence in holds][0]

def create_new_partial_hold(temp, partial_sequence, hand):
    """
    Create new partial hold
    """
    return [add_sequence_to_holds(temp, partial_sequence, item) for item in hand
            if hand.count(item) > partial_sequence.count(item)][0]

def add_sequence_to_holds(temp, partial_sequence, item):
    """
    Add a new sequence to the set of possible holds
    """
    new_sequence = list(partial_sequence)
    new_sequence.append(item)
    new_sequence.sort()
    temp.add(tuple(new_sequence))
    temp.add(partial_sequence)
    return temp

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
    return max([(expected_value(hold, num_die_sides, len(hand)-len(hold)), hold) for hold in possible_holds])

def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    hand = (3, 2, 3, 5, 3)
    possible_holds = list(gen_all_holds(hand))
    print [(expected_value(hold, 6, len(hand)-len(hold)), hold) for hold in possible_holds]
    print [expected_value(hold, 6, len(hand)-len(hold)) for hold in possible_holds]
    print strategy(hand, 6)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    all_sequences = set([()])
    for dummy_number in range(length):
        all_sequences = update_partial_sequences(all_sequences, outcomes)
    return all_sequences

def update_partial_sequences(all_sequences, outcomes):
    """
    Iterate through the partial sequences in the list and return the updated version
    """
    temp_set = set()
    return set([add_outcome_to_tempset(temp_set, sequence, outcomes) for sequence in all_sequences][0])

def add_outcome_to_tempset(new_set, sequence, outcomes):
    """
    Add the updated partial to the tempset
    """
    # might have to use this method if I need to check an empty list of outcomes being passed in
    # [update_set(new_set, sequence, item) for item in outcomes]
    # return new_set
    return [update_set(new_set, sequence, item) for item in outcomes][0]
    # cannot pass outcomes [] if use this method

def update_set(new_set, sequence, item):
    """
    Return a new set with elements that should be in the
    seqeunce appended to it
    """
    temp_sequence = list(sequence)
    temp_sequence.append(item)
    new_set.add(tuple(temp_sequence))
    return new_set

run_example()

print gen_all_holds([0, 2, 2, 3, 3])
print gen_all_sequences([0, 2, 3, 8], 3)
gen_seq = list(gen_all_sequences([1, 2, 3, 4, 5, 6], 3))
print sum([score((2, 2) + roll) for roll in gen_seq])/float(len(gen_seq))
