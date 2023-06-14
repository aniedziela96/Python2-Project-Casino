from typing import Union
from blackjack.blackjack_player import Blackjack_player
from blackjack.croupier_bj import Croupier_bj
from poker.deck import Deck
from blackjack.blackjack_hand import Blackjack_hand

class Blackjack():
    """Class representing one blackjack bet.

    :param croupier: Croupier playing current bet.
    :type croupier: class:`blackjack.croupier_bj.Croupier_bj`
    :param bj_player: Blackjack player playing current bet.
    :type bj_player: class:`blackjack.blackjack_player.Blackjack_player`
    :param bet_money: Number of tokens that player paid to play current bet.
    :type bet_money: int
    :param deck: Deck, with which the bet is played
    :type deck: class:`poker.deck.Deck`
    :param bet_number: Deck, with which the bet is played, defaults to 1.
    :type bet_number: int
    """
    def __init__(self, croupier: Croupier_bj, bj_player: Blackjack_player, 
                 bet_money: int, deck: Deck, bet_number = 1) -> None:
        """Blackjack Class constructor.
        """
        self.croupier = croupier
        self.player = bj_player 
        self.players_bet = bj_player.bets[bet_number - 1]
        self.bet_money = bet_money
        self.bet_number = bet_number
        self.deck = deck


    def end(self, player_win: bool) -> str:
        """Returns a string representing if player won or lost the bet

        :param player_win: True if player is supposed to win the bet, 
            False if they are supposed to lose
        :type player_win: bool
        ...
        :return: string "player wins" or "player lost"
        :rtype: str
        """
        if player_win:
            return "player wins"
        else:
            return "player lost"

    def hit(self) -> str:
        """Plays a hit action, draws one card from the deck and adds it to player's
            bet that is currently played. The score of the bet is calculated, if it is
            greater than 21 player is busted if not the hit was a success.
        
        :return: "bust" or "success" depending on result of hit action
        :rtype: str
        """
        card = self.deck.draw()
        self.player.player_hit(card, self.bet_number)
        self.players_bet.calculate_score()
        if self.players_bet.score > 21:
            return "bust"
        else:
            return "success"
        
        
    def double_down(self) -> str:
        """Plays a double down action. Checks if the player has enough money to play
            (player needs to have the same amount as he betted when he entered the game). 
            If he has, double down is played, bet_money is doubled, player spends required 
            tokens and plays the hit action.

        :return: "failed" if player didn't have enough tokens, "bust" if player busted,
            "success" if the double down was successful
        :rtype: str
        """
        if self.player.get_tokens() < self.bet_money:
            return "failed"
        else:
            self.bet_money *= 2
            self.player.spend_tokens(self.bet_money)
            res = self.hit()
            return res
            

    def insurance(self) -> Union[str, None]:
        """Plays insurance for half the tokens that where spent to play the game. If 
            player has required tokens calculates the score of croupier's hand. If croupier 
            has the score of 21, meaning he has a blackjack player wins twice the insurance 
            tokens if not he loses the insurance bet. The suitable message is printed.

        :return: "failed" if player didn't have enough money to play insurance or None
            if player had required tokens.
        :rtype: str or NoneType
        """ 
        insurance = int(0.5 * self.bet_money)
        if self.player.get_tokens() < insurance:
            return "failed"
        
        self.player.spend_tokens(insurance)
        self.croupier.set_score()
        if self.croupier.hand.score == 21:
            self.player.add_tokens(3 * insurance)
            print("You won insurance")
        else:
            print("You lost insurance")   
    
        
    def split(self) -> Union[str, 'Blackjack']:
        """Plays split action. Splits the bet into two separate bets and creates 
            new Blackjack with one card from the bet that was splitted and one
            that is drawn from the deck.

            :return: "failed" if player didn't have enough tokens to create new bet
                or the Blackjack bet that was created
            :rtype: str or class:`blackjack.Blackjack`
        """
        if self.player.get_tokens() < self.bet_money:
            return "failed"
        else:
            self.player.spend_tokens(self.bet_money)
            card_splitted = self.players_bet.card_split()
            new_bet = Blackjack_hand()
            new_bet.add_cards([card_splitted, self.deck.draw()[0]])
            self.player.add_bet(new_bet)
            self.players_bet.add_cards(self.deck.draw())
            return Blackjack(self.croupier, self.player, self.bet_money,
                             self.deck, len(self.player.bets))
            