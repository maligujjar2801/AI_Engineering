# Day 22 — Advanced Data Structures & Comprehension Patterns 🐍

Day 22 focuses on Python comprehensions and practical collection processing.

## 🎯 Objectives

- List comprehensions
- Conditional filtering
- Conditional expressions
- Dictionary comprehensions
- Set comprehensions
- Nested comprehensions
- Nested data structures
- Flattening data
- Real-world data transformation
- Readability and professional Python style

---

## 📚 Topics Covered

### List Comprehension

```python
squares = [x ** 2 for x in numbers]
```

### Filtering

```python
even_numbers = [
    x for x in numbers
    if x % 2 == 0
]
```

### Conditional Expression

```python
labels = [
    "even" if x % 2 == 0 else "odd"
    for x in numbers
]
```

### Dictionary Comprehension

```python
squares = {
    x: x ** 2
    for x in numbers
}
```

### Set Comprehension

```python
unique_squares = {
    x ** 2
    for x in numbers
}
```

### Nested Comprehension

```python
flat = [
    number
    for row in matrix
    for number in row
]
```

---

## 🧠 Important Concept

A nested comprehension such as:

```python
[number for row in matrix for number in row]
```

is conceptually equivalent to:

```python
for row in matrix:
    for number in row:
        ...
```

Understanding the underlying loop structure is more important than memorizing the syntax.

---

## 🔥 Practical Project

### Student Data Processor

Input:

```python
students = [
    {"name": "Ali", "marks": 85},
    {"name": "Ahmed", "marks": 48},
    {"name": "Usman", "marks": 92},
    {"name": "Hamza", "marks": 55},
    {"name": "Bilal", "marks": 76}
]
```

The project processes the data using:

- List comprehensions
- Dictionary comprehensions
- Set comprehensions
- Filtering
- Conditional transformations

Required outputs include:

1. Student names
2. Passed students
3. Name → marks dictionary
4. Students scoring ≥ 80
5. Unique marks
6. Grade mapping as a bonus challenge

---

## 💡 Professional Rule

> Pythonic does not mean the shortest possible code.

Use comprehensions when they make a transformation or filtering operation clearer.

Use a normal loop when the logic becomes complex or difficult to read.

Priorities:

**Readability → Correctness → Maintainability → Conciseness**

---

## 🔗 Connection to Previous Days

| Day | Topic | Connection |
|---|---|---|
| 19 | Log Stream Processor | Data filtering and transformation |
| 20 | Decorators | Higher-order Python patterns |
| 21 | Context Managers | Resource-management patterns |
| **22** | **Comprehensions** | **Collection transformation patterns** |

---

## 🚀 Connection to AI Engineering

Comprehensions provide useful foundations for processing:

- JSON
- API responses
- CSV records
- Logs
- Database results
- Cleaned datasets
- ML preprocessing data

These patterns will become increasingly useful as the Python journey moves toward data processing, automation, and AI/ML.

---

## 📂 Suggested Structure

```text
Day-22/
├── main.py
├── practice.py
├── notes.md
└── README.md
```

---

## ✅ Completion Checklist

- [x] List comprehensions
- [x] Filtering
- [x] Conditional expressions
- [x] Dictionary comprehensions
- [x] Set comprehensions
- [x] Nested comprehensions
- [x] Flattening nested data
- [x] Real-world log processing
- [x] Student Data Processor
- [x] Knowing when not to use comprehensions
- [x] Day 22 completed

---

## 🏁 Status

**Day 22 — Completed ✅**

Main skill:

> Transforming, filtering, and restructuring collections using clean Python comprehension patterns.
