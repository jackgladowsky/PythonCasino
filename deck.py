import random

class Deck:
    def __init__(self, values):
        self.values = values
        self.deck = [card for card in self.values]
        
    def shuffle(self):
        random.shuffle(self.deck)    

    def deal(self):
        return self.deck.pop()
    
    def checkIfEmpty(self):
        if len(self.deck) == 0:
            self.deck = [card for card in self.values]
            random.shuffle(self.deck)
            print('Shuffling Deck...')
            print('------------------------------')
