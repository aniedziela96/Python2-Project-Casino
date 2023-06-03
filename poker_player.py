from player import Player
from hand import Hand

class Poker_Player(Player):
    def __init__(self, name: str, money: int) -> None:
        super().__init__(name, money)
        self.hand = Hand()
        self.rank = None

    def draw_cards(self, cards: list):
        self.hand.add_cards(cards)

    def __str__(self) -> str:
        return self.name + str(self.hand)
    
    def rank(self):
        if self.hand.is_five():
            setattr(self.rank, "rank", self.hand.rank())



    
