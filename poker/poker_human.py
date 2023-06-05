from poker.poker_player import Poker_Player

class Poker_human(Poker_Player):
    def players_bet(self, money) -> bool:
        if self.wallet > money:
            setattr(self, 'wallet',  
                    self.wallet - money)
            return True # the bet was successful
        elif self.wallet < money:
            print(f"{self.name}, you don't have enough money, \
                  you have {self.wallet} tokens.")
            return False # the bet didn't go through
        else: 
            return "all_in"
        
    def player_match(self, last_bet):
        pass

    def player_fold(self):
        pass
