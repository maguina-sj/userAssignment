class bankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        bankAccount.accounts.append(self)

    def deposit (self, amount):
        self.balance += amount
        return self

    def withdraw (self, amount):
        if bankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            self.balance -= 5
            print("Insufficient Funds: Charging $5 fee")
        return self

    def display_account_info (self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if (self.balance > 0):
            self.balance += (self.balance * self.int_rate)
            return self

    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

    @classmethod
    def allInfo (cls):
        for account in cls.accounts: 
            account.display_account_info()



class User:
    def __init__(self, name):
        self.account = {
            "checking": bankAccount(.02, 500),
            "saving": bankAccount(.03,1000)
        }
        self.name = name

    # def make_deposit(self, amount):
    #     self.account += amount
    #     return self

    # def make_withdrawal(self, amount):
    #     self.account -= amount
    #     return self

    def display_user_balance (self):
        print(f"User: {self.name}, Balance: ${self.account}")
        return self

    def transfer_money (self, amount, other_self):
        self.account -= amount
        other_self.account += amount
        self.display_user_balance()
        other_self.display_user_balance()


marc = User("Marc")
marc.account["checking"].deposit (100)
marc.account["checking"].display_account_info()
marc.account["saving"].display_account_info()
steph = User("Steph")
lima = User("Lima")
# steph.make_deposit(500).make_deposit(75).make_deposit(30).make_withdrawal(100).display_user_balance()

# marc.make_deposit(300).make_deposit(300).make_withdrawal(150).make_withdrawal(100).display_user_balance()

# marc.transfer_money(100, steph)



        
# savings = bankAccount(.02,500)
# savings.deposit(200).deposit(400).deposit(150).withdraw(500).yield_interest().display_account_info()
# checking = bankAccount(.01, 500)
# checking.deposit(200).deposit(200).withdraw(300).withdraw(200).withdraw(175).withdraw(300).yield_interest().display_account_info()

# bankAccount.allInfo()