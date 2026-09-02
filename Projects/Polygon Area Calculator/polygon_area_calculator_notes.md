# Polygon Area Calculator — Notes

## Overview

This project practices Object-Oriented Programming (OOP) in Python by creating a `Rectangle` class and a `Square` class.

`Square` inherits from `Rectangle`, so it can use the rectangle's methods while overriding methods that need square-specific behavior.

---

## 1. Rectangle Class

A rectangle needs two attributes:

```python
self.width = width
self.height = height
```

### Constructor

```python
def __init__(self, width, height):
    self.width = width
    self.height = height
```

### Setters

```python
def set_width(self, new_width):
    self.width = new_width

def set_height(self, new_height):
    self.height = new_height
```

These methods change the dimensions after the object has been created.

---

## 2. Calculating Area

The area of a rectangle is:

```text
width × height
```

Python:

```python
def get_area(self):
    return self.width * self.height
```

Example:

```python
Rectangle(3, 6).get_area()
```

returns:

```text
18
```

---

## 3. Calculating Perimeter

The perimeter formula is:

```text
2 × (width + height)
```

Correct Python:

```python
def get_perimeter(self):
    return 2 * (self.width + self.height)
```

### Common mistake

This is wrong:

```python
2 * self.width * self.height
```

because that calculates twice the area, not the perimeter.

---

## 4. Calculating the Diagonal

The diagonal uses the Pythagorean theorem:

```text
√(width² + height²)
```

Because the project imports the `math` module:

```python
import math
```

the correct code is:

```python
def get_diagonal(self):
    return math.sqrt(self.width ** 2 + self.height ** 2)
```

### Important Python operators

`**` means exponentiation:

```python
5 ** 2
```

gives:

```text
25
```

`^` does NOT mean exponentiation in Python. It is the bitwise XOR operator.

---

## 5. get_picture()

The method must return a string containing stars.

For:

```python
Rectangle(4, 3)
```

the result is:

```text
****
****
****
```

with a newline after each row.

Implementation:

```python
def get_picture(self):
    if self.width > 50 or self.height > 50:
        return "Too big for picture."

    picture = ""

    for _ in range(self.height):
        picture += "*" * self.width + "\n"

    return picture
```

### Important

Do not use `print()` inside `get_picture()`.

The FCC tests expect the method to **return** the string.

---

## 6. Checking Whether a Picture Is Too Large

The FCC requirement says that if either dimension is larger than 50, return:

```text
Too big for picture.
```

Correct condition:

```python
if self.width > 50 or self.height > 50:
```

A condition such as:

```python
if self.height or self.width > 50:
```

does not perform the intended comparison.

---

## 7. get_amount_inside()

This method determines how many complete copies of another rectangle or square fit inside the current rectangle without rotation.

Correct implementation:

```python
def get_amount_inside(self, shape):
    return (self.width // shape.width) * (self.height // shape.height)
```

Example:

```python
Rectangle(15, 10).get_amount_inside(Square(5))
```

Width:

```text
15 // 5 = 3
```

Height:

```text
10 // 5 = 2
```

Total:

```text
3 × 2 = 6
```

### Why use `//`?

`//` performs floor division.

For example:

```python
10 // 3
```

returns:

```text
3
```

because only three complete shapes fit.

---

# 8. Square Inheritance

The square is a specialized rectangle:

```python
class Square(Rectangle):
```

This means `Square` inherits methods from `Rectangle`.

For example:

```python
sq = Square(5)
sq.get_area()
```

can use the inherited `get_area()` method.

---

## 9. Square Constructor

A square has one side length, but the parent `Rectangle` class needs width and height.

Therefore:

```python
def __init__(self, side):
    super().__init__(side, side)
    self.side = side
```

This gives the square:

```text
width = side
height = side
side = side
```

### Common mistake

This is incorrect:

```python
super().__init__(self)
```

The parent constructor expects:

```python
width, height
```

so it needs:

```python
super().__init__(side, side)
```

---

## 10. Square Setters

A square must always have equal width and height.

Therefore `set_width()` must update both:

```python
def set_width(self, new_width):
    self.width = new_width
    self.height = new_width
    self.side = new_width
```

Likewise:

```python
def set_height(self, new_height):
    self.width = new_height
    self.height = new_height
    self.side = new_height
```

And:

```python
def set_side(self, new_side):
    self.width = new_side
    self.height = new_side
    self.side = new_side
```

---

## 11. String Representation

Rectangle:

```python
def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
```

Example:

```python
print(Rectangle(3, 6))
```

Output:

```text
Rectangle(width=3, height=6)
```

Square:

```python
def __str__(self):
    return f"Square(side={self.side})"
```

Example:

```python
print(Square(5))
```

Output:

```text
Square(side=5)
```

---

# Common Mistakes From My First Attempt

### Mistake 1 — Wrong perimeter

```python
2 * width * height
```

Correct:

```python
2 * (width + height)
```

### Mistake 2 — Wrong exponent operator

```python
width ^ 2
```

Correct:

```python
width ** 2
```

### Mistake 3 — Calling sqrt incorrectly

```python
sqrt(...)
```

when only `import math` was used.

Correct:

```python
math.sqrt(...)
```

### Mistake 4 — Printing instead of returning

Wrong:

```python
print("*" * self.width)
```

Correct:

```python
picture += "*" * self.width + "\n"
return picture
```

### Mistake 5 — Incorrect large-picture condition

Wrong:

```python
if self.height or self.width > 50:
```

Correct:

```python
if self.width > 50 or self.height > 50:
```

### Mistake 6 — Incorrect `super()`

Wrong:

```python
super().__init__(self)
```

Correct:

```python
super().__init__(side, side)
```

### Mistake 7 — Not storing `side`

A square needs:

```python
self.side = side
```

so that:

```python
Square(5)
```

can be represented as:

```text
Square(side=5)
```

### Mistake 8 — Square setters changing only `side`

Changing only `self.side` does not automatically change inherited `width` and `height`.

All three should stay synchronized.

---

# Key OOP Concepts Learned

## Inheritance

```python
class Square(Rectangle):
```

Square inherits from Rectangle.

## Method Overriding

Square replaces inherited methods with its own versions:

```python
def set_width(self, new_width):
```

and

```python
def set_height(self, new_height):
```

## super()

```python
super().__init__(side, side)
```

calls the parent class constructor.

## Encapsulation Through Methods

Instead of directly changing dimensions everywhere, methods such as:

```python
set_width()
set_height()
set_side()
```

control how dimensions are updated.

## Polymorphism

`get_amount_inside()` accepts another shape object and uses its common attributes:

```python
shape.width
shape.height
```

This allows it to work with both rectangles and squares.

---

# Final Correct Implementation

```python
import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ""

        for _ in range(self.height):
            picture += "*" * self.width + "\n"

        return picture

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def set_width(self, new_width):
        self.width = new_width
        self.height = new_width
        self.side = new_width

    def set_height(self, new_height):
        self.width = new_height
        self.height = new_height
        self.side = new_height

    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side
        self.side = new_side

    def __str__(self):
        return f"Square(side={self.side})"
```
