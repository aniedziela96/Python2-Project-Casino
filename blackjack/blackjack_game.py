from blackjack.blackjack_player import Blackjack_player
from blackjack.croupier_bj import Croupier_bj
from poker.deck import Deck

class Blackjack():
    def __init__(self, croupier: Croupier_bj, bj_player: Blackjack_player, 
                 bet_money, deck: Deck, bet_number = 1) -> None:
        self.croupier = croupier
        self.player = bj_player 
        self.players_bet = bj_player.bets[bet_number - 1]
        self.bet_money = bet_money
        self.bet_number = bet_number
        self.deck = deck


    def end(self, player_win: bool):
        if player_win:
            return "player wins"
        else:
            return "player lost"

    def hit(self):
        card = self.deck.draw()
        self.player.player_hit(card, self.bet_number)
        self.players_bet.calculate_score()
        if self.players_bet.score > 21:
            return "bust"
        
    def stand(self):
        self.croupier.croupiers_move(self.deck)
        return self.result()
        
    def double_down(self):
        if self.player.get_tokens() < self.bet_money:
            return "failed"
        else:
            self.bet_money *= 2
            self.player.spend_tokens(self.bet_money)
            res = self.hit()
            if res == "bust":
                return res
            else:
                return self.result()
            
    def insurance(self):
        insurance = int(0.5 * self.bet_money) + 1
        if self.player.get_tokens() < insurance:
            return "failed"
        
        self.player.spend_tokens(insurance)
        self.croupier.set_score
        if self.croupier.hand.score == 21:
            self.player.add_tokens(2 * insurance)
            return self.result()
        else:
            self.croupier.croupiers_move(self.deck)
            return self.result()
        
    def result(self):
        self.players_bet.calculate_score()
        if self.players_bet.score > self.croupier.score:
            return self.end(player_win = True)
        elif self.players_bet.score < self.croupier.score:
            return self.end(player_win = False)
        else:
            return "draw"