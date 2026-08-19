# Day 14 - Polymorphism in OOP 
## What is polymorphism ?
This is a greek word that means :

- **Poly** = Many
- **Morphs** = Forms
- **One Interface, Multiple Implimentation.**
 - It means that a method can react differently with different objects.

 ## Method Overriding :
 Method overriding means over-writting a method in child class that is created in parent class .
 ## Example 
 ```python
 class Animal :
    def speak(self):
        pass

 class Dog(Animal):
    def speak(self):
        print("Woof woof !")

 class Cat(Animal):
    def speak(self):
        print("Meoww...!")


cat = Cat()
dog = Dog()

cat.speak() # Meowww...!
dog.speak() # Woof woof !
```
## Polymophism through Inheritance :
When different classes use the same method inherited from parent class , then it's called **Polymophism through Inheritance .**

### Example 
``` python 
class Animal :
    def sound(self) :
        pass
class Dog(Animal) :
    def sound(self) :
        return "woof woof !"
 class Cat(Animal) :
    def sound(self):
        return "Meoww...!"