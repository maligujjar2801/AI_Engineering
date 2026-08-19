# 🚀 Day 13 - Dunder Methods
##  What are Dunder methods ?
These methods are used to perform built-in functions with objects in python .

### Like :
```python 
__init__()
__str__()
__len__()
__repr__()
``` 
 etc .
 - These methods are also called magic methods .

 ## `__str__()` method :
 `__str__()` method deciedes what to print on screen , when the object is printed.

 ### Example 
 ```python
 class Student :
    def __init__(self,name) :
        self.name = name
    def __str__(self) :
        return self.name
 student = Student("Ali")
 print(student) # Ali
 ```
 ## `__repr__()`Student method : 
 It returns the string that represents the official 
 initialization of the objects .
 - It is called by calling the repr() funtion outside the class.
 ```python

class Student :
    def __init__(self,name) :
        self.name = name
    def __repr__(self) :
        return f"Student('{self.name}')"
student = Student("Ali")
print(repr(student)) # Student("Ali")
```
## `__len__()` method :
It defines what happen when the `len()` function is called on object .

## Example
```python
class Book :
    def __init__(self,page) :
        self.page = page
    def __len__(self) :
        return self.page
book = Book(167)
print(len(book)) # 167
```
## `__eq__()` method :
This method controls the functionality of (`==`) operator .
### Example
```python
class Student:
    def __init__(self, marks):
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks 
```
## `__add__()` method :
This method adds two objects of a class.
### Example 
```python
class Wallet:
    def __init__(self, money):
        self.money = money

    def __add__(self, other):
        return self.money + other.money
w1 = Wallet(500)
w2 = Wallet(700)

print(w1 + w2) # 1200
```

## Comparison dunder Operators:
These operators are used to perform comparison operations with objects .

### Example
```python
__lt__()   # <
__gt__()   # >
__le__()   # <=
__ge__()   # >=
```
## `NotImplimented` :
It is used in magic(dunder) methods if the python doesn't know how to perform that dunder in the specific class .
- It returns `False` if the operation fails in both classes .
### Example 
```python
class Rectangle :
    def __init__(self,length,width):
        self.length = length 
        self.width = width 
    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.length * self.width + other.length * other.width
```
- It will return `False` if the `other` doesn't belong from the same class.
- It executes the code in two ways .
## Operator Overloading

Magic methods allow operators to work with custom objects.

Without magic methods:
```python
student1 + student2
```
 ### Error :

- With __add__():
```python
student1 + student2
```
 ### Python knows exactly what to do.
 ---
 