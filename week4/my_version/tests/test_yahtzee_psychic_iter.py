import unittest

from i_yahtzee_psychic import IYahtzeePsychic
from yahtzee_psychic import YahtzeePsychic
from yahtzee_psychic_iter import YahtzeePsychicIter

class YahtzeePsychicTest(unittest.TestCase):
    def test(self):
        yahtzee_psychic = YahtzeePsychicIter()
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
        yahtzee = YahtzeePsychicIter()

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
        yahtzee = YahtzeePsychicIter()

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

class GenAllSequencesTest(unittest.TestCase):
    """
    Tests for gen_all_sequences method
    """
    def test_gen_all_sequences_length_one(self):
        """
        Test the case for all sequences of length 1
        """
        yahtzee = YahtzeePsychicIter()

        self.assertEqual(yahtzee.gen_all_sequences([4, 5, 3], 1), set([(4,), (5,), (3,)]))

    def test_gen_all_sequences_length_two(self):
        """
        Test the case for all sequences of length 2
        """
        yahtzee = YahtzeePsychicIter()

        self.assertEqual(yahtzee.gen_all_sequences([4, 5, 3], 2), set([(4, 5), (4, 4), (4, 3),
                                                              (5, 5), (5, 4), (5, 3),
                                                              (3, 3), (3, 4), (3, 5)]))

    def test_gen_all_sequences_length_three(self):
        """
        Test the case for all sequences of length 3
        """
        yahtzee = YahtzeePsychicIter()

        self.assertEqual(yahtzee.gen_all_sequences([4, 5], 3), set([(4, 4, 4), (4, 4, 5), (4, 5, 4),
                                                            (4, 5, 5), (5, 4, 4), (5, 4, 5),
                                                            (5, 5, 4), (5, 5, 5)]))

class GenAllHoldsTest(unittest.TestCase):
    """
    Test gen_all_holds method
    """
    def test(self):
        """
        Test that gen_all_holds returns a set of all of
        sorted tuples containing all of the possible holds
        """
        yahtzee = YahtzeePsychicIter()

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
