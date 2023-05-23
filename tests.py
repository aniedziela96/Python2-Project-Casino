import unittest
from deck import Deck
from cards import Rank, Suit
from hand import Hand

class TestDeckMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.deck_1 = Deck()
        self.hand_1 = Hand()

    def test_is_empty(self):
        self.assertFalse(self.deck_1.is_empty())
        Deck.draw(self.deck_1, n = 52)
        self.assertTrue(self.deck_1.is_empty())

    def test_draw(self): 
        self.assertEqual(self.deck_1.draw(n = 1), [(Rank.ACE, Suit.CLUBS)])
        with self.assertRaises(IndexError):
            Deck.draw(self.deck_1, n = 100)

    def test_add_cards(self):
        cards_drawn = self.deck_1.draw(6)
        self.hand_1.add_cards(cards_drawn)
        self.assertEqual(self.hand_1.cards, cards_drawn)

    def test_str_hand(self):
        self.hand_1.add_cards([(Rank.ACE, Suit.CLUBS), (Rank.ACE, Suit.HEARTS)])
        self.assertEqual(str(self.hand_1), "ACE OF CLUBS, ACE OF HEARTS")



if __name__ == '__main__':
    unittest.main()