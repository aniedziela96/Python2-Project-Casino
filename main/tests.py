import sys
sys.path.insert(0, '/Users/hss/Documents/Python2-Project-Casino')

from main.casino import Casino
from main.player import Player
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.player = Player("Tester", 100)
        self.casino = Casino("none")

    def test_check_tokens(self):
        self.assertEqual(self.casino.check_tokens(99, self.player, True), True)
        self.assertEqual(self.casino.check_tokens(101, self.player, True), False)


if __name__ == "__main__":
    unittest.main()