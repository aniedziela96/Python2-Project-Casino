from main.player import Player
from poker.hand import Hand

class Poker_Player(Player):
    """Class representnig a player plaing poker
    
    :param name: Player's name
    :type name: str
    :param money: tokens that player will have
    :type money: int  
    """
    def __init__(self, name: str, money: int) -> None:
        """Contructor method
        """
        super().__init__(name, money)
        self.hand = Hand()
        self.hand_rank = None

    def draw_cards(self, cards: list) -> None:
        """Adds `cards` to player's hand
        
        :param cards: list of cards
        :type cards: list
        """
        self.hand.add_cards(cards)

    def __str__(self) -> str:
        return self.name + str(self.hand)
    
    def rank(self) -> None:
        """Determines the rank of players hand
        """
        if self.hand.is_five():
            self.hand_rank = self.hand.rank()

    def show_player_hand(self) -> None:
        """Shows player's hand
        """
        self.hand.show_hand()
