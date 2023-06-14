from poker.cards import Rank, Suit
from random import shuffle

# The Deck class represents a deck of cards and provides methods for shuffling, checking if it's
# empty, and drawing cards from it.
class Deck:
    def __init__(self) -> None:
        self.card_list = []
        for suit in Suit:
            for rank in Rank:
                self.card_list.append((rank, suit))

    def shuffle(self) -> None:
        shuffle(self.card_list)

    def is_empty(self) -> bool:
        if len(self.card_list) == 0:
            return True
        else:
            return False

    def draw(self, n = 1) -> list:
        drawn_cards = []
        for i in range(n):
            if not self.is_empty():
                drawn_cards.append(self.card_list.pop(-1))
            else:
                raise IndexError ('Deck is empty')
                
        return drawn_cards


