from poker.hand import Hand
from poker.deck import Deck

class Blackjack_hand(Hand):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0

    def calculate_score(self):
        self.score = 0
        for card in sorted(self.cards):
            if card[0].value < 10:
                self.score += card[0].value
            elif card[0].value <= 13:
                self.score += 10
            else:
                if self.score <= 10:
                    self.score += 11
                else:
                    self.score += 1

    def is_pair(self):
        if len(self.cards) != 2:
            raise ValueError("Only possible if thera are two cards")
        
        if self.cards[0][0] == self.cards[1][0]:
            return True
        else:
            return False

