from poker.hand import Hand, HAND_RANKS
from main.player import Player
from poker.croupier import Croupier
from poker.winners import Winners
from poker.poker_human import Poker_human
from poker.deck import Deck
from typing import Union

class Poker():
    """Class contaning methods that handle possible poker actions
    :param player: Player playing poker
    :type player: class:`main.player.Player`
    """
    def __init__(self, player: Player) -> None:
        """Constructor method
        """
        self.player = player
        self.poker_player = Poker_human(player.name, player.tokens)
        self.croupier = Croupier()
        self.bet_money = 20 #how much money is in the game
        self.last_bet = 0


    def bet(self, player = True, all_in = False) -> None:
        """Plays the action of bet in poker game

        :param player: If `True` player plays the bet, if False `Croupier` is playing
            Croupier move - under construction
        :type player: bool
        :param all_in: `True` if player wants to bet all his tokens
        :type all_in: bool
        """
        if player:
            if all_in:
                player_bet = self.poker_player.tokens
                self.poker_player.all_in()
                self.bet_money += player_bet
                self.last_bet = player_bet
            else:
                while True:
                    player_bet = int(input("Place your bet: "))
                    success = self.poker_player.players_bet(player_bet)
                    if success == True:
                        self.bet_money += player_bet
                        self.last_bet = player_bet
                        break
                    elif success == "all_in":
                        print(f"{self.player.name} you wish to go all in.")
                        decision = input("Do you want to continue? (Y/N) ")
                        if decision in "Yy":
                            self.bet(player=True, all_in=True)
                            break
            
        else:
            pass
        #TODO: what croupier does in bet situation

    def match(self, player = True) -> None:
        """Plays the match action in poker game
        
        :param player: If `True` player plays the bet, if False `Croupier` is playing
            Croupier move - under construction
        :type player: bool
        """
        self.bet_money += self.last_bet
        if player:
            self.poker_player.spend_tokens(self.last_bet)
        
        self.last_bet = 0

    def fold(self, player = True):
        """Plays the fold
        
        :param player: If `True` nothing happens - allows the game to end, if `False` player
            wins all the tokens because Croupier is automatically loses
        :type player: bool
        """
        if not player:
            self.poker_player.add_tokens(self.bet_money)
    
    def winner(self) -> Union['Poker_human' , 'Croupier']:
        """Establishes a winner of the poker game. First checks the rank of player and 
            croupier, than compares it. If both ranks are the same uses a `winner` class 
            to determine the winner

        :return: player or croupier, depending on who one the poker game
        :rtype: class:`poker.poker_human.Poker_human` or class:`poker.croupier.Croupier`
        """
        self.poker_player.rank()
        self.croupier.rank()
        self_rank = self.poker_player.hand_rank
        croupier_rank = self.croupier.hand_rank
        if HAND_RANKS.index(self_rank) > HAND_RANKS.index(croupier_rank):
            return self.poker_player
        elif HAND_RANKS.index(self_rank) < HAND_RANKS.index(croupier_rank):
            return self.croupier
        else:
            # we have same rank, we need to look at more specific conditions
            w = Winners(self.poker_player, self.croupier)
            if self_rank == "High Card":
                return w.winner_high_card()
                
            if self_rank == "Pair":
                return w.winner_pair()
                
            if self_rank == "Two Pair":
                return w.winner_three_of_a_kind()
            
            if self_rank == "Three of a kind":
                return w.winner_three_of_a_kind()
            
            if self_rank == "Straight":
                return w.winner_straight()
            
            if self_rank == "Flush":
                return w.winner_flush()
            
            if self_rank == "Full House":
                return w.winner_flush()
            
            if self_rank == "Four of a kind":
                return w.winner_four_of_a_kind()
            
            if self_rank == "Straight Flush":
                return w.winner_straight_flush()
            
            if self_rank == "Royal Flush":
                return w.winner_royal_flush()
