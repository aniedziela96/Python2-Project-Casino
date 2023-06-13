from roulette.bet import Bet


class OneNumber(Bet):
    def __init__(self, option: int) -> None:
        super().__init__(35, [i for i in range(37)])
        self.option = self.correct_option(option)

    def is_in_bet(self, number) -> bool:
        if number == self.option:
            return True
        return False
