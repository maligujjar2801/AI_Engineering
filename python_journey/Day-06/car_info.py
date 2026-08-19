class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

car_1 = Car("Toyota", "Camry", 2020)
car_2 = Car("Honda", "Civic", 2019)

print("First Car:")
print("Brand:\t", car_1.brand)
print("Model:\t", car_1.model)
print("Year:\t", car_1.year)

print("Second Car:")
print("Brand:\t", car_2.brand)
print("Model:\t", car_2.model)
print("Year:\t", car_2.year)