from deck import Deck
from cards import Rank, Suit
from hand import Hand, HAND_RANKS

class Poker_Game():
    def __init__(self, player) -> None:
        self.poker_player = player