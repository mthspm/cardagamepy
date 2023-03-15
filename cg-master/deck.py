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
        if self.validation(package):
            for card in package:
                self.cards.append(card)
        else:
            return

    def destroy(self):
        self.cards.clear()

    def add(self,card,position):
        rnd_pos = random.randint(0,len(self.cards))
        if position == 'end':
            self.cards.append(card)
        elif position == 'random':
            self.cards.index(rnd_pos,card)
        elif position == 'start':
            self.cards.insert(0,card)
        else:
            return

    def add_multiple(self,package,position):
        for card in package:
            self.add(card,position)

    def remove(self,card):
        self.cards.remove(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def validation(self,deck):
        valid_card_types = ['common', 'rare', 'epic', 'legendary']
        name_counts = {}
        legendary_counts = {}

        for card in deck:
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