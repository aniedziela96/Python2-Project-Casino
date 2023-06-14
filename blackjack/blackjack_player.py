from blackjack.blackjack_hand import Blackjack_hand
from main.player import Player
from poker.hand import Hand
from poker.deck import Deck

class Blackjack_player(Player):
    def __init__(self, name: str, tokens: int) -> None:
        super().__init__(name, tokens)
        self.bets = [] #list of blackjack hands

    def show_bets(self) -> None:
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


    def player_hit(self, card: list, hand_number = 1) -> None:
        self.bets[hand_number - 1].add_cards(card)

    def add_bet(self, hand: Blackjack_hand) -> None:
        self.bets.append(hand)
  