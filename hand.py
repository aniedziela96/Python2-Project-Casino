from deck import Deck

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
            if card[0].value == 14:
                rank = "A"
            elif card[0].value == 13:
                rank = "K"
            elif card[0].value == 12:
                rank = "Q"
            elif card[0].value == 11:
                rank = "J"
            else:
                rank = str(card[0].value)

            if card[1].name == "HEARTS":
                suit = "\N{White Heart Suit}"
            elif card[1].name == "DIAMONDS":
                suit = "\N{White Diamond Suit}"
            elif card[1].name == "CLUBS":
                suit = "\N{White Club Suit}"
            elif card[1].name == "SPADES":
                suit = "\N{White Spade Suit}"
        
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


    def rank(self) -> tuple:
        if len(self.cards) != 5:
            raise ValueError ('only possible for 5 cards hands')
        sorted_hand = sorted(self.cards)
        score = 0
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
                        return (HAND_RANKS[7], score)
                    else: 
                        return(HAND_RANKS[6], score) # Full
                else:
                    return(HAND_RANKS[2], score)
                    # Two Pairs, there's no Three, so it only can be Two Pairs
            elif (sorted_hand[0][0] == sorted_hand[2][0] or 
                  sorted_hand[1][0] == sorted_hand[3][0] or 
                  sorted_hand[2][0] == sorted_hand[4][0]):
            # Check for Three, but now without the Two Pairs
                    return(HAND_RANKS[3], score) # Three of a kind
            # if there is no Three or Two Pairs, there only can be a One Pair
            else:
                return(HAND_RANKS[1], score)
    
        elif self.is_one_color(): #check for straight, flush
            if self.is_straight():
                if sorted_hand[0][0] == 10:
                    return(HAND_RANKS[9], score) # Royal flush
                else: 
                    return(HAND_RANKS[8], score) # Straight flush
            else:
                return(HAND_RANKS[5], score) # flush
        elif self.is_straight():
            return(HAND_RANKS[4], score) # straight 
        else: 
            return(HAND_RANKS[0], score)
        
        # TODO: scoring system
  

if __name__ == "__main__":
    s = set()
    for i in range(100000):
        d = Deck()
        d.shuffle()
        h = Hand()
        c = d.draw(n = 5)
        h.add_cards(c)
        r = h.rank()
        if r[0] not in ["Pair", "High card", "Three of a kind", "Two Pair", 
                        "Straight", 'Flush', 'Full House', "Four of a kind"]:
            print(h)
            print(r)
        
        s.add(r)

    print(s)
