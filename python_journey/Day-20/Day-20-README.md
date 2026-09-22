# Day 20 — Python Decorators

Part of my **Python Engineering Track**.

## Overview

Day 20 focuses on **Python Decorators** — a powerful way to add reusable behavior around existing functions without changing their core implementation.

The goal of this day was to understand both the syntax and the underlying mechanism behind decorators.

---

## Topics Covered

- First-class functions
- Higher-order functions
- Nested functions
- Basic decorators
- `@decorator` syntax
- Wrapper functions
- `*args` and `**kwargs`
- Preserving return values
- `functools.wraps`
- Logging decorators
- Timing decorators
- Error-handling decorators
- Retry decorators
- Decorators with arguments
- Decorator factories
- Multiple decorators
- Practical decorator design

---

## How Decorators Work

A decorator receives a function and returns an enhanced function.

```text
Original Function
       ↓
    Decorator
       ↓
    Wrapper
       ↓
Enhanced Behavior
```

Example:

```python
from functools import wraps


def logger(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Starting {function.__name__}")

        result = function(*args, **kwargs)

        print(f"[LOG] Finished {function.__name__}")

        return result

    return wrapper
```

Usage:

```python
@logger
def greet(name):
    print(f"Hello {name}")
```

---

## The `@` Syntax

This:

```python
@logger
def greet():
    print("Hello")
```

is equivalent to:

```python
def greet():
    print("Hello")

greet = logger(greet)
```

---

## Why `*args` and `**kwargs`?

A decorator should ideally be reusable for functions with different parameters.

```python
def wrapper(*args, **kwargs):
    return function(*args, **kwargs)
```

This allows the wrapper to accept positional and keyword arguments and pass them to the original function.

---

## Preserving Function Metadata

Professional decorators use:

```python
from functools import wraps
```

and:

```python
@wraps(function)
```

This preserves metadata such as the original function's name and docstring.

---

## Retry Decorator

One of the main Day 20 challenges was understanding how a decorator can retry a function when it fails.

Example usage:

```python
@retry(3)
def unstable_function():
    ...
```

The important idea is that retry logic normally reacts to **raised exceptions**.

```python
for attempt in range(times):

    try:
        return function(*args, **kwargs)

    except Exception as error:
        print(f"Attempt {attempt + 1} failed: {error}")
```

If the function succeeds, its result is returned immediately.

If it raises an exception, the exception is caught and another attempt can be made.

---

## Day 20 Challenge

Completed ✅

The challenge involved building and understanding retry behavior with decorators, exceptions, and multiple attempts.

Core concept:

```text
Call function
      ↓
Does it raise an exception?
   ↙             ↘
 No               Yes
 ↓                 ↓
Return result    Catch exception
 ↓                 ↓
Success          Try again
```

---

## Mini Project

### Function Monitoring System

The Day 20 project combines decorators for:

- Logging
- Timing
- Error handling
- Retry logic

Example:

```python
@handle_errors
@timer
@logger
def divide(a, b):
    return a / b
```

Recommended structure:

```text
Day-20/
├── decorators.py
├── main.py
└── README.md
```

---

## Example Output

A monitoring system may produce output such as:

```text
[LOG] Function started: divide
[TIMER] divide took 0.000012 seconds
[LOG] Function finished: divide
10.0
```

For a failed operation:

```text
Attempt 1 failed: division by zero
Attempt 2 failed: division by zero
Attempt 3 failed: division by zero
All attempts failed.
```

---

## What I Learned

By completing Day 20, I learned how to:

1. Pass functions as arguments.
2. Return functions from other functions.
3. Build decorators using wrapper functions.
4. Use `@decorator` syntax.
5. Handle arbitrary function arguments with `*args` and `**kwargs`.
6. Preserve original function metadata with `functools.wraps`.
7. Build decorators for logging, timing, and error handling.
8. Create decorator factories such as `@retry(3)`.
9. Use `try/except` inside a decorator to detect raised exceptions.
10. Understand how multiple decorators are stacked.

---

## Key Pattern

Standard decorator:

```python
from functools import wraps


def decorator(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        # Extra behavior

        result = function(*args, **kwargs)

        # Extra behavior

        return result

    return wrapper
```

Decorator factory:

```python
def decorator_factory(value):

    def decorator(function):

        @wraps(function)
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)

        return wrapper

    return decorator
```

---

## Why This Matters for Software Engineering

Decorators introduce an important software-engineering idea:

> **Add reusable behavior around existing logic without rewriting the original logic.**

This pattern is useful in areas such as:

```text
Logging
Performance monitoring
Authentication
Authorization
Validation
Caching
Retries
Error handling
```

It is an important concept for backend development, APIs, testing, and Python frameworks.

---

## Status

**Day 20 — Completed ✅**

Next topic:

**Day 21 — Context Managers**
