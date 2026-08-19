class Category:
    def __init__(self,name):
        self.name = name 
        self.ledger = []

    def deposit(self,amount,description = ""):
        self.ledger.append({
            'amount': amount,
            'description': description
            })

    def withdraw(self,amount,description = ""):
        if self.check_funds(amount):
            amount *= -1
            self.ledger.append({'amount': amount,
           "description": description})
            return True
        else : 
           return False

    def transfer(self,amount,category):
        if self.check_funds(amount):
            self.withdraw(amount,f"Transfer to {category.name}")
            category.deposit(amount,f"Transfer from {self.name}")
            return True
        else:
            return False

    def get_balance(self):
        balance=0
        for transaction in self.ledger:
            
            balance += transaction["amount"]
        return balance

    def check_funds(self,amount):
        balance = self.get_balance()
        if amount <= balance :
            return True 
        else :
            return False

    def __str__(self):
        title = self.name.center(30,"*")
        output = title
        for dic in self.ledger :
            amount = dic["amount"]
            description = dic["description"][:23]
            line = f"{description:<23}{amount:>7.2f}"
            output += "\n"+line
        total = self.get_balance()
        output += "\nTotal: " + f"{total:.2f}"
        return output
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")

food.transfer(50, clothing)

print(food)
print()
print(clothing)



def create_spend_chart(categories):
    catogary_spendings = []
    output = "Percentage spent by category\n"

    for category in categories:
        spent = 0
        for dic in category.ledger:
            if dic["amount"] < 0:
                spent += abs(dic["amount"])
        catogary_spendings.append(spent)

    total = 0
    for i in catogary_spendings:
        total += i

    percentage = []
    for spending in catogary_spendings:
        percent = (spending / total) * 100
        percent = percent // 10
        percent = percent * 10
        percentage.append(percent)

    for i in range(100, -10, -10):
        output += f"{i:>3}|"
        for percent in percentage:
            if percent >= i:
                output += " o "
            else:
                output += "   "
        output += " \n"

    output += "    "
    n = len(categories)
    for i in range(n):
        output += "---"
    output += "-"
    output += "\n"

    longest = 0
    for category in categories:
        name = len(category.name)
        if name > longest:
            longest = name

    for i in range(longest):
        output += "     "
        for category in categories:
            if i < len(category.name):
                output += category.name[i]
            else:
                output += " "
            output += "  "
        if i != longest - 1:
            output += "\n"

    return output
print(create_spend_chart([food, clothing]))