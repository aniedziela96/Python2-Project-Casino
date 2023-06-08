from blackjack.blackjack_hand import Blackjack_hand
from blackjack_player import Blackjack_player
from blackjack.croupier_bj import Croupier_bj
from poker.deck import Deck

class Strat_blackjack():
    def __init__(self, player) -> None:
        self.player = player
        self.blackjack_player = Blackjack_player(player.name, player.tokens)
        self.croupier = Croupier_bj()
        self.deck = Deck()
        self.deck.shuffle()

    def deal(self):
        self.croupier.draw_cards(self.deck.draw(2))
        self.blackjack_player.add_bet()
        self.blackjack_player.bets[0].add_cards(self.deck.draw(2))

    def action(self):
        print("1: Stand")
        print("2: Hit")
        print("3: Double down")
        print("4: Insurance")
        print("5: Split")
        action = input("Choose your action: ")
        if action == "1":
            self.poker.bet(player = True)
            self.poker.match(player = False)
            return "bet"
        elif action == "2":
            setattr(self.poker_player, 'wallet', 
                    self.poker.poker_player.get_tokens())
            return "fold"
        elif action == "3":
            self.poker.bet(player=True, all_in=True)
            self.poker.match(player=False)
            return "all_in"
        elif action == "4":
            print(f"{self.poker_player.name} you have "
                          f"{self.poker.poker_player.get_tokens()} tokens")
            return None
        
    def final(self, bet_number):
        self.croupier.set_score()
        if self.croupier.score > self.blackjack_player.bets[bet_number - 1].score:
            pass
