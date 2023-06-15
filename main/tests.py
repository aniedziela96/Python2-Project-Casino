from casino import Casino
from player import Player
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