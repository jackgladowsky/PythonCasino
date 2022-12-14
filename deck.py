import random


class Deck:
    def __init__(self, values, suits):
        self.values = values
        self.suits = suits
        self.deck = []
        for suit in self.suits:
            for value in self.values:
                self.deck.append((value, suit))

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
