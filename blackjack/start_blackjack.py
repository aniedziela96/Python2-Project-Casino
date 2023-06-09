from blackjack.blackjack_hand import Blackjack_hand
from blackjack.blackjack_player import Blackjack_player
from blackjack.croupier_bj import Croupier_bj
from poker.deck import Deck
from blackjack.blackjack_game import Blackjack
from main.player import Player

class Strat_blackjack():
    def __init__(self, player: Player, bet_money) -> None:
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

    def action(self, bet_number = 1, first = False):
        print("1: Stand")
        print("2: Hit")
        print("3: Double down")
        if self.croupier.hand.cards[1][0] == 14:
            print("4: Insurance")
        
        if first:
            if self.blackjack_player.bets[bet_number - 1].is_pair():
                print("5: Split")
        
        action = input("Choose your action: ")

        return action
    
    def game_status(self, start = False):
        if start:
            print("Croupier's hand: ")
            self.croupier.show_hidden()
        else:
            print("Croupier's hand: ")
            self.croupier.show_open()
            
        print("Your hand: ")
        self.blackjack_player.show_bets()
    
    def chosen_stand(self, game: Blackjack):
        result = game.stand()
        self.final(result)
        
        
    def play_bet(self, current_bet = 1):
        game = Blackjack(self.croupier, self.blackjack_player, 
                         self.bet_money, self.deck, bet_number=current_bet)
        
        self.game_status(start=True)
        
        self.decision(game, if_first=True)

    def final(self, result):
        if result == "player wins":
            self.player.add_tokens(self.bet_money * 2)
            print(f"You win {self.bet_money * 2} tokens")
        elif result == "player lost":
            print("You lost")
            return None
        else:
            self.player.add_tokens(self.bet_money)
            print("It's a draw")
            return None

                
    def decision(self, game: Blackjack, if_first=False):
        chosen_action = self.action(first=if_first)

        if chosen_action == "1":
            self.chosen_stand(game)
            return None 

        elif chosen_action == "2":
            result = game.hit()
            if result == "success":
                self.game_status()
                self.decision(game)
            elif result == "bust":
                print("Busted!")
                self.game_status()
                return None
            
        elif chosen_action == "4":
            result = game.insurance()
            if result == "failed":
                print("You don't have enough money for insurance"
                      ", choose different option")
                self.decision(game)
            else:
                setattr(self.player, 'tokens', game.player.get_tokens())
                self.final(result)


    def start_game(self):
        self.deal()
        self.play_bet()
        input("Press Enter to continue")

