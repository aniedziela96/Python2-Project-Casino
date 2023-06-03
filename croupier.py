from poker_player import Poker_Player
from hand import Hand

class Croupier(Poker_Player):
    def __init__(self, name: str, money: int) -> None:
        super().__init__("Bogus", money)
        self.hand = Hand()

    def croupiers_bet(self):
        pass