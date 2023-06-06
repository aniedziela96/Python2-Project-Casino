from poker.cards import Rank, Suit
from random import shuffle

class Deck:
    def __init__(self) -> None:
        self.card_list = []
        for suit in Suit:
            for rank in Rank:
                self.card_list.append((rank, suit))

    def shuffle(self) -> None:
        shuffle(self.card_list)

    def is_empty(self) -> bool:
        if len(self.card_list) == 0:
            return True
        else:
            return False

    def draw(self, n = 1) -> list:
        drawn_cards = []
        for i in range(n):
            if not self.is_empty():
                drawn_cards.append(self.card_list.pop(-1))
            else:
                raise IndexError ('Deck is empty')
                
        return drawn_cards

if __name__ == "__main__":
    d = Deck()
    # print(d.card_list)
    d.shuffle()
    # print(d.card_list)
    # print('-' * 20)
    # print(d.is_empty())
    # print(d.draw(n = 5))
    # print('-' * 20)
    # print(len(d.card_list))
    c = d.draw()
    print(c[0][0].name)


