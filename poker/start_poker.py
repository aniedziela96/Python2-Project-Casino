from poker.deck import Deck
from poker.poker_game import Poker
from main.player import Player
from typing import Union

class Poker_Game():
    def __init__(self, player: Player) -> None:
        self.poker_player = player
        self.deck = Deck()
        self.poker = Poker(player)
        
    def round_one(self) -> None:
        self.deck.shuffle()
        print("Drawing two cards...")
        self.poker.poker_player.draw_cards(self.deck.draw(2))
        self.poker.croupier.draw_cards(self.deck.draw(2))


    def action(self) -> Union[None , str]:
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
                setattr(self.poker_player, 'tokens', 
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

    def round_two(self) -> None:
        print("drawing three cards...")
        self.poker.poker_player.draw_cards(self.deck.draw(3))
        self.poker.croupier.draw_cards(self.deck.draw(3))

    def final(self) -> None:
        print("Your hand: ")
        self.poker.poker_player.show_player_hand()
        print("Croupier's hand:")
        self.poker.croupier.show_player_hand()
        if self.poker.winner() == self.poker.poker_player:
            print(f"You win {self.poker.bet_money} tokens.")
            setattr(self.poker_player, 'tokens', 
                    self.poker.poker_player.get_tokens() + self.poker.bet_money)
        else:
            setattr(self.poker_player, 'tokens', 
                    self.poker.poker_player.get_tokens())
            print(f"You lose, better luck next time.")


    def start_game(self) -> None:

        self.round_one()
        while True:
            self.poker.poker_player.show_player_hand()
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
            self.poker.poker_player.show_player_hand()
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

    @staticmethod
    def end_game():
        input("Press Enter to continue")
        