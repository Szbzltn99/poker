import random

class Deck:
    def __init__(self):
        self.ranks = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
        self.suits = ['h', 'd', 'c', 's']
        self.cards = [] #ez lesz a pakli
        for suit in self.suits:
            for rank in self.ranks: #(saját osztály baszás mindig self,,, nem sajátosztály---paraméter nem kell self
                card = rank + suit
                self.cards.append(card)

    def shuffle(self): #összekeveri
        random.shuffle(self.cards)

