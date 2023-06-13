class BingoGame:
    def __init__(self, bingo_players: tuple, boards: list) -> None:
        self.bingo_players = bingo_players
        self.boards = boards

    def get_bingo_players(self) -> tuple:
        return self.bingo_players

    def check_boards(self, number: int) -> None:
        for board in self.boards:
            board.check(number)

    def is_bingos(self) -> list:
        bingos = []
        for i in range(0, len(self.boards)):
            if self.boards[i].is_bingo():
                bingos.append(i)
        return bingos

    def show_players_board(self) -> None:
        self.boards[0].show()
