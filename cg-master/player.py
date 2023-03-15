from deck import Deck
from hand import Hand

class Player:

    def __init__(self, user, id):
        self.user = user
        self.id = id
        self.maxlife = 30
        self.maxmana = 10
        self.life = 30
        self.mana = 0
        self.hero = None
        self.deck = Deck()
        self.hand = Hand(self.deck)
        self.board = {
            'pos1': None,
            'pos2': None,
            'pos3': None,
            'pos4': None,
            'pos5': None,
            'pos6': None,
            'pos7': None
                     }
        self.fatigue = -1

    def __str__(self):
        return self.user

    def __hash__(self):
        return self.id.__hash__()

    def change_life(self,amount):
        if amount + self.life >= self.maxlife:
            self.life = self.maxlife
        else:
            self.life += amount

    def change_mana(self,amount):
        if amount + self.mana >= self.maxmana:
            self.mana = self.maxmana
        else:
            self.life += amount