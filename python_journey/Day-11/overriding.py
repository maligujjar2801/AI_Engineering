class Animal:
    def sound(self):
        print("Some sound")
class Cat(Animal):
    def sound(self):
        print("Meow") # This method overrides the sound method of the Animal class

