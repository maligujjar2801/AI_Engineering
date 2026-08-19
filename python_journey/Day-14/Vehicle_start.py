class Vehicle :
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def start(self):
        print("Car is starting")

class Bike(Vehicle):
    def start(self):
        print("Bike is starting")


car = Car()
bike = Bike()
car.start()
bike.start()