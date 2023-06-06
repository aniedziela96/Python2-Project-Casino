from poker.poker_player import Poker_Player

class Poker_human(Poker_Player):
    def players_bet(self, tokens) -> bool:
        if self.tokens > tokens:
            self.spend_tokens(tokens)
            return True # the bet was successful
        elif self.tokens < tokens:
            print(f"{self.name}, you don't have enough money, "
                  f"you have {self.tokens} tokens.")
            return False # the bet didn't go through
        else: 
            return "all_in"
        
    def player_match(self, last_bet):
        pass

    def player_fold(self):
        pass
