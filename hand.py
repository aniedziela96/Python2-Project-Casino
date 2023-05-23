from deck import Deck

class Hand():
    def __init__(self) -> None:
        self.cards = []

    def add_cards(self, cards: list) -> None:
        for card in cards:
            self.cards.append(card)
    
    def __str__(self) -> str:
        cards_str = ""
        for card in self.cards:
            cards_str = cards_str + card[0].name + " OF " + card[1].name + ", "
        
        return cards_str.removesuffix(', ')
    
    def rank(self) -> str:
        pass

if __name__ == "__main__":
    d = Deck()
    d.shuffle()
    h = Hand()
    c = d.draw(n = 5)
    print(c)
    h.add_cards(c)
    p = str(h)
    print(p)
    print(sorted(h.cards))
