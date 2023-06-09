from poker.deck import Deck

HAND_RANKS = ['High card', 'Pair', 'Two Pair', 'Three of a kind', 
              'Straight', 'Flush', 'Full House', 'Four of a kind', 
           'Straight Flush', 'Royal Flush']

class Hand():
    """Class representing a hand with cards.
    """
    def __init__(self) -> None:
        """Constructor method
        """
        self.cards = []

    def add_cards(self, cards: list) -> None:
        """Adds the card to the hand.

        :param cards: a list of cards to be added to the hand
        :type cards: list
        """
        for card in cards:
            self.cards.append(card)
    
    def __str__(self) -> str:
        """String representation of a hand
        """
        cards_str = ""
        for card in self.cards:
            rank = str(card[0])

            suit = str(card[1])
        
            cards_str = cards_str + rank + suit + ", "

        return cards_str.removesuffix(", ")

    def is_one_color(self) -> bool:
        """Checks if the cards on the hand have the same suit

        :return: `True` if all the cards have the same suit, `False` otherwise
        :rtype: bool
        """
        for i in range(len(self.cards) - 1):
            if self.cards[i][1] != self.cards[i + 1][1]:
                return False
            
        return True
    
    def is_straight(self) -> bool:
        """Checks if after sorting the values of cards create sequence that are
            increasing by one -straight.

        :return: `True` if cards are straight, `False` otherwie
        :rtype: bool
        """
        sorted_cards = sorted(self.cards)
        for i in range(len(self.cards) - 1):
            if sorted_cards[i][0] + 1 != sorted_cards[i + 1][0]:
                return False
            
        return True
    
    def is_five(self) -> bool:
        """Checks if there are five cards on the hand

        :return: `True` if there are 5 cards on the hand, `False` otherwise
        :rtype: bool
        """
        if len(self.cards) == 5:
            return True
        else:
            return False

    def rank(self) -> str:
        """Checks a poker rank that the cards on the hand create.

        :raises IndexError: If there are not 5 cards on the hand raises an error, 
            the rank can be only determined for 5 cards.
        ...
        :return: The name of a rank
        :rtype: str
        """
        if not self.is_five():
            raise IndexError ('only possible for 5 cards hands')
        
        sorted_hand = sorted(self.cards)
        # checks if there is a pair - if there is there's no possibility for straight, colour etc.
        if sorted_hand[0][0] == sorted_hand[1][0] or \
           sorted_hand[1][0] == sorted_hand[2][0] or \
           sorted_hand[2][0] == sorted_hand[3][0] or \
           sorted_hand[3][0] == sorted_hand[4][0]:
        # checks if there are two pairs, there are the options
            if((sorted_hand[0][0] == sorted_hand[1][0] and
                (sorted_hand[2][0] == sorted_hand[3][0] or
                sorted_hand[3][0] == sorted_hand [4][0])) or
                (sorted_hand[1][0] == sorted_hand[2][0] and
                sorted_hand[3][0] == sorted_hand[4][0])):
            # checks if there is a three
                if(sorted_hand[0][0] == sorted_hand[2][0] or
                   sorted_hand[1][0] == sorted_hand[3][0] or 
                   sorted_hand[2][0] == sorted_hand[4][0]):
                # two possible options: full or four
                # checks for four, if it is not, then we have a full
                    if(sorted_hand[0][0] == sorted_hand[3][0] or
                       sorted_hand[1][0] == sorted_hand[4][0]):
                        return HAND_RANKS[7] 
                    else: 
                        return HAND_RANKS[6] # Full
                else:
                    return HAND_RANKS[2]
                    # Two Pairs, there's no Three, so it only can be Two Pairs
            elif (sorted_hand[0][0] == sorted_hand[2][0] or 
                  sorted_hand[1][0] == sorted_hand[3][0] or 
                  sorted_hand[2][0] == sorted_hand[4][0]):
            # Check for Three, but now without the Two Pairs
                    return HAND_RANKS[3]  # Three of a kind
            # if there is no Three or Two Pairs, there only can be a One Pair
            else:
                return HAND_RANKS[1]
    
        elif self.is_one_color(): #check for straight, flush
            if self.is_straight():
                if sorted_hand[0][0] == 10:
                    return HAND_RANKS[9] # Royal flush
                else: 
                    return HAND_RANKS[8] # Straight flush
            else:
                return HAND_RANKS[5] # flush
        elif self.is_straight():
            return HAND_RANKS[4] # straight 
        else: 
            return HAND_RANKS[0]
        
    def show_hand(self) -> None:
        """Shows a representation of a cards in the hand.
        """
        if self.cards == []:
            print(" ")
        else:
            empyt_row = "|           |   "
            top = " ___________    "
            bottom = "|___________|   "
            n = len(self.cards)
            rows_fig_top = ""
            rows_suit = ""
            rows_fig_bottom = ""
            for card in self.cards:
                if card[0] != 10:
                    rows_fig_top = rows_fig_top + "|  " + str(card[0]) + "        |   "
                    rows_suit = rows_suit + "|     " + str(card[1]) + "     |   "
                    rows_fig_bottom = rows_fig_bottom + "|        " + str(card[0]) + "  |   "
                else:
                    rows_fig_top = rows_fig_top + "|  " + str(card[0]) + "       |   "
                    rows_suit = rows_suit + "|     " + str(card[1]) + "     |   "
                    rows_fig_bottom = rows_fig_bottom + "|       " + str(card[0]) + "  |   "
            print(top * n)
            print(empyt_row * n)
            print(rows_fig_top)
            print(empyt_row * n)
            print(rows_suit)
            print(empyt_row * n)
            print(rows_fig_bottom)
            print(bottom * n)
    
