import sys
sys.path.insert(0, 'C:/Users/niedz/Documents/Python projects/Casino/Python2-Project-Casino')
import unittest
from poker.deck import Deck
from poker.cards import Rank, Suit
from poker.hand import Hand
from poker.poker_player import Poker_Player
from main.player import Player 

class TestDeckMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.deck_1 = Deck()
        self.hand_1 = Hand()
        self.hand_2 = Hand()
        self.poker_player = Poker_Player("rysio", 1000)


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

    # def test_poker_player_init(self):
    #     self.assertEqual(self.poker_player.name, "rysio")
    #     self.assertEqual(self.poker_player.wallet, 1000)


if __name__ == '__main__':
    unittest.main()