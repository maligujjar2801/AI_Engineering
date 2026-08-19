🚀 Day 7 - Object-Oriented Programming (OOP)

What is OOP?

Object-Oriented Programming, also known as OOP, is a programming approach that focuses on real-world objects and makes code more organized, reusable, and easier to manage.

- It uses classes and objects.
- A single class can be used to create multiple objects.
- It models real-world entities as objects.

---

Class

A class is a blueprint used to create real-world objects.

- We can create multiple objects using a class.
- Every object created from the same class follows the same blueprint.

---

Object

An object is an instance of a class. It is created by providing values (attributes) to the class.

- Every object has its own unique attribute values.
- An object stores data according to the class used to create it.
- We can access an object's data using dot notation (".").

---

Constructor ("__init__()")

The "__init__()" method is a special dunder (double underscore) method that is automatically called when an object is created. It is used to initialize the instance attributes of a class.

Example

class Student:
    def __init__(self, name, age):
        pass

---

"self" Keyword

The "self" keyword refers to the current object (current instance).

- It allows every object to have its own unique data.
- It is used inside instance methods, including "__init__()".
- It is passed automatically when an object calls a method.

Example

person_2 = Person("Zainab", 17)

---

Instance Attributes

Instance attributes are variables that store data unique to each object.

- They store the values passed when an object is created.
- They are usually declared inside the "__init__()" method.

Example

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

---

Instance Methods

Instance methods are functions defined inside a class that perform operations using an object's data.

- They always take "self" as their first parameter.
- They are accessed using dot notation.

Example

def intro(self):
    print(f"Hi! I'm {self.name}. I'm {self.age} years old.")

---

Complete Example

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"Hi! I'm {self.name}. I'm {self.age} years old.")

person_1 = Person("Ali", 17)
person_2 = Person("Zainab", 17)

person_1.intro()
person_2.intro()

---

Key Takeaways

- OOP helps organize code into classes and objects.
- A class is a blueprint for creating objects.
- An object is an instance of a class.
- The "__init__()" method initializes an object's attributes.
- The "self" keyword refers to the current object (instance).
- Instance attributes store data unique to each object.
- Instance methods define the actions an object can perform.
- Multiple objects can be created from the same class, each with its own data.