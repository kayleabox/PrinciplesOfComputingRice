"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

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
    return round(sum([score(held_dice + roll) for roll in all_rolls])/float(len(all_rolls)), 11)

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
    holds = set([()])
    return recursive_gen_holds(hand, len(hand), holds)

def recursive_gen_holds(hand, length, holds):
    """
    Recursively generate all possible holds
    """
    return recursive_gen_holds(hand, length-1,
                               generate_temp_holds(hand, holds)) if length else holds

def generate_temp_holds(hand, holds):
    """
    Add a group of holds to the set of holds
    """
    temp_set = set()
    return [update_hold(temp_set, hold, hand) for hold in holds][0]

def update_hold(temp_set, hold, hand):
    """
    Update each hold by adding value to it
    """
    return [add_hold_to_set(temp_set, hold, value) for value in hand
            if hand.count(value) > hold.count(value)][0]

def add_hold_to_set(temp_set, hold, value):
    """
    Add a new hold to the set of possible holds
    """
    temp_set.add(generate_sorted_sequence(hold, value))
    temp_set.add(hold)
    return temp_set

def generate_sorted_sequence(hold, value):
    """
    Add value to an old hold to create a new hold
    """
    temp_sequence = list(hold) + [value]
    temp_sequence.sort()
    return tuple(temp_sequence)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    all_sequences = set([()])
    for dummy_number in range(length):
        all_sequences = update_sequences(all_sequences, outcomes)
    return all_sequences

def update_sequences(all_sequences, outcomes):
    """
    Iterate through the partial sequences in the list and return the updated version
    """
    temp_set = set()
    return [add_outcome_to_tempset(temp_set, sequence, outcomes)
            for sequence in all_sequences][0]

def add_outcome_to_tempset(temp_set, sequence, outcomes):
    """
    Add the updated partial to the tempset
    """
    return [update_set(temp_set, sequence, value) for value in outcomes][0]

def update_set(temp_set, sequence, value):
    """
    Return a new set with elements that should be in the
    seqeunce appended to it
    """
    temp_sequence = list(sequence) + [value]
    temp_set.add(tuple(temp_sequence))
    return temp_set
