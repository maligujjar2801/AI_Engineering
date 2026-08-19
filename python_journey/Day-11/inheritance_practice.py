class Vehicle :
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def start(self):
        print("Car started")

car = Car()
car.start()  # Output: Car started