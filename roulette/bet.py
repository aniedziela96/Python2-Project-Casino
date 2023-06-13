class Bet:
    """
    A class used to represent a bet (basis for all types of bets).
    ...

    Attributes
    ----------
    weight : int
        the weight of the bet
    options : list
        the list with available options for the bet


    Methods
    -------
    is_option_ok(option: int)
        Checks if the chosen option is acceptable.
        Returns a bool which answers the title question (True if the option is ok, False if it is not).
    correct_option(option: int)
        Takes an option as long as it is not acceptable.
        If the first try is ok, does nothing but return.
        Returns the correct option(int).
    winner_prize(tokens: int)
        Returns a winner's prize in tokens(int).
    """
    def __init__(self, weight: int, options: list) -> None:
        """
        Parameters
        ----------
        weight : int
            the weight of the bet
        options : list
            the list with available options for the bet
        """
        self.weight = weight
        self.options = options

    def is_option_ok(self, option: int) -> bool:
        """Checks if the chosen option is acceptable.

        Parameters
        ----------
        option: int
            The number of the option the player has chosen

        Returns
        -------
        bool
            a bool which answers the title question (True if the option is ok, False if it is not)
        """
        if option in self.options:
            return True
        return False

    def correct_option(self, option: int) -> int:
        """Takes an option as long as it is not acceptable.
        If the first try is ok, does nothing but return.

        Parameters
        ----------
        option: int
            The number of the option the player has chosen

        Returns
        -------
        option
            the acceptable option
        """
        while not self.is_option_ok(option):
            option = int(input("This option is not permissible! Try again: "))
        return option

    def winner_prize(self, tokens: int) -> int:
        """Takes an option as long as it is not acceptable.
        If the first try is ok, does nothing but return.

        Parameters
        ----------
        tokens: int
            the number of tokens that were placed in the bet

        Returns
        -------
        int
            the winner's prize in tokens
        """
        return tokens*self.weight
