from typing import Any


class Player():
    """Class representing a casino player
    
    :param name: Player's name
    :type name: str
    :param tokens: Amount of tokens the player has.
    :type tokens: int
    """
    def __init__(self, name: str, tokens: int) -> None:
        """Constructor method
        """
        self.name = name
        self.tokens = tokens

    def get_name(self) -> str:
        """
        Name's getter.

        :return: Player's name
        :rtype: str
        """
        return self.name
    
    def get_tokens(self) -> int:
        """
        Tokens' getter.

        :return: Player's tokens
        :rtype: int
        """
        return self.tokens
    
    def spend_tokens(self, tokens: int) -> None:
        """Removes given number of `tokens` from player's account
        
        :param tokens: Number of tokens to be removed.
        :type tokens: int
        """
        self.tokens -= tokens

    def add_tokens(self, tokens: int) -> None:
        """Adds given number of `tokens` from player's account
        
        :param tokens: Number of tokens to be added.
        :type tokens: int
        """
        self.tokens += tokens

    def all_in(self) -> None:
        """Removes all of the tokens from player's acoount.
        """
        self.tokens = 0
    