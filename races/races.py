from random import choice, randrange, uniform, sample
import numpy as np
from tabulate import tabulate
from main.player import Player
from races.mouse import Mouse
from races.track import Track
from races.race import Race


class Races:
    """
    A class used to represent races and operate whole races game.

    :param names: A tuple with names for runners (constant: ("Całeczka", "Pochodniusia", "Różniczka", "Miareczka", "Sumka", "Dystrybuantka", "Transformatka",
                      "Bazunia", "Graniczka", "Metryczka", "Potęgusia"))
    :type names: tuple
    :param tracks: A tuple with types of tracks (constant: ("flat", "rising", "sloping"))
    :type tracks: tuple
    :param converters: A tuple with prize converters (constant: (4, 2, 1.5, 1.2, 1.1))
    :type converters: tuple
    :param enter_price: An enter price 
    :type enter_price: int
    :param gamblers: A tuple with fake players (constant: ("Darek", "Rysiek", "Piotrek", "Bodzio"))
    :type gamblers: tuple
    :param player: The player who plays races
    :type player: class: `main.Player`    
    """
    def __init__(self, player: Player) -> None:
        """
        Constructor method.
        """
        self.names = ("Całeczka", "Pochodniusia", "Różniczka", "Miareczka", "Sumka", "Dystrybuantka", "Transformatka",
                      "Bazunia", "Graniczka", "Metryczka", "Potęgusia")
        self.tracks = ("flat", "rising", "sloping")
        self.converters = (4, 2, 1.5, 1.2, 1.1)
        self.enter_price = 10
        self.gamblers = ("Darek", "Rysiek", "Piotrek", "Bodzio")
        self.player = player

    # taking random gamblers
    @staticmethod
    def other_bets(number_of_gamblers) -> list:
        """"
        Makes fake players' bets.

        :param number_of_gamblers: A number of fake players
        :type number_of_gamblers: int

        :return: A list with other bets
        :rtype: list
        """
        others = [randrange(0, number_of_gamblers) for _ in range(4)]
        return others

    def show_other_bets(self, other_bets: list) -> None:
        """"
        Show fake players' bets.

        :param other_bets: A list with fake players' bets.
        :type other_bets: list
        """
        for i in range(len(self.gamblers)):
            print(f"{self.gamblers[i]} bets on number {other_bets[i]+1}.")

    def make_bet(self) -> int:
        """"
        Allows the player to make a bet by the interaction.

        :return: A bet as an number of player's favourite mouse
        :rtype: int
        """
        ok = False
        favorite = None

        while not ok:
            favorite = input("Please, enter the number of the player you want to bet on: ")
            try:
                int(favorite)
            except ValueError:
                print("This number is not permissible! Try again.")
                continue
            favorite = int(favorite)
            if favorite < 1 or favorite > 5:
                print("This number is not permissible! Try again.")
                continue
            else:
                ok = True

        self.player.spend_tokens(self.enter_price)

        return favorite

    def make_race(self) -> None:
        """
        Operates the races.
        Makes the whole race, operates bets and sums up the race.
        """

        print("")
        print("Let the races begin!")
        print("")

        # making new track;
        # distance is an int (in meters)
        track = Track(choice(self.tracks), randrange(10, 15))
        runners = []
        lst_of_names = sample(self.names, k=5)

        # making runners
        for i in range(5):
            mouse = Mouse(lst_of_names[i], round(uniform(3.5, 4.75), 5), round(uniform(4.5, 5), 5),
                          choice(self.tracks), round(abs(np.random.normal(1, 0.2, 1)[0]), 5))
            runners.append(mouse)
        race = Race(track, runners)
        race.show_random_stats(2)
        print(race.get_track())
        print("")

        # making other bets
        other_bets = self.other_bets(5)
        self.show_other_bets(other_bets)
        print("")

        # making player's bet
        bet = self.make_bet()
        times = race.start_race()
        print("")

        # getting the winners
        winners = race.get_winners(times)
        race.show_results(times, winners)
        print("")

        # summing up and results
        self.sum_up(bet, winners, other_bets)
        print("")
        print("Do you wish to see full table of parameters('no' for no, anything else for yes)?")
        ans = input("")
        if ans != "no":
            race.show_full_stats()
        print("")
        print("Feel free to play again!")
        print("")
        input("Press ENTER to come back to main menu ")

    def sum_up(self, bet: int, winners: list, other_bets: list) -> None:
        """
        Sums up the races. Adds tokens in a case of winning a bet.
        
        :param bet: A player's favourite mouse (number)
        :type bet: int
        :param winners: A list of winners
        :type winners: list
        :param other_bets: A list with fake players' bets
        :type other_bets: list
        """
        if not winners:
            self.player.add_tokens(self.enter_price)
            print("Because there is no winner, your tokens comes back to you!")
            return
        elif bet-1 in winners:
            counter = 1
            if bet-1 in other_bets:
                counter += other_bets.count(bet-1)
            if counter == 1:
                print(f"There is only 1 good bet! You win {int(self.enter_price * self.converters[0])} tokens!")
                self.player.add_tokens(int(self.enter_price * self.converters[0]))
            else:
                print(f"There are {counter} good bets! You win {int(self.enter_price * self.converters[counter-1])} tokens!")
                self.player.add_tokens(int(self.enter_price * self.converters[counter-1]))
        else:
            print("This was not you lucky race...")
        print("")
        print(f"Your current wallet balance is: {self.player.get_tokens()} tokens")
