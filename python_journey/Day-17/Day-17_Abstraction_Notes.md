# Day 17 — Abstraction in OOP

## 1. What is Abstraction?

Abstraction is one of the four major pillars of Object-Oriented Programming.

The four pillars are:

1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction

**Abstraction means hiding unnecessary implementation details and exposing only the important functionality.**

A simple example is a car.

When we call:

```python
car.start()
```

we do not need to know every internal step involved in starting the engine.

We only need to know that the car provides a `start()` operation.

---

## 2. Why Do We Use Abstraction?

Abstraction helps us:

- Reduce complexity
- Hide unnecessary implementation details
- Create a clear structure for classes
- Make large programs easier to maintain
- Define what functionality a class must provide
- Allow different classes to implement the same functionality in different ways

The main idea is:

```text
What something does
        ↓
is separated from
        ↓
How it does it
```

---

# 3. Abstract Base Classes

Python provides the `abc` module for creating Abstract Base Classes (ABCs).

We can import:

```python
from abc import ABC, abstractmethod
```

`ABC` is used as the base class for an abstract class.

`abstractmethod` is used to mark a method as abstract.

Basic structure:

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass
```

Here, `Animal` acts as a blueprint.

---

# 4. What is an Abstract Method?

An abstract method is a method that defines functionality that a child class is expected to implement.

Example:

```python
@abstractmethod
def make_sound(self):
    pass
```

The parent class is saying:

> Any concrete child class must provide its own `make_sound()` implementation.

The parent class does not need to define the actual behavior.

---

# 5. `ABC`

`ABC` stands for:

**Abstract Base Class**

Example:

```python
class Animal(ABC):
```

This tells Python that `Animal` is being used as an abstract base class.

Complete example:

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass
```

---

# 6. `@abstractmethod`

`@abstractmethod` is a decorator from the `abc` module.

Example:

```python
@abstractmethod
def make_sound(self):
    pass
```

It tells Python that this method must be implemented by a concrete child class.

---

# 7. Creating Child Classes

A child class can inherit from the abstract class.

```python
class Dog(Animal):

    def make_sound(self):
        print("Woof!")
```

Here:

```python
class Dog(Animal):
```

means `Dog` inherits from `Animal`.

`Dog` then provides its own implementation of:

```python
make_sound()
```

---

# 8. Today's Main Program

The program created an abstract `Animal` class.

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass
```

The class contains an abstract method called `make_sound()`.

Then three child classes were created.

---

## Dog

```python
class Dog(Animal):

    def make_sound(self):
        print("Woof!")
```

The Dog implementation produces:

```text
Woof!
```

---

## Cat

```python
class Cat(Animal):

    def make_sound(self):
        print("Meoww!")
```

The Cat implementation produces:

```text
Meoww!
```

---

## Cow

```python
class Cow(Animal):

    def make_sound(self):
        print("Boo...!")
```

The Cow implementation produces:

```text
Boo...!
```

---

# 9. Using the Objects

The program creates a list containing different Animal objects:

```python
animals = [Cat(), Dog(), Cow()]
```

Then a loop is used:

```python
for animal in animals:
    animal.make_sound()
```

The same method call is made for every object:

```python
animal.make_sound()
```

But each object gives a different result.

Output:

```text
Meoww!
Woof!
Boo...!
```

---

# 10. Abstraction and Polymorphism

This example also demonstrates polymorphism.

The parent class defines the common interface:

```python
make_sound()
```

The child classes implement it differently.

```text
Animal
  │
  └── make_sound()
        │
        ├── Dog → Woof!
        ├── Cat → Meoww!
        └── Cow → Boo...!
```

The same method name can therefore produce different behavior depending on the object.

---

# 11. Why Can't We Just Use a Normal Parent Class?

A normal parent class can also contain methods that child classes override.

However, an abstract class lets us explicitly define a requirement:

> A concrete subclass must implement this method.

This makes the design of a larger program clearer.

For example:

```python
class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass
```

This establishes a common contract for the child classes.

---

# 12. Abstract Classes as Blueprints

An abstract class can be thought of as a blueprint.

```text
              Animal
          Abstract Class
                 │
        ┌────────┼────────┐
        ↓        ↓        ↓
       Dog      Cat      Cow
        │        │        │
      sound    sound    sound
```

The parent determines the required structure.

The children determine the actual implementation.

---

# 13. Abstract Methods vs Normal Methods

### Normal method

A normal method already contains an implementation.

```python
def sleep(self):
    print("Sleeping")
```

### Abstract method

An abstract method defines a required method without providing the concrete implementation.

```python
@abstractmethod
def make_sound(self):
    pass
```

So:

```text
Normal method
→ Parent provides implementation

Abstract method
→ Child provides implementation
```

---

# 14. Abstract Classes Can Have Normal Methods

An abstract class does not have to contain only abstract methods.

For example:

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

    def sleep(self):
        print("Animal is sleeping")
```

A child class can implement `make_sound()` and also use `sleep()`.

---

# 15. What Happens If a Child Does Not Implement the Abstract Method?

Suppose:

```python
class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass
```

And:

```python
class Dog(Animal):
    pass
```

`Dog` has not implemented `make_sound()`.

Therefore, `Dog` remains abstract and cannot be instantiated as a concrete object.

The important rule is:

```text
If a child class does not implement
all required abstract methods,
it cannot be used as a concrete class.
```

---

# 16. Abstraction vs Encapsulation

These concepts are related but different.

## Encapsulation

Encapsulation focuses on bundling data and methods together and controlling access to internal data.

Example:

```python
class BankAccount:

    def __init__(self):
        self.__balance = 0
```

The balance is kept inside the class.

## Abstraction

Abstraction focuses on hiding unnecessary implementation details.

Example:

```python
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
```

The user only needs to know that the shape provides `area()`.

### Easy way to remember

```text
Encapsulation → Protect the data

Abstraction → Hide the complexity
```

---

# 17. Abstraction vs Inheritance

Inheritance means that one class derives from another.

Example:

```python
class Dog(Animal):
```

Abstraction defines what functionality a class should provide.

Example:

```python
@abstractmethod
def make_sound(self):
    pass
```

They often work together:

```text
Abstract Parent
      ↓
Inheritance
      ↓
Child Class
      ↓
Implement required methods
```

---

# 18. Abstraction vs Polymorphism

Polymorphism means that the same interface can behave differently for different objects.

In today's program:

```python
for animal in animals:
    animal.make_sound()
```

The method is the same:

```python
make_sound()
```

But the behavior depends on the object:

```text
Dog → Woof!
Cat → Meoww!
Cow → Boo...!
```

Abstraction provides the common structure, while polymorphism allows different implementations.

---

# 19. Real-World Example

Consider a payment system.

Different payment methods may have different internal processes.

```text
             Payment
          Abstract Class
                │
       ┌────────┼────────┐
       ↓        ↓        ↓
 CreditCard   Cash   BankTransfer
```

The abstract class could define:

```python
@abstractmethod
def pay(self, amount):
    pass
```

Every payment method would then implement `pay()` in its own way.

The rest of the application only needs to know that:

```python
payment.pay(amount)
```

is available.

It does not need to know the internal implementation.

---

# 20. Another Example — Shapes

An abstract `Shape` class could define:

```python
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
```

Different shapes could then implement:

```python
class Rectangle(Shape):

    def area(self):
        ...
```

and:

```python
class Circle(Shape):

    def area(self):
        ...
```

The common requirement is:

```text
Every Shape must provide area()
```

But the calculation can be different for every shape.

---

# 21. Important Syntax to Remember

### Import

```python
from abc import ABC, abstractmethod
```

### Abstract class

```python
class Parent(ABC):
```

### Abstract method

```python
@abstractmethod
def method(self):
    pass
```

### Child class

```python
class Child(Parent):
```

### Implementing the method

```python
def method(self):
    # implementation
    pass
```

---

# 22. General Pattern

This is the basic pattern to remember:

```python
from abc import ABC, abstractmethod


class Parent(ABC):

    @abstractmethod
    def method(self):
        pass


class Child(Parent):

    def method(self):
        print("Implementation")
```

This pattern is important for understanding abstraction in Python.

---

# 23. Key Takeaways

### Abstraction

Hides unnecessary implementation details and exposes essential functionality.

### ABC

`ABC` is used to create Abstract Base Classes.

### `@abstractmethod`

Marks a method that concrete subclasses are required to implement.

### Abstract class

Acts as a blueprint/common structure for related classes.

### Child class

Provides the actual implementation of abstract methods.

### Polymorphism

Allows the same method call to behave differently for different objects.

---

# 24. Quick Revision

```text
What is abstraction?
→ Hiding unnecessary implementation details.

What is ABC?
→ Abstract Base Class.

Which module provides ABC?
→ abc

Which decorator creates an abstract method?
→ @abstractmethod

Can a concrete child class ignore an abstract method?
→ No. It must implement the required abstract methods.

Can an abstract class have normal methods?
→ Yes.

Why is abstraction useful?
→ It creates clear interfaces and reduces complexity.
```

---

# 25. Day 17 Summary

Today I learned **Abstraction in OOP** and practiced it using Python's `abc` module.

My main program used:

```text
ABC
abstractmethod
Inheritance
Abstract methods
Child classes
Polymorphism
```

The most important concept I learned is:

> **An abstract class defines what a class should provide, while the child class defines how it provides it.**

---

## 🐍 Python Journey Progress

**Day 17 — Abstraction in OOP ✅**

Continuing step by step toward stronger Python, OOP, and software engineering fundamentals.
