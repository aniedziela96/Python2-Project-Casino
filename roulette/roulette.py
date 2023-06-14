from random import randrange
from tabulate import tabulate
from main.player import Player
from roulette.bet import Bet
from roulette.evenodd import EvenOdd
from roulette.eighteens import Eighteens
from roulette.dozens import Dozens
from roulette.fournumbers import FourNumbers
from roulette.threenumbers import ThreeNumbers
from roulette.twonumbers import TwoNumbers
from roulette.onenumber import OneNumber


class Roulette:
    """
    A class used to play the roulette.

    :param player: The player who plays the game
    :type player: class: `main.Player`
    :param bet_weights: A tuple with weights of different bets (constant)
    :type bet_weights: tuple
    :param bet_names: A tuple with names of different bets (constant)
    :type bet_names: tuple
    """
    def __init__(self, player: Player) -> None:
        """
        Constructor method.
        """
        self.player = player
        self.bet_weights = (1, 1, 2, 8, 11, 17, 35)
        self.bet_names = ("even/odd", "eighteens", "dozens", "four numbers",
                          "three numbers", "two numbers", "one number")

    def show_available_bets(self) -> None:
        """
        Shows available bets as a table.
        """

        print("-------------AVAILABLE BETS------------")
        table = [["number", "name", "weights"]]
        for i in range(len(self.bet_weights)):
            verse = [i+1, self.bet_names[i], f"{self.bet_weights[i]}:1"]
            table.append(verse)
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

    def make_bet(self) -> tuple:
        """
        Makes a bet by the interaction with a user.

        :return: A tuple of the type of the bet and a number of tokens to bet
        :rtype: tuple
        """

        ok = False
        choice = 0
        tokens = 0

        while not ok:
            tokens = input("Please, enter the number of tokens you want to bet: ")
            try:
                int(tokens)
            except ValueError:
                print("This number is not permissible! Try again.")
                continue
            tokens = int(tokens)
            if tokens < 1 or tokens > self.player.get_tokens():
                print("This number is not permissible! Try again.")
                continue
            else:
                ok = True

        ok = False
        while not ok:
            choice = input("Please, enter the number of the bet you want to choose: ")
            try:
                int(choice)
            except ValueError:
                print("This number is not permissible! Try again.")
                continue
            choice = int(choice)
            if choice < 1 or choice > 7:
                print("This number is not permissible! Try again.")
                continue
            else:
                ok = True

        self.player.spend_tokens(tokens)
        return choice, tokens

    def start_roulette(self) -> None:
        """
        Operates the entire game by the if/elif/else conditions.
        Communicates with roulette's player, spends his tokens, takes bet,
        draws a random number, shows it and
        adds tokens to the player's account after the eventual win.
        """

        print("")
        print("Let the roulette spin!")
        print("")
        self.show_available_bets()
        print("")
        choice, tokens = self.make_bet()
        number = randrange(0, 37)

        if choice == 1:
            print("Options:")
            print("1: Even")
            print("2: Odd")
            option = int(input("Your choice: "))
            bet = EvenOdd(option)

        elif choice == 2:
            print("Options:")
            print("1: 1-18")
            print("2: 19-36")
            option = int(input("Your choice: "))
            bet = Eighteens(option)

        elif choice == 3:
            print("Options:")
            print("1: 1-12")
            print("2: 13-24")
            print("3: 25-36")
            option = int(input("Your choice: "))
            bet = Dozens(option)

        elif choice == 4:
            print("Your choice:")
            option = [int(input("The first of four numbers: ")), int(input("The second of four numbers: ")),
                      int(input("The third of four numbers: ")), int(input("The fourth of four numbers: "))]
            bet = FourNumbers(option)

        elif choice == 5:
            print("Your choice:")
            option = [int(input("The first of three numbers: ")), int(input("The second of three numbers: ")),
                      int(input("The third of three numbers: "))]
            bet = ThreeNumbers(option)

        elif choice == 6:
            print("Your choice:")
            option = [int(input("The first of two numbers: ")), int(input("The second of two numbers: "))]
            bet = TwoNumbers(option)

        #elif choice == 7:
        else:
            option = int(input("Your choice: "))
            bet = OneNumber(option)

        print("")
        print(f"The drawn number is {number}")
        print("")
        win = bet.is_in_bet(number)
        if win:
            print(f"Congratulations! You win {bet.winner_prize(tokens) + tokens} tokens!")
            self.player.add_tokens(bet.winner_prize(tokens) + tokens)
        else:
            print("This was not your lucky game...")

        print(f"Your current wallet balance is: {self.player.get_tokens()} tokens")
        print("")
        print("Feel free to play again!")
