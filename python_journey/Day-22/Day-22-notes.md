# Day 22 — Advanced Data Structures & Comprehension Patterns 🐍

## Overview

Day 22 focuses on Python comprehensions and practical data transformation.

The goal is not just to write shorter code, but to recognize when a comprehension makes the intent of the program clearer and when a normal loop is more readable.

### Learning Path

**Concept → Under the Hood → Syntax → Examples → Prediction → Practical Challenge → Review**

---

## 1. What Are Comprehensions?

A comprehension is a compact Python syntax for creating a new collection from an iterable.

Instead of:

```python
numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number ** 2)
```

We can write:

```python
squares = [number ** 2 for number in numbers]
```

Output:

```text
[1, 4, 9, 16, 25]
```

The important skill is recognizing the operation:

> Take items from an iterable, transform or filter them, and build a new collection.

---

# 2. List Comprehensions

## Basic Syntax

```python
[expression for item in iterable]
```

Example:

```python
numbers = [1, 2, 3, 4]

squares = [x ** 2 for x in numbers]

print(squares)
```

Output:

```text
[1, 4, 9, 16]
```

### Mental Model

```text
iterable
   ↓
take each item
   ↓
apply expression
   ↓
store result in a new list
```

---

# 3. List Comprehensions with Filtering

A condition can be added after the `for` clause.

## Syntax

```python
[expression for item in iterable if condition]
```

Example:

```python
numbers = range(1, 11)

even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)
```

Output:

```text
[2, 4, 6, 8, 10]
```

The condition determines whether an item is included.

```text
1 → odd  → reject
2 → even → keep
3 → odd  → reject
4 → even → keep
...
```

### Another Example

```python
even_squares = [
    x ** 2
    for x in range(1, 11)
    if x % 2 == 0
]
```

Result:

```text
[4, 16, 36, 64, 100]
```

---

# 4. Filtering vs Conditional Expression

This distinction is extremely important.

## Filtering

```python
[x for x in numbers if x > 5]
```

Filtering means:

> Keep some items and remove others.

Example:

```python
numbers = [2, 5, 7, 9]

result = [x for x in numbers if x > 5]
```

Output:

```text
[7, 9]
```

The output contains fewer items.

---

## Conditional Expression

A conditional expression changes the value depending on a condition.

```python
["even" if x % 2 == 0 else "odd" for x in numbers]
```

Example:

```python
numbers = [1, 2, 3, 4]

result = [
    "even" if x % 2 == 0 else "odd"
    for x in numbers
]
```

Output:

```text
['odd', 'even', 'odd', 'even']
```

Every item is processed.

### Compare the Patterns

Filtering:

```python
[expression for x in data if condition]
```

Conditional expression:

```python
[value_if_true if condition else value_if_false for x in data]
```

Remember:

> `if` at the end usually filters; `if/else` before `for` usually transforms.

---

# 5. Dictionary Comprehensions

Dictionaries can also be generated with comprehensions.

## Traditional Approach

```python
numbers = [1, 2, 3, 4]

squares = {}

for x in numbers:
    squares[x] = x ** 2
```

## Dictionary Comprehension

```python
squares = {x: x ** 2 for x in numbers}
```

Output:

```python
{
    1: 1,
    2: 4,
    3: 9,
    4: 16
}
```

## Syntax

```python
{key_expression: value_expression for item in iterable}
```

---

# 6. Filtering a Dictionary

Consider:

```python
scores = {
    "Ali": 85,
    "Ahmed": 42,
    "Usman": 91,
    "Hamza": 67
}
```

We can select students who passed:

```python
passed = {
    name: score
    for name, score in scores.items()
    if score >= 60
}
```

Result:

```python
{
    "Ali": 85,
    "Usman": 91,
    "Hamza": 67
}
```

### Important

For a dictionary, `.items()` gives access to both keys and values:

```python
for name, score in scores.items():
    ...
```

---

# 7. Set Comprehensions

Sets use a similar comprehension syntax.

## Syntax

```python
{expression for item in iterable}
```

Example:

```python
numbers = [1, 2, 2, 3, 3, 4]

unique_squares = {x ** 2 for x in numbers}

print(unique_squares)
```

Result:

```text
{1, 4, 9, 16}
```

Duplicate values are automatically removed because sets only store unique elements.

### List vs Set

```python
[x ** 2 for x in numbers]
```

creates a list.

```python
{x ** 2 for x in numbers}
```

creates a set.

The braces alone do not make something a dictionary; a dictionary comprehension has `key: value`.

---

# 8. Nested Data Structures

Real-world data is often nested.

Example:

```python
students = [
    ["Ali", 85, 90],
    ["Ahmed", 70, 80],
    ["Usman", 92, 88]
]
```

Each inner list represents:

```text
[name, math, physics]
```

## Extract Names

```python
names = [student[0] for student in students]
```

Output:

```text
['Ali', 'Ahmed', 'Usman']
```

## Extract Physics Marks

```python
physics = [student[2] for student in students]
```

Output:

```text
[90, 80, 88]
```

---

# 9. Nested Comprehensions

Consider a matrix:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

We want to flatten it:

```text
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

A nested comprehension can do this:

```python
flat = [number for row in matrix for number in row]
```

Output:

```text
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## Equivalent Normal Loop

The comprehension:

```python
flat = [number for row in matrix for number in row]
```

is equivalent to:

```python
flat = []

for row in matrix:
    for number in row:
        flat.append(number)
```

### Mental Model

Read:

```python
[number for row in matrix for number in row]
```

as:

```text
for each row in matrix:
    for each number in row:
        produce number
```

This is one of the most important patterns to understand.

---

# 10. General Nested Comprehension Pattern

When you see:

```python
[expression for x in A for y in B]
```

mentally expand it into:

```python
for x in A:
    for y in B:
        expression
```

For example:

```python
pairs = [
    (x, y)
    for x in [1, 2]
    for y in ["A", "B"]
]
```

Result:

```python
[
    (1, "A"),
    (1, "B"),
    (2, "A"),
    (2, "B")
]
```

The inner loop runs completely for each iteration of the outer loop.

---

# 11. Practical Example — Log Processing

This connects directly to the Day 19 Log Stream Processor.

Suppose:

```python
logs = [
    "INFO: Server started",
    "ERROR: Database failed",
    "INFO: User logged in",
    "ERROR: Connection timeout"
]
```

## Extract Errors

```python
errors = [
    log
    for log in logs
    if log.startswith("ERROR")
]
```

Result:

```python
[
    "ERROR: Database failed",
    "ERROR: Connection timeout"
]
```

## Extract Actual Messages

```python
messages = [
    log.split(": ", 1)[1]
    for log in logs
]
```

Result:

```python
[
    "Server started",
    "Database failed",
    "User logged in",
    "Connection timeout"
]
```

This is a realistic example of transformation and filtering.

---

# 12. Student Data Processing

Consider:

```python
students = [
    {"name": "Ali", "marks": 85},
    {"name": "Ahmed", "marks": 48},
    {"name": "Usman", "marks": 92},
    {"name": "Hamza", "marks": 55},
    {"name": "Bilal", "marks": 76}
]
```

## Extract Names

```python
names = [student["name"] for student in students]
```

## Filter Passed Students

```python
passed = [
    student
    for student in students
    if student["marks"] >= 50
]
```

## Create Name → Marks Dictionary

```python
marks = {
    student["name"]: student["marks"]
    for student in students
}
```

## Students With Marks ≥ 80

```python
high_scorers = {
    student["name"]: student["marks"]
    for student in students
    if student["marks"] >= 80
}
```

## Unique Marks

```python
unique_marks = {
    student["marks"]
    for student in students
}
```

These examples demonstrate list, dictionary, and set comprehensions on the same data.

---

# 13. When NOT to Use a Comprehension

A comprehension is not automatically better because it uses fewer lines.

Avoid overly complicated comprehensions such as:

```python
result = [
    do_something(x)
    for x in data
    if complicated_condition(x)
    and other_condition(x)
    and another_condition(x)
]
```

If the logic becomes difficult to understand, use a normal loop.

For example:

```python
results = []

for item in data:
    if complicated_condition(item):
        processed = process(item)

        if processed:
            results.append(processed)
```

This may be longer, but it can be much easier to maintain.

### Professional Rule

> Pythonic does not mean "shortest possible code."

Good Python aims for:

- Readability
- Correctness
- Maintainability
- Clear intent

---

# 14. Under the Hood

A list comprehension:

```python
squares = [x ** 2 for x in numbers]
```

conceptually performs the same task as:

```python
squares = []

for x in numbers:
    squares.append(x ** 2)
```

The comprehension creates a new list and evaluates the expression once for each accepted item.

It is not simply a magical replacement for every loop.

Use it when the operation naturally represents:

```text
input collection
       ↓
transform/filter
       ↓
new collection
```

---

# 15. Prediction Challenge 1

Predict before running:

```python
numbers = [1, 2, 3, 4, 5]

result = [x * 2 for x in numbers if x % 2 != 0]

print(result)
```

Expected reasoning:

- `1` is odd → `1 * 2 = 2`
- `2` is even → reject
- `3` is odd → `3 * 2 = 6`
- `4` is even → reject
- `5` is odd → `5 * 2 = 10`

Result:

```text
[2, 6, 10]
```

---

# 16. Prediction Challenge 2

```python
numbers = [1, 2, 3, 4]

result = {
    x: x ** 2
    for x in numbers
    if x % 2 == 0
}

print(result)
```

Result:

```python
{
    2: 4,
    4: 16
}
```

---

# 17. Prediction Challenge 3 — Nested

```python
matrix = [
    [1, 2],
    [3, 4]
]

result = [x for row in matrix for x in row]

print(result)
```

Result:

```text
[1, 2, 3, 4]
```

The equivalent loops are:

```python
for row in matrix:
    for x in row:
        ...
```

---

# 18. Practical Challenge

Build a **Student Data Processor** using:

```python
students = [
    {"name": "Ali", "marks": 85},
    {"name": "Ahmed", "marks": 48},
    {"name": "Usman", "marks": 92},
    {"name": "Hamza", "marks": 55},
    {"name": "Bilal", "marks": 76}
]
```

Implement:

### 1. Student names

Expected:

```python
["Ali", "Ahmed", "Usman", "Hamza", "Bilal"]
```

### 2. Passed students

Passing marks = `50`.

Return the original student dictionaries.

### 3. Name → marks dictionary

Expected structure:

```python
{
    "Ali": 85,
    "Ahmed": 48,
    ...
}
```

### 4. Students with ≥ 80

Expected:

```python
{
    "Ali": 85,
    "Usman": 92
}
```

### 5. Unique marks

Use a set comprehension.

### Bonus

Generate grades:

```text
85 → A
92 → A
76 → B
55 → C
48 → F
```

Design the grade logic yourself.

---

# 19. Day 22 Completion Checklist

- [x] Understand list comprehensions
- [x] Understand filtering
- [x] Understand conditional expressions
- [x] Understand dictionary comprehensions
- [x] Understand set comprehensions
- [x] Understand nested comprehensions
- [x] Understand flattening nested data
- [x] Apply comprehensions to log data
- [x] Apply comprehensions to student data
- [x] Understand when not to use comprehensions
- [x] Complete the Student Data Processor

---

# 20. Connection to Future Python / AI Engineering

Comprehensions are especially useful when working with:

- JSON data
- API responses
- CSV records
- Log files
- Data cleaning
- Feature preparation
- Database results
- Data analysis
- Machine-learning preprocessing

For example, later you may encounter API data like:

```python
users = response["users"]
```

and need:

```python
active_users = [
    user
    for user in users
    if user["active"]
]
```

The same transformation mindset will transfer directly to data-processing and AI/ML workflows.

---

# Key Takeaways

1. List comprehension:

```python
[expression for item in iterable]
```

2. Filter:

```python
[expression for item in iterable if condition]
```

3. Conditional transformation:

```python
[value_if_true if condition else value_if_false for item in iterable]
```

4. Dictionary comprehension:

```python
{key: value for item in iterable}
```

5. Set comprehension:

```python
{expression for item in iterable}
```

6. Nested comprehension:

```python
[expression for x in outer for y in x]
```

7. Always prioritize readable code over unnecessarily compact code.

---

## Day 22 Status

**Completed ✅**

Main skill gained:

> Transforming, filtering, and restructuring collections using clean Python comprehension patterns.
