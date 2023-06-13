from roulette.bet import Bet


class Dozens(Bet):
    def __init__(self, option: int) -> None:
        super().__init__(2, [1, 2, 3])
        self.option = self.correct_option(option)

    def is_in_bet(self, number) -> bool:
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
