import random

class Hand:

    def __init__(self, deck) -> None:

        self.hand = []
        self.deck = deck

    def draw(self):
        if not self.deck.cards:       #verificando se a lista esta vazia
            self.fatigue()
        elif len(self.hand) == 10:    #verificando se a mao esta cheia
            self.deck.cards.pop(0)    #se sim, queima a cartra que seria comprada
        else:
            draw = self.deck.cards.pop(0)   #removendo uma carta do deck
            self.hand.append(draw)          #e adicionando ela a mao
        
    def discard(self,card):
        self.hand.remove(card)

    def mulligan(self):
        for i in range(3):
            self.draw()

    def destroy(self):    
        self.hand.clear()