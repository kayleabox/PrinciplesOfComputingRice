"""
abstract class for yahtzee psychic
"""

from abc import ABC, ABCMeta, abstractmethod

class IYahtzeePsychic(ABC):
    #__metaclass__ = ABCMeta

    @abstractmethod
    def score(self, hand): raise NotImplementedError
    @abstractmethod
    def expected_value(self, held_dice, num_die_sides, num_free_dice): raise NotImplementedError
    @abstractmethod
    def strategy(self, hand, num_die_sides): raise NotImplementedError
    @abstractmethod
    def gen_all_holds(self, hand): raise NotImplementedError
    @abstractmethod
    def gen_all_sequences(self, outcomes, length): raise NotImplementedError
    @abstractmethod
    def run_example(self): raise NotImplementedError
