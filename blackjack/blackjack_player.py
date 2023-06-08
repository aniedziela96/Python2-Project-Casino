from blackjack.blackjack_hand import Blackjack_hand
from main.player import Player
from poker.hand import Hand
from poker.deck import Deck

class Blackjack_player(Player):
    def __init__(self, name: str, tokens: int) -> None:
        super().__init__(name, tokens)
        self.bets = [] #list of blackjack hands

    def show_bets(self):
        if len(self.bets) == 0:
            print(" ")
        else:
            empty_row = "|           |   "
            top = " ___________    "
            bottom = "|___________|   "
            rows_fig_top = ""
            rows_suit = ""
            rows_fig_bottom = ""
            tops = ""
            bottoms = ""
            empty_rows = ""
            bet_row = ""
            i = 0
            for bet in self.bets:
                i += 1
                n = len(bet.cards)
                bet_row += "Bet " + str(i) + ":            " + "                 " * (n-1)
                for card in bet.cards:
                    if card[0] != 10:
                        rows_fig_top = rows_fig_top + "|  " + str(card[0]) + "        |   "
                        rows_suit = rows_suit + "|     " + str(card[1]) + "     |   "
                        rows_fig_bottom = rows_fig_bottom + "|        " + str(card[0]) + "  |   "
                    else:
                        rows_fig_top = rows_fig_top + "|  " + str(card[0]) + "       |   "
                        rows_suit = rows_suit + "|     " + str(card[1]) + "     |   "
                        rows_fig_bottom = rows_fig_bottom + "|       " + str(card[0]) + "  |   "
                
                rows_fig_top = rows_fig_top + "   "
                rows_suit = rows_suit + "   "
                rows_fig_bottom = rows_fig_bottom + "   "
                empty_rows += empty_row * n + "   "
                tops += top * n + "   "
                bottoms += bottom * n + "   "

            print(bet_row)
            print(tops)
            print(empty_rows)
            print(rows_fig_top)
            print(empty_rows)
            print(rows_suit)
            print(empty_rows)
            print(rows_fig_bottom)
            print(bottoms)


    def player_hit(self, card, hand_number = 1):
        self.bets[hand_number - 1].add_cards(card)

    def add_bet(self, hand: Blackjack_hand):
        self.bets.append(hand)

    def split(self, bet_number):
        pass


if __name__ == "__main__":
    d = Deck()
    d.shuffle()
    h1 = Blackjack_hand()
    h2 = Blackjack_hand()
    h3 = Blackjack_hand()
    h1.add_cards(d.draw(2))
    print(h1)
    h2.add_cards(d.draw(3))
    print(h2)
    h3.add_cards(d.draw(2))
    print(h3)
    p = Blackjack_player("rysio", 1000)
    p.add_bet(h1)
    p.add_bet(h2)
    p.add_bet(h3)
    p.show_bets()
        