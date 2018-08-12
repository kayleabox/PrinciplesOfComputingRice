import unittest
from unittest.mock import patch

from i_yahtzee_psychic import IYahtzeePsychic

class IYahtzeePsychicTest(unittest.TestCase):
    @patch.multiple(IYahtzeePsychic, __abstractmethods__=set())
    def i_yahtzee_test(self):
         self.instance = IYahtzeePsychic()