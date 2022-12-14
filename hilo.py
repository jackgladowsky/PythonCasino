from deck import Deck


class HiLo:
    def __init__(self, player):
        self.player = player
        self.suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self.ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
                      'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
        self.values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
                       'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
        self.deck = Deck(self.values)

    def playHiLo(self):
        self.deck.shuffle()
        self.deck.checkIfEmpty()

        gameLoop = True
        currentCard = self.deck.deal()
        nextCard = self.deck.deal()
        userWinnings = 0

        print('Welcome to HiLo.')
        print('The game will display the current card and you have to guess if the next card will be higher or lower.')
        print('Your winnings will double every time you get one right.')
        print('You can try and keep guessing correctly, but one wrong and you lose everything.')
        print('------------------------------')
        print('How much would you like to bet?')
        try:
            userBet = int(input('Enter bet: '))
        except ValueError:
            print('Please input a valid bet!')
            userBet = int(input('Enter bet: '))
        print('------------------------------')

        userWinnings = 0
        USERBET = userBet

        while gameLoop:

            # TODO
            # winnings dont account for bet
            # change winnings from 2x and maybe losses more every time user goes on

            print(f'The current card is a {currentCard}.')
            print(
                'Do you think the next card will be higher or lower? Press e to exit with winnings. (h/l/e)')
            userChoice = input('Enter here: ')
            print('------------------------------')

            if userChoice == 'e':
                self.player.balance += userWinnings
                self.player.writeBalance()
                gameLoop = False
            elif userChoice == 'h':
                if self.values[currentCard] > self.values[nextCard]:
                    print(f'Wrong. The next card was a {nextCard}.')
                    print(f'You lost {USERBET}.')
                    print('------------------------------')
                    self.player.balance -= USERBET
                    self.player.writeBalance()
                    gameLoop = False
                else:
                    print(f'Correct. The next card was a {nextCard}.')
                    userWinnings += userBet
                    userBet += userBet
                    print(f'Your current winnings are {userWinnings}.')
                    print('------------------------------')
            elif userChoice == 'l':
                if self.values[currentCard] > self.values[nextCard]:
                    print(f'Correct. The next card was a {nextCard}.')
                    userWinnings += userBet
                    userBet += userBet
                    print(f'Your current winnings are {userWinnings}.')
                    print('------------------------------')
                else:
                    print(f'Wrong. The next card was a {nextCard}.')
                    print(f'You lost {USERBET}.')
                    print('------------------------------')
                    self.player.balance -= USERBET
                    self.player.writeBalance()
                    gameLoop = False
            else:
                print('Enter a valid choice (h/l/e)')
                print('------------------------------')

            currentCard = nextCard
            self.deck.checkIfEmpty()
            nextCard = self.deck.deal()
