from abc import ABC , abstractmethod

class Payment(ABC) :
    @abstractmethod
    def pay(self):
        pass

class CreditCard(Payment) :
    def pay(self,amount):
            print(f"{amount} paid via credit card.")

class Cash(Payment) :
    def pay(self,amount):
            print(f"{amount} paid via cash.")

class BankTransfer(Payment) :
    def pay(self,amount):
            print(f"{amount} paid via bank transfer.")

methods = [CreditCard(),Cash(), BankTransfer()]

for method in methods :
    method.pay("70,000")