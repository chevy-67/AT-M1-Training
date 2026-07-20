class InsufficientBalance(Exception):
    pass

class Account:
    def __init__(self,bal):
        self.bal = bal
    def deposit(self,amnt):
        self.bal+=amnt
    def withdraw(self,amnt):
        if amnt>self.bal:
            raise InsufficientBalance("Not enough money")
        self.bal-=amnt

a = Account(100)
a.deposit(10)
try:
    a.withdraw(200)
except InsufficientBalance as e:
    print(e)
finally:
    print("Transaction completed...")