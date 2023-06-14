from blackjack.blackjack_hand import Blackjack_hand
from blackjack.blackjack_player import Blackjack_player
from blackjack.croupier_bj import Croupier_bj
from poker.deck import Deck
from blackjack.blackjack_game import Blackjack
from main.player import Player
from poker.cards import Rank, Suit

class Strat_blackjack():
    def __init__(self, player: Player, bet_money: int) -> None:
        self.player = player
        self.blackjack_player = Blackjack_player(player.name, player.tokens)
        self.croupier = Croupier_bj()
        self.deck = Deck()
        self.deck.shuffle()
        self.bet_money = bet_money
        self.tokens_bet = bet_money
        self.list_of_games = []

    def deal(self) -> None:
        
        self.croupier.draw_cards(self.deck.draw(2))
        first_bet = Blackjack_hand()
        first_bet.add_cards(self.deck.draw(2))
        self.blackjack_player.add_bet(first_bet)
        self.list_of_games.append(Blackjack(self.croupier, self.blackjack_player, 
                                            self.bet_money, self.deck))

    def action(self, bet_number = 1, first = False) -> str:
        print(f"Playing bet number {bet_number}")
        print("1: Stand")
        print("2: Hit")
        
        if first:
            print("3: Double down")

            if self.croupier.hand.cards[1][0] == 14:
                print("4: Insurance")

            if self.blackjack_player.bets[bet_number - 1].is_pair():
                print("5: Split")
        
        action = input("Choose your action: ")

        return action
    
    def game_status(self, hidden = True) -> None:
        if hidden:
            print("Croupier's hand: ")
            self.croupier.show_hidden()
        else:
            print("Croupier's hand: ")
            self.croupier.show_open()
            
        print("Your hand: ")
        self.blackjack_player.show_bets()

        
    def play_bet(self, game: Blackjack, split=False) -> None:
        self.game_status(hidden=True)
        self.decision(game, if_first=True, split=split)
            

    def decision(self, game: Blackjack, if_first=False) -> None:
        chosen_action = self.action(first=if_first, 
                                    bet_number=game.bet_number)

        if chosen_action == "1":
            pass
        
        elif chosen_action == "2":
            result = game.hit()
            if result == "success":
                self.game_status()
                self.decision(game)
            elif result == "bust":
                print("Busted!")
                self.game_status(hidden=False)

            
        elif chosen_action == "3":
            result = game.double_down()
            if result == "failed":
                print("You don't have enough money for double down")
                self.decision(game)
            else:
                self.player.spend_tokens(self.tokens_bet)
                if result == "bust":
                    print("Busted")
                    self.game_status()
                else:
                    self.game_status()

            
        elif chosen_action == "4":
            result = game.insurance()
            if result == "failed":
                print("You don't have enough money for insurance"
                      ", choose different option")
                self.decision(game)
            else:
                setattr(self.player, 'tokens', self.blackjack_player.get_tokens())


        elif chosen_action == "5":
            result = game.split()
            if result == "failed":
                self.decision(game)
            else:
                self.list_of_games.append(result)
                self.play_bet(game)


    def players_score(self) -> list:
        scores = []
        bets_number = len(self.blackjack_player.bets)
        for i in range(bets_number):
            self.blackjack_player.bets[i].calculate_score()
            scores.append(self.blackjack_player.bets[i].score)

        return scores


    def final(self) -> None:
        players_score = self.players_score()
        for i in range(len(self.list_of_games)):
            if players_score[i] > 21 or players_score[i] < self.croupier.score:
                print(f"You lost bet {i + 1}")
            elif players_score[i] > self.croupier.score:
                self.player.add_tokens(self.list_of_games[i].bet_money * 2)
                print(f"You won bet {i + 1}")
            elif players_score[i] == self.croupier.score:
                self.player.add_tokens(self.list_of_games[i].bet_money)
                print(f"It's a draw in bet {i + 1}")

    def start_game(self):
        self.deal()
        for game in self.list_of_games:
            self.play_bet(game)
            game.players_bet.calculate_score()
            if game.players_bet.score > 21 and len(self.list_of_games) == 1:
                print("Busted")
                self.final()
                input("Press Enter to continue")
                return None

        self.croupier.croupiers_move(self.deck)
        self.final()
        input("Press Enter to continue")

