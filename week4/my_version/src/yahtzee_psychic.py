"""
base class that will give advice on which dice to keep while playing yahtzee
"""
from i_yahtzee_psychic import IYahtzeePsychic

class YahtzeePsychic(IYahtzeePsychic):
    def score(self, hand):
        """
        Compute the maximal score for a Yahtzee hand according to the
        upper section of the Yahtzee score card.

        hand: full yahtzee hand

        Returns an integer score
        """
        return max([hand.count(number) * number for number in hand])

    def expected_value(self, held_dice, num_die_sides, num_free_dice):
        """
        Compute the expected value based on held_dice given that there
        are num_free_dice to be rolled, each with num_die_sides.

        held_dice: dice that you will hold
        num_die_sides: number of sides on each die
        num_free_dice: number of dice to be rolled

        Returns a floating point expected value
        """
        dice_sides = range(1, num_die_sides+1)
        all_rolls = list(self.gen_all_sequences(dice_sides, num_free_dice))
        summed_scores = sum([self.score(held_dice + roll) for roll in all_rolls])
        num_rolls = float(len(all_rolls))
        return round(summed_scores/num_rolls, 11)

    def strategy(self, hand, num_die_sides):
        """
        Compute the hold that maximizes the expected value when the
        discarded dice are rolled.

        hand: full yahtzee hand
        num_die_sides: number of sides on each die

        Returns a tuple where the first element is the expected score and
        the second element is a tuple of the dice to hold
        """
        possible_holds = list(self.gen_all_holds(hand))
        return max([(self.expected_value(hold, num_die_sides, len(hand)-len(hold)), hold)
                    for hold in possible_holds])

    def gen_all_holds(self, hand):
        """
        Generate all possible choices of dice from hand to hold.

        hand: full yahtzee hand

        Returns a set of tuples, where each tuple is dice to hold
        """
        return set([(1, )])
    
    def gen_all_sequences(self, outcomes, length):
        """
        Iterative function that enumerates the set of all sequences of
        outcomes of given length.
        """
        return set([(1, )])

    def run_example(self):
        """
        Compute the dice to hold and expected score for an example hand
        """
        num_die_sides = 3
        hand = (1, 2, 1)
        print(self.gen_all_holds(hand))
        print(self.gen_all_sequences([1, 3, 4, 3], 2))
        hand_score, hold = self.strategy(hand, num_die_sides)
        print(f"Best strategy for hand {hand} is to hold {hold} with expected score {hand_score}")
