# 🚀 Day 5 – Functions in Python

## 📖 Brief Introduction

Today, I learned about **functions** in Python. Functions are one of the most important concepts in programming because they help us divide a program into small, reusable blocks of code. They make programs easier to read, maintain, and reuse.

---

# ❓ Q1. What is a Function?

### ✅ Answer

A function is a reusable block of code that performs a specific task. Once a function is created, it can be called multiple times without rewriting the same code.

### 💻 Example

```python
def greet(name):
    print(f"Hello! {name}")

greet("Ali")
```

---

# ❓ Q2. Why are Functions Useful?

### ✅ Answer

Functions are useful because they provide several advantages:

- **Reusability:** A function can be called multiple times after being written once.
- **Readability:** Functions make code easier to read and understand.
- **Reliability:** Well-written functions produce consistent and predictable results.
- **Maintainability:** Updating one function updates every place where it is used.

---

# ❓ Q3. How Do You Define a Function?

### ✅ Answer

A function is defined using the **`def`** keyword, followed by the function name, parameters (if any), and a colon (`:`).

### 💻 Example

```python
def sum(a, b):
    return a + b
```

---

# ❓ Q4. How Do You Call a Function?

### ✅ Answer

A function is called by writing its name followed by parentheses. If the function requires input values, they are passed as arguments inside the parentheses.

Calling a function transfers program control to the function body.

### 💻 Example

```python
def greet(name):
    print(f"Hello! {name}")

greet("Ali")
```

---

# ❓ Q5. What are Parameters?

### ✅ Answer

Parameters are variables defined inside a function declaration. They receive values when the function is called and are used within the function body.

### 💻 Example

```python
def sum(a, b):
    return a + b
```

Here, **`a`** and **`b`** are parameters.

---

# ❓ Q6. What are Arguments?

### ✅ Answer

Arguments are the actual values passed to a function when it is called.

### 💻 Example

```python
def greet(name):
    print(f"Hello! {name}")

greet("Ali")
```

Here, **"Ali"** is the argument.

---

# ❓ Q7. What is the `return` Statement?

### ✅ Answer

The `return` statement sends a value back from a function to the place where it was called. After the `return` statement executes, the function ends immediately.

### 💻 Example

```python
def divide(a, b):
    result = a / b
    return result

print(divide(10, 5))
```

---

# ❓ Q8. Difference Between `print()` and `return`

| `print()` | `return` |
|-----------|-----------|
| Displays output on the screen. | Sends a value back to the caller. |
| Used only for displaying information. | Used when another part of the program needs the result. |
| The function continues after `print()` unless it reaches the end. | The function ends immediately after `return` executes. |

### 💻 Example

```python
def greet(name):
    print(f"Hello! {name}")
```

```python
def sum(a, b):
    return a + b
```

---

# ❓ Q9. Difference Between Local and Global Variables

## Local Variables

### ✅ Answer

Local variables are created inside a function and can only be used within that function.

### 💻 Example

```python
def divide(a, b):
    result = a / b
    return result
```

Here, **`result`** is a local variable.

---

## Global Variables

### ✅ Answer

Global variables are created outside functions and can be accessed throughout the program. The `global` keyword is used when a function needs to modify a global variable.

### 💻 Example

```python
age = 17

def greet(name):
    return f"I'm {name}. I'm {age} years old."

print(greet("Ali"))
```

Here, **`age`** is a global variable.

---

# 💡 What I Learned Today

Today, I learned the following concepts about functions:

- What a function is
- Why functions are useful
- Function definition
- Function calling
- Parameters and arguments
- The `return` statement
- Local and global variables

Functions help make programs more organized, reusable, and easier to understand.

---

# 🌟 Quote of the Day

> **"Great programs are built one function at a time."**

---

# 📌 Summary

Today was an important milestone in my Python journey. I learned how functions allow programmers to write reusable and organized code. I also understood the concepts of parameters, arguments, return values, and variable scope. These concepts will help me write cleaner and more efficient Python programs in the future.
