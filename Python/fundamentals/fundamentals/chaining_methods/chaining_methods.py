class User():
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        
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
        return self


ricky = User('Ricky', 'Rodriguez-Van Dusen', 'medic.rodriguez88@gmail.com', 33)
ricky.enroll()
ricky.spend_points(10).spend_points(11).spend_points(4).spend_points(6).spend_points(12).spend_points(17)
ricky.display_info()
sam = User('Sam', 'Doe', 'samdoe@gmail.com', 40)
sam.enroll()
sam.spend_points(80).spend_points(11).spend_points(4).spend_points(6).spend_points(12).spend_points(17)
sam.display_info()
ronald = User('Ronald', 'McDonald', 'clown@McDonalds.com', 82)
ronald.enroll()
ronald.spend_points(40).spend_points(11).spend_points(4).spend_points(6).spend_points(12).spend_points(17)
ronald.display_info()