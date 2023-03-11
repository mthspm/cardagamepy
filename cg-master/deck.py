import random

class Deck:
    
    MAX_CARDS = 30
    MAX_UNIQUE_CARDS = 2
    MAX_UNIQUE_LEGENDARIES = 1

    def __init__(self, cards = []) -> None:
        
        self.cards = cards

    def __str__(self):
        if not self.cards:
            return self.cards

    def build(self,package):
        for card in range(len(package)):
            self.cards.append(card)

    def add(self,card):
        self.cards.append(card)

    def remove(self,card):
        self.cards.remove(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def destroy(self):
        self.cards.clear()