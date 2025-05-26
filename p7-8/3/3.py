from random import shuffle

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.suit}{self.rank}'
    
class Deck:
    SUITS = ("♣", "♢", "♡", "♠")
    RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")


    def __init__(self):
        self.deck = [Card(s, r) for s in self.SUITS for r in self.RANKS]

    def deal(self):
        if self.deck:
            return self.deck.pop()
        raise ValueError('Все карты разыграны')
    
    def shuffle(self):
        if len(self.deck) < 52:
            raise ValueError('Перемешивать можно только полную колоду')
        return shuffle(self.deck)
    
    def __str__(self):
        return f'Карт в колоде: {len(self.deck)}'
