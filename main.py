import os

from hilo import HiLo
from player import Player
from blackjack import Blackjack
from roulette import Roulette


def main():

    print('------------------------------')
    print('Welcome to the Python Casino!')
    print('------------------------------')

    playerName = input('Enter your name: ')
    print('------------------------------')

    player = Player(playerName)
    player.writeBalance()
    blackjack = Blackjack(player)
    roulette = Roulette(player)
    hilo = HiLo(player)

    print(f'Welcome {player.name}! Your starting balance is {player.balance}.')
    print('------------------------------')

    gameLoop = True

    while gameLoop:
        if player.checkBalance() == False:
            print('Your out of money! Better luck next time!')
            print('------------------------------')
            gameLoop = False
            break

        print(
            'Please choose from the available games below or type b to view your balance:')
        print('1. Blackjack')
        print('2. Roulette')
        print('3. Hi/Lo')
        print('4. Exit Casino')
        playerGameChoice = input('Enter choice here: ')
        print('------------------------------')

        if playerGameChoice == '1':
            print('You chose Blackjack!')
            print('------------------------------')
            os.system('cls')
            blackjack.playBlackjack()
        elif playerGameChoice == '2':
            print('You chose Roulette!')
            print('------------------------------')
            os.system('cls')
            roulette.playRoulette()
        elif playerGameChoice == '3':
            print('You chose Hi/Lo!')
            print('------------------------------')
            os.system('cls')
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
