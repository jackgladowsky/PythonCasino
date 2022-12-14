import random

import numpy as np


class Roulette:
    def __init__(self, player):
        self.player = player

    def playRoulette(self):
        # Declare first iteration of while loop

        choice = 'y'

        # Welcome user to the game

        print("Welcome to European Roulette")
        print('------------------------------')

        # Quick Instructions guide

        print('Individual numbers pay 35:1. They are any number between 0-36')
        print('Sections of the table are 1-12, 13-24, and 25-36 in the game they are labled as sections 1, 2 & 3 respectively.')
        print('Sections pay 2:1.')
        print('Lastly, we have the outside of the board where everything pays 1:1.')
        print('Your bets can be on red, black, even, odd, all numbers 1-18, or all numbers 19-36')

        # declare arrays with types of bets

        numberbets = []
        thirdbets = []
        outsidebets = []

        # declare sections of thirds of board

        firsthird = np.arange(1, 13)
        secondthird = np.arange(13, 25)
        thirdthird = np.arange(25, 37)

        # declare which numbers are red and black

        redList = [1, 3, 5, 7, 9, 12, 14, 16, 18,
                   19, 21, 23, 25, 27, 30, 32, 34, 36]

        blackList = [2, 4, 6, 8, 10, 11, 13, 15,
                     17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

        # start while loop in case user wants multiple games

        while choice == "y":

            # clear all arrays from previous games

            numberbets.clear()
            thirdbets.clear()
            outsidebets.clear()

            # ask user if they would like to bet on individual number

            wanttobetnumbers = str(
                input("Would you like to bet on individual numbers? 36:1 (y/n)\n"))

            # if they do, ask what numbers

            if wanttobetnumbers == 'y':

                number_of_numbers = int(
                    input("enter how many numbers you would like to play\n"))

                # enter all the numbers they bet on into a list

                for i in range(0, number_of_numbers):

                    numberbets.append(int(input("enter your number:\n")))

            # ask user if they would like to bet on a third of the board

            wanttobetthirds = str(
                input("Would you like to bet on the sections of the board? pay = 2:1 (y/n)\n"))

            # if they do, ask what sections

            if wanttobetthirds == 'y':

                number_of_thirds = int(
                    input("enter how many sections you would like to play (out of 3)\n"))

                # enter all sections into a list

                for i in range(0, number_of_thirds):

                    thirdbets.append(int(
                        input("enter your section(s) (1st 12, 2nd 12, 3rd 12)... enter as 1, 2, 3:\n")))

            # ask user if they would like to bet on outside of the board

            betnoutside = str(input(
                "Would you like to bet on whether the number is even, odd, red, black, 1-18, 19-36? pay: 1:1 (y/n)\n"))

            # if they do, ask what part of the outside

            if betnoutside == 'y':

                number_of_outside = int(
                    input("how many outside bets would you like to place? \n"))

                # enter all bets into a list

                for i in range(0, number_of_outside):

                    outsidebets.append(
                        str(input("Input either 'even', 'odd' 'red', 'black', '1-18', '19-36':\n")))

            # print the final bets

            print(
                f"your final bets are {numberbets} on the inside {thirdbets} on the thirds, and {outsidebets} on the outside")

            # simulate the rolling of the ball

            print("Rolling the ball...\n")

            rouletteball = random.randint(0, 36)

            print(f"The number is....\n {rouletteball}")

            # declare number win

            if rouletteball in numberbets:

                numberWin = True

                print(
                    f"Congradulations you win with your number {rouletteball}")

            # declare win if in one of the sections

            elif (rouletteball in range(1, 13)) and (1 in thirdbets):

                firsthirdWin = True

                print(
                    f"Congradulations you win with the number being in the first third")

            elif (rouletteball in range(13, 25)) and (2 in thirdbets):

                secondhirdWin = True

                print(
                    "Congradulations you win with the number being in the second third ")

            elif (rouletteball in range(25, 37)) and (3 in thirdbets):

                thirdthirdWin = True

                print(
                    "Congradulations you win with the number being in the third third ")

            # declare win if on the outside

            elif (rouletteball % 2 == 0) and ('even' in outsidebets):

                EvenWin = True

                print("Congradulations you win with the number being even")

            elif (rouletteball % 2 == 1) and ('odd' in outsidebets):

                oddWin = True

                print("Congradulations you win with the number being odd")

            elif (rouletteball in range(1, 19)) and ('1-18' in outsidebets):

                firsthalfWin = True

                print("Congradulations you win through the number being 1-18")

            elif (rouletteball in range(19, 37)) and ('19-36' in outsidebets):

                secondhalfWin = True

                print("Congradulations you win through the number being 19-36")

            elif (rouletteball in blackList) and ('black' in outsidebets):

                BlackWin = True

                print("Congradulations you win because it landed on black")

            elif (rouletteball in redList) and ('red' in outsidebets):

                RedWin = True

                print("Congradulations you win because it landed on red")

            else:

                print("Sorry, you lose!")

            # ask user to play again

            choice = input(
                "would you like to play again? enter y to continue or anything else to quit\n")

            if choice == 'y':

                print("NEW GAME!!\n\n")
