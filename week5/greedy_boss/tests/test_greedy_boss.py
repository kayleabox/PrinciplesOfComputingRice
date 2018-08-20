import unittest

from greedy_boss import (GreedyBoss, LOGLOG, STANDARD)

class TrialTest(unittest.TestCase):
    def test(self):
        gb = GreedyBoss(35, STANDARD)
        self.assertEqual(gb.greedy_boss(100), [(0, 0), (10, 1000),
                                               (16, 2200), (20, 3400),
                                               (23, 4600), (26, 6100),
                                               (29, 7900), (31, 9300),
                                               (33, 10900), (35, 12700)])
        gb = GreedyBoss(35, STANDARD)
        self.assertEqual(gb.greedy_boss(0), [(0, 0), (10, 1000), (15, 2000),
                                             (19, 3200), (21, 4000), (23, 5000),
                                             (25, 6200), (27, 7600), (28, 8400),
                                             (29, 9300), (30, 10300),
                                             (31, 11400), (32, 12600),
                                             (33, 13900), (34, 15300),
                                             (34, 15300), (35, 16900)])
