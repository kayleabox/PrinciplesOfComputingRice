"""
Tests for class version of yahtzee_with_recursion
"""
import unittest

from src.yahtzee_with_recursion import(expected_value, generate_all_holds,
                                       gen_all_sequences, score, strategy,
                                       recursive_generate_holds, 
                                       generate_temp_holds, update_holds,
                                       add_sorted_hold_to_set, generate_sorted_hold,
                                       recursive_generate_sequences,
                                       update_sequences, recursive_update_set,
                                       add_sequence_to_set)


class GenAllSequencesTest(unittest.TestCase):
    """
    Tests for gen_all_sequences method
    """
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
    def test_score(self):
        """
        Tests that different hands return the highest possible score
        """
        self.assertEqual(score([3, 3, 3, 5, 5]), 10)
        self.assertEqual(score([2, 4, 3, 5, 5]), 10)
        self.assertEqual(score([4, 3, 3, 4, 5]), 8)
        self.assertEqual(score([1, 1, 1, 2, 3]), 3)

class ExpectedValueTest(unittest.TestCase):
    """
    Test the expected_value(held_dice, num_die_sides, num_free_dice) method
    """
    def test_expected_value(self):
        """
        Test the expected value of several different hands
        """
        self.assertEqual(expected_value((), 6, 1), 3.5)
        self.assertEqual(expected_value((2, 2), 6, 3), 6.91203703704)
        self.assertEqual(expected_value((3, 2), 4, 3), 6.5)
        self.assertEqual(expected_value((2, 2), 6, 2), 5.83333333333)

class GenAllHandsTest(unittest.TestCase):
    """
    Test generate_all_holds method
    """
    def test_generate_all_holds(self):
        """
        Tests all of the possible combinations
        of dice to hold are listed, order does not
        matter
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
    Test strategy(hand, num_die_sides) method
    """
    def test_strategy(self):
        """
        Basic test for strategy
        """
        self.assertEqual(strategy((1,), 6), (3.5, ()))

    def test_strategy_several_hands(self):
        """
        Tests strategy with several hands
        """
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

class RecursiveGenHoldsTest(unittest.TestCase):
    """
    Test recursive_gen_holds method
    """
    def test_recursive_gen_holds(self):
        """
        Test that recursive_gen_holds returns a set
        of all of the possible holds that can be
        generated using the numbers in the hand
        """
        holds = set([()])
        self.assertEqual(recursive_generate_holds([1], 1, holds), set([(), (1, )]))
        holds = set([()])
        self.assertEqual(recursive_generate_holds([0, 1, 2], 3, holds), 
                                              set([(), (0, ), (1, ), (2, ),
                                                  (0, 1), (0, 2), (1, 2),
                                                  (0, 1, 2)]))
        holds = set([()])
        self.assertEqual(recursive_generate_holds([0, 2, 2, 3], 4, holds),
                                             set([(), (0, ), (2, ), (3, ),
                                                 (0, 2), (0, 3), (2, 2), 
                                                 (2, 3), (0, 2, 3), (0, 2, 2),
                                                 (2, 2, 3), (0, 2, 2, 3)]))
        holds = set([()])
        self.assertEqual(recursive_generate_holds([0, 2, 2, 3, 3], 5, holds), 
                                            set([(0, 3, 3), (0,), (0, 2, 3, 3),
                                                (2, 2, 3), (2,), (2, 2, 3, 3), 
                                                (3,), (0, 2, 2), (0, 2, 3), (),
                                                (2, 3), (2, 3, 3), (2, 2), 
                                                (0, 2, 2, 3), (0, 3), (0, 2, 2, 3, 3),
                                                (0, 2), (3, 3)]))

class AddSortedHoldToSetTest(unittest.TestCase):
    """
    Test add_sorted_hold_to_set(temp_set, hold, value) method
    """
    def test_add_sorted_hold_to_set(self):
        """
        Test that add_sorted_hold_to_set creates a
        sorted tuple with value appened to hold and
        returns a set with the tuple appended to it
        """   
        temp_set = set()
        self.assertEqual(add_sorted_hold_to_set(temp_set, (1, 2, 5), 5), set([(1, 2, 5), (1, 2, 5, 5)]))
        self.assertEqual(add_sorted_hold_to_set(temp_set, (2, 3, 4), 6), set([(1, 2, 5), (1, 2, 5, 5),
                                                                       (2, 3, 4), (2, 3, 4, 6)]))

class UpdateHoldsTest(unittest.TestCase):
    """
    Test update_hold(temp_set, hold, hand) method
    """
    def test_update_hold(self):
        """
        Test that update_hold returns a set of tuples.
        The set should contain the hold passed in and
        a new hold for each of the numbers in hand
        that were not in original hold appended to the
        original hold. Numbers in the original hold are
        ignored unless they are duplicates and there
        are more of them in the hand than in the hold. 
        """   
        temp_set = set()
        self.assertEqual(update_holds(temp_set, (1, 2), (1, 1, 2, 3)), set([(1, 2), (1, 2, 3), (1, 1, 2)]))
        temp_set = set()
        self.assertEqual(update_holds(temp_set, (1, 2, 5), (1, 2, 3, 4, 5)), set([(1, 2, 5), (1, 2, 3, 5), (1, 2, 4, 5)]))

class GeneratePartialHoldsTest(unittest.TestCase):
    """
    Test generate_partial_holds method
    """
    def test_generate_partial_holds_with_empty_set(self):
        """
        Test that passing a tuple of numbers and an empty
        set to generate_partial_holds returns a set with
        with a tuple for each element in the tuple passed
        the function
        """
        holds = set([()])
        self.assertEqual(generate_temp_holds((1, 2), holds), set([(), (1, ), (2, )]))
        holds = set([()])
        self.assertEqual(generate_temp_holds((3, 4, 7), holds), set([(), (3, ), (4, ), (7, )]))

    def test_generate_partial_holds_with_non_empty_set(self):
        """
        Test that generate_partial_holds takes in a tuple
        of numbers and a set of tuples of numbers and
        returns a set of tuples with the new tuple appended
        """
        holds = set([(1, 2, 5), (1, 2, 3, 5), (1, 2, 4, 5)])
        self.assertEqual(generate_temp_holds((1, 2, 3, 4, 5), holds), 
                         set([(1, 2, 5), (1, 2, 3, 5), (1, 2, 4, 5), (1, 2, 3, 4, 5)]))
        holds = set([(), (1, ), (2, )])
        self.assertEqual(generate_temp_holds((1, 2), holds), set([(), (1, ), (2, ), (1, 2)]))

class GenerateSortedHoldTest(unittest.TestCase):
    """
    Test generate_sorted_hold(hold, value) method
    """
    def test_generate_sorted_hold_with_empty_hold(self):
        """
        Test that generate_sorted_hold returns a tuple with
        the value appended to it
        """
        self.assertEqual(generate_sorted_hold((), 3), (3, ))

    def test_generate_sorted_hold_with_non_empty_hold(self):
        """
        Test that generate_sorted_hold returns a sorted tuple
        with the value appended to it
        """
        self.assertEqual(generate_sorted_hold((1, 5, 3), 2), (1, 2, 3, 5))
        self.assertEqual(generate_sorted_hold((3, 6, 7, 1, 5, 2), 3), (1, 2, 3, 3, 5, 6, 7))

class AddSequenceToSetTest(unittest.TestCase):
    """
    Test add_sequence_to_set(temp_set, sequence, outcome) method
    """
    def test_add_sequence_to_set(self):
        """
        Test that add_sequence_to_set returns a set
        with the tuples in temp_set appended to it
        and a new tuple with the sequence + outcome.
        """   
        temp_set = set()
        self.assertEqual(add_sequence_to_set(temp_set, (1, 2), 3), set([(1, 2, 3)]))    
        temp_set = set([(1, 2), (1, 3)])
        self.assertEqual(add_sequence_to_set(temp_set, (1, 2), 5), set([(1, 2), (1, 3), (1, 2, 5)]))
        temp_set = set([(1, 2, 3)])
        self.assertEqual(add_sequence_to_set(temp_set, (1, 2, 3), 5), set([(1, 2, 3), (1, 2, 3, 5)]))    

class RecursiveUpdateSetTest(unittest.TestCase):
    """
    Test recursive_update_set(temp_set, sequence, outcomes) method
    """
    def test_recursive_update_set(self):
        """
        Test that recursive_update_set returns a set with
        a tuple for each outcome appended to the sequence
        passed in.
        """   
        temp_set = set()
        self.assertEqual(recursive_update_set(temp_set, (1, 2), [3, 2]), set([(1, 2, 3), (1, 2, 2)]))
        temp_set = set([(1, 2, 5), (1, 2, 3, 5), (1, 2, 4, 5)])
        self.assertEqual(recursive_update_set(temp_set, (1, 2, 4, 5), [3, 1]), 
                         set([(1, 2, 5), (1, 2, 3, 5), (1, 2, 4, 5), 
                              (1, 2, 4, 5, 3), (1, 2, 4, 5, 1)]))
 
class RecursiveGenerateSequencesTest(unittest.TestCase):
    """
    Test recursive_generate_sequences(outcomes, length, sequences) method
    """
    def test_recursive_generate_sequences_without_outcomes(self):
        """
        Test that recursive_generate_sequences returns an empty set
        when passed no outcomes
        """
        sequences = set([()])
        self.assertEqual(recursive_generate_sequences([], 0, sequences), set([()]))
    
    def test_recursive_generate_sequences(self):
        """
        Test that recursive_generate_sequences returns all
        the sequences of length, length that can be made
        from outcomes with repeats included
        """
        outcomes = [1, 2, 3]
        length = 1
        sequences = set([()])
        self.assertEqual(recursive_generate_sequences(outcomes, length, sequences), 
                         set([(1, ), (2, ), (3, )]))
        outcomes = [1, 2, 3]
        length = 2
        sequences = set([()])
        self.assertEqual(recursive_generate_sequences(outcomes, length, sequences), 
                         set([(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3),
                             (3, 1), (3, 2), (3, 3)]))
        outcomes = [1, 2, 3]
        length = 3
        sequences = set([()])
        self.assertEqual(recursive_generate_sequences(outcomes, length, sequences), 
                         set([(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 1), (1, 2, 2), (1, 2, 3),
                             (1, 3, 2), (1, 3, 1), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1),
                             (1, 3, 3), (2, 1, 1), (2, 1, 2), (2, 2, 2), (2, 2, 1), (2, 2, 3),
                             (2, 3, 2), (2, 3, 3), (3, 1, 1), (3, 1, 3), (3, 3, 1), (3, 2, 2),
                             (3, 2, 3), (3, 3, 2), (3, 3, 3) ]))

class UpdateSequencesTest(unittest.TestCase):
    """
    Test update_sequences(all_sequences, outcomes) method
    """
    def test_update_sequences(self):
        """
        Test that update_sequences returns a set with the 
        with a new tuple for each tuple that was in the set
        for each outcome in the list
        """
        all_sequences = set([()])
        outcomes = [3, 4]
        self.assertEqual(update_sequences(all_sequences, outcomes), set([(3, ), (4, )]))
        all_sequences = set([(3, ), (4, )])
        self.assertEqual(update_sequences(all_sequences, outcomes), set([(3, 3), (3, 4), (4, 4), (4, 3)]))
