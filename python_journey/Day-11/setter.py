class BankAccount :
    def __init__(self, balance):
        self.__balance = balance
    def add_balance(self,amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.__balance += amount
    def get_balance(self):
        return self.__balance
acc = BankAccount(1000)
acc.add_balance(500)
print(acc.get_balance())