from abc import ABC , abstractmethod

class Animal(ABC) :
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal) :
    def make_sound(self):
        print("Woof!")

class Cat(Animal) :
    def make_sound(self):
        print("Meoww!")

class Cow(Animal) :
    def make_sound(self):
        print("Boo...!")
    
animals = [Cat(),Dog(),Cow()]

for animal in animals :
    animal.make_sound()
    