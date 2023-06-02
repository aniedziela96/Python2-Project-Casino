class Player():
    def __init__(self, name: str, money: int) -> None:
        self.name = name
        self.wallet = money

    def get_name(self) -> str:
        return self.name
    
    def get_money(self) -> int:
        return self.wallet
    