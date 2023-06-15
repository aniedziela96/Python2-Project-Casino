import unittest
import sys
sys.path.insert(0, 'C:/Users/niedz/Documents/Python projects/Casino/Casino')
from blackjack.blackjack_hand import Blackjack_hand

class TestDeckMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.bj_hand_1 = Blackjack_hand()

if __name__ == '__main__':
    unittest.main()