class Bet:
    """
    A class used to represent a bet (basis for all types of bets).

    :param weight: The weight of the bet
    :type weight: int
    :param options: The list with available options for the bet
    :type options: list
    """
    def __init__(self, weight: int, options: list) -> None:
        """
        Constructor method
        """
        self.weight = weight
        self.options = options

    def is_option_ok(self, option: int) -> bool:
        """Checks if the chosen option is acceptable.

        :param option: The number of the option the player has chosen
        :type option: int

        :return: A bool which answers the title question (True if the option is ok, False if it is not)
        :rtype: bool
        """
        if option in self.options:
            return True
        return False

    def correct_option(self, option: int) -> int:
        """Takes an option as long as it is not acceptable.
        If the first try is ok, does nothing but return.

        :param option: The number of the option the player has chosen
        :type option: int

        :return: An acceptable option
        :rtype: bool
        """
        while not self.is_option_ok(option):
            option = int(input("This option is not permissible! Try again: "))
        return option

    def winner_prize(self, tokens: int) -> int:
        """Takes an option as long as it is not acceptable.
        If the first try is ok, does nothing but return.

        :param tokens: The number of tokens that were placed in the bet
        :type tokens: int

        :return: The winner's prize in tokens
        :rtype: int
        """
        return tokens*self.weight
