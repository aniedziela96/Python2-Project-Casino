import unittest
from deck import Deck
from cards import Rank, Suit

class TestDeckMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.deck_1 = Deck()
    
    def test_is_empty(self):
        self.assertFalse(self.deck_1.is_empty())
        Deck.draw(self.deck_1, n = 51)
        self.assertTrue(self.deck_1.is_empty())

    def test_draw(self):
        self.assertEqual(self.deck_1.draw(n = 1), [(Rank.ACE, Suit.CLUBS)])
        with self.assertRaises(IndexError):
            Deck.draw(self.deck_1, n = 100)


if __name__ == '__main__':
    unittest.main()