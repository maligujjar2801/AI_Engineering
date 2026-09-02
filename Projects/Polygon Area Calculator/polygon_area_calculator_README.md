# 📐 Polygon Area Calculator

A Python Object-Oriented Programming project based on the freeCodeCamp **Build a Polygon Area Calculator** lab.

The project implements a `Rectangle` class and a `Square` class. `Square` is a subclass of `Rectangle` and demonstrates inheritance, method overriding, constructors, and object attributes.

## 🚀 Features

### Rectangle

The `Rectangle` class supports:

- Setting width
- Setting height
- Calculating area
- Calculating perimeter
- Calculating diagonal
- Generating an ASCII-art picture
- Checking how many other shapes fit inside it
- Custom string representation

### Square

The `Square` class:

- Inherits from `Rectangle`
- Uses one side length for both width and height
- Overrides `set_width()`
- Overrides `set_height()`
- Provides `set_side()`
- Provides a square-specific string representation

## 🧠 Concepts Practiced

- Classes and objects
- Constructors with `__init__`
- Instance attributes
- Inheritance
- Method overriding
- `super()`
- String formatting with f-strings
- Loops
- Conditional statements
- Floor division (`//`)
- Mathematical operations
- Working with parent and child classes

## 📁 Project Structure

```text
Polygon-Area-Calculator/
│
├── polygon_area_calculator.py
├── README.md
└── notes.md
```

## 💻 Example

```python
rect = Rectangle(10, 5)

print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)

print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)

print(rect.get_amount_inside(sq))
```

### Expected Output

```text
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```

## 🔍 Class Design

### Rectangle

```python
class Rectangle:
```

Main methods:

```text
set_width()
set_height()
get_area()
get_perimeter()
get_diagonal()
get_picture()
get_amount_inside()
__str__()
```

### Square

```python
class Square(Rectangle):
```

Main methods:

```text
__init__()
set_width()
set_height()
set_side()
__str__()
```

## 📐 Formulas

### Area

```text
width × height
```

### Perimeter

```text
2 × (width + height)
```

### Diagonal

```text
√(width² + height²)
```

### Shapes Inside Another Shape

Because rotation is not allowed:

```python
(self.width // shape.width) * (self.height // shape.height)
```

## ⚠️ Important Python Lessons

### `**` vs `^`

Python uses:

```python
width ** 2
```

for powers.

`^` is bitwise XOR and should not be used for exponentiation.

### `return` vs `print`

Methods such as `get_picture()` should return their result so that the caller or tests can use it.

```python
return picture
```

rather than:

```python
print(picture)
```

### `super()`

The Square constructor uses:

```python
super().__init__(side, side)
```

to initialize the inherited `width` and `height` attributes.

## 🧪 FCC Lab Status

The implementation is designed to satisfy the freeCodeCamp Polygon Area Calculator user stories and tests, including:

- Rectangle creation
- Square inheritance
- Correct string representations
- Area
- Perimeter
- Diagonal
- Picture generation
- Picture size limit
- Shape-fitting calculation
- Square setter behavior

## 📚 What I Learned

This project helped reinforce how inheritance works in Python.

The most important relationship is:

```text
Rectangle
    ↑
    │ inherits
    │
  Square
```

A `Square` is a specialized `Rectangle`, but it needs additional logic to ensure that its width and height always remain equal.

## 🔗 Course

This project is part of the **freeCodeCamp Python curriculum** and focuses on Object-Oriented Programming.

## 👨‍💻 Project Goal

Build stronger Python OOP fundamentals through practical projects and progressively more complex programming challenges.
