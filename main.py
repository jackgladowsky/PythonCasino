from hilo import HiLo
from player import Player
                
def main():

    print('------------------------------')
    print('Welcome to the Python Casino!')
    print('------------------------------')
    
    playerName = input('Enter your name: ')
    print('------------------------------')
    
    player = Player(playerName)
    player.writeBalance()
    hilo = HiLo(player)
    
    
    print(f'Welcome {player.name}! Your current balance is {player.balance}.')
    print('------------------------------')
    
    gameLoop = True
    
    while gameLoop:
        print('Please choose from the available games below or type b to view your balance:')
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
        elif playerGameChoice == 'b':
            print(f'Your balance is {player.balance}.')
            print('------------------------------')
        else:
            print('Choose a valid selection.')
            print('------------------------------')

    
if __name__ == "__main__":
    main()