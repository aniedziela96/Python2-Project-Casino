from poker.poker_player import Poker_Player
from poker.hand import Hand

class Croupier(Poker_Player):
    def __init__(self) -> None:
        super().__init__("Bogus", 0)
        self.hand = Hand()

    def croupiers_bet(self):
        pass
        #TODO: maybe in the future

    def croupier_match(self, last_bet):
        pass
        #TODO: 