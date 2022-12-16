import matplotlib.pyplot as plt
import numpy as np


class Player:
    writeCount = 0

    def __init__(self, name="Unknown"):
        self.name = name
        self.balance = 100

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, bal):
        self._balance = bal

    def checkBalance(self):
        if self._balance <= 0:
            return False

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

    def drawBalance(self):
        with open('balance.txt', 'r') as file:
            # Read all the lines from the file
            nums = file.readlines()

        # Split each line on the newline character
        balanceArrayOld = [num.split('\n') for num in nums]
        balanceArrayNew = []
        for array in range(len(balanceArrayOld)):
            balanceArrayOld[array].remove('')
            for num in balanceArrayOld[array]:
                balanceArrayNew.append(int(num))

        plt.plot(range(len(balanceArrayNew)), balanceArrayNew)
        plt.xlabel('Bets Made')
        plt.ylabel('Balance')
        plt.title('Balance vs Amount of Bets')
        plt.xticks(np.arange(0, len(balanceArrayNew), 1))
        plt.yticks(np.arange(min(balanceArrayNew), max(balanceArrayNew), 25))
        plt.show()
