class BankAccount():
    def __init__(self, int_rate= 0.01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
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
    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.balance * (1 + self.int_rate))
            return self
    @classmethod
    def __repr__(self):
        return f'BankAccount("{self.int_rate}{self.balance}"'

class User():
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.account = BankAccount(int_rate=0.02, balance= 0)
        self.savings_account = BankAccount(int_rate = 0.03, balance=0)
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"{self.first_name}\n{self.last_name}\n{self.email}\n{self.age}\n{self.is_rewards_member}\n{self.gold_card_points}")
                
    def enroll(self):
        if self.is_rewards_member == True:
            print('User already a member.')
            return False
        self.is_rewards_member = True
        self.gold_card_points = 200
        
    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points = self.gold_card_points - amount
        if self.gold_card_points < amount:
            print('Sorry, you dont have enough points')
        return amount
    def make_deposit(self, account):
        self.account.BankAccount.deposit(account)
    def make_withdrawl(self, account):
        self.account.withdraw(account)
    def display_user_balance(self, account):
        self.display_account_info(account)


ricky = User('Ricky', 'Rodriguez-Van Dusen', 'medic.rodriguez88@gmail.com', 33)
ricky.enroll()
ricky.spend_points(50)
sam = User('Sam', 'Doe', 'samdoe@gmail.com', 40)
sam.enroll()
sam.spend_points(80)
ronald = User('Ronald', 'McDonald', 'clown@McDonalds.com', 82)
ronald.enroll()
ronald.spend_points(40)
ricky.account.deposit(50).deposit(1000).withdraw(250).display_account_info()
ricky.savings_account.deposit(500).withdraw(50).display_account_info()