import random

class Deck:
    
    MAX_CARDS = 30
    MAX_UNIQUE_CARDS = 2
    MAX_UNIQUE_LEGENDARIES = 1

    def __init__(self) -> None:
        
        self.cards = []
        self.isvalid = bool

    def __str__(self):
        if not self.cards:
            return self.cards

    def build(self,package):
        for card in range(len(package)):
            self.cards.append(card)

    def destroy(self):
        self.cards.clear()

    def add(self,card):
        self.cards.append(card)

    def add_multiple(self,package):
        for card in package:
            self.add(card)

    def remove(self,card):
        self.cards.remove(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def validation(self):
        valid_card_types = ['common', 'rare', 'epic', 'legendary']
        name_counts = {}
        legendary_counts = {}

        for card in self.cards:
            if card.type in valid_card_types:
                if card.type == 'legendary':
                    legendary_counts[card.name] = legendary_counts.get(card.name, 0) + 1
                    if legendary_counts[card.name] > 1:
                        return False
                else:
                    name_counts[card.name] = name_counts.get(card.name, 0) + 1
                    if name_counts[card.name] > 2:
                        return False

        return True