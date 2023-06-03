from poker_player import Poker_Player
from hand import Hand, HAND_RANKS
from player import Player

class Poker():
    def __init__(self, player) -> None:
        self.player = player
        self.poker_player = Poker_Player(player.name, player.wallet)
        self.croupier = Poker_Player("Bogus", 0)
        self.bet_money = 0 #how much money is in the game
        self.last_bet = 0


    def bet(self, player = True):
        if player:
            while True:
                player_bet = int(input("Place your bet: "))
                success = self.poker_player.players_bet(player_bet)
                if success:
                    break

            self.bet_money += player_bet
            self.last_bet = player_bet
            setattr(self.player, 'wallet', 
                    self.player.wallet - player_bet)
        else:
            pass
        #TODO: what croupier does in bet situation

    def match(self, player = True):
        self.bet_money += self.last_bet
        if player:
            setattr(self.player, 'wallet',  
                    self.player.wallet - self.last_bet)
        
        self.last_bet = 0

    def fold(self, player = True):
        if player:
            self.bet_money = 0
        else:
            setattr(self.player, 'wallet',  
                    self.player.wallet + self.bet_money)
    
    def winner(self):
        self_rank = self.player.hand.rank()
        other_rank = self.croupier.hand.rank()
        if HAND_RANKS.index(self_rank) > HAND_RANKS.index(other_rank):
            return self
        elif HAND_RANKS.index(self_rank) < HAND_RANKS.index(other_rank):
            return other_rank
        else:
            # we have same rank, we need to look at more specific conditions
            sorted_player = sorted(self.player.hand.cards())
            sorted_croupier = sorted(self.croupier.hand.cards())
            if self_rank == "High Card":
                if sorted_player > sorted_croupier():
                    return self.player
                else:
                    return self.croupier
                
            if self_rank == "Pair":
                for i in range(4):
                    if sorted_player[i][0] == sorted_player[i + 1][0]:
                        pair_card_self = sorted_player[i + 1]
                    if sorted_croupier[i][0] == sorted_croupier[i + 1][0]:
                        pair_card_other = sorted_croupier[i + 1]
                
                if pair_card_other[0] < pair_card_self[0]:
                    return self.player
                elif pair_card_other[0] > pair_card_self[0]:
                    return self.croupier
                else:
                    return None
                
            if self_rank == "Two Pair":
                if sorted_player[3][0] > sorted_croupier[3][0]:
                    return self
    

if __name__ == "__main__":
    rysio = Player("rysio", 1000)
    p = Poker(rysio)
    print(type(rysio))
    print(rysio.wallet)
    p.bet()
    print(p.bet_money)
    print(rysio.wallet)