class Animal :
    pass
class Dog(Animal) :
    def sound(self):
        print("Woof woof !")
class Cat(Animal) :
    def sound(self):
        print("Meoww... !")
class Cow(Animal) :
    def sound(self):
        print("Boooo... !")

def make_sound(obj):
    print(obj.sound)
