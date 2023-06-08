from poker.deck import Deck

HAND_RANKS = ['High card', 'Pair', 'Two Pair', 'Three of a kind', 
              'Straight', 'Flush', 'Full House', 'Four of a kind', 
           'Straight Flush', 'Royal Flush']

class Hand():
    def __init__(self) -> None:
        self.cards = []


    def add_cards(self, cards: list) -> None:
        for card in cards:
            self.cards.append(card)
    

    def __str__(self) -> str:
        cards_str = ""
        for card in self.cards:
            rank = str(card[0])

            suit = str(card[1])
        
            cards_str = cards_str + rank + suit + ", "

        return cards_str.removesuffix(", ")
    

    def highest_hards(self) -> tuple:
        return max(self.cards)
    

    def is_one_color(self) -> bool:
        for i in range(len(self.cards) - 1):
            if self.cards[i][1] != self.cards[i + 1][1]:
                return False
            
        return True
    
    def is_straight(self) -> bool:
        sorted_cards = sorted(self.cards)
        for i in range(len(self.cards) - 1):
            if sorted_cards[i][0] + 1 != sorted_cards[i + 1][0]:
                return False
            
        return True
    
    def is_five(self) -> bool:
        if len(self.cards) == 5:
            return True
        else:
            return False

    def rank(self) -> str:
        if not self.is_five:
            raise ValueError ('only possible for 5 cards hands')
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
        
    def show_hand(self) -> str:
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
    

if __name__ == "__main__":
    
    d = Deck()
    d.shuffle()
    h = Hand()
    h.add_cards(d.draw(n = 5))
    print(h)
    h.show_hand()
