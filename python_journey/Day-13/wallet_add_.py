class Wallet :
    def __init__(self, amount):
        self.amount = amount
    def __add__(self, other):
        return self.amount + other.amount
wallet = Wallet(100)
print(wallet.amount)
wallet2 = Wallet(200)
print(wallet + wallet2)