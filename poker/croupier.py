from poker.poker_player import Poker_Player

class Croupier(Poker_Player):
    def __init__(self) -> None:
        super().__init__("Bodzio", 0)

    def croupier_bet(self) -> None:
        pass
        #TODO: maybe in the future

    def croupier_match(self, last_bet) -> None:
        pass
        #TODO: 