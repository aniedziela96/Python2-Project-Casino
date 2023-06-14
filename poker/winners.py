from poker.hand import Hand, HAND_RANKS
from poker.poker_player import Poker_Player
from poker.cards import Suit, Rank
from poker.deck import Deck

class Winners():
    def __init__(self, poker_player1: Poker_Player, poker_player2: Poker_Player) -> None:
        self.player1 = poker_player1
        self.hand1 = sorted(poker_player1.hand.cards)
        self.player2 = poker_player2
        self.hand2 = sorted(poker_player2.hand.cards)

    def winner_high_card(self):
        for i in range(5):
            if self.hand1[i] > self.hand2[i]:
                return self.player1
            else:
                return self.player2

        
    def winner_pair(self):
        last_pair1 = False
        last_pair2 = False
        for i in range(4):
            if self.hand1[i][0] == self.hand1[i + 1][0]:
                pair_card_1 = self.hand1[i + 1]
                if i == 3:
                    last_pair1 = True
            if self.hand2[i][0] == self.hand2[i + 1][0]:
                pair_card_2 = self.hand2[i + 1]
                if i == 3:
                    last_pair2 = True
                
        if pair_card_1[0] > pair_card_2[0]:
            return self.player1
        elif pair_card_1[0] < pair_card_2[0]:
            return self.player2
        else:
            if last_pair1 and last_pair2:
                if self.hand1[2] > self.hand2[2]:
                    return self.player1
                if self.hand1[2] < self.hand2[2]:
                    return self.player2
            else:
                if self.hand1[4] > self.hand2[4]:
                    return self.player1
                if self.hand1[4] < self.hand2[4]:
                    return self.player2
                
    def find_high_card(hand):
        for i in range(4):
            if hand[i][0] != hand[i + 1][0]:
                if i == 0:
                    return hand[i]
                else:
                    return hand[i + 1]
                
         
    def winner_two_pairs(self):
        if self.hand1[3][0] > self.hand2[3][0]:
            return self.player1
        elif self.hand1[3][0] < self.hand2[3][0]:
            return self.player2
        else:
            if self.hand1[1][0] > self.hand2[1][0]:
                return self.player1
            elif self.hand1[1][0] < self.hand2[1][0]:
                return self.player2
            else:
                if self.find_high_card(self.hand1) > self.find_high_card(self.hand2):
                    return self.player1
                else:
                    return self.player2
                
    def winner_three_of_a_kind(self):
        if self.hand1[2] > self.hand2[2]:
            return self.player1
        elif self.hand1[2] < self.hand2[2]:
            return self.player2
    
    def winner_straight(self):
        if self.hand1[4][0] > self.hand2[4][0]:
            return self.player1
        elif self.hand1[4][0] < self.hand2[4][0]:
            return self.player2
        
    def winner_flush(self):
        for i in range(5):
            if self.hand1[i][0] > self.hand2[i][0]:
                return self.player1
            elif self.hand1[i][0] > self.hand2[i][0]:
                return self.player2
            
        if self.hand1[i][1] > self.hand2[i][1]:
            return self.player1
        else:
            return self.player2
        
    def winner_full_house(self):
        if self.hand1[2] > self.hand2[2]:
            return self.player1
        else:
            return self.player2
        
    def winner_four_of_a_kind(self):
        if self.hand1[2] > self.hand2[2]:
            return self.player1
        else:
            return self.player2
        
    def winner_straight_flush(self):
        if self.hand1[4] > self.hand2[4]:
            return self.player1
        else:
            return self.player2
        
    def winner_royal_flush(self):
        return "JACKPOT"
    