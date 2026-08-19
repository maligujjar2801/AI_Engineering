class Laptop:
    def __init__(self, price):
        self.__price = price  # Private attribute
    def get_price(self):
        return self.__price  # Public method to access the private attribute
    def set_price(self, price):
        if price > 0:
            self.__price = price  # Public method to modify the private attribute
        else:
            print("Price must be positive.")
laptop = Laptop(1000)
print(laptop.get_price())  # Accessing the private attribute using the public method
laptop.set_price(-150)  # Attempting to set a negative price
laptop.set_price(1500)  # Modifying the private attribute using the public method
print(laptop.get_price())  # Accessing the modified private attribute using the public method