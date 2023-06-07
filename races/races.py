from random import choice, randrange, uniform, sample
import numpy as np
from tabulate import tabulate
from main.player import Player
from races.mouse import Mouse
from races.track import Track
from races.race import Race


class Races:
    def __init__(self) -> None:
        self.names = ("Całeczka", "Pochodniusia", "Różniczka", "Miareczka", "Sumka", "Dystrybuantka", "Transformatka",
                      "Bazunia", "Graniczka", "Metryczka", "Potęgusia")
        self.tracks = ("flat", "rising", "sloping")
        self.converters = (4, 2, 1.5, 1.2, 1.1)
        self.enter_price = 10
        self.gamblers = ("Darek", "Rysiek", "Piotrek", "Boguś")

    # losujemy zakłady pozostałych graczy
    def other_bets(self, number_of_gamblers):
        others = [randrange(0, number_of_gamblers) for _ in range(4)]
        return others

    def show_other_bets(self, other_bets):
        for i in range(len(self.gamblers)):
            print(f"{self.gamblers[i]} bets on number {other_bets[i]+1}.")

    def make_bet(self, player):
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

        player.spend_tokens(self.enter_price)

        return favorite

    def make_race(self, player):
        print("Let the races begin!")
        print("")

        # tworzymy nowy tor; typ trasy losujemy z tracks,
        # zaś dystans to liczba całkowita z przedziału 5-8 włącznie (w metrach)
        track = Track(choice(self.tracks), randrange(5, 9))
        runners = []
        lst_of_names = sample(self.names, k=5)

        # losujemy zawodników i prezentujemy ich graczowi
        for i in range(5):
            mouse = Mouse(lst_of_names[i], round(uniform(0.2, 0.3), 5), round(uniform(-.25, .25), 5),
                          choice(self.tracks), round(abs(np.random.normal(1, 0.2, 1)[0]), 5))
            runners.append(mouse)
        race = Race(track, runners)
        race.show_random_stats(2)
        print(race.get_track())
        print("")

        # losujemy i prezentujemy inne zakłady
        other_bets = self.other_bets(5)
        self.show_other_bets(other_bets)
        print("")

        # po prezentacji prosimy gracza o zrobienie zakładu
        bet = self.make_bet(player)
        times = race.start_race()
        print("")

        # wyłaniamy zwycięzców i prezentujemy wyniki
        winners = race.get_winners(times)
        race.show_results(times, winners)
        print("")

        # podsumowujemy zakłady i prezentujemy wyniki
        self.sum_up(bet, winners, player, other_bets)
        print("")
        print("Do you wish to see full table of parameters('no' for no, anything else for yes)?")
        ans = input("")
        if ans != "no":
            race.show_full_stats()
        print("")
        print("Feel free to play again!")

    def sum_up(self, bet, winners, player, other_bets):
        if not winners:
            player.add_tokens(self.enter_price)
            print("Because there is no winner, your tokens comes back to you!")
            return
        elif bet-1 in winners:
            counter = 1
            if bet-1 in other_bets:
                counter += other_bets.count(bet-1)
            if counter == 1:
                print(f"There is only 1 good bet! You win {self.enter_price * self.converters[0]}$!")
                player.add_tokens(self.enter_price * self.converters[0])
            else:
                print(f"There are {counter} good bets! You win {self.enter_price * self.converters[counter-1]}$!")
                player.add_tokens(self.enter_price * self.converters[counter-1])
        else:
            print("This was not you lucky race...")
        print("")
        print(f"Your current wallet balance is: {player.get_tokens()} tokens")


if __name__ == "__main__":
    player1 = Player("Misiek", 100)
    races = Races()
    races.make_race(player1)
