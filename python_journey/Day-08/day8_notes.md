# 🚀 Day 8 - Advanced OOP 

## 📚 What is class attributes ?


A class variable is defined as an instance that is accessable by all objects and it's same for all objects defined by a class. 

---

### Example 


```python 
class Myclass :
    name = "Ali" # name is a class attribute. 
```
## 📚 What is instance attributes ?


An instance attribute is defined as a variable that is specific to every object defined by the class. It can be unique to every object.

---
### Example



```python
class Myclass :
    def __init__(self,name):
        self.name = name # self.name is an instance attribute.
```

---
## 📚 What is a `@classmethod` ?

A class method is a method that works on class itself unlike instance methods that applies on objects.

- `cls`keyword is used for class methods .
- `self` keyword is used for instance methods .

---

### Example 

```python 
class Myclass:
    @classmethod
    def __init__(cls):
        pass
```
---

## 📚 What is a `@staticmethod` ?


A static method is defined as a method that does not need any details of class or object's data .It performs an independent task and can be called by using the class name .

---

### Example
```python
class math :
    @staticmethod
    def add(a,b):
        return a+b
```

## 📚 `__str()` magic method :


It is used to return a string is useful way. Without it , the program can react unexpectidly.

- `__str__()` = __Pretty print__

### Example 
---

```python
class Person :
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name
person = Person("Ali")
print(person.name)
```
---
## 📚 Object Interaction

Object Interacction refers to using an object in another object's method.

### Example 

```python
class Book :
    def __init__(self,title):
        self.title = title

class Library :
    def __init__(self):
        self.books = []
    def add_books(self,book):
        self.books.append(book)
book_1 = Book("Atomic Habits")
library = Library()
library.add_books(book_1)
print(library.books[0].title)
```

# Key Takeaways

- Objects can work together using Composition.
- Composition creates a "Has-A" relationship.
- `__str__()` makes objects easy to print.
- `__repr__()` gives an official object representation.
- `@classmethod` works with the class.
- `@staticmethod` is an independent helper function.
- Magic methods make Python classes more powerful and readable.

---

# Programs

- Student and Laptop (Object Interaction)
- Library and Book (Composition)
- Using `__str__()`
- Using `@classmethod`
- Using `@staticmethod`

---

# What I Learned

Today I learned how Python objects can interact with one another using Composition. I also explored special methods like `__str__()` to improve object output and understood the difference between instance methods, class methods, and static methods. These concepts helped me understand how real-world programs are designed using Object-Oriented Programming.