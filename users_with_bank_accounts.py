class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        return self.balance

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def all_info(cls):
        for account in cls.all_accounts:
            print(f"Balance: {account.balance}, Interest Rate: {account.int_rate}")

class User:
    bank_name = "Brandon's Bank"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {
            "Checking Account" : BankAccount(.01,50),
            "Savings Account" : BankAccount(.03,50)
        }

    def display_user_balance(self):
        print(f"Member Name: {self.name}, Checking Account Balance: ${self.account['Checking Account'].display_account_info()}")
        print(f"Member Name: {self.name}, Savings Account Balance: ${self.account['Savings Account'].display_account_info()}")
        return self

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

brandon = User('Brandon Schumacher', 'brandon@gmail.com')
jacie = User('Jacie Schumacher', 'jacie@gmail.com')

brandon.account["Checking Account"].deposit(200).withdraw(50).withdraw(32).yield_interest()
brandon.account["Savings Account"].deposit(350).withdraw(50).deposit(5000).yield_interest()

jacie.account["Savings Account"].deposit(500).deposit(350).withdraw(50).yield_interest()
jacie.account["Checking Account"].withdraw(55).yield_interest()

brandon.display_user_balance()
jacie.display_user_balance()




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
