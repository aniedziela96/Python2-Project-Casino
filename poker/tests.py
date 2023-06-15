import unittest
import sys
sys.path.insert(0, 'C:/Users/niedz/Documents/Python projects/Casino/Casino')
from poker.deck import Deck
from poker.cards import Rank, Suit
from poker.hand import Hand
from poker.poker_player import Poker_Player
from main.player import Player 
from poker.poker_human import Poker_human
from poker.winners import Winners

class TestDeckMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.deck_1 = Deck()
        self.hand_1 = Hand()
        self.hand_2 = Hand()
        self.poker_player = Poker_Player("rysio", 1000)
        self.bodzio = Poker_human("bodzio", 1000)
        self.rysio = Poker_human("rysio", 1000)


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
        self.hand_1.add_cards([(Rank.ACE, Suit.CLUBS), (Rank.FIVE, Suit.DIAMONDS),
                               (Rank.SIX, Suit.SPADES), (Rank.EIGHT, Suit.DIAMONDS),
                               (Rank.KING, Suit.CLUBS)])
        self.assertEqual(self.hand_1.rank(), "High card")
        self.hand_1 = Hand()
        self.hand_1.add_cards([(Rank.ACE, Suit.CLUBS), (Rank.FIVE, Suit.DIAMONDS),
                               (Rank.SIX, Suit.SPADES), (Rank.ACE, Suit.DIAMONDS),
                               (Rank.KING, Suit.CLUBS)])
        self.assertEqual(self.hand_1.rank(), "Pair")
        self.hand_1 = Hand()
        self.hand_1.add_cards([(Rank.ACE, Suit.CLUBS), (Rank.FIVE, Suit.DIAMONDS),
                               (Rank.SIX, Suit.SPADES), (Rank.ACE, Suit.DIAMONDS),
                               (Rank.FIVE, Suit.CLUBS)])
        self.assertEqual(self.hand_1.rank(), "Two Pair")
        self.hand_1 = Hand()
        self.hand_1.add_cards([(Rank.FIVE, Suit.CLUBS), (Rank.FIVE, Suit.DIAMONDS),
                               (Rank.FIVE, Suit.SPADES), (Rank.ACE, Suit.DIAMONDS),
                               (Rank.KING, Suit.CLUBS)])
        self.assertEqual(self.hand_1.rank(), "Three of a kind")
        self.hand_1 = Hand()
        self.hand_1.add_cards([(Rank.FOUR, Suit.CLUBS), (Rank.FIVE, Suit.DIAMONDS),
                               (Rank.SIX, Suit.SPADES), (Rank.SEVEN, Suit.DIAMONDS),
                               (Rank.EIGHT, Suit.CLUBS)])
        self.assertEqual(self.hand_1.rank(), "Straight")
        self.hand_1 = Hand()
        self.hand_1.add_cards([(Rank.ACE, Suit.CLUBS), (Rank.FIVE, Suit.CLUBS),
                               (Rank.SIX, Suit.CLUBS), (Rank.SEVEN, Suit.CLUBS),
                               (Rank.KING, Suit.CLUBS)])
        self.assertEqual(self.hand_1.rank(), "Flush")
        self.hand_1 = Hand()
        self.hand_1.add_cards([(Rank.ACE, Suit.CLUBS), (Rank.FIVE, Suit.DIAMONDS),
                               (Rank.FIVE, Suit.SPADES), (Rank.ACE, Suit.DIAMONDS),
                               (Rank.FIVE, Suit.CLUBS)])
        self.assertEqual(self.hand_1.rank(), "Full House")
        self.hand_1 = Hand()
        self.hand_1.add_cards([(Rank.FIVE, Suit.CLUBS), (Rank.FIVE, Suit.DIAMONDS),
                               (Rank.FIVE, Suit.SPADES), (Rank.ACE, Suit.DIAMONDS),
                               (Rank.FIVE, Suit.HEARTS)])
        self.assertEqual(self.hand_1.rank(), "Four of a kind")
        self.hand_1 = Hand()
        self.hand_1.add_cards([(Rank.FOUR, Suit.CLUBS), (Rank.FIVE, Suit.CLUBS),
                               (Rank.SIX, Suit.CLUBS), (Rank.SEVEN, Suit.CLUBS),
                               (Rank.EIGHT, Suit.CLUBS)])
        self.assertEqual(self.hand_1.rank(), "Straight Flush")
        self.hand_1 = Hand()
        self.hand_1.add_cards([(Rank.TEN, Suit.CLUBS), (Rank.JACK, Suit.CLUBS),
                               (Rank.QUEEN, Suit.CLUBS), (Rank.KING, Suit.CLUBS),
                               (Rank.ACE, Suit.CLUBS)])
        self.assertEqual(self.hand_1.rank(), "Royal Flush")
        self.hand_1.add_cards(self.deck_1.draw(16))
        with self.assertRaises(IndexError):
            self.hand_1.rank()

    def test_players_bet(self):
        self.assertTrue(self.rysio.players_bet(100))
        self.assertFalse(self.rysio.players_bet(10000000))
        self.assertEqual(self.rysio.players_bet(900), 'all_in')


    def test_winners_high_card(self):
        self.rysio.draw_cards([(Rank.ACE, Suit.CLUBS), (Rank.FIVE, Suit.DIAMONDS),
                               (Rank.SIX, Suit.SPADES), (Rank.EIGHT, Suit.DIAMONDS),
                               (Rank.KING, Suit.CLUBS)])
        self.bodzio.draw_cards([(Rank.ACE, Suit.CLUBS), (Rank.FIVE, Suit.DIAMONDS),
                               (Rank.SEVEN, Suit.SPADES), (Rank.EIGHT, Suit.DIAMONDS),
                               (Rank.KING, Suit.CLUBS)])
        w = Winners(self.rysio, self.bodzio)
        self.assertEqual(w.winner_high_card().name, "bodzio")

    def test_winners_same_pair(self):
        self.rysio.draw_cards([(Rank.SIX, Suit.CLUBS), (Rank.FIVE, Suit.DIAMONDS),
                               (Rank.FOUR, Suit.SPADES), (Rank.SIX, Suit.HEARTS),
                               (Rank.TWO, Suit.CLUBS)])
        self.bodzio.draw_cards([(Rank.SIX, Suit.SPADES), (Rank.SIX, Suit.DIAMONDS),
                               (Rank.SEVEN, Suit.SPADES), (Rank.EIGHT, Suit.DIAMONDS),
                               (Rank.KING, Suit.HEARTS)])
        w = Winners(self.rysio, self.bodzio)
        self.assertEqual(w.winner_pair().name, "bodzio")

    def test_winners_pair(self):
        self.rysio.draw_cards([(Rank.ACE, Suit.CLUBS), (Rank.FIVE, Suit.DIAMONDS),
                               (Rank.SIX, Suit.SPADES), (Rank.ACE, Suit.DIAMONDS),
                               (Rank.KING, Suit.CLUBS)])
        self.bodzio.draw_cards([(Rank.ACE, Suit.CLUBS), (Rank.KING, Suit.DIAMONDS),
                               (Rank.SEVEN, Suit.SPADES), (Rank.EIGHT, Suit.DIAMONDS),
                               (Rank.KING, Suit.CLUBS)])
        w = Winners(self.rysio, self.bodzio)
        self.assertEqual(w.winner_pair().name, "rysio")

    def test_winners_two_pairs(self):
        self.rysio.draw_cards([(Rank.SIX, Suit.CLUBS), (Rank.KING, Suit.DIAMONDS),
                               (Rank.SIX, Suit.SPADES), (Rank.ACE, Suit.DIAMONDS),
                               (Rank.KING, Suit.CLUBS)])
        self.bodzio.draw_cards([(Rank.EIGHT, Suit.CLUBS), (Rank.KING, Suit.HEARTS),
                               (Rank.SEVEN, Suit.SPADES), (Rank.EIGHT, Suit.DIAMONDS),
                               (Rank.KING, Suit.SPADES)])
        w = Winners(self.rysio, self.bodzio)
        self.assertEqual(w.winner_two_pairs().name, "bodzio")

    def test_winners_three_of_a_kind(self):
        self.rysio.draw_cards([(Rank.ACE, Suit.HEARTS), (Rank.ACE, Suit.DIAMONDS),
                               (Rank.SIX, Suit.SPADES), (Rank.ACE, Suit.CLUBS),
                               (Rank.KING, Suit.HEARTS)])
        self.bodzio.draw_cards([(Rank.SEVEN, Suit.CLUBS), (Rank.FIVE, Suit.DIAMONDS),
                               (Rank.SEVEN, Suit.SPADES), (Rank.SEVEN, Suit.DIAMONDS),
                               (Rank.KING, Suit.CLUBS)])
        w = Winners(self.rysio, self.bodzio)
        self.assertEqual(w.winner_three_of_a_kind().name, "rysio")

    def test_winners_straight(self):
        self.rysio.draw_cards([(Rank.SIX, Suit.CLUBS), (Rank.TEN, Suit.DIAMONDS),
                               (Rank.SEVEN, Suit.SPADES), (Rank.NINE, Suit.DIAMONDS),
                               (Rank.EIGHT, Suit.CLUBS)])
        self.bodzio.draw_cards([(Rank.EIGHT, Suit.CLUBS), (Rank.JACK, Suit.HEARTS),
                               (Rank.TEN, Suit.SPADES), (Rank.NINE, Suit.DIAMONDS),
                               (Rank.QUEEN, Suit.CLUBS)])
        w = Winners(self.rysio, self.bodzio)
        self.assertEqual(w.winner_straight().name, "bodzio")

    def test_winners_flush(self):
        self.rysio.draw_cards([(Rank.ACE, Suit.CLUBS), (Rank.FIVE, Suit.CLUBS),
                               (Rank.SIX, Suit.CLUBS), (Rank.EIGHT, Suit.CLUBS),
                               (Rank.KING, Suit.CLUBS)])
        self.bodzio.draw_cards([(Rank.ACE, Suit.DIAMONDS), (Rank.FIVE, Suit.DIAMONDS),
                               (Rank.SEVEN, Suit.DIAMONDS), (Rank.EIGHT, Suit.DIAMONDS),
                               (Rank.KING, Suit.DIAMONDS)])
        w = Winners(self.rysio, self.bodzio)
        self.assertEqual(w.winner_high_card().name, "bodzio")

    def test_winners_full_house(self):
        self.rysio.draw_cards([(Rank.ACE, Suit.HEARTS), (Rank.ACE, Suit.DIAMONDS),
                               (Rank.SIX, Suit.SPADES), (Rank.ACE, Suit.CLUBS),
                               (Rank.SIX, Suit.HEARTS)])
        self.bodzio.draw_cards([(Rank.SEVEN, Suit.CLUBS), (Rank.KING, Suit.DIAMONDS),
                               (Rank.SEVEN, Suit.SPADES), (Rank.SEVEN, Suit.DIAMONDS),
                               (Rank.KING, Suit.CLUBS)])
        w = Winners(self.rysio, self.bodzio)
        self.assertEqual(w.winner_full_house().name, "rysio")

    def test_winners_four_of_a_kind(self):
        self.rysio.draw_cards([(Rank.ACE, Suit.HEARTS), (Rank.ACE, Suit.DIAMONDS),
                               (Rank.ACE, Suit.SPADES), (Rank.ACE, Suit.CLUBS),
                               (Rank.KING, Suit.HEARTS)])
        self.bodzio.draw_cards([(Rank.SEVEN, Suit.CLUBS), (Rank.SEVEN, Suit.HEARTS),
                               (Rank.SEVEN, Suit.SPADES), (Rank.SEVEN, Suit.DIAMONDS),
                               (Rank.KING, Suit.CLUBS)])
        w = Winners(self.rysio, self.bodzio)
        self.assertEqual(w.winner_four_of_a_kind().name, "rysio")

    def test_winners_straight_flussh(self):
        self.rysio.draw_cards([(Rank.QUEEN, Suit.HEARTS), (Rank.TEN, Suit.HEARTS),
                               (Rank.JACK, Suit.HEARTS), (Rank.NINE, Suit.HEARTS),
                               (Rank.KING, Suit.HEARTS)])
        self.bodzio.draw_cards([(Rank.SEVEN, Suit.CLUBS), (Rank.FOUR, Suit.CLUBS),
                               (Rank.SIX, Suit.CLUBS), (Rank.FIVE, Suit.CLUBS),
                               (Rank.EIGHT, Suit.CLUBS)])
        w = Winners(self.rysio, self.bodzio)
        self.assertEqual(w.winner_straight_flush().name, "rysio")

    def test_winners_royal_flush(self):
        self.rysio.draw_cards([(Rank.QUEEN, Suit.HEARTS), (Rank.TEN, Suit.HEARTS),
                               (Rank.JACK, Suit.HEARTS), (Rank.ACE, Suit.HEARTS),
                               (Rank.KING, Suit.HEARTS)])
        self.bodzio.draw_cards([(Rank.KING, Suit.CLUBS), (Rank.QUEEN, Suit.CLUBS),
                               (Rank.JACK, Suit.CLUBS), (Rank.ACE, Suit.CLUBS),
                               (Rank.TEN, Suit.CLUBS)])
        w = Winners(self.rysio, self.bodzio)
        self.assertEqual(w.winner_royal_flush(), "JACKPOT")


if __name__ == '__main__':
    unittest.main()