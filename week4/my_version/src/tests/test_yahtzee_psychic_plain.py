import unittest

from i_yahtzee_psychic import IYahtzeePsychic
from yahtzee_psychic import YahtzeePsychic
from yahtzee_psychic_plain import YahtzeePsychicPlain

class YahtzeePsychicTest(unittest.TestCase):
    def test(self):
        yahtzee_psychic = YahtzeePsychic()
        self.assertIsInstance(yahtzee_psychic, IYahtzeePsychic)
        self.assertIsInstance(yahtzee_psychic, YahtzeePsychic)

class ExpectedValueTest(unittest.TestCase):
    """
    Test the expected_value method
    """
    def test(self):
        """
        Tests something...
        """
        yahtzee = YahtzeePsychicPlain()

        held_dice = ()
        num_die_sides = 6
        num_free_dice = 1
        self.assertEqual(yahtzee.expected_value(held_dice, num_die_sides, num_free_dice), 3.5)
        self.assertEqual(yahtzee.expected_value((2, 2), 6, 3), 6.91203703704)
        self.assertEqual(yahtzee.expected_value((3, 2), 4, 3), 6.5)
        self.assertEqual(yahtzee.expected_value((2, 2), 6, 2), 5.83333333333)

class StrategyTest(unittest.TestCase):
    """
    Test strategy method
    """
    def test(self):
        """
        Basic test for strategy
        """
        yahtzee = YahtzeePsychicPlain()

        self.assertEqual(yahtzee.strategy((1,), 6), (3.5, ()))

        hand = (1, 2, 3, 4, 4)
        possible_holds = list(yahtzee.gen_all_holds(hand))
        best_score = max([(yahtzee.expected_value(hold, 6, len(hand)-len(hold)), hold) for hold in possible_holds])
        scores = [yahtzee.expected_value(hold, 6, len(hand)-len(hold)) for hold in possible_holds]
        strat = yahtzee.strategy(hand, 6)
        self.assertEqual(strat, best_score)
        self.assertTrue(strat[0] == max(scores))

        hand = (1, 2, 3, 5, 3)
        possible_holds = list(yahtzee.gen_all_holds(hand))
        best_score = max([(yahtzee.expected_value(hold, 6, len(hand)-len(hold)), hold) for hold in possible_holds])
        scores = [yahtzee.expected_value(hold, 6, len(hand)-len(hold)) for hold in possible_holds]
        strat = yahtzee.strategy(hand, 6)
        self.assertEqual(strat, best_score)
        self.assertTrue(strat[0] == max(scores))

"""
Tests for YahtzeePsychicPlain
"""
class GenAllHoldsTest(unittest.TestCase):
    """
    Test gen_all_holds method
    """
    def test(self):
        """
        Test that gen_all_holds returns a set of all of
        sorted tuples containing all of the possible holds
        """
        yahtzee = YahtzeePsychicPlain()
        
        self.assertEqual(yahtzee.gen_all_holds([]), set([()]))
        self.assertEqual(yahtzee.gen_all_holds([1]), set([(), (1, )]))
        self.assertEqual(yahtzee.gen_all_holds([1, 2]), set([(), (1, ), (2, ), (1, 2)]))
        self.assertEqual(yahtzee.gen_all_holds([0, 1, 2]), set([(), (0, ), (1, ), (2, ), (0, 1), (0, 2), (1, 2), (0, 1, 2)]))
        self.assertEqual(yahtzee.gen_all_holds([0, 2, 2]), set([(), (0, ), (2, ), (0, 2), (2, 2), (0, 2, 2)]))
        self.assertEqual(yahtzee.gen_all_holds([0, 2, 2, 3]), set([(), (0, ), (2, ), (3, ),
                                                           (0, 2), (0, 3), (2, 2), 
                                                           (2, 3), (0, 2, 3), (0, 2, 2),
                                                           (2, 2, 3), (0, 2, 2, 3)]))
        self.assertEqual(yahtzee.gen_all_holds([0, 2, 2, 3, 3]), set([(0, 3, 3), (0,), (0, 2, 3, 3),
                                                           (2, 2, 3), (2,), (2, 2, 3, 3), 
                                                           (3,), (0, 2, 2), (0, 2, 3), (),
                                                           (2, 3), (2, 3, 3), (2, 2), 
                                                           (0, 2, 2, 3), (0, 3), (0, 2, 2, 3, 3),
                                                           (0, 2), (3, 3)]))     


class GenAllSequencesTest(unittest.TestCase):
    """
    Tests for gen_all_sequences method
    """

    def test_gen_all_sequences_length_one(self):
        """
        Test the case for all sequences of length 1
        """
        yahtzee = YahtzeePsychicPlain()

        self.assertEqual(yahtzee.gen_all_sequences([4, 5, 3], 1), set([(4,), (5,), (3,)]))

    def test_gen_all_sequences_length_two(self):
        """
        Test the case for all sequences of length 2
        """
        yahtzee = YahtzeePsychicPlain()

        self.assertEqual(yahtzee.gen_all_sequences([4, 5, 3], 2), set([(4, 5), (4, 4), (4, 3),
                                                              (5, 5), (5, 4), (5, 3),
                                                              (3, 3), (3, 4), (3, 5)]))

    def test_gen_all_sequences_length_three(self):
        """
        Test the case for all sequences of length 3
        """
        yahtzee = YahtzeePsychicPlain()

        self.assertEqual(yahtzee.gen_all_sequences([4, 5], 3), set([(4, 4, 4), (4, 4, 5), (4, 5, 4),
                                                            (4, 5, 5), (5, 4, 4), (5, 4, 5),
                                                            (5, 5, 4), (5, 5, 5)]))

class RecursiveGenHoldsTest(unittest.TestCase):
    """
    Test recursive_gen_holds method
    """
    def test(self):
        """
        Basic test for recursive_gen_holds
        """
        yahtzee = YahtzeePsychicPlain()

        holds = set([()])
        self.assertEqual(yahtzee.recursive_gen_holds([1], 1, holds), set([(), (1, )]))
        holds = set([()])
        self.assertEqual(yahtzee.recursive_gen_holds([0, 1, 2], 3, holds), 
                                              set([(), (0, ), (1, ), (2, ),
                                                  (0, 1), (0, 2), (1, 2),
                                                  (0, 1, 2)]))
        holds = set([()])
        self.assertEqual(yahtzee.recursive_gen_holds([0, 2, 2, 3], 4, holds),
                                             set([(), (0, ), (2, ), (3, ),
                                                 (0, 2), (0, 3), (2, 2), 
                                                 (2, 3), (0, 2, 3), (0, 2, 2),
                                                 (2, 2, 3), (0, 2, 2, 3)]))
        holds = set([()])
        self.assertEqual(yahtzee.recursive_gen_holds([0, 2, 2, 3, 3], 5, holds), 
                                            set([(0, 3, 3), (0,), (0, 2, 3, 3),
                                                (2, 2, 3), (2,), (2, 2, 3, 3), 
                                                (3,), (0, 2, 2), (0, 2, 3), (),
                                                (2, 3), (2, 3, 3), (2, 2), 
                                                (0, 2, 2, 3), (0, 3), (0, 2, 2, 3, 3),
                                                (0, 2), (3, 3)]))

class GenerateSortedSequenceTest(unittest.TestCase):
    """
    Test generate_sorted_sequence method
    """
    def test(self):
        """
        Basic test for generate_sorted_sequence
        """      
        yahtzee = YahtzeePsychicPlain()

        self.assertEqual(yahtzee.generate_sorted_sequence((1, 2, 3), 4), (1, 2, 3, 4))
        self.assertEqual(yahtzee.generate_sorted_sequence((5, 2, 3), 4), (2, 3, 4, 5))


class AddHoldToSetTest(unittest.TestCase):
    """
    Test add_hold_to_set method
    """
    def test(self):
        """
        Basic test for add_hold_to_set
        """
        yahtzee = YahtzeePsychicPlain()

        temp_set = set()
        self.assertEqual(yahtzee.add_hold_to_set(temp_set, (1, 2, 5), 5), set([(1, 2, 5), (1, 2, 5, 5)]))
        self.assertEqual(yahtzee.add_hold_to_set(temp_set, (2, 3, 4), 6), set([(1, 2, 5), (1, 2, 5, 5),
                                                                       (2, 3, 4), (2, 3, 4, 6)]))

class UpdateHoldTest(unittest.TestCase):
    """
    Test update_hold method
    """
    def test(self):
        """
        Basic test for update_hold
        """
        yahtzee = YahtzeePsychicPlain()

        temp_set = set()
        self.assertEqual(yahtzee.update_hold(temp_set, (1, 2), (1, 1, 2, 3)), set([(1, 2), (1, 2, 3), (1, 1, 2)]))
        temp_set = set()
        self.assertEqual(yahtzee.update_hold(temp_set, (1, 2, 5), (1, 2, 3, 4, 5)), set([(1, 2, 5), (1, 2, 3, 5), (1, 2, 4, 5)]))

class GeneratePartialHoldsTest(unittest.TestCase):
    """
    Test generate_partial_holds method
    """
    def test(self):
        """
        Basic test for generate_partial_holds
        """
        yahtzee = YahtzeePsychicPlain()

        holds = set([(1, 2, 5), (1, 2, 3, 5), (1, 2, 4, 5)])
        self.assertEqual(yahtzee.generate_temp_holds((1, 2, 3, 4, 5), holds), set([(1, 2, 5), (1, 2, 3, 5), (1, 2, 4, 5), (1, 2, 3, 4, 5)]))
        holds = set([()])
        self.assertEqual(yahtzee.generate_temp_holds((1, 2), holds), set([(), (1, ), (2, )]))
        holds = set([(), (1, ), (2, )])
        self.assertEqual(yahtzee.generate_temp_holds((1, 2), holds), set([(), (1, ), (2, ), (1, 2)]))

class UpdateSetTest(unittest.TestCase):
    """
    Test update_set method
    """
    def test(self):
        """
        Basic test for update_set
        """  
        yahtzee = YahtzeePsychicPlain()
        
        temp_set = set()
        self.assertEqual(yahtzee.update_set(temp_set, (1, 2), 3), set([(1, 2, 3)]))
        temp_set = set([(1, 2, 5), (1, 2, 3, 5), (1, 2, 4, 5)])
        self.assertEqual(yahtzee.update_set(temp_set, (1, 2, 4, 5), 3), set([(1, 2, 5), (1, 2, 3, 5), (1, 2, 4, 5), (1, 2, 4, 5, 3)]))
               
class AddOutComeToTempsetTest(unittest.TestCase):
    """
    Test add_outcome_to_tempset method
    """
    def test(self):
        """
        Basic test for add_outcome_to_tempset
        """
        yahtzee = YahtzeePsychicPlain()

        temp_set = set()
        self.assertEqual(yahtzee.add_outcome_to_tempset(temp_set, (1, 2), [3, 2]), set([(1, 2, 3), (1, 2, 2)]))    
        temp_set = set([(1, 2), (1, 3)])
        self.assertEqual(yahtzee.add_outcome_to_tempset(temp_set, (1, 2), [5]), set([(1, 2), (1, 3), (1, 2, 5)]))    

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
        yahtzee = YahtzeePsychicPlain()

        all_sequences = set([()])
        outcomes = [3, 4]
        self.assertEqual(yahtzee.update_sequences(all_sequences, outcomes), set([(3, ), (4, )]))
        all_sequences = set([(3, ), (4, )])
        self.assertEqual(yahtzee.update_sequences(all_sequences, outcomes), set([(3, 3), (3, 4), (4, 4), (4, 3)]))
