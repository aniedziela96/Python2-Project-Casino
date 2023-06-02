import unittest
from deck import Deck
from cards import Rank, Suit
from hand import Hand

class TestDeckMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.deck_1 = Deck()
        self.hand_1 = Hand()
        self.hand_2 = Hand()


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


    def test_one_color(self):
        self.hand_1.add_cards([(Rank.ACE, Suit.CLUBS), (Rank.ACE, Suit.HEARTS)])
        self.hand_2.add_cards(self.deck_1.draw(7))
        self.assertFalse(self.hand_1.is_one_color())
        self.assertTrue(self.hand_2.is_one_color())
        self.hand_2.add_cards([(Rank.ACE, Suit.HEARTS)])
        self.assertFalse(self.hand_2.is_one_color())

    def test_is_straight(self):
        self.hand_1.add_cards([(Rank.ACE, Suit.CLUBS), (Rank.ACE, Suit.HEARTS)])
        self.hand_2.add_cards(self.deck_1.draw(7))
        self.assertFalse(self.hand_1.is_straight())
        self.assertTrue(self.hand_2.is_straight())

    def test_rank(self):
        #TODO: test rank function
        pass


if __name__ == '__main__':
    unittest.main()