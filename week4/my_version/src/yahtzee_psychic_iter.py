"""

"""
from itertools import chain, combinations, product

from yahtzee_psychic import YahtzeePsychic

class YahtzeePsychicIter(YahtzeePsychic):
    def gen_all_holds(self, hand):
        powerset = self.generate_powerset(hand)
        return set([self.sort_tuples(element) for element in powerset])

    def sort_tuples(self, element):
        element = list(element)
        element.sort()
        return tuple(element)

    def generate_powerset(self, hand):
        """
        Returns an iterable with the powerset of
        the array hand
        """
        return chain.from_iterable(combinations(hand, number)
                                for number in range(len(hand)+1))
    
    def gen_all_sequences(self, outcomes, length):
        """
        Iterative function that enumerates the set of all sequences of
        outcomes of given length.
        """
        return set(product(outcomes, repeat=length))

yahtzee_psychic_iter = YahtzeePsychicIter()
yahtzee_psychic_iter.run_example()
