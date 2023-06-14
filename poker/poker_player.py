from main.player import Player
from poker.hand import Hand

class Poker_Player(Player):
    def __init__(self, name: str, money: int) -> None:
        super().__init__(name, money)
        self.hand = Hand()
        self.hand_rank = None

    def draw_cards(self, cards: list):
        self.hand.add_cards(cards)

    def __str__(self) -> str:
        return self.name + str(self.hand)
    
    def rank(self) -> None:
        if self.hand.is_five():
            self.hand_rank = self.hand.rank()

    def show_player_hand(self):
        self.hand.show_hand()
