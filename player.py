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