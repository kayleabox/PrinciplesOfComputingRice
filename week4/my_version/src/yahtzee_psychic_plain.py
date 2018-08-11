"""

"""
from yahtzee_psychic import YahtzeePsychic

class YahtzeePsychicPlain(YahtzeePsychic):
    def gen_all_holds(self, hand):
        """
        Generate all possible choices of dice from hand to hold.

        hand: full yahtzee hand

        Returns a set of tuples, where each tuple is dice to hold
        """
        holds = set([()])
        return self.recursive_gen_holds(hand, len(hand), holds)

    def recursive_gen_holds(self, hand, length, holds):
        """
        Recursively generate all possible holds
        """
        return self.recursive_gen_holds(hand, length-1,
                                self.generate_temp_holds(hand, holds)) if length else holds

    def generate_temp_holds(self, hand, holds):
        """
        Add a group of holds to the set of holds
        """
        temp_set = set()
        return [self.update_hold(temp_set, hold, hand) for hold in holds][0]

    def update_hold(self, temp_set, hold, hand):
        """
        Update each hold by adding value to it
        """
        return [self.add_hold_to_set(temp_set, hold, value) for value in hand
                if hand.count(value) > hold.count(value)][0]

    def add_hold_to_set(self, temp_set, hold, value):
        """
        Add a new hold to the set of possible holds
        """
        temp_set.add(self.generate_sorted_sequence(hold, value))
        temp_set.add(hold)
        return temp_set

    def generate_sorted_sequence(self, hold, value):
        """
        Add value to an old hold to create a new hold
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
        for dummy_number in range(length):
            all_sequences = self.update_sequences(all_sequences, outcomes)
        return all_sequences

    def update_sequences(self, all_sequences, outcomes):
        """
        Iterate through the partial sequences in the list and return the updated version
        """
        temp_set = set()
        return [self.add_outcome_to_tempset(temp_set, sequence, outcomes)
                for sequence in all_sequences][0]

    def add_outcome_to_tempset(self, temp_set, sequence, outcomes):
        """
        Add the updated partial to the tempset
        """
        return [self.update_set(temp_set, sequence, value) for value in outcomes][0]

    def update_set(self, temp_set, sequence, value):
        """
        Return a new set with elements that should be in the
        seqeunce appended to it
        """
        temp_sequence = list(sequence) + [value]
        temp_set.add(tuple(temp_sequence))
        return temp_set

yahtzee_psychic = YahtzeePsychicPlain()
yahtzee_psychic.run_example()
