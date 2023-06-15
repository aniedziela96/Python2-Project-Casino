from random import choice, randrange, uniform, sample
import numpy as np
from races.track import Track
from tabulate import tabulate


class Race:
    """
    A class used to operate a single race.

    :param track: The track of the race
    :type track: class: `races.Track`
    :param runners: A list of runners (mice)
    :type runners: list
    """
    def __init__(self, track: Track, runners: list) -> None:
        """
        Constructor method.
        """
        self.track = track
        self.runners = runners

    def get_runners(self) -> list:
        """
        Runners' getter.

        :return: A list of runners (mice)
        :rtype: list
        """
        return self.runners

    def get_track(self) -> Track:
        """
        Track's getter.

        :return: The track of the race
        :rtype: class: `races.Track`
        """
        return self.track

    def start_race(self) -> list:
        """
        Runs the races. Calculates times based on the list of runners.

        :return: 
        """
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
            # If a mouse has a good day, she starts faster. If not, starts slower.
            speed = speed * daily_well_being
            if stamina != 0.0:
                if self.track == "flat":
                    if preference == "flat":
                        # If a mouse likes current type of a track, she runs faster
                        stamina += 0.1
                    # This formula is based on the uniformly accelerated/retraded motion equation
                    time = (-speed + ((speed ** 2.0 + 2.0 * stamina * distance) ** 0.5)) / stamina
                elif self.track == "rising":
                    if preference == "rising":
                        stamina += 0.1
                    # This formula is based on the uniformly accelerated/retraded motion equation
                    # on an inclined plane with an angle of inclination of 30 degrees, 
                    # so we subtract g*sin(30) from the acceleration, where g is the acceleration due to gravity
                    time = (-speed +
                            ((speed ** 2.0 + 2.0 * (stamina - 9.81 * 0.5) * distance) ** 0.5)) / (stamina - 9.81 * 0.5)
                else:
                    if preference == "sloping":
                        stamina += 0.1
                    # This formula is based on the uniformly accelerated/retraded motion equation
                    # on an inclined plane with an angle of inclination of 30 degrees, 
                    # so we add g*sin(30) from the acceleration, where g is the acceleration due to gravity
                    time = (-speed +
                            ((speed ** 2.0 + 2.0 * (stamina + 9.81 * 0.5) * distance) ** 0.5)) / (stamina + 9.81 * 0.5)
            else:
                time = distance / speed
            if time >= 0:
                times.append(time)
            else:
                times.append("has not finished the race!")
        return times

    def show_full_stats(self) -> None:
        print("-------------------------------FULL TABLE OF PARAMETERS------------------------------")
        table = [["number", "name", "speed", "stamina", "preference", "daily well-being"]]
        for i in range(5):
            # making a tuple with mouse attributes
            runners = self.runners
            mouse_attributes = (i+1, runners[i].get_name(), runners[i].get_speed(),
                               runners[i].get_stamina(), runners[i].get_preference(), runners[i].get_daily_well_being())
            # adding it to the table
            table.append(mouse_attributes)
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

    # number_to_show is a number of attributes to show the player (a number and a name of a mouse not included)
    def show_random_stats(self, number_to_show: int) -> None:
        print("-----------------------------------LIST OF RUNNERS-----------------------------------")
        table = [["number", "name", "speed", "stamina", "preference", "daily well-being"]]

        # drawing the number of attributes from all_attributes
        all_attributes = [i for i in range(4)]

        for i in range(5):
            # drawing numbers of attributes to show
            numbers_to_show = sample(all_attributes, number_to_show)

            # making a tuple with mouse attributes
            runners = self.runners
            mouse_attributes = (i+1, runners[i].get_name(), runners[i].get_speed(), runners[i].get_stamina(),
                               runners[i].get_preference(), runners[i].get_daily_well_being())

            # adding a number and a name of a mouse
            attributes_to_show = list(mouse_attributes[0:2])

            # filling the rest of the table
            for j in range(4):
                if j in numbers_to_show:
                    attributes_to_show.append(mouse_attributes[j+2])
                else:
                    attributes_to_show.append(" ")
            table.append(attributes_to_show)
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

    @staticmethod
    def get_winners(times: list) -> list:
        winner_time = np.inf
        for i in times:
            if type(i) == str:
                continue
            if i < winner_time:
                winner_time = i
        # winners is a list of winners' numbers
        winners = []
        for i in range(5):
            if type(times[i]) != str:
                if times[i] == winner_time:
                    winners.append(i)
        return winners

    def show_results(self, times: list, winners: list) -> None:
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
