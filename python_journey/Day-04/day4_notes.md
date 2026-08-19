# 🚀 Day 4

Today was my fourth day of learning Python. I learned one of the most important concepts in programming: **loops**. Loops allow a program to repeat a block of code multiple times without writing the same statements repeatedly. I also learned how to use `for` loops, `while` loops, the `range()` function, and loop control statements such as `break` and `continue`.

---

# 🎯 Objective

Today's objective was to understand how repetition works in Python using loops. I learned when to use a `for` loop, when a `while` loop is more suitable, and how loops help programmers write shorter, cleaner, and more efficient code.

---

# 📚 Concepts Learned

## 1. Loops

A loop is a programming structure that repeats a block of code until a specific condition is met or for a fixed number of iterations.

### Example

```python
for i in range(5):
    print("Hello")
```

Output

```text
Hello
Hello
Hello
Hello
Hello
```

---

## 2. The `for` Loop

A `for` loop is used when the number of repetitions is known or when iterating over a sequence.

### Example

```python
for number in range(1, 6):
    print(number)
```

Output

```text
1
2
3
4
5
```

---

## 3. The `range()` Function

The `range()` function generates a sequence of numbers.

### Syntax

```python
range(start, stop, step)
```

### Examples

```python
range(5)
```

Produces:

```text
0 1 2 3 4
```

```python
range(1, 6)
```

Produces:

```text
1 2 3 4 5
```

```python
range(2, 11, 2)
```

Produces:

```text
2 4 6 8 10
```

---

## 4. Loop Variable

A loop variable stores the current value during each iteration of the loop.

### Example

```python
for i in range(5):
    print(i)
```

Here, `i` is the loop variable.

---

## 5. The `while` Loop

A `while` loop repeats as long as its condition remains `True`.

### Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## 6. Infinite Loop

An infinite loop keeps running because its condition never becomes `False`.

### Example

```python
while True:
    print("Running...")
```

Such loops should be used carefully.

---

## 7. The `break` Statement

The `break` statement immediately terminates the loop.

### Example

```python
for i in range(10):
    if i == 5:
        break

    print(i)
```

Output

```text
0
1
2
3
4
```

---

## 8. The `continue` Statement

The `continue` statement skips the current iteration and moves to the next one.

### Example

```python
for i in range(6):
    if i == 3:
        continue

    print(i)
```

Output

```text
0
1
2
4
5
```

---

# 💻 Programs Completed

1. **print_numbers.py**
2. **multiplication_table.py**
3. **sum_numbers.py**
4. **countdown.py**
5. **even_numbers.py**
6. **guessing_game.py**

---

# 🧠 Challenges Faced

- Understanding the difference between `for` and `while` loops.
- Learning how the `range()` function works with different arguments.
- Remembering to update variables correctly inside a `while` loop.
- Avoiding infinite loops.
- Understanding the purpose of `break` and `continue`.

Although these concepts were challenging at first, practicing different programs helped me understand them better.

---

# 💡 What I Learned Today

Today I learned how loops make programming more efficient by repeating tasks automatically. I understood the difference between `for` and `while` loops and learned how the `range()` function generates sequences of numbers.

I also learned how `break` can stop a loop immediately and how `continue` skips the current iteration without ending the loop.

---

# 📚 Resources Used

- Python Official Documentation
- Automate the Boring Stuff with Python
- Personal coding practice
- GitHub repository for organizing my projects

---

# 📝 Reflection

Day 4 helped me understand one of the most powerful features of Python. Before learning loops, I had to write repetitive code manually. Now I can repeat tasks efficiently using only a few lines of code.

The guessing game and multiplication table programs improved my logical thinking and showed me how loops are used in real programs.

Every day I become more confident in Python, and I am one step closer to achieving my goal of becoming an AI Engineer and building a professional career in software development.