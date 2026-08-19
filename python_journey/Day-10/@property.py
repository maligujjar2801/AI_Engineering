class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    @property
    def balance(self):
        return self.__balance   
    @balance.setter
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")
acc = BankAccount(1000)
print(acc.balance)  # Accessing the balance using the property
acc.deposit = 500  # Using the deposit property to add funds
print(acc.balance)  # Accessing the updated balance using the property