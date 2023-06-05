from poker.poker_player import Poker_Player

class Poker_human(Poker_Player):
    def players_bet(self, money) -> bool:
        self.last_bet = money
        if self.wallet >= money:
            setattr(self, 'wallet',  
                    self.wallet - money)
            return True # the bet was successful
        else:
            print(f"{self.name}, you don't have enough money")
            return False # the bet didn't go through
        
    def player_match(self, last_bet):
        pass

    def player_fold(self):
        pass
