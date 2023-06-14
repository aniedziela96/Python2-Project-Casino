from blackjack.blackjack_hand import Blackjack_hand
from poker.deck import Deck
from time import sleep

class Croupier_bj():
    """Class representing a blackjack croupier
    """
    def __init__(self) -> None:
        """Croupier_bj constructor
        """
        self.hand = Blackjack_hand()
        self.score = 0

    def draw_cards(self, cards: list) -> None:
        """Adds cards to croupier's hand.
            :param cards: List of cards that will be added to croupier's hand
            :type cards: list
        """
        self.hand.add_cards(cards)

    def show_hidden(self) -> None:
        """Prints a representation of croupiers hand, when first card is hidden
        """
        empty_row = "|           |   "
        print(" ___________    " * 2)
        print("|   *****   |   " + empty_row)
        if self.hand.cards[1][0] != 10:
            print(f"|  *     *  |   |  {self.hand.cards[1][0]}        |")
            print("|      **   |   " + empty_row)
            print(f"|     *     |   |     {self.hand.cards[1][1]}     |")
            print(empty_row * 2)
            print(f"|     *     |   |        {self.hand.cards[1][0]}  |")
            print("|___________|   " * 2)
        else:
            print(f"|  *     *  |   |  {self.hand.cards[1][0]}       |")
            print("|      **   |   " + empty_row)
            print(f"|     *     |   |     {self.hand.cards[1][1]}     |")
            print(empty_row * 2)
            print(f"|     *     |   |       {self.hand.cards[1][0]}  |")
            print("|___________|   " * 2)
            

    def show_open(self) -> None:
        """Shows croupier's cards
        """
        self.hand.show_hand()

    def set_score(self) -> None:
        """Calculates and sets croupier's hand score, according to blackjack rules"""
        self.hand.calculate_score()
        self.score = self.hand.score

    def croupiers_move(self, deck: Deck) -> None:
        """Plays a croupier move, draws cards from the `deck` and calculates score until croupier's
            score reaches 17, if a score is greater than 21 prints a message that 
            the croupier busted and changes score to 0

            :param deck: Deck from wich croupier will draw cards
            :type deck: class:`poker.deck.Deck`
            """
        self.set_score()
        print("Croupier's hand: ")
        self.hand.show_hand()

        while self.score < 17:
            print(self.score)
            print("Croupier is drawing a card... ")
            self.hand.add_cards(deck.draw())
            self.set_score()
            self.hand.show_hand()
            sleep(1)

        if self.score > 21:
            print("Crupier busted!")
            self.score = 0