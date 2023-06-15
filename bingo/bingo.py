from random import sample, randrange, uniform
from main.player import Player
from tabulate import tabulate
from time import perf_counter
from bingo.board import Board
from bingo.bingogame import BingoGame
import os


class Bingo:
    """
    A class used to play the `bingo`.

    :param player: The player who plays the game
    :type player: class: `main.Player`
    :param gamblers: A tuple with names of fake players
    :type bet_weights: tuple
    :param enter_price: A price the `player` must pay to play the game (constant: 10)
    :type enter_price: int
    :param winner_prize: A prize to win (constant: 20)
    :type winner_prize: int
    """
    def __init__(self, player: Player) -> None:
        """
        Constructor method.
        """
        self.player = player
        self.gamblers = ("Darek", "Rysiek", "Piotrek", "Bodzio")
        self.enter_price = 10
        self.winner_prize = 20

    @staticmethod
    def make_bingo_board() -> Board:
        """
        Makes bingo board by creating columns with random numbers (and a circle in the center field).

        :return: A bingo board
        :rtype: class: `bingo.Board`
        """

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
        """
        Makes bingo game based on `player`, 2 random fake players and 3 random bingo boards.

        :return: A single bingo game
        :rtype: class: `bingo.BingoGame`
        """
        fake_players = sample(self.gamblers, 2)
        return BingoGame((self.player, fake_players[0], fake_players[1]),
                         [self.make_bingo_board(), self.make_bingo_board(), self.make_bingo_board()])

    @staticmethod
    def make_times(number_of_fake_players: int, time: float) -> list:
        """
        Makes reaction times for fake player(s) based on player's time.

        :param number_of_fake_players: A number of fake players who have the bingo
        at the same time.
        :type number_of_fake_players: int
        :param time: A time of reaction of a player
        :type time: float

        :return: A list with times
        :rtype: list
        """
        times = []
        for _ in range(number_of_fake_players):
                times.append(round(uniform(time-2, time+3), 5))
        return times

    def pay_prize(self) -> None:
        """
        Pays the prize when the player wins.
        """
        self.player.add_tokens(self.winner_prize)

    def sum_up(self) -> None:
        """
        Shows ballance and endtapes after the game.
        """
        print("")

        print(f"Your current wallet balance is: {self.player.get_tokens()} tokens")
        print("Feel free to play again!")
        print("")
        input("Press ENTER to come back to main menu ")

    def start_game(self) -> None:
        """
        Operates the entire game by the while loop, if/elif/else conditions.
        At first, spends player's tokens.
        Then starts the game.
        Every round is drawing random number, showing it, checking it on boards, printing 
        player's board, check if players have bingo and waits for the player's input.
        The function also handles adding tokens to the player's account after the eventual win.
        """
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
            # beggining of a new round
            print("")
            print(f"ROUND {round_number}.")

            # drawing a new number (takes as long as the number is not unique)
            drawn = randrange(1, 76)
            while True:
                if drawn not in drawns:
                    drawns.add(drawn)
                    break
                drawn = randrange(1, 76)

            print(f"The drawn number is: {drawn}")
            print("")
            # checking the drawn number on the boards
            game.check_boards(drawn)

            # showing player's the board and taking the reaction
            game.show_players_board()
            print("")
            t0 = perf_counter()
            reaction = input("If you have bingo, write 'bingo' as fast as you can! If not, press ENTER: ")
            t1 = perf_counter()

            # making list of players with bingo (maybe empty)
            bingos = game.is_bingos()
            number_of_bingos = len(bingos)

            # player reported bingo
            if reaction == "bingo":

                # player has bingo
                if 0 in bingos:

                    # player is the only one with bingos
                    if number_of_bingos == 1:
                        print("Congratulations! You win!")
                        self.pay_prize()
                        self.sum_up()
                        break

                    # other player also has bingo
                    elif number_of_bingos == 2:
                        time = round(t1-t0, 5)
                        other_winner = game.get_bingo_players()[bingos[1]]
                        other_time = self.make_times(1, time)[0]
                        if time < other_time:
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

                    # all players have bingo
                    else:
                        time = round(t1-t0, 5)
                        other_winners = [game.get_bingo_players()[bingos[1]], game.get_bingo_players()[bingos[2]]]
                        other_times = self.make_times(2, time)
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

                # player does not have bingo
                else:
                    print("There's no bingo on your board! Sorry, you lose.")
                    self.sum_up()
                    break

            # player was not report bingo
            else:

                # there is bingo on some board
                if bingos:

                    # player has bingo but was not report it
                    if 0 in bingos:
                        # if it is the only bingo, the game is continued

                        # other player has bingo
                        if number_of_bingos == 2:
                            winner = game.get_bingo_players()[bingos[1]]
                            print(f"{winner} has bingo!")
                            print(f"{winner} wins!")
                            self.sum_up()
                            break

                        # all players have bingo
                        elif number_of_bingos == 3:
                            winners = [game.get_bingo_players()[bingos[1]], game.get_bingo_players()[bingos[2]]]
                            print(f"{winners[0]} and {winners[1]} have bingo!")
                            times = self.make_times(2, 3.5)
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

                    # player do not have bingo, but other player has
                    else:

                        # one of other players has bingo
                        if number_of_bingos == 1:
                            winner = game.get_bingo_players()[bingos[0]]
                            print(f"{winner} has bingo!")
                            print(f"{winner} wins!")
                            self.sum_up()
                            break

                        # both other players have bingo
                        else:
                            winners = [game.get_bingo_players()[bingos[0]], game.get_bingo_players()[bingos[1]]]
                            print(f"{winners[0]} and {winners[1]} have bingo!")
                            times = self.make_times(2, 3.5)
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
