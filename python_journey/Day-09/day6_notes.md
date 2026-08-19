# Day 6 Notes

## Object-Oriented Programming Revision

### Class

A blueprint used to create objects.

### Object

An instance of a class.

### Instance Attributes

Variables that belong to each object.

Example:

```python
self.name
self.ledger
```

---

## Methods Used

- __init__()
- deposit()
- withdraw()
- transfer()
- get_balance()
- check_funds()
- __str__()

---

## New Concepts Learned

### Nested Loops

Useful when processing data inside lists of dictionaries.

Example:

```python
for category in categories:
    for transaction in category.ledger:
```

---

### String Formatting

Left align

```python
f"{text:<23}"
```

Right align

```python
f"{amount:>7.2f}"
```

Center text

```python
text.center(30, "*")
```

---

### List of Dictionaries

Example:

```python
ledger = [
    {
        "amount": 100,
        "description": "Deposit"
    }
]
```

---

### Percentage Calculation

```python
percent = (spent / total) * 100
percent = (percent // 10) * 10
```

Rounds the percentage down to the nearest 10.

---

## Biggest Challenge

The create_spend_chart() function.

The logic was manageable, but matching the exact spacing required by freeCodeCamp took the most time.

---

## What I Improved

- Better understanding of classes
- Better use of nested loops
- More confidence with string formatting
- Improved debugging skills