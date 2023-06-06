from typing import Any


class Player():
    def __init__(self, name: str, tokens: int) -> None:
        self.name = name
        self.tokens = tokens

    def get_name(self) -> str:
        return self.name
    
    def get_tokens(self) -> int:
        return self.tokens
    
    def spend_tokens(self, tokens):
        self.tokens -= tokens

    def add_tokens(self, tokens):
        self.tokens += tokens

    def all_in(self):
        self.tokens = 0
    