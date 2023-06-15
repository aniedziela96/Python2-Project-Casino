from poker.poker_player import Poker_Player

class Croupier(Poker_Player):
    """Class representing croupier that will be playing poker
    """
    def __init__(self) -> None:
        """Constructor of croupier
        """
        super().__init__("Bodzio", 0)

    def croupier_bet(self) -> None:
        pass
        #TODO: maybe in the future

    def croupier_match(self, last_bet) -> None:
        pass
        #TODO: 