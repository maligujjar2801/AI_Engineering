# 🚀 Day 10 - Inheritance in Python

## 1. What is Inheritance in OOP ?


Inheritance let a class use the methodds and attributes of another class without rewritting the same code again.

### Example 


```python
class Animal :
    def eat(self):
        print("Eating....")

class lion(Animal) :
    pass

lion = lion()
lion.eat()  # Eating....
```

- `eat()` method was inherited from Animal by lion .

## 2. Parent class :

The class from which the method or instance are being inherited is called Parent class .


### In the above example,
```python
class Animal:
    ...
```
 - `Animal()` class is the parent class.

## 3. Child class :

The class that inherits the method or attribute is called the Child class.

### In th above example, 
 ```python 
 class lion :
    ...
```
- `lion()`  class was child class.

## 4. `super()` method :

A super() method lets a child class to inherit the `__init__()` method of it's parent class.

### Example : 

```python
class Perosn :
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age 
        self.gender = gender 
class Student(Person):
    def __init__(self,name,age,gender,grade):
        super().__init__(name,age,gender,grade):
        self.grade = grade
```
- `super()` imports all attributes from parent's class.

## 5. Method Overriding:

Method overiding let child class modify and use the method defined in Parent's class. 

### Example :


```python 
class Animal :
    def sound(self):
        print("Some sound.")
class Dog(Animal):
    def sound(self):
        print("Woof woof")
dog = Dog()
dog.sound()
```

## 6. `isinstance()` method :

`isinstance()`  method checks if the given object belongs to a class.

### Example :

```python 
class Animal :
    pass

class Dog(Animal):
    pass

dog = Dog()
print(isinstance(dog,Dog))  #True
print(isinstance(dog,Animal))  #True 
```
- Because Dog is also an Animal.

## 7. `issubclass()` method :

`issubclass()` method checks if a class is a child class of another class or not .

### Example :

```python 
class Animal :
    pass

class Dog(Animal):
    pass
print(issubclass(Dog,Animal))  # True
```

## Programs created :

 - ### inheritance_practice.py
 - ### overriding.py
 - ### super_method.py
 - ### challenge.py

---

