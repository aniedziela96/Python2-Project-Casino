from blackjack.blackjack_hand import Blackjack_hand
from blackjack.blackjack_player import Blackjack_player
from blackjack.croupier_bj import Croupier_bj
from poker.deck import Deck
from blackjack.blackjack_game import Blackjack

class Strat_blackjack():
    def __init__(self, player, bet_money) -> None:
        self.player = player
        self.blackjack_player = Blackjack_player(player.name, player.tokens)
        self.croupier = Croupier_bj()
        self.deck = Deck()
        self.deck.shuffle()
        self.bet_money = bet_money

    def deal(self):
        self.croupier.draw_cards(self.deck.draw(2))
        first_bet = Blackjack_hand()
        first_bet.add_cards(self.deck.draw(2))
        self.blackjack_player.add_bet(first_bet)

    def action(self, bet_number = 1):
        print("1: Stand")
        print("2: Hit")
        print("3: Double down")
        if self.croupier.hand.cards[1][0] == 14:
            print("4: Insurance")
        
        if self.blackjack_player.bets[bet_number - 1].is_pair():
            print("5: Split")
        
        action = input("Choose your action: ")

        return action

    def start_game(self):
        self.deal()

        game = Blackjack(self.croupier, self.blackjack_player, 
                         self.bet_money, self.deck, bet_number=1)
        
        print("Croupier's hand: ")
        self.croupier.show_hidden()
        print("Your hand: ")
        self.blackjack_player.show_bets()

        self.action()
    
