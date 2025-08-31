class BancaryAccount:
    def __init__(self, accountNumber, userName, balance):
        self.accountNumber = accountNumber
        self.userName = userName
        self.__balance = balance

    def ShowAccountData(self):
        print(f"Showing all data from the {self.accountNumber} account.")
        print(f'Hello, {self.userName}! Great see you again!')
        print(f'Your balance is: ${self._BancaryAccount__balance}')


bancaryAccount1 = BancaryAccount(1268752, "Filipe de Oliveira Alexandre", 0.00)

bancaryAccount1.ShowAccountData()

