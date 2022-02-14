from audioop import lin2adpcm


class User:
    def __init__(self, name):
        self.account_balance = 0
        self.name = name
        self.other_self = name
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance (self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def transfer_money (self, amount, other_self):
        self.account_balance -= amount
        other_self.account_balance += amount
        self.display_user_balance()
        other_self.display_user_balance()


marc = User("Marc")
steph = User("Steph")
lima = User("Lima")
steph.make_deposit(500).make_deposit(75).make_deposit(30).make_withdrawal(100).display_user_balance()

marc.make_deposit(300).make_deposit(300).make_withdrawal(150).make_withdrawal(100).display_user_balance()

marc.transfer_money(100, steph)
