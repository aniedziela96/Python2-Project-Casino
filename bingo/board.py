from tabulate import tabulate

class Board:
    """
    A class used to represent and operate the bingo board.

    :param columns: Columns of the board
    :type columns: list
    """
    def __init__(self, columns: list) -> None:
        """
        Constructor method.
        """
        self.columns = columns

    
    def check(self, number: int) -> None:
        """
        Checks the drawn number on the board. If it is not on the board, does nothing.

        :param number: The drawn number
        :type number: int
        """
        for column in self.columns:
            for i in range(5):
                if column[i] == number:
                    column[i] = '\N{BLACK CIRCLE}'
                    return None

    def is_bingo(self) -> bool:
        """
        Checks if there is a bingo on the board. Returns the answer.

        :return: The answer
        :rtype: bool
        """
        # checking columns
        for column in self.columns:
            if column.count('\N{BLACK CIRCLE}') == 5:
                return True

        # checking verses
        counter = 0
        for i in range(0, 5):
            for j in range(0, 5):
                if self.columns[j][i] == '\N{BLACK CIRCLE}':
                    counter += 1
            if counter == 5:
                return True
            counter = 0

        # checking diagonals
        if self.columns[0][0] == self.columns[1][1] == self.columns[2][2] == self.columns[3][3] == self.columns[4][4]:
            return True
        if self.columns[0][4] == self.columns[1][3] == self.columns[2][2] == self.columns[3][1] == self.columns[4][0]:
            return True

        return False

    def show(self):
        """
        Shows the board as a table (from module tabulate)
        """
        table = [["B", "I", "N", "G", "O"]]
        for i in range(5):
            row = []
            for column in self.columns:
                row.append(column[i])
            table.append(row)
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid', numalign="center", stralign="center"))
