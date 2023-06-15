from poker.poker_player import Poker_Player
from typing import Union

class Poker_human(Poker_Player):
    """Class representing a human poker player
    """

    def players_bet(self, tokens: int) -> Union[bool, str]:
        """Spends the tokens that player wants to bet.

        :param tokens: Tokens that will be bet.
        :type tokens: int
        ...
        :return: `True` if the player has the tokens, `False` otherwise. `all_in` if 
            player wants to bet all theirs available tokens
        :rtype: bool or str     
        """
        if self.tokens > tokens:
            self.spend_tokens(tokens)
            return True # the bet was successful
        elif self.tokens < tokens:
            print(f"{self.name}, you don't have enough money, "
                  f"you have {self.tokens} tokens.")
            return False # the bet didn't go through
        else:
            return "all_in"
