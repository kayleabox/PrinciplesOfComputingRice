import unittest

from i_yahtzee_psychic import IYahtzeePsychic
from yahtzee_psychic import YahtzeePsychic
from yahtzee_psychic_plain import YahtzeePsychicPlain
from yahtzee_psychic_recursion import YahtzeePsychicRecursion

class YahtzeePsychicTest(unittest.TestCase):
    def test(self):
        yahtzee_psychic = YahtzeePsychic()
        self.assertIsInstance(yahtzee_psychic, IYahtzeePsychic)

class ScoreTest(unittest.TestCase):
    """
    Tests for the score method
    """
    def test(self):
        """
        Tests that different hands return the highest possible score
        """
        yahtzee = YahtzeePsychic()

        self.assertEqual(yahtzee.score([3, 3, 3, 5, 5]), 10)
        self.assertEqual(yahtzee.score([2, 4, 3, 5, 5]), 10)
        self.assertEqual(yahtzee.score([4, 3, 3, 4, 5]), 8)
        self.assertEqual(yahtzee.score([1, 1, 1, 2, 3]), 3)


class ExpectedValueTest(unittest.TestCase):
    """
    Test the expected_value method
    """
    def test(self):
        """
        Tests something...
        """
        yahtzee = YahtzeePsychic()

        held_dice = ()
        num_die_sides = 6
        num_free_dice = 1
        self.assertEqual(yahtzee.expected_value(held_dice, num_die_sides, num_free_dice), 1.0)

class StrategyTest(unittest.TestCase):
    """
    Test strategy method
    """
    def test(self):
        """
        Basic test for strategy
        """
        yahtzee = YahtzeePsychicPlain()

        self.assertEqual(yahtzee.strategy((1,), 6), (3.5, ()), 1.0)

class GenAllHoldsSequencesTest(unittest.TestCase):
    """

    """
    def test(self):
        """

        """
        yahtzee = YahtzeePsychic()

        self.assertEqual(yahtzee.gen_all_holds([1, 2, 3]), set([(1, )]))
        self.assertEqual(yahtzee.gen_all_sequences([1, 1, 1], 2), set([(1, )]))