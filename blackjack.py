from deck import Deck


class Blackjack:
    def __init__(self, player):
        self.player = player
        self.suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self.values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
                       'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
        self.deck = Deck(self.values, self.suits)

    def playBlackjack(self):
        print('Welcome to Blackjack!')
        print('------------------------------')

        gameLoop = True

        while gameLoop:
            print(f'Your balance is {self.player.balance}.')
            try:
                userBet = int(input('Enter bet: '))
            except ValueError:
                print('Please input a valid bet!')
                userBet = int(input('Enter bet: '))
            print('------------------------------')
