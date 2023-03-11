import random

class Hand:

    def __init__(self) -> None:

        self.hand = []

    def __str__(self):
        if not self.hand:
            return self.hand

    def draw(self, deck):
        card = deck.pop(0)
        self.hand.append(card)

    def pop(self, card):
        self.hand.remove(card)

    def random_pop(self):
        random_card = random.choice(self.hand)
        self.hand.remove(random_card)

    def destroy(self):    
        self.hand.clear()