from roulette.bet import Bet


class TwoNumbers(Bet):
    def __init__(self, option: list) -> None:
        super().__init__(17, [i for i in range(37)])
        self.option = self.correct_option(option)

    def is_option_ok(self, option: list) -> bool:
        if all(elem in self.options for elem in option) and len(set(option)) == 2:
            return True
        return False

    def correct_option(self, option: list) -> list:
        while not self.is_option_ok(option):
            print("This option is not permissible! Try again.")
            option = [int(input("The first of two numbers: ")), int(input("The second of two numbers: "))]
        return option

    def is_in_bet(self, number) -> bool:
        if number in self.option:
            return True
        return False