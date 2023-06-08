from blackjack.blackjack_hand import Blackjack_hand
from poker.deck import Deck

class Croupier_bj():
    def __init__(self) -> None:
        self.hand = Blackjack_hand()
        self.score = 0

    def draw_cards(self, cards: list):
        self.hand.add_cards(cards)

    def show_hidden(self):
        empty_row = "|           |   "
        print(" ___________    " * 2)
        print("|   *****   |   " + empty_row)
        print(f"|  *     *  |   |  {self.hand.cards[1][0]}        |")
        print("|      **   |   " + empty_row)
        print(f"|     *     |   |     {self.hand.cards[1][1]}     |")
        print(empty_row * 2)
        print(f"|     *     |   |        {self.hand.cards[1][0]}  |")
        print("|___________|   " * 2)

    def show_open(self):
        self.hand.show_hand()

    def set_score(self):
        self.score = self.hand.calculate_score()

    def croupiers_move(self, deck: Deck):
        self.set_score()
        while self.score < 17:
            print("Drawing card... ")
            self.hand.add_cards(deck.draw())
            self.set_score()
            self.show_open

        if self.score > 21:
            self.score = 0