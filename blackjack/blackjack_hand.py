from poker.hand import Hand
from poker.deck import Deck

class Blackjack_hand(Hand):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0

    def calculate_score(self):
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

