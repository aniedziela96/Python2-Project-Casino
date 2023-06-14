from poker.hand import Hand
from poker.deck import Deck

class Blackjack_hand(Hand):
    """ Represents a hand in blackjack game. 
    """
    def __init__(self) -> None:
        """Blackjack_hand constructor
        """
        super().__init__()
        self.score = 0

    def calculate_score(self) -> None:
        """Calculates and sets the score for hand. Sums the value of each card in hand,
            ace has a value 11 or 1, depending what is best for player.
        """
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
                    

    def is_pair(self) -> bool:
        """Checks if cards in hand have the same value

        :raises IndexError: This is only possible if there are exacly two cards in hand
        ...
        :return: `True` if both cards hae the same value, `False` otherwise
        :rtype: bool
        """
        if len(self.cards) != 2:
            raise IndexError("Only possible if there are two cards")
        
        if self.cards[0][0] == self.cards[1][0]:
            return True
        else:
            return False
        
    def card_split(self) -> tuple:
        """Removes the second card from the hand.

        :raises IndexError: This is only possible if there are exacly two cards in hand
        ...
        :return: Card that has been removed
        :rtype: tuple
        """
        if self.is_pair():
            raise ValueError("Only possible if there are two cards")
        
        card_splitted = self.cards.pop()
        return card_splitted

