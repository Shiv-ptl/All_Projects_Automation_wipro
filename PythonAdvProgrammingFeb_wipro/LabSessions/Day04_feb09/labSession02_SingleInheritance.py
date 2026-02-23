# create a python program with class name savingsccount
# and functions deposit in parent class  and  addinterest
# in the child class
from datetime import datetime

class SavingAccount:
    def __init__(self,Balance):
        self.Balance = Balance
        self.OpenDateTime = datetime.now()
        # self.AccNo = AccNo

        # self.Deposit = Deposit
        # self.Balance += Deposit
    def deposit(self,amount):
        self.Balance +=amount
        print("Amount Deposited: ",amount)

    def Bal(self):
        print("Account Balance is : ",self.Balance)

class InteresstAcc(SavingAccount):
    def addInterest(self,rate):
        interest = self.Balance * rate/100
        self.Balance += interest
        print("Interest Added = ",interest)
        print("Updated Account Balance = ",self.Balance)


# acc1 = InteresstAcc(10000)
#
# acc1.deposit(3000)
# acc1.addInterest(7)
class AccDetails(InteresstAcc):
    def displayDetails(self):
        print("Account opened on: ",self.OpenDateTime)


acc = AccDetails(10000)
acc.displayDetails()
acc.Bal()
acc.deposit(35000)
acc.addInterest(12)
acc.displayDetails()





