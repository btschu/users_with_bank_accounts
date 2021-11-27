class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds: Charging a $5 Fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        return self.balance
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (1 + self.int_rate)
        return self

    @classmethod
    def all_info(cls):
        for account in cls.all_accounts:
            print("Balance:",account.balance,"Rate:",account.int_rate)

class User:
    bank_name = "Brandon's Bank"
    def __init__(self, name, email, type):
        self.name = name
        self.email = email
        self.account = {
            "Checking Account" : BankAccount(.01,800),
            "Savings Account" : BankAccount(.03,2000)
        }
    def display_user_balance(self):
        print(f"Member Name: {self.name}, Checking Account Balance: {self.account['Checking Account'].display_account_info()}")
        print(f"Member Name: {self.name}, Savings Account Balance: {self.account['Savings Account'].display_account_info()}")
        return self
    def transfer_money(self, type, other_user, other_user_type, amount):
        self.accounts[type].withdraw(amount)
        other_user.accounts[other_user_type].deposit(amount)
        return self

brandon = User('Brandon Schumacher', 'brandon@gmail.com', 'Savings Account')
brandon.account["Checking Account"].deposit(200).withdraw(200).withdraw(32)
brandon.account["Savings Account"].deposit(350).withdraw(50).deposit(5000)
brandon.display_user_balance()

#! Instructor's Solution

# class BankAccount:
#     accounts = []
#     def __init__(self,int_rate,balance):
#         self.int_rate = int_rate
#         self.balance = balance
#         BankAccount.accounts.append(self)

#     def deposit(self, amount):
#         self.balance += amount
#         return self

#     def withdraw(self,amount):
#         if(self.balance - amount) >= 0:
#             self.balance -= amount
#         else:
#             print("Insufficient Funds: Charging a $5 fee")
#             self.balance -= 5
#         return self

#     def display_account_info(self):
#         return f"{self.balance}"

#     def yeild_interest(self):
#         if self.balance > 0:
#             self.balance += (self.balance * self.int_rate)
#         return self

#     @classmethod
#     def print_all_accounts(cls):
#         for account in cls.accounts:
#             account.display_account_info()


# class User:

#     def __init__(self, name):
#         self.name = name
#         self.account = {
#             "checking" : BankAccount(.02,1000),
#             "savings" : BankAccount(.05,3000)
#         }


#     def display_user_balance(self):
#         print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
#         print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
#         return self

#     def transfer_money(self,amount,user):
#         self.amount -= amount
#         user.amount += amount
#         self.display_user_balance()
#         user.display_user_balance()
#         return self


# adrien = User("Adrien")

# adrien.account['checking'].deposit(100)
# adrien.display_user_balance()
