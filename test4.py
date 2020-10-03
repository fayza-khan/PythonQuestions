"""
Object Oriented Programming Challenge
For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""


class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print("Owner: ", self.owner)
        print("Balance: $", self.balance)

    def deposit(self, deposit_amount):
        bal = self.balance + deposit_amount
        print("Deposited", deposit_amount, "\nTotal balance now:", bal)

    def withdraw(self, withdraw_amount):
        if self.balance > withdraw_amount:
            bal = self.balance - withdraw_amount
            print("Withdrawal of", withdraw_amount, "\nTotal balance now:", bal)
        else:
            print("Cannot withdraw as balance is lower than withdrawal amount!")


account1 = BankAccount("Fayza", 2000)
account1.deposit(2000)
account1.withdraw(500)
account1.withdraw(4000)


