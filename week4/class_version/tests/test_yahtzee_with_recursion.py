"""
Tests for class version of yahtzee
"""
import unittest

from src.yahtzee_with_recursion import(expected_value, generate_all_holds,
                    gen_all_sequences, score,
                    strategy)

class GenAllSequencesTest(unittest.TestCase):
    """
    Tests for gen_all_sequences method
    """
    # def test_gen_all_sequences_empty(self):
    #     """
    #     Test that  passing an empty output array to gen_all_sequences
    #     returns an empty set
    #     """
    #     self.assertEqual(gen_all_sequences([], 1), set([]))

    def test_gen_all_sequences_length_one(self):
        """
        Test the case for all sequences of length 1
        """
        self.assertEqual(gen_all_sequences([4, 5, 3], 1), set([(4,), (5,), (3,)]))

    def test_gen_all_sequences_length_two(self):
        """
        Test the case for all sequences of length 2
        """
        self.assertEqual(gen_all_sequences([4, 5, 3], 2), set([(4, 5), (4, 4), (4, 3),
                                                              (5, 5), (5, 4), (5, 3),
                                                              (3, 3), (3, 4), (3, 5)]))

    def test_gen_all_sequences_length_three(self):
        """
        Test the case for all sequences of length 3
        """
        self.assertEqual(gen_all_sequences([4, 5], 3), set([(4, 4, 4), (4, 4, 5), (4, 5, 4),
                                                            (4, 5, 5), (5, 4, 4), (5, 4, 5),
                                                            (5, 5, 4), (5, 5, 5)]))

class ScoreTest(unittest.TestCase):
    """
    Tests for the score method
    """
    def test(self):
        """
        Tests that different hands return the highest possible score
        """
        self.assertEqual(score([3, 3, 3, 5, 5]), 10)
        self.assertEqual(score([2, 4, 3, 5, 5]), 10)
        self.assertEqual(score([4, 3, 3, 4, 5]), 8)
        self.assertEqual(score([1, 1, 1, 2, 3]), 3)


class ExpectedValueTest(unittest.TestCase):
    """
    Test the expected_value method
    """
    def test(self):
        """
        Tests something...
        """
        held_dice = ()
        num_die_sides = 6
        num_free_dice = 1
        self.assertEqual(expected_value(held_dice, num_die_sides, num_free_dice), 3.5)
        self.assertEqual(expected_value((2, 2), 6, 3), 6.91203703704)
        self.assertEqual(expected_value((3, 2), 4, 3), 6.5)
        self.assertEqual(expected_value((2, 2), 6, 2), 5.83333333333)

class GenAllHandsTest(unittest.TestCase):
    """
    Test gen_all_hand method
    """
    def test(self):
        """
        Tests ...
        """
        self.assertEqual(generate_all_holds([]), set([()]))
        self.assertEqual(generate_all_holds([1]), set([(), (1, )]))
        self.assertEqual(generate_all_holds([1, 2]), set([(), (1, ), (2, ), (1, 2)]))
        self.assertEqual(generate_all_holds([0, 1, 2]), set([(), (0, ), (1, ), (2, ), (0, 1), (0, 2), (1, 2), (0, 1, 2)]))
        self.assertEqual(generate_all_holds([0, 2, 2]), set([(), (0, ), (2, ), (0, 2), (2, 2), (0, 2, 2)]))
        self.assertEqual(generate_all_holds([0, 2, 2, 3]), set([(), (0, ), (2, ), (3, ),
                                                           (0, 2), (0, 3), (2, 2), 
                                                           (2, 3), (0, 2, 3), (0, 2, 2),
                                                           (2, 2, 3), (0, 2, 2, 3)]))
        self.assertEqual(generate_all_holds([0, 2, 2, 3, 3]), set([(0, 3, 3), (0,), (0, 2, 3, 3),
                                                           (2, 2, 3), (2,), (2, 2, 3, 3), 
                                                           (3,), (0, 2, 2), (0, 2, 3), (),
                                                           (2, 3), (2, 3, 3), (2, 2), 
                                                           (0, 2, 2, 3), (0, 3), (0, 2, 2, 3, 3),
                                                           (0, 2), (3, 3)]))        

class StrategyTest(unittest.TestCase):
    """
    Test strategy method
    """
    def test(self):
        """
        Basic test for strategy
        """
        self.assertEqual(strategy((1,), 6), (3.5, ()))

        hand = (1, 2, 3, 4, 4)
        possible_holds = list(generate_all_holds(hand))
        best_score = max([(expected_value(hold, 6, len(hand)-len(hold)), hold) for hold in possible_holds])
        scores = [expected_value(hold, 6, len(hand)-len(hold)) for hold in possible_holds]
        strat = strategy(hand, 6)
        self.assertEqual(strat, best_score)
        self.assertTrue(strat[0] == max(scores))

        hand = (1, 2, 3, 5, 3)
        possible_holds = list(generate_all_holds(hand))
        best_score = max([(expected_value(hold, 6, len(hand)-len(hold)), hold) for hold in possible_holds])
        scores = [expected_value(hold, 6, len(hand)-len(hold)) for hold in possible_holds]
        strat = strategy(hand, 6)
        self.assertEqual(strat, best_score)
        self.assertTrue(strat[0] == max(scores))