from roulette.bet import Bet


class ThreeNumbers(Bet):
    """
    A class used to represent a bet for four numbers.
    ...

    :param weight: 11
    :type weight: int
    :param options: [i for i in range(37)]
    :type options: list
    :param option: An acceptable bet option (list of three numbers)
    :type option: list
    """
    def __init__(self, option: list) -> None:
        """
        Constructor method.
        """
        super().__init__(11, [i for i in range(37)])
        self.option = self.correct_option(option)

    def is_option_ok(self, option: list) -> bool:
        """
        Overriding method from a parent class (the cause is a different method of checking - all
        elements from the option must be in options and the length of option must be 3)

        :param option: bet option (list of three numbers)
        :type option: list

        :return: A bool which answers the title question (True if the option is ok, False if it is not)
        :rtype: bool
        """
        if all(elem in self.options for elem in option) and len(set(option)) == 3:
            return True
        return False

    def correct_option(self, option: list) -> list:
        """
        Overriding method from a parent class (the cause is a different method of inputing the
        new, correct option - it is a list of numbers, not one number)

        :param option: bet option (list of three numbers)
        :type option: list

        :return: A new, correct option
        :rtype: list
        """
        while not self.is_option_ok(option):
            print("This option is not permissible! Try again.")
            option = [int(input("The first of three numbers: ")), int(input("The second of three numbers: ")),
                      int(input("The third of three numbers: "))]
        return option

    def is_in_bet(self, number) -> bool:
        """Takes a number and checks if it is in the range of the bet (in the chosen option of it).

        :param number: The number that was drawn in the roulette.
        :type number: int

        :return: A bool which answers the title question (True if the number is in the range of the bet, False if it is not)
        :rtype: bool
        """
        if number in self.option:
            return True
        return False
