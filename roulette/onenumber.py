from roulette.bet import Bet


class OneNumber(Bet):
    """
    A class used to represent a bet for a one number.
    ...

    :param weight: 35
    :type weight: int
    :param options: [i for i in range(37)]
    :type options: list
    :param option: An acceptable bet option (one number)
    :type option: int
    """
    def __init__(self, option: int) -> None:
        """
        Constructor method.
        """
        super().__init__(35, [i for i in range(37)])
        self.option = self.correct_option(option)

    def is_in_bet(self, number) -> bool:
        """Takes a number and checks if it is in the range of the bet (in the chosen option of it).

        :param number: The number that was drawn in the roulette.
        :type number: int

        :return: A bool which answers the title question (True if the number is in the range of the bet, False if it is not)
        :rtype: bool
        """
        if number == self.option:
            return True
        return False
