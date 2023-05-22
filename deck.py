from cards import Rank, Suit
from random import shuffle

CARDS_LST = []
# create the list of possible playing cards
for suit in Suit:
    for rank in Rank:
        CARDS_LST.append((rank, suit))

class Deck:
    def __init__(self) -> None:
        self.card_list = CARDS_LST

    def shuffle(self) -> None:
        shuffle(self.card_list)


if __name__ == "__main__":
    d = Deck()
    print(d.card_list)
    d.shuffle()
    print(d.card_list)