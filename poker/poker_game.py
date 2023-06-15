from poker.hand import Hand, HAND_RANKS
from main.player import Player
from poker.croupier import Croupier
from poker.winners import Winners
from poker.poker_human import Poker_human
from poker.deck import Deck

class Poker():
    """Class contaning methods that handle possible poker actions
    :param player: Player playing poker
    :type player: class:`main.player.Player`
    """
    def __init__(self, player: Player) -> None:
        self.player = player
        self.poker_player = Poker_human(player.name, player.tokens)
        self.croupier = Croupier()
        self.bet_money = 20 #how much money is in the game
        self.last_bet = 0


    def bet(self, player = True, all_in = False) -> None:
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
        self.bet_money += self.last_bet
        if player:
            self.poker_player.spend_tokens(self.last_bet)
        
        self.last_bet = 0

    def fold(self, player = True):
        if not player:
            self.poker_player.add_tokens(self.bet_money)
    
    def winner(self):
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
