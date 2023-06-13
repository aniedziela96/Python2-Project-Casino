from roulette.bet import Bet


class EvenOdd(Bet):
    """
    A class used to represent a bet for even and odd numbers. Children of Bet.
    ...

    Attributes
    ----------
    weight : int
        1
    options : list
        [1, 2]
    option : int
        an acceptable bet option (1 for even or 2 for odd)

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
            an acceptable bet option (1 for even or 2 for odd)
        """
        super().__init__(1, [1, 2])
        self.option = self.correct_option(option)

    def is_in_bet(self, number: int) -> bool:
        """Takes a number and checks if it is in a range of the bet (in the chosen option of it).

        Parameters
        ----------
        number: int
            The number that was drawn in the roulette.

        Returns
        -------
        bool
            a bool which answers the title question (True if the number is in the range of the bet, False if it is not)
        """
        if number == 0:
            return False
        if self.option == 1:
            if number % 2 == 0:
                return True
            else:
                return False
        # elif self.option == 2:
        else:
            if number % 2 == 1:
                return True
            else:
                return False
