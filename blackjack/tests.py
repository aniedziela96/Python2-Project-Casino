import unittest
import sys
sys.path.insert(0, 'C:/Users/niedz/Documents/Python projects/Casino/Casino')
from blackjack_hand import Blackjack_hand
from poker.cards import Rank, Suit
from blackjack.blackjack_game import Blackjack
from blackjack.croupier_bj import Croupier_bj
from blackjack_player import Blackjack_player
from poker.deck import Deck

class TestDeckMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.bj_hand_1 = Blackjack_hand()
        self.bj_hand_2 = Blackjack_hand()
        self.croupier = Croupier_bj()
        self.deck = Deck()
        self.bj_player = Blackjack_player("rysio", 1000)
        self.bj_player.add_bet(self.bj_hand_1)
        self.blackjack = Blackjack(self.croupier, self.bj_player, 200, self.deck)

    def test_calculate_score(self):
        self.bj_hand_1.add_cards([(Rank.ACE, Suit.CLUBS), (Rank.SIX, Suit.SPADES)])
        self.bj_hand_1.calculate_score()
        self.assertEqual(self.bj_hand_1.score, 17)
        self.bj_hand_1.add_cards([(Rank.THREE, Suit.CLUBS)])
        self.bj_hand_1.calculate_score()
        self.assertEqual(self.bj_hand_1.score, 20)
        self.bj_hand_1.add_cards([(Rank.ACE, Suit.DIAMONDS)])
        self.bj_hand_1.calculate_score()
        self.assertEqual(self.bj_hand_1.score, 21)

    def test_split(self):
        self.bj_hand_1.add_cards([(Rank.ACE, Suit.CLUBS), (Rank.SIX, Suit.SPADES)])
        with self.assertRaises(ValueError):
            self.bj_hand_1.card_split()
        self.bj_hand_2.add_cards([(Rank.FIVE, Suit.CLUBS), (Rank.FIVE, Suit.DIAMONDS)])
        self.assertEqual(self.bj_hand_2.card_split(), ((Rank.FIVE, Suit.DIAMONDS)))
        

    def test_is_pair(self):
        self.bj_hand_1.add_cards([(Rank.ACE, Suit.CLUBS), (Rank.SIX, Suit.SPADES)])
        self.assertFalse(self.bj_hand_1.is_pair())
        self.bj_hand_1.add_cards([(Rank.FIVE, Suit.CLUBS)])
        with self.assertRaises(IndexError):
            self.bj_hand_1.is_pair()
        self.bj_hand_2.add_cards([(Rank.SIX, Suit.CLUBS), (Rank.SIX, Suit.SPADES)])
        self.assertTrue(self.bj_hand_2.is_pair())
        
    def test_hit(self):
        self.assertEqual(self.blackjack.hit(), 'success')
        self.assertEqual(self.blackjack.hit(), 'success')
        self.assertEqual(self.blackjack.hit(), 'success')
        self.assertEqual(self.blackjack.hit(), 'bust')
        
        
if __name__ == '__main__':
    unittest.main()