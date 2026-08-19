# 🚀 Day  11 - Encapsulation in OOP

## 1. What is encapsulation ?

Encapsulation is the way to contol the access to an attribute with it's internal state by other methodss in class.

- Think of it like a capsule 💊 .
- It is used to secure sensitive or private attributes . 
### Real life example :
Consider a bank balance attribute that may contain private info.

```python
account.balance = -10000
```
- This attribute should not be accesable.

## Public attribute :

These are normal attributes in OOP that are accessable normally .
 ### Example 
 ```python 
class Person :
    def __init__(self,name):
        self.name = name 
```
- `self.name` is simply a public attribute .

### Examole 

##  Protected Attributes :
 These attributes are cosidered protected or safe by convention .
 - An underscore ( _ ) is used to show it .
 - It tells other programmers that this attribute is protected ( only by convention ) .
### Example
 ```python 
 class Person :
    def __init__(self,name) :
        self._name = name
```
- `self._name` is considered protected attribute .

## Private attribute :
These attributes are actually protected by interpretor and cannot be accesed by user using an object. 
- It uses two underscores ( __ ).
- These attributes cannot be accesed by an object .
### Example
```python

class Account :
    def __init__(self,pin):
        self.__pin = pin
```
- Accesing `self.__pin` will raise an error.
## Name Mangling :
This convention is used to access the private attribute because python doesn't hide private attributes completely. 
``` python 
class Account:
    def __init__(self):
        self.__pin = 1234

account = Account()
print(account.pin) # Error
print(account._Account__pin) # 1234
```
- It an convention for accessing the private methods.
## Getter Methods :
A method that is used to return the value of a priavte attribute.
### Example 
```python 
class Account :
    def __init__(self) :
        self.__pin = 1234
    def my_pin(self) :
        return self.__pin 
acc = Account()
print(acc.my_pin()) # 1234
```
- `my_pin()` is a getter method .
## Setter Methods :
These methods are used to change the value of a private attribute.
``` python
class Student:
    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
```
## Key Takeaways

- Encapsulation is one of the four pillars of Object-Oriented Programming (OOP).
- It helps protect an object's data by controlling direct access to it.
- Public attributes can be accessed from anywhere.
- Protected attributes (prefixed with `_`) are intended for internal use, but they can still be accessed.
- Private attributes (prefixed with `__`) cannot be accessed directly from outside the class.
- Python uses **Name Mangling** to rename private attributes internally.
- Getter methods are used to safely access private attributes.
- Setter methods are used to modify private attributes while validating the data.
- Encapsulation improves code security, maintainability, and organization by preventing accidental modification of important data.
---