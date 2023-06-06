# TODO imports
from main.player import Player
from poker.start_poker import Poker_Game


LIST_OF_GAMES = ["Races", "Poker", "Blackjack", "Roulette", "Bingo"] 

def get_pass():
    import tkinter
    import tkinter.simpledialog
    tk_root = tkinter.Tk()
    tk_root.withdraw()
    return tkinter.simpledialog.askstring('Password','Password:', show='*')

class Casino():
    def __init__(self, players_file) -> None:
        self.file = players_file

    def create_player(self, name, money):
        return Player(name, money)

    def login(self):
        print("Welcome to AH Casino!")
        first_time = input("Are you visiting us for the first time? (Y/N) ")
        if first_time in "Yesyes":
            while True:
                name = input("Give us your name: ")
                with open(self.file, 'r') as players:
                    for line in players:
                        line = line.strip('\n')
                        login, password, money = line.split(';')
                        if name == login:
                            print("Sorry this login is already taken"
                                  "Please choose another one.")
                            break
                    else:
                        break
            password = input("Password: ")
            with open(self.file, 'a') as players:
                players.write(name + ";" + password + ";" + "1000\n")

            player = self.create_player(name, 1000)
            return player

        elif first_time in "Nono":
            player_login = input("Login: ")
            while True:
                with open(self.file, 'r') as players:
                    for line in players:
                        line = line.strip('\n')
                        login, password, money = line.split(';')
                        if player_login == login:
                            player_password = get_pass()
                            while player_password != password:
                                print("Invalid password.")
                                player_password = get_pass()
                            money = int(money)
                            player = self.create_player(login, money)
                            return player
                print("Sorry I couldn't find that login.")
                player_login = input("Login: ")
        
        else:
            print("Are you dumb? YES or NO")
            return None


    def start(self):
        player = self.login()
        
        while True:
            print("Please choose a game from the list below:")
            for index, game in enumerate(LIST_OF_GAMES):
                print(f"{index + 1}: {game}")
            print("Type 'b' if you want to check your balance")
            print("Type 'q' if you want to quit")

            choice = input("Type a number of a game: ")

            if choice == "1":
                print("Races are starting")
                pass

            elif choice == "2":
                if player.get_tokens() < 100:
                    print("In order to play poker you need to bet 100 tokens, "
                          "please come back later with the money")
                else:
                    
                    player.spend_tokens(100)
                    print("Poker is starting")
                    game = Poker_Game(player)
                    
                    game.start_game()
                

            elif choice == "3":
                print("BlackJack is starting")
                pass

            elif choice == "4":
                print("Roulette is starting")
                pass

            elif choice == "5":
                print("Bingo is starting")
                pass

            elif choice == "q":
                print("Thank you for playing, hope to see you soon!")
                self.logout()
                break

            elif choice == "b":
                print(f"You have {player.get_tokens()} tokens")

    def logout(self):
        pass


if __name__ == "__main__":
    c = Casino("main/players_file.csv")
    c.start()

    