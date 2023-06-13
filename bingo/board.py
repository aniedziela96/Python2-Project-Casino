class Board:
    def __init__(self, columns: list) -> None:
        self.columns = columns

    # funkcja zaznaczająca pole na planszy; jeśli danego pola nie ma, funkcja nic nie robi
    def check(self, number: int):
        for column in self.columns:
            for i in range(5):
                if column[i] == number:
                    column[i] = '\N{BLACK CIRCLE}'
                    return

    def is_bingo(self) -> bool:
        # sprawdzamy, czy bingo jest w którejś kolumnie
        for column in self.columns:
            if column.count('\N{BLACK CIRCLE}') == 5:
                return True

        # sprawdzamy, czy bingo jest w którymś wierszu
        counter = 0
        for i in range(0, 5):
            for j in range(0, 5):
                if self.columns[j][i] == '\N{BLACK CIRCLE}':
                    counter += 1
            if counter == 5:
                return True
            counter = 0

        # sprawdzamy, czy bingo jest na ukos
        if self.columns[0][0] == self.columns[1][1] == self.columns[2][2] == self.columns[3][3] == self.columns[4][4]:
            return True
        if self.columns[0][4] == self.columns[1][3] == self.columns[2][2] == self.columns[3][1] == self.columns[4][0]:
            return True

        return False

    def show(self):
        table = [["B", "I", "N", "G", "O"]]
        for i in range(5):
            row = []
            for column in self.columns:
                row.append(column[i])
            table.append(row)
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid', numalign="center", stralign="center"))
