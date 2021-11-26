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
        print("Balance:", self.balance)
        return self
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
        self.type = type
        self.accounts = {type: BankAccount(int_rate = 0.03, balance = 0)}

    def make_deposit(self, amount, type):
        self.accounts[type].deposit(amount)
        return self
    def make_withdraw(self, amount, type):
        self.accounts[type].withdraw(amount)
        return self
    def display_user_balance(self, type):
        print(self.name, type, self.accounts[type].balance)
        return self
    def transfer_money(self, type, other_user, other_user_type, amount):
        self.accounts[type].withdraw(amount)
        other_user.accounts[other_user_type].deposit(amount)
        return self
    def open_new_account(self, type):
        if type not in self.accounts:
            self.accounts[type] = BankAccount(int_rate = 0.03, balance = 0)
        else:
            print('account of this type already exists')
        return self


brandon = User('Brandon Schumacher', 'brandon@gmail.com', 'Savings Account')
print(brandon)
brandon.make_deposit(200, 'Savings Account')
brandon.display_user_balance('Savings Account')
brandon.open_new_account('Checking Account')
print(brandon.accounts)
brandon.open_new_account('Checking Account')
print(brandon.accounts)
brandon.make_deposit(1000, 'Checking Account')
brandon.display_user_balance('Checking Account')