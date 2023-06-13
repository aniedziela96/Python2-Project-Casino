from roulette.bet import Bet


class Eighteens(Bet):
    """
    A class used to represent a bet for eighteens. Children of Bet.
    ...

    Attributes
    ----------
    weight : int
        1
    options : list
        [1, 2]
    option : int
        an acceptable bet option (1 for 1-18 or 2 for 19-36)

    Methods
    -------
    is_option_ok(option: int)
        Exactly the same as in the parent class.
    correct_option(self, option: int)
        Exactly the same as in the parent class.
    winner_prize(tokens: int)
        Exactly the same as in the parent class.
    is_in_bet(number: int)
        Takes a number and checks if it is in a range of the bet (in the chosen option of it).
        Returns a bool which answers the title question (True if the number is in the range of the bet,
        False if it is not).
    """
    def __init__(self, option: int) -> None:
        """
        Parameters
        ----------
        weight : int
            1
        options : list
            [1, 2]
        option : int
            an acceptable bet option (1 for 1-18 or 2 for 19-36)
        """
        super().__init__(1, [1, 2])
        self.option = self.correct_option(option)

    def is_in_bet(self, number: int) -> bool:
        """Takes a number and checks if it is in the range of the bet (in the chosen option of it).

        Parameters
        ----------
        number: int
            The number that was drawn in the roulette.

        Returns
        -------
        bool
            a bool which answers the title question (True if the number is in the range of the bet, False if it is not)
        """
        if self.option == 1:
            if 0 < number < 19:
                return True
            else:
                return False

        #elif self.option == 2:
        else:
            if 18 < number < 37:
                return True
            else:
                return False
