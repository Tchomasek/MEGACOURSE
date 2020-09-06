class Account:

    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, ammount):
        self.balance-=ammount

    def deposit(self,ammount):
        self.balance+=ammount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):

    type='checking'

    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee=fee

    def transfer(self,ammount):
        self.balance-= ammount + self.fee

checking=Checking("balance.txt",1)
checking.transfer(100)

print(checking.balance)
checking.commit()
