class Bank:
    def __init__(self,balance, acc_num):
        self.balance = balance
        self.accno = acc_num

    def debit(self, amount):
        self.balance -= amount
        print(self.balance, amount)

    def credit(self, amount):
        self.balance += amount
        print(self.balance, amount)

    def TotalBln(self):
        print(self.balance)

stm = Bank(50000,123)
print(stm.balance)
print(stm.accno)

stm.debit(5000)
print(stm.accno)

stm.credit(10000)
print(stm.accno)

stm.TotalBln()
stm.credit(100000)
print(stm.accno)
stm.TotalBln()