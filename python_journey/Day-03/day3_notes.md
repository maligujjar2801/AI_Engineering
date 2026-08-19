# 🚀 Day 3

Today was my third day of learning Python. I learned one of the most important concepts in programming: **decision making**. By using `if`, `elif`, and `else` statements, I can now write programs that make decisions based on different conditions instead of simply executing every line of code.

---

# 🎯 Objective

Today's objective was to understand how Python makes decisions using conditional statements. I also learned how Boolean values and comparison operators work together to control the flow of a program.

---

# 📚 Concepts Learned

## 1. Boolean Values

A Boolean data type can only have one of two values:

- `True`
- `False`

Boolean values are produced when comparison operators evaluate a condition.

### Example

```python
age = 17

print(age >= 18)
```

**Output**

```text
False
```

---

## 2. Comparison Operators

Comparison operators compare two values and return either `True` or `False`.

| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

### Example

```python
marks = 75

print(marks >= 40)
```

Output:

```text
True
```

---

## 3. The `if` Statement

The `if` statement is used to execute a block of code only when a condition is `True`.

### Example

```python
age = 20

if age >= 18:
    print("You are eligible to vote.")
```

---

## 4. The `if...else` Statement

The `else` statement executes when the condition inside the `if` statement is `False`.

### Example

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## 5. The `if...elif...else` Statement

The `elif` statement allows Python to check multiple conditions one after another.

### Example

```python
marks = 82

if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
else:
    print("Needs Improvement")
```

---

## 6. Indentation

Python uses indentation (spaces at the beginning of a line) to define a block of code.

Unlike some programming languages, Python does not use curly braces `{}` to group statements.

### Correct Example

```python
age = 18

if age >= 18:
    print("Eligible")
```

---

## 7. Nested `if`

A nested `if` is an `if` statement placed inside another `if` statement. It is used when another condition needs to be checked after the first one is true.

### Example

```python
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
```

---

# 💻 Programs Completed

1. **positive_negative.py**
2. **voting.py**
3. **largest_number.py**
4. **even_or_odd.py**
5. **pass_fail.py**
6. **grade_calculator.py**

---

# 🧠 Challenges Faced

- Understanding the difference between `if`, `elif`, and `else`.
- Deciding which condition should be checked first.
- Making sure the indentation was correct.
- Writing the grade calculator without logical errors.

Although these challenges took time, solving them helped me improve my logical thinking and confidence in writing Python programs.

---

# 💡 What I Learned Today

Today I learned that programs can make decisions using conditional statements. I also understood how comparison operators return Boolean values and how indentation controls the execution of code blocks in Python.

I practiced writing different decision-making programs, which helped me improve my problem-solving skills.

---

# 📚 Resources Used

- Python Official Tutorial
- Automate the Boring Stuff with Python
- Personal coding practice
- GitHub repository for organizing my work

---

# 📝 Reflection

Day 3 was one of the most interesting days of my Python journey because I finally learned how programs make decisions. Writing programs using `if`, `elif`, and `else` helped me understand programming logic more deeply.

I also realized that writing code is not only about syntax but also about thinking logically before solving a problem. Every program I completed today increased my confidence and brought me one step closer to my goal of becoming an AI Engineer.

I will continue learning consistently, improving my coding skills every day, and building projects that will strengthen my portfolio in the future.