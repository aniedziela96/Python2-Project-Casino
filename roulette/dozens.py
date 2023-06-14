from roulette.bet import Bet


class Dozens(Bet):
    """
    A class used to represent a bet for dozens.

    :param weight: 2
    :type weight: int
    :param options: [1, 2, 3]
    :type options: list
    :param option: An acceptable bet option (1 for 1-12, 2 for 13-24 and 3 for 25-36)
    :type option: int
    """
    def __init__(self, option: int) -> None:
        """
        Constructor method.
        """
        super().__init__(2, [1, 2, 3])
        self.option = self.correct_option(option)

    def is_in_bet(self, number: int) -> bool:
        """Takes a number and checks if it is in the range of the bet (in the chosen option of it).

        :param number: The number that was drawn in the roulette.
        :type number: int

        :return: A bool which answers the title question (True if the number is in the range of the bet, False if it is not)
        :rtype: bool
        """
        if self.option == 1:
            if 0 < number < 13:
                return True
            else:
                return False
        elif self.option == 2:
            if 12 < number < 25:
                return True
            else:
                return False
        elif self.option == 3:
            if 24 < number < 37:
                return True
            else:
                return False
