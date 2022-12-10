import random

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Player:
    writeCount = 0
    def __init__(self, name='Unknown'):
        self.name = name
        self.balance = 100
        
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, bal):
        self._balance = bal
        
    def writeBalance(self):
        if self.writeCount == 0:
            with open('balance.txt', 'w') as file:
                file.write(str(self._balance))
                file.write('\n')
        else:
            with open('balance.txt', 'a+') as file:
                file.write(str(self._balance))
                file.write('\n')   
        self.writeCount += 1
            
class Deck:
    def __init__(self):
        self.deck = [card for card in values]
        
    def shuffle(self):
        random.shuffle(self.deck)    

    def deal(self):
        return self.deck.pop()
    
    def checkIfEmpty(self):
        if len(self.deck) == 0:
            self.deck = [card for card in values]
            random.shuffle(self.deck)
            print('Shuffling Deck...')
            print('------------------------------')
        
        
class HiLo:
    
    def __init__(self, player, deck):
        self.player = player
        self.deck = deck
        
    def playHiLo(self):

        gameLoop = True
        currentCard = self.deck.deal()
        nextCard = self.deck.deal()
        
        print('Welcome to HiLo.')
        print('How much would you like to bet?')
        userBet = int(input('Enter bet: '))
        
        while gameLoop:
            
            print(f'The current card is a {currentCard}.')
            print('Do you think the next card will be higher or lower? Press e to exit. (h/l/e)')
            userChoice = input('Enter here: ')
            print('------------------------------')
            
            if userChoice == 'e':
                gameLoop = False
            elif userChoice == 'h':
                if values[currentCard] > values[nextCard]:
                    print(f'Wrong. The next card was a {nextCard}.')
                    self.player.balance -= userBet
                else:
                    print(f'Correct. The next card was a {nextCard}.')
                    self.player.balance += userBet
            elif userChoice == 'l':
                if values[currentCard] > values[nextCard]:
                    print(f'Correct. The next card was a {nextCard}.')
                    self.player.balance += userBet
                else:
                    print(f'Wrong. The next card was a {nextCard}.')
                    self.player.balance -= userBet
            else:
                print('Enter a valid choice (h/l/e)')
            print('------------------------------')
            
            self.player.writeBalance()
            print(f'Your current balance is {self.player.balance}.')
            print('------------------------------')
            currentCard = nextCard
            self.deck.checkIfEmpty()
            nextCard = self.deck.deal()

                
def main():

    print('------------------------------')
    print('Welcome to the Python Casino!')
    print('------------------------------')
    
    playerName = input('Enter your name: ')
    print('------------------------------')
    
    player = Player(playerName)
    player.writeBalance()
    deck = Deck()
    deck.shuffle()
    hilo = HiLo(player, deck)
    
    
    print(f'Welcome {player.name}! Your current balance is {player.balance}.')
    print('------------------------------')
    
    gameLoop = True
    
    while gameLoop:
        print('Please choose from the available games below:')
        print('1. Blackjack')
        print('2. Roulette')
        print('3. Hi/Lo')
        print('4. Exit Casino')
        playerGameChoice = input('Enter choice here: ')
        print('------------------------------')
        
        if playerGameChoice == '1':
            print('You chose Blackjack!')
            print('------------------------------')
            gameLoop = False
        elif playerGameChoice == '2':
            print('You chose Roulette!')
            print('------------------------------')
            gameLoop = False
        elif playerGameChoice == '3':
            print('You chose Hi/Lo!')
            print('------------------------------')
            print(f'Your current balance is {player.balance}.')
            print('------------------------------')
            hilo.playHiLo()
        elif playerGameChoice == '4':
            print('Leaving Casino.')
            print('------------------------------')
            gameLoop = False
        else:
            print('Choose a valid selection.')
            print('------------------------------')

    
if __name__ == "__main__":
    main()