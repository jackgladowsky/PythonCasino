from deck import Deck


class Blackjack:
    def __init__(self, player):
        self.player = player
        self.suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self.values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        self.deck = Deck(self.values, self.suits)

    def checkForAce(self, cards):
        if 14 in cards:
            return True
        else:
            return False

    def playBlackjack(self):
        print('Welcome to Blackjack!')
        print('------------------------------')

        print(f'Your balance is {self.player.balance}.')
        try:
            userBet = int(input('Enter bet: '))
            if userBet > self.player.balance:
                print('You cant bet more than you have in your balance.')
                userBet = int(input('Enter bet: '))
        except ValueError:
            print('Please input a valid bet!')
            userBet = int(input('Enter bet: '))
        print('------------------------------')

        gameLoop = True
        playerCards = []
        dealerCards = []

        playerHitCount = 0
        dealerHitCount = 0

        playerValue = 0
        dealerValue = 0

        while gameLoop:
            self.deck.shuffle()
            self.deck.checkIfEmpty()

            playerCards.append(self.deck.deal())
            dealerCards.append(self.deck.deal())
            playerCards.append(self.deck.deal())
            dealerCards.append(self.deck.deal())

            playerValue = int(
                playerCards[0][0]) + int(playerCards[1][0])
            dealerValue = int(dealerCards[0][0])

            print(
                f'Your first card is a {playerCards[0][2]} of {playerCards[0][1]}.')
            print(
                f'The dealers first card is a {dealerCards[0][2]} of {dealerCards[0][1]}.')
            print(
                f'Your second card is a {playerCards[1][2]} of {playerCards[1][1]}.')
            print('------------------------------')

            if self.checkForAce(playerCards):
                print(f'You have {playerValue} or {playerValue-14}.')
            else:
                print(f'You have {playerValue}.')

            print(f'The dealer has {dealerValue}.')
            print('------------------------------')

            print('Would you like to hit or stay?')

            userHandChoice = input('h to hit or s to stay (h/s): ')
            print('------------------------------')

            if userHandChoice != 'h' and userHandChoice != 's':
                print('Input Valid Choice')
                userHandChoice = input('h to hit or s to stay (h/s): ')
                print('------------------------------')

            while userHandChoice == 'h':
                self.deck.checkIfEmpty()
                playerHitCount += 1
                playerCards.append(self.deck.deal())
                playerValue += int(playerCards[playerHitCount+1][0])
                print(
                    f'Your new card is a {playerCards[playerHitCount+1][2]} of {playerCards[playerHitCount+1][1]}.')
                print(f'You now have {playerValue}.')
                print('------------------------------')
                if playerValue == 21:
                    userHandChoice = 's'
                elif playerValue > 21:
                    print('You busted!')
                    self.player.balance -= userBet
                    print(
                        f'You lose {userBet}. Your balance is now {self.player.balance}.')
                    print('------------------------------')
                    self.player.writeBalance()
                    userHandChoice = 's'

                else:
                    userHandChoice = input('h to hit or s to stay (h/s): ')
                    print('------------------------------')

            if playerValue > 21:
                gameLoop = False
                break

            print(
                f'The dealer flips a {dealerCards[1][2]} of {dealerCards[1][1]}.')
            dealerValue += int(dealerCards[1][0])
            print(f'The dealers new value is {dealerValue}.')
            print('------------------------------')

            if playerValue == 21 and playerHitCount == 0:
                if dealerValue == 21:
                    print('You push!')
                    self.player.balance += userBet
                    gameLoop = False
                    break
                print('Blackjack!')
                self.player.balance += round(userBet * 1.5)
                self.player.writeBalance()
                print(
                    f'You win {round(userBet * 1.5)}. Your balance is now {self.player.balance}.')
                print('------------------------------')
                gameLoop = False
                break

            while dealerValue < 17:
                self.deck.checkIfEmpty()
                dealerCards.append(self.deck.deal())
                dealerHitCount += 1
                dealerValue += int(dealerCards[dealerHitCount+1][0])
                print(
                    f'The dealer hits and flips a {dealerCards[dealerHitCount+1][2]} of {dealerCards[dealerHitCount+1][1]}.')
                print(f'The dealers new value is {dealerValue}.')
                print('------------------------------')

                if dealerValue > 21:
                    print('Dealer Busted!')
                    print('You Win!')
                    self.player.balance += userBet
                    self.player.writeBalance()
                    print(
                        f'You win {userBet}. Your balance is now {self.player.balance}.')
                    print('------------------------------')
                    gameLoop = False
                    break

            if dealerValue > 21:
                gameLoop = False
                break

            if playerValue == dealerValue:
                print('Push')
                print(
                    f'You kept {userBet}. Your balance is now {self.player.balance}.')
                self.player.writeBalance()
                print('------------------------------')
                gameLoop = False
            elif playerValue > dealerValue:
                print('You win!')
                self.player.balance += userBet
                self.player.writeBalance()
                print(
                    f'You win {userBet}. Your balance is now {self.player.balance}.')
                print('------------------------------')
                gameLoop = False
            elif playerValue < dealerValue:
                print('You lose!')
                self.player.balance -= userBet
                self.player.writeBalance()
                print(
                    f'You lose {userBet}. Your balance is now {self.player.balance}.')
                print('------------------------------')
                gameLoop = False
