from deck import Deck


class HiLo:
    def __init__(self, player):
        self.player = player
        self.suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self.values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
                       'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
        self.deck = Deck(self.values, self.suits)

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
        print('Type h for high or l for low.')
        print('------------------------------')
        print(f'Your balance is {self.player.balance}.')
        print('How much would you like to bet?')

        # check to make sure user can cover bet
        try:
            userBet = int(input('Enter bet: '))
        except ValueError:
            print('Please input a valid bet!')
            userBet = int(input('Enter bet: '))
        print('------------------------------')

        userWinnings = 0
        USERBET = userBet

        while gameLoop:
            print(
                f'The current card is a {currentCard[0]} of {currentCard[1]}.')
            print(
                'Do you think the next card will be higher or lower? Press e to exit with winnings. (h/l/e)')
            userChoice = input('Enter here: ')
            print('------------------------------')

            if userChoice == 'e':
                self.player.balance += userWinnings
                self.player.writeBalance()
                gameLoop = False
            elif userChoice == 'h':
                if self.values[currentCard[0]] > self.values[nextCard[0]]:
                    print(
                        f'Wrong. The next card was a {nextCard[0]} of {nextCard[1]}.')
                    print(f'You lost {USERBET}.')
                    print('------------------------------')
                    self.player.balance -= USERBET
                    self.player.writeBalance()
                    gameLoop = False
                else:
                    print(
                        f'Correct. The next card was a {nextCard[0]} of {nextCard[1]}.')
                    userWinnings += userBet
                    userBet += userBet
                    print(f'Your current winnings are {userWinnings}.')
                    print('------------------------------')
            elif userChoice == 'l':
                if self.values[currentCard[0]] > self.values[nextCard[0]]:
                    print(
                        f'Correct. The next card was a {nextCard[0]} of {nextCard[1]}.')
                    userWinnings += userBet
                    userBet += userBet
                    print(f'Your current winnings are {userWinnings}.')
                    print('------------------------------')
                else:
                    print(
                        f'Wrong. The next card was a {nextCard[0]} of {nextCard[1]}.')
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
