"""

"""
from yahtzee_psychic import YahtzeePsychic

class YahtzeePsychicRecursion(YahtzeePsychic):
    def gen_all_holds(self, hand):
        """
        Generate all possible choices of dice from hand to hold.

        hand: full yahtzee hand

        Returns a set of tuples, where each tuple is dice to hold
        """
        holds = set([()])
        return self.recursive_generate_holds(hand, len(hand), holds)

    def recursive_generate_holds(self, hand, length, holds):
        """
        Recursively generate all possible holds
        """
        return self.recursive_generate_holds(hand, length-1,
                                        self.generate_temp_holds(hand, holds)) if length else holds

    def generate_temp_holds(self, hand, holds):
        """
        Add a group of holds to the set of holds
        """
        temp_set = set()
        return [self.update_holds(temp_set, hold, hand) for hold in holds][0]

    def update_holds(self, temp_set, hold, hand):
        """
        Update the holds with the next value in hand
        if it has not been added to the hold already
        """
        if hand:
            if hand.count(hand[0]) > hold.count(hand[0]):
                temp_set = self.add_sorted_hold_to_set(temp_set, hold, hand[0])
            return self.update_holds(temp_set, hold, hand[1:])
        return temp_set

    def add_sorted_hold_to_set(self, temp_set, hold, value):
        """
        Add a new sorted hold and the old hold to a temp_set
        """
        temp_set.add(self.generate_sorted_hold(hold, value))
        temp_set.add(hold)
        return temp_set

    def generate_sorted_hold(self, hold, value):
        """
        Add the new element to the temp_sequence
        """
        temp_sequence = list(hold) + [value]
        temp_sequence.sort()
        return tuple(temp_sequence)

    def gen_all_sequences(self, outcomes, length):
        """
        Iterative function that enumerates the set of all sequences of
        outcomes of given length.
        """
        all_sequences = set([()])
        return self.recursive_generate_sequences(outcomes, length, all_sequences)

    def recursive_generate_sequences(self, outcomes, length, sequences):
        """
        Recursively generate all possible holds
        """
        return self.recursive_generate_sequences(outcomes, length-1,
                                            self.update_sequences(sequences, outcomes)) if length else sequences

    def update_sequences(self, all_sequences, outcomes):
        """
        Iterate through the partial sequences in the list
        and append each outcome to it, return the set of
        sequences with outcomes added
        """
        temp_set = set()
        return [self.recursive_update_set(temp_set, sequence, outcomes)
                for sequence in all_sequences][0]

    def recursive_update_set(self, temp_set, sequence, outcomes):
        """
        Return a new set with outcomes appended to it
        """
        if outcomes:
            temp_set.add(tuple(list(sequence) + [outcomes[0]]))
            return self.recursive_update_set(temp_set, sequence, outcomes[1:])
        return temp_set

yahtzee_psychic = YahtzeePsychicRecursion()
yahtzee_psychic.run_example()
