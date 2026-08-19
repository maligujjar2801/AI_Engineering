class Account:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: ${amount:.2f}")
        else:
            print("Insufficient Balance!")

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")


account_1 = Account("John Doe", 1000)

account_1.deposit(500)
account_1.withdraw(200)
account_1.display_balance()