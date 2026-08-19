class Animal :
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof woof !")

class Cat(Animal):
    def speak(self):
        print("Meoww...!")
dog = Dog()
cat = Cat()
dog.speak()
cat.speak()