from blackjack.blackjack_hand import Black_jack_hand
from main.player import Player

class Blackjack_player(Player):
    def __init__(self, name: str, tokens: int) -> None:
        super().__init__(name, tokens)
        self.hands = [Black_jack_hand()]

    def hit(self, card, hand_number = 0):
        self.hands[hand_number].add_cards(card)
        
