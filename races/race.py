from random import choice, randrange, uniform, sample
import numpy as np
from races.track import Track
from tabulate import tabulate


class Race:
    def __init__(self, track: Track, runners: list):
        self.track = track
        self.runners = runners

    def get_runners(self) -> list:
        return self.runners

    def get_track(self) -> Track:
        return self.track

    def start_race(self) -> list:
        times = []
        for i in range(5):
            speed = self.runners[i].get_speed()
            stamina = self.runners[i].get_stamina()
            distance = self.track.get_distance()
            daily_well_being = self.runners[i].get_daily_well_being()
            preference = self.runners[i].get_preference()
            if daily_well_being < 1.0:
                if 1.0 - daily_well_being > uniform(0, 1):
                    times.append("has not finished the race!")
                    continue
            # Jeśli myszka jest wypoczęta i ma dobry dzień, startuje szybciej.
            # W przeciwnym razie zaczyna wolniej.
            speed = speed * daily_well_being
            if stamina != 0.0:
                if self.track == "flat":
                    if preference == "flat":
                        # jeśli myszka lubi dany typ toru, biegnie chętniej,
                        stamina += 0.1
                    # wzór wyprowadzony na podstawie opisu ruchu jednostajnie przyspieszonego (lub opóźnionego)
                    time = (-speed + ((speed ** 2.0 + 2.0 * stamina * distance) ** 0.5)) / stamina
                elif self.track == "rising":
                    if preference == "rising":
                        stamina += 0.1
                    # wzór wyprowadzony na podstawie opisu ruchu jednostajnie przyspieszonego (lub opóźnionego) na równi
                    # pochyłej o nachyleniu 30 stopni, czyli od przyspieszenia odejmujemy g*sin(30), gdzie g to
                    # przyspieszenie ziemskie
                    time = (-speed +
                            ((speed ** 2.0 + 2.0 * (stamina - 9.81 * 0.5) * distance) ** 0.5)) / (stamina - 9.81 * 0.5)
                else:
                    if preference == "sloping":
                        stamina += 0.1
                    # wzór wyprowadzony na podstawie opisu ruchu jednostajnie przyspieszonego (lub opóźnionego) na równi
                    # pochyłej o nachyleniu 30 stopni, czyli do przyspieszenia dodajemy g*sin(30), gdzie g to
                    # przyspieszenie ziemskie
                    time = (-speed +
                            ((speed ** 2.0 + 2.0 * (stamina + 9.81 * 0.5) * distance) ** 0.5)) / (stamina + 9.81 * 0.5)
            else:
                time = distance / speed
            if time >= 0:
                times.append(time)
            else:
                times.append("has not finished the race!")
        return times

    def show_full_stats(self):
        print("-------------------------------FULL TABLE OF PARAMETERS------------------------------")
        table = [["number", "name", "speed", "stamina", "preference", "daily well-being"]]
        for i in range(5):
            # tworzymy krotkę z atrybutami myszki
            runners = self.runners
            mouse_atributes = (i+1, runners[i].get_name(), runners[i].get_speed(),
                               runners[i].get_stamina(), runners[i].get_preference(), runners[i].get_daily_well_being())
            # dodajemy ją do tabeli
            table.append(mouse_atributes)
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

    # number_to_show to liczba atrybutów, które mają się wyświetlić graczowi(nie licząc numeru i imienia)
    def show_random_stats(self, number_to_show: int):
        print("-----------------------------------LIST OF RUNNERS-----------------------------------")
        table = [["number", "name", "speed", "stamina", "preference", "daily well-being"]]

        # z all_atributes będziemy losować numery atrybutów, które gracz zobaczy
        all_atributes = [i for i in range(4)]

        for i in range(5):
            # losujemy numery atrybutów to pokazania
            numbers_to_show = sample(all_atributes, number_to_show)

            # tworzymy krotkę z atrybutami myszki
            runners = self.runners
            mouse_atributes = (i+1, runners[i].get_name(), runners[i].get_speed(), runners[i].get_stamina(),
                               runners[i].get_preference(), runners[i].get_daily_well_being())

            # dodajemy atrybuty stałe - numer i imię
            atributes_to_show = list(mouse_atributes[0:2])

            # uzupełniamy dalszą część tabeli
            for j in range(4):
                if j in numbers_to_show:
                    atributes_to_show.append(mouse_atributes[j+2])
                else:
                    atributes_to_show.append(" ")
            table.append(atributes_to_show)
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

    def get_winners(self, times: list) -> list:
        winner_time = np.inf
        for i in times:
            if type(i) == str:
                continue
            if i < winner_time:
                winner_time = i
        # winners to lista numerów zwycięzców
        winners = []
        for i in range(5):
            if type(times[i]) != str:
                if times[i] == winner_time:
                    winners.append(i)
        return winners

    def show_results(self, times: list, winners: list):
        print("----------------RESULTS----------------")
        table = [["number", "name", "time"]]

        for i in range(5):
            if type(times[i]) != str:
                table.append([i + 1, self.runners[i].get_name(), str(round(times[i], 5)) + " s"])
            else:
                table.append([i + 1, self.runners[i].get_name(), times[i]])
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        number_of_winners = len(winners)
        if number_of_winners == 1:
            print(f"...and the winner is {self.runners[winners[0]].get_name()}!")
        elif number_of_winners > 1:
            print("...and the winners are:")
            for i in range(number_of_winners):
                if i < number_of_winners-1:
                    print(f"{self.runners[winners[i]].get_name()},")
                else:
                    print(f"{self.runners[winners[i]].get_name()}!")
        else:
            print("This race has no winner!")
