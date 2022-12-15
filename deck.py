import random


class Deck:
    def __init__(self, values, suits):
        count = 0

        self.values = values
        self.suits = suits
        self.deck = []
        self.names = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
                      'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

        for suit in self.suits:
            for i in range(len(self.values)):
                self.deck.append((self.values[i], suit, self.names[i]))

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
