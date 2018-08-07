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
    possible_holds = list(generate_all_holds(hand))
    return max([(expected_value(hold, num_die_sides, len(hand)-len(hold)), hold)
                for hold in possible_holds])

def generate_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    holds = set([()])
    return recursive_generate_holds(hand, len(hand), holds)

def recursive_generate_holds(hand, length, holds):
    """
    Recursively generate all possible holds
    """
    return recursive_generate_holds(hand, length-1,
                               generate_partial_holds(hand, holds)) if length else holds

def generate_partial_holds(hand, holds):
    """
    Add a partial hold to the set of holds
    """
    temp_set = set()
    return [update_holds(temp_set, hold, hand) for hold in holds][0]

def update_holds(temp_set, hold, hand):
    """
    Update the holds with the next value in hand
    if it has not been added to the hold
    """
    if hand: 
        if hand.count(hand[0]) > hold.count(hand[0]):
            temp_set = add_sorted_hold_to_set(temp_set, hold, hand[0])
        return update_holds(temp_set, hold, hand[1:])
    return temp_set

def add_sorted_hold_to_set(temp_set, hold, value):
    """
    Add a new sorted hold and the old hold to a temp_set
    """
    temp_set.add(generate_sorted_hold(hold, value))
    temp_set.add(hold)
    return temp_set

def generate_sorted_hold(hold, value):
    """
    Add the new element to the temp_sequence
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
    return recursive_generate_sequences(outcomes, length, all_sequences)

def recursive_generate_sequences(outcomes, length, sequences):
    """
    Recursively generate all possible holds
    """
    return recursive_generate_sequences(outcomes, length-1,
                               update_sequences(sequences, outcomes)) if length else sequences

def update_sequences(all_sequences, outcomes):
    """
    Iterate through the partial sequences in the list
    and return the updated version
    """
    temp_set = set()
    return [recursive_update_set(temp_set, sequence, outcomes)
        for sequence in all_sequences][0]

def recursive_update_set(temp_set, sequence, outcomes):
    """
    Return a new set with elements that should be in the
    seqeunce appended to it
    """
    if outcomes:
        temp_set.add(tuple(list(sequence) + [outcomes[0]]))
        # temp_set = add_sequence_to_set(temp_set, sequence, outcomes[0])
        return recursive_update_set(temp_set, sequence, outcomes[1:])
    return temp_set

def add_sequence_to_set(temp_set, sequence, outcome):
    """
    Add a new outcome to a sequence and add the new sequence
    to a temp_set
    """
    #temp_sequence = list(sequence) + [outcome]
    temp_set.add(tuple(list(sequence) + [outcome]))
    return temp_set

