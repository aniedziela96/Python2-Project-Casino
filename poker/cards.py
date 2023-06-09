import enum


class Suit(enum.IntEnum):
    """Class representing card suits
    """
    HEARTS = 1
    DIAMONDS = 2
    SPADES = 3
    CLUBS = 4

    def __str__(self) -> str:
        if self.name == "HEARTS":
            suit = "\N{White Heart Suit}"
        elif self.name == "DIAMONDS":
            suit = "\N{White Diamond Suit}"
        elif self.name == "CLUBS":
            suit = "\N{White Club Suit}"
        elif self.name == "SPADES":
            suit = "\N{White Spade Suit}"

        return suit

class Rank(enum.IntEnum):
    """Class representing card ranks
    """
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    def __str__(self) -> str:
        if self.value == 14:
            rank = "A"
        elif self.value == 13:
            rank = "K"
        elif self.value == 12:
            rank = "Q"
        elif self.value == 11:
            rank = "J"
        else:
            rank = str(self.value)

        return rank

    
