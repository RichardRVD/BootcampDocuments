class BankAccount():
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate= 0.01, balance = 0): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
        # your code here
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance = self.balance - amount
            return self
        if self.balance < amount:
            print('Insufficient funds: Charging a $5 fee')
            self.balance = self.balance - 5
            return self.balance
    def display_account_info(self):
        print('Balance: $' + str(self.balance))
        # your code here
    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.balance * (1 + self.int_rate))
            return self
        # your code here

    @classmethod
    def __repr__(self):
        return f'BankAccount("{self.int_rate}{self.balance}"'

account1 = BankAccount(.01, 0)
account1.deposit(100).deposit(25).deposit(50).withdraw(25).yield_interest().display_account_info()
account2 = BankAccount(.05, 0)
account2.deposit(100).deposit(200).withdraw(25).withdraw(25).withdraw(25).withdraw(25).yield_interest().display_account_info()
