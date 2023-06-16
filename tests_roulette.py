from roulette.bet import Bet
from roulette.dozens import Dozens
from roulette.eighteens import Eighteens
from roulette.fournumbers import FourNumbers
from roulette.threenumbers import ThreeNumbers
from roulette.twonumbers import TwoNumbers
from roulette.onenumber import OneNumber
from roulette.evenodd import EvenOdd
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.dozens1 = Dozens(1)
        self.dozens2 = Dozens(2)
        self.dozens3 = Dozens(3)
        self.eighteens1 = Eighteens(1)
        self.eighteens2 = Eighteens(2)
        self.evenodd1 = EvenOdd(1)
        self.evenodd2 = EvenOdd(2)
        self.fournumbers = FourNumbers([1, 2, 3, 4])
        self.threenumbers = ThreeNumbers([1, 2, 3])
        self.twonumbers = TwoNumbers([1, 2])
        self.onenumber = OneNumber(1)

    def test_is_in_bet(self):
        self.assertEqual(self.dozens1.is_in_bet(30), False)
        self.assertEqual(self.dozens2.is_in_bet(20), True)
        self.assertEqual(self.dozens2.is_in_bet(1), False)
        self.assertEqual(self.dozens3.is_in_bet(30), True)
        self.assertEqual(self.dozens3.is_in_bet(1), False)
        self.assertEqual(self.dozens2.is_in_bet(20), True)
        self.assertEqual(self.eighteens1.is_in_bet(1), True)
        self.assertEqual(self.eighteens1.is_in_bet(20), False)
        self.assertEqual(self.eighteens2.is_in_bet(20), True)
        self.assertEqual(self.eighteens2.is_in_bet(1), False)
        self.assertEqual(self.eighteens1.is_in_bet(1), True)
        self.assertEqual(self.evenodd1.is_in_bet(20), True)
        self.assertEqual(self.evenodd1.is_in_bet(21), False)
        self.assertEqual(self.evenodd2.is_in_bet(20), False)
        self.assertEqual(self.evenodd2.is_in_bet(21), True)
        self.assertEqual(self.fournumbers.is_in_bet(1), True)
        self.assertEqual(self.fournumbers.is_in_bet(30), False)
        self.assertEqual(self.threenumbers.is_in_bet(1), True)
        self.assertEqual(self.threenumbers.is_in_bet(30), False)
        self.assertEqual(self.twonumbers.is_in_bet(1), True)
        self.assertEqual(self.twonumbers.is_in_bet(30), False)
        self.assertEqual(self.onenumber.is_in_bet(1), True)
        self.assertEqual(self.onenumber.is_in_bet(30), False)


if __name__ == "__main__":
    unittest.main()
