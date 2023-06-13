from random import sample, randrange, uniform
from player import Player
from tabulate import tabulate
from time import perf_counter
from bingo.board import Board
from bingo.bingogame import BingoGame
import os


class Bingo:
    def __init__(self, player: Player) -> None:
        self.player = player
        self.gamblers = ("Darek", "Rysiek", "Piotrek", "Boguś")
        self.enter_price = 10
        self.winner_prize = 20

    def make_bingo_board(self) -> Board:
        columns = []
        start = 1
        stop = 16
        for i in range(5):
            numbers = [i for i in range(start, stop)]
            fields = sample(numbers, 5)
            columns.append(fields)
            start += 15
            stop += 15
        columns[2][2] = '\N{BLACK CIRCLE}'

        return Board(columns)

    def make_bingo_game(self) -> BingoGame:
        fake_players = sample(self.gamblers, 2)
        # tworzymy układ do naszego bingo - trzech graczy (w tym jeden to prawdziwy), każdy ma swoją planszę
        return BingoGame((self.player, fake_players[0], fake_players[1]),
                         [self.make_bingo_board(), self.make_bingo_board(), self.make_bingo_board()])

    def make_times(self, number_of_fake_players) -> list:
        times = []
        for _ in range(number_of_fake_players):
                times.append(round(uniform(3, 11), 5))
        return times

    def pay_prize(self) -> None:
        self.player.add_tokens(self.winner_prize)

    def sum_up(self) -> None:
        print("")

        print(f"Your current wallet balance is: {self.player.get_tokens()} tokens")
        print("Feel free to play again!")
        print("")
        input("Press ENTER to come back to main menu ")

    def start_game(self):
        self.player.spend_tokens(self.enter_price)
        print("Let the bingo begins!")
        print("")
        game = self.make_bingo_game()
        print(f"Your opponents are {game.get_bingo_players()[1]} and {game.get_bingo_players()[2]}.")
        print("")
        print("Your board:")
        game.show_players_board()
        print("")
        print("In every round if you have bingo, write 'bingo' as fast as you can! If not, press ENTER.")
        print("Be careful - if you write 'bingo' without a bingo on your board, you will lose!")
        input("Press ENTER to continue ")
        os.system('cls' if os.name == 'nt' else 'clear')

        drawns = set()

        round_number = 1

        while True:
            # rozpoczęcie nowej tury
            print("")
            print(f"ROUND {round_number}.")

            # losujemy liczbę, aź dostaniemy taką, której jeszcze nie było
            drawn = randrange(1, 76)
            while True:
                if drawn not in drawns:
                    drawns.add(drawn)
                    break
                drawn = randrange(1, 76)

            print(f"The drawn number is: {drawn}")
            print("")
            # zaznaczamy liczbę na planszach
            game.check_boards(drawn)

            # pokazujemy graczowi jego planszę i prosimy o reakcję
            game.show_players_board()
            print("")
            t0 = perf_counter()
            reaction = input("If you have bingo, write 'bingo' as fast as you can! If not, press ENTER: ")
            t1 = perf_counter()

            # tworzymy listę graczy, którzy mają bingo (być może pustą)
            bingos = game.is_bingos()
            number_of_bingos = len(bingos)

            # gracz zgłosił, że ma bingo
            if reaction == "bingo":

                # gracz ma bingo
                if 0 in bingos:

                    # tylko gracz ma bingo
                    if number_of_bingos == 1:
                        print("Congratulations! You win!")
                        self.pay_prize()
                        self.sum_up()
                        break

                    # inny gracz też ma bingo
                    elif number_of_bingos == 2:
                        time = round(t1-t0, 5)
                        other_winner = game.get_bingo_players()[bingos[1]]
                        other_time = self.make_times(1)[0]
                        if time < other_time[0]:
                            print(f"Congratulations! You win over {other_winner}!")
                            print("")
                            print(f"Your time: {time} s")
                            print(f"{other_winner}'s time: {other_time} s")
                            self.pay_prize()
                            self.sum_up()
                            break
                        else:
                            print(f"Sorry, {other_winner} was faster.")
                            print(f"{other_winner} wins!")
                            print("")
                            print(f"Your time: {time} s")
                            print(f"{other_winner}'s time: {other_time} s")
                            self.sum_up()
                            break

                    # wszyscy gracze mają bingo:
                    else:
                        time = round(t1-t0, 5)
                        other_winners = [game.get_bingo_players()[bingos[1]], game.get_bingo_players()[bingos[2]]]
                        other_times = self.make_times(2)
                        if time < min(other_times):
                            print("Congratulations! You win!")
                            print(f"Your time: {time} s")
                            print(f"{other_winners[0]}'s time: {other_times[0]} s")
                            print(f"{other_winners[1]}'s time: {other_times[1]} s")
                            self.pay_prize()
                            self.sum_up()
                            break
                        else:
                            if other_times[0] < other_times[1]:
                                print(f"Sorry, {other_winners[0]} was faster.")
                                print(f"{other_winners[0]} wins!")

                            elif other_times[1] < other_times[0]:
                                print(f"Sorry, {other_winners[1]} was faster.")
                                print(f"{other_winners[1]} wins!")

                            print("")
                            print(f"Your time: {time}")
                            print(f"{other_winners[0]}'s time: {other_times[0]}")
                            print(f"{other_winners[1]}'s time: {other_times[1]}")
                            self.sum_up()
                            break

                # gracz nie ma bingo
                else:
                    print("There's no bingo on your board! Sorry, you lose.")
                    self.sum_up()
                    break

            # gracz nie zgłosił, że ma bingo
            else:

                # ktoś ma bingo
                if bingos:

                    # gracz ma bingo, ale tego nie zgłosił
                    if 0 in bingos:
                        # jeśli nikt poza graczem nie ma bingo, ale gracz go nie zgłosił, gra toczy się dalej

                        # jednocześnie inny gracz ma bingo
                        if number_of_bingos == 2:
                            winner = game.get_bingo_players()[bingos[1]]
                            print(f"{winner} has bingo!")
                            print(f"{winner} wins!")
                            self.sum_up()
                            break

                        # obaj pozostali gracze mają bingo
                        elif number_of_bingos == 3:
                            winners = [game.get_bingo_players()[bingos[1]], game.get_bingo_players()[bingos[2]]]
                            print(f"{winners[0]} and {winners[1]} have bingo!")
                            times = self.make_times(2)
                            if times[0] < times[1]:
                                print(f"{winners[0]} wins!")
                            elif times[1] < times[0]:
                                print(f"{winners[1]} wins!")
                            else:
                                print(f"{winners[1]} and {winners[2]}"
                                      f"win together!")
                            print("")
                            print(f"{winners[0]}'s time: {times[0]}")
                            print(f"{winners[1]}'s time: {times[1]}")
                            self.sum_up()
                            break

                    # gracz nie ma bingo, ale ktoś inny ma
                    else:

                        # inny gracz ma bingo
                        if number_of_bingos == 1:
                            winner = game.get_bingo_players()[bingos[0]]
                            print(f"{winner} has bingo!")
                            print(f"{winner} wins!")
                            self.sum_up()
                            break

                        # obaj pozostali gracze mają bingo
                        else:
                            winners = [game.get_bingo_players()[bingos[0]], game.get_bingo_players()[bingos[1]]]
                            print(f"{winners[0]} and {winners[1]} have bingo!")
                            times = self.make_times(2)
                            if times[0] < times[1]:
                                print(f"{winners[0]} wins!")
                            elif times[1] < times[0]:
                                print(f"{winners[1]} wins!")
                            else:
                                print(f"{winners[1]} and {winners[2]}"
                                      f"win together!")
                            print("")
                            print(f"{winners[0]}'s time: {times[0]}")
                            print(f"{winners[1]}'s time: {times[1]}")
                            self.sum_up()
                            break

            round_number += 1
            os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    player1 = Player("Misiek", 1000)
    bingo = Bingo(player1)
    bingo.start_game()
