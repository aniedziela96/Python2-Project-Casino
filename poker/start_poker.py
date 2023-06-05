from poker.deck import Deck
from poker.poker_game import Poker


class Poker_Game():
    def __init__(self, player) -> None:
        self.poker_player = player
        self.deck = Deck()
        self.poker = Poker(player)
        
    def round_one(self):
        self.deck.shuffle()
        print("Drawing two cards...")
        self.poker.poker_player.draw_cards(self.deck.draw(2))
        self.poker.croupier.draw_cards(self.deck.draw(2))
        print(self.poker.poker_player.hand)


    def action(self):
        while True:
            print("1: Bet")
            print("2: Fold")
            print("3: All in")
            print("4: Balance")
            action = input("Choose your action: ")
            if action == "1":
                self.poker.bet(player = True)
                self.poker.match(player = False)
                return "bet"
            elif action == "2":
                setattr(self.poker_player, 'wallet', 
                        self.poker.poker_player.get_money())
                return "fold"
            elif action == "3":
                self.poker.bet(player=True, all_in=True)
                self.poker.match(player=False)
                return "all_in"
            elif action == "4":
                print(f"{self.poker_player.name} you have "
                      f"{self.poker.poker_player.get_money()} tokens")
                return None

    def round_two(self):
        print("drawing three cards...")
        self.poker.poker_player.draw_cards(self.deck.draw(3))
        self.poker.croupier.draw_cards(self.deck.draw(3))
        print(self.poker.poker_player.hand)


    def final(self):
        print(f"Your hand: {self.poker.poker_player.hand}")
        print(f"Croupier's hand: {self.poker.croupier.hand}")
        if self.poker.winner() == self.poker.poker_player:
            print(f"You win {self.poker.bet_money} tokens.")
            setattr(self.poker_player, 'wallet', 
                    self.poker.poker_player.get_money() + self.poker.bet_money)
        else:
            setattr(self.poker_player, 'wallet', 
                    self.poker.poker_player.get_money())
            print(f"You lose, better luck next time.")

    def start_game(self):

        self.round_one()
        while True:
            round_one_decision = self.action() 
            if round_one_decision == "bet":
                break
            elif round_one_decision == "fold":
                print("You folded!")
                print("The game has finished")
                return None
            elif round_one_decision == "all_in":
                self.round_two()
                self.final()
                return None
                    
        self.round_two()
        while True:
            round_two_decision = self.action()
            if round_two_decision == "bet":
                self.final()
                break
            elif round_two_decision == "fold":
                print("You folded!")
                print("The game has finished")
                return None
            elif round_two_decision == "all_in":
                self.final()
                break


        