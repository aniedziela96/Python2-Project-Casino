from poker.cards import Rank, Suit
from random import shuffle

class Deck:
    "Class representing a deck of cards"
    def __init__(self) -> None:
        """Constructior method for deck, iterates through the Suits and Ranks, to 
        every possible card.
        """
        self.card_list = []
        for suit in Suit:
            for rank in Rank:
                self.card_list.append((rank, suit))

    def shuffle(self) -> None:
        """Shuffles the deck
        """
        shuffle(self.card_list)

    def is_empty(self) -> bool:
        """Checks if the deck is empty

        :return: `True` if there are no cards in the deck, `False` otherwise
        :rtype: bool
        """
        if len(self.card_list) == 0:
            return True
        else:
            return False

    def draw(self, n = 1) -> list:
        """Draws `n` cards from a deck.

        :raises IndexError: if `n` is greater than the number of cards in the deck 
            raises an Error, it is not possible to draw from empt deck.
        ...
        :return: list of cards that were drawn
        :rtype: list
        """
        drawn_cards = []
        for i in range(n):
            if not self.is_empty():
                drawn_cards.append(self.card_list.pop(-1))
            else:
                raise IndexError ('Deck is empty')
                
        return drawn_cards


