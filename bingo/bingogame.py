class BingoGame:
    """
    A class used to operate a single bingo game.

    :param bingo_players: The players who plays the game (one real player and two fake players)
    :type bingo_players: tuple
    :param boards: A list of players' boards
    :type boards: list
    """
    def __init__(self, bingo_players: tuple, boards: list) -> None:
        """
        Constructor method.
        """
        self.bingo_players = bingo_players
        self.boards = boards

    def get_bingo_players(self) -> tuple:
        """
        Players' getter.

        :return: A tuple of players
        :rtype: tuple
        """
        return self.bingo_players

    def check_boards(self, number: int) -> None:
        """
        Checks drawn number on players' boards.

        :param number: The drawn number
        :type number: int
        """
        for board in self.boards:
            board.check(number)

    def is_bingos(self) -> list:
        """
        Checks if there is a bingo on some board.

        :return: A list of numbers of players with bingo
        :rtype: list
        """
        bingos = []
        for i in range(0, len(self.boards)):
            if self.boards[i].is_bingo():
                bingos.append(i)
        return bingos

    def show_players_board(self) -> None:
        """
        Shows player's board.
        """
        self.boards[0].show()
