# 🐍 Day 17 — Abstraction in OOP

## 📚 Python Journey

**Day 17** of my Python learning journey, focused on **Abstraction in Object-Oriented Programming (OOP)**.

Today I learned how abstraction can be used to define a common structure for related classes while allowing each child class to provide its own implementation.

---

## 🎯 What I Learned

- What abstraction means in OOP
- Abstract Base Classes (ABCs)
- The `ABC` class
- The `@abstractmethod` decorator
- Abstract methods
- Inheritance with abstract classes
- Implementing abstract methods in child classes
- Polymorphism through a common abstract interface
- Why abstract classes are useful in larger programs

---

## 🧠 Main Concept

**Abstraction** means hiding unnecessary implementation details and exposing the essential functionality.

In Python, abstraction can be implemented using the `abc` module:

```python
from abc import ABC, abstractmethod
```

An abstract class acts as a blueprint for its child classes.

---

## 💻 Practical Program

In today's program, I created an abstract `Animal` class with an abstract `make_sound()` method.

Then I created three child classes:

- `Dog`
- `Cat`
- `Cow`

Each class implements `make_sound()` differently.

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):

    def make_sound(self):
        print("Woof!")

class Cat(Animal):

    def make_sound(self):
        print("Meoww!")

class Cow(Animal):

    def make_sound(self):
        print("Boo...!")

animals = [Cat(), Dog(), Cow()]

for animal in animals:
    animal.make_sound()
```

The program demonstrates abstraction because `Animal` defines what every animal must provide, while the child classes decide how `make_sound()` actually behaves.

---

## 🔑 Important Syntax

### Abstract Base Class

```python
class Animal(ABC):
```

### Abstract Method

```python
@abstractmethod
def make_sound(self):
    pass
```

### Child Class

```python
class Dog(Animal):
```

### Implementing the Abstract Method

```python
def make_sound(self):
    print("Woof!")
```

---

## 🔄 Connection with Polymorphism

The final part of the program:

```python
for animal in animals:
    animal.make_sound()
```

uses the same method call:

```python
animal.make_sound()
```

but produces different results depending on the object.

This connects **abstraction** with **polymorphism**.

---

## 📁 Files

```text
Day-17/
│
├── README.md
├── abstraction.py
└── Abstraction_Notes.md
```

---

## 🚀 Progress

**Day 17 completed ✅**

I am continuing my Python journey by building a stronger understanding of OOP concepts and writing practical programs instead of only studying theory.

### Next Step

Continue learning advanced Python/OOP concepts and apply them in more real-world projects.

---

## 🧑‍💻 Learning Journey

This project is part of my complete Python learning journey in my **AI Engineering** repository.

⭐ Learning Python step by step  
💻 Building practical projects  
🧠 Strengthening OOP fundamentals  
🚀 Preparing for AI/ML and software engineering
