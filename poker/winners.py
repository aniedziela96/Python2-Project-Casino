from poker.hand import Hand, HAND_RANKS
from poker.poker_player import Poker_Player
from poker.cards import Suit, Rank
from poker.deck import Deck

class Winners():
    """Class that helps determine the player that has better hand if both
        of them have the same rank.
        """
    def __init__(self, poker_player1: Poker_Player, poker_player2: Poker_Player) -> None:
        """Constructor method
        """
        self.player1 = poker_player1
        self.hand1 = sorted(poker_player1.hand.cards)
        self.player2 = poker_player2
        self.hand2 = sorted(poker_player2.hand.cards)

    def winner_high_card(self) -> Poker_Player:
        """Finds the winner if both players have high card by iterating from 
            highest to lowest card.

        :return: Player with the highest card value
        :rtype: class:`poker.poker_player.Poker_Player    
        """
        for i in range(5):
            if self.hand1[i][0] > self.hand2[i][0]:
                return self.player1
            else:
                return self.player2

        
    def winner_pair(self) -> Poker_Player:
        """Finds the winner if both players have high card by checking who has
            older pair, if pairs are the same looks for the highest card.

        :return: Player with older pair or higher card.
        :rtype: class:`poker.poker_player.Poker_Player    
        """
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

    @staticmethod        
    def find_high_card(hand: Hand) -> tuple:
        """Finds the card which doesn't create a pair when player has two pairs
        
        :return: cards which isn't in pair
        :rtype: tuple
        """
        for i in range(4):
            if hand[i][0] != hand[i + 1][0]:
                if i == 0:
                    return hand[i]
                else:
                    return hand[i + 1]
                
         
    def winner_two_pairs(self) -> Poker_Player:
        """Finds the winner if both players have two pairs.

        :return: Player with the highest card value
        :rtype: class:`poker.poker_player.Poker_Player    
        """
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
                
    def winner_three_of_a_kind(self) -> Poker_Player:
        """Finds the winner if both players have three of a kind.

        :return: Player with the oldest three
        :rtype: class:`poker.poker_player.Poker_Player    
        """
        if self.hand1[2] > self.hand2[2]:
            return self.player1
        elif self.hand1[2] < self.hand2[2]:
            return self.player2
    
    def winner_straight(self) -> Poker_Player:
        """Finds the winner if both players have straight.

        :return: Player with the highest card.
        :rtype: class:`poker.poker_player.Poker_Player    
        """
        if self.hand1[4][0] > self.hand2[4][0]:
            return self.player1
        elif self.hand1[4][0] < self.hand2[4][0]:
            return self.player2
        
    def winner_flush(self) -> Poker_Player:
        """Finds the winner if both players have flush.

        :return: Player with the highest card.
        :rtype: class:`poker.poker_player.Poker_Player    
        """
        for i in range(5):
            if self.hand1[i][0] > self.hand2[i][0]:
                return self.player1
            elif self.hand1[i][0] > self.hand2[i][0]:
                return self.player2
            
        if self.hand1[i][1] > self.hand2[i][1]:
            return self.player1
        else:
            return self.player2
        
    def winner_full_house(self) -> Poker_Player:
        """Finds the winner if both players have full house.

        :return: Player with the oldest three
        :rtype: class:`poker.poker_player.Poker_Player    
        """
        if self.hand1[2] > self.hand2[2]:
            return self.player1
        else:
            return self.player2
        
    def winner_four_of_a_kind(self) -> Poker_Player:
        """Finds the winner if both players have four of a kind.

        :return: Player with the oldest four.
        :rtype: class:`poker.poker_player.Poker_Player    
        """
        if self.hand1[2] > self.hand2[2]:
            return self.player1
        else:
            return self.player2
        
    def winner_straight_flush(self) -> Poker_Player:
        """Finds the winner if both players have three of a kind.

        :return: Player with the highest card.
        :rtype: class:`poker.poker_player.Poker_Player    
        """
        if self.hand1[4] > self.hand2[4]:
            return self.player1
        else:
            return self.player2
        
    def winner_royal_flush(self) -> str:
        """It won't happen in your lifetime ;)

        :return: JACKPOT!
        :rtype: str   
        """
        return "JACKPOT"
    