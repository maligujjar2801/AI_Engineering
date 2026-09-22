# Day 20 — Python Decorators

## 1. What is a Decorator?

A decorator is a function that takes another function, adds or changes its behavior, and returns a function.

Basic idea:

```text
Original Function
       ↓
   Decorator
       ↓
Enhanced Function
```

Decorators are commonly used for logging, timing, authentication, validation, caching, error handling, and retry logic.

---

## 2. Functions Are First-Class Objects

Python functions can be:

- stored in variables
- passed as arguments
- returned from other functions

Example:

```python
def greet():
    print("Hello")


x = greet
x()
```

A function that accepts or returns another function is called a higher-order function.

This idea is the foundation of decorators.

---

## 3. Building a Basic Decorator

```python
def decorator(function):

    def wrapper():
        print("Before function")
        function()
        print("After function")

    return wrapper
```

Usage:

```python
def greet():
    print("Hello!")


greet = decorator(greet)

greet()
```

Output:

```text
Before function
Hello!
After function
```

---

## 4. Understanding `@decorator`

This:

```python
@decorator
def greet():
    print("Hello!")
```

is equivalent to:

```python
def greet():
    print("Hello!")

greet = decorator(greet)
```

The `@decorator` syntax is therefore mainly a cleaner way to apply a decorator.

---

## 5. The Wrapper Function

A decorator normally creates an inner function called a wrapper.

```python
def decorator(function):

    def wrapper():
        print("Before")
        function()
        print("After")

    return wrapper
```

Flow:

```text
greet()
  ↓
wrapper()
  ↓
extra behavior
  ↓
original greet()
  ↓
more extra behavior
```

The wrapper controls what happens before, during, and after the original function call.

---

## 6. Decorators with Function Arguments

A decorator that only uses:

```python
def wrapper():
```

cannot correctly wrap functions that receive arguments.

Use:

```python
def decorator(function):

    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper
```

This allows the decorator to work with many different function signatures.

Example:

```python
@decorator
def add(a, b):
    return a + b

print(add(10, 20))
```

---

## 7. Understanding `*args` and `**kwargs`

For a call like:

```python
function(10, 20)
```

the positional arguments are collected in:

```python
args = (10, 20)
```

Then:

```python
function(*args)
```

unpacks them back into:

```python
function(10, 20)
```

For keyword arguments:

```python
function(name="Ali", age=17)
```

they are collected in `kwargs`.

Then:

```python
function(**kwargs)
```

unpacks them back into keyword arguments.

---

## 8. Always Preserve the Return Value

Bad decorator:

```python
def decorator(function):

    def wrapper(*args, **kwargs):
        function(*args, **kwargs)

    return wrapper
```

If the original function returns something, this wrapper loses it.

Correct:

```python
def decorator(function):

    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result

    return wrapper
```

Or:

```python
def decorator(function):

    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper
```

---

## 9. `functools.wraps`

A wrapper can hide useful metadata from the original function.

Without `wraps`, properties such as the function name and docstring may refer to the wrapper instead.

Use:

```python
from functools import wraps
```

Professional decorator pattern:

```python
from functools import wraps


def decorator(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result

    return wrapper
```

`@wraps(function)` preserves metadata such as:

- function name
- docstring
- useful introspection information

---

## 10. Logging Decorator

```python
from functools import wraps


def log_function(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Running: {function.__name__}")

        result = function(*args, **kwargs)

        print(f"Finished: {function.__name__}")

        return result

    return wrapper
```

Usage:

```python
@log_function
def add(a, b):
    return a + b

print(add(10, 20))
```

This adds logging without changing the main logic of `add()`.

---

## 11. Timing Decorator

```python
import time
from functools import wraps


def timer(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        result = function(*args, **kwargs)

        end = time.perf_counter()

        print(
            f"{function.__name__} took "
            f"{end - start:.6f} seconds"
        )

        return result

    return wrapper
```

This is useful for performance testing and optimization.

---

## 12. Error-Handling Decorator

```python
from functools import wraps


def handle_errors(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        try:
            return function(*args, **kwargs)

        except Exception as error:
            print(f"Error: {error}")
            return None

    return wrapper
```

Important:

The decorator detects an error when the wrapped function **raises an exception**.

For example:

```python
def divide(a, b):
    return a / b
```

Calling:

```python
divide(10, 0)
```

raises `ZeroDivisionError`.

The decorator can catch that exception with:

```python
try:
    ...
except Exception as error:
    ...
```

However, a function that simply returns a value such as:

```python
return "Invalid input"
```

has not raised an exception. A normal `except` block will not detect that as an error.

---

## 13. Retry Decorator

A retry decorator can run a function again when it raises an exception.

Example target usage:

```python
@retry(3)
def unstable_function():
    ...
```

Implementation:

```python
from functools import wraps


def retry(times):

    def decorator(function):

        @wraps(function)
        def wrapper(*args, **kwargs):

            for attempt in range(times):
                try:
                    return function(*args, **kwargs)

                except Exception as error:
                    print(
                        f"Attempt {attempt + 1} failed: {error}"
                    )

            print("All attempts failed.")

        return wrapper

    return decorator
```

The core logic is:

```python
for attempt in range(times):

    try:
        return function(*args, **kwargs)

    except Exception:
        continue
```

If the function succeeds, `return` immediately stops the loop.

If it raises an exception, the `except` block runs and the next attempt begins.

---

## 14. How Does Retry Know That the Function Failed?

It does not magically know.

The function tells Python that something went wrong by **raising an exception**.

Flow:

```text
Call function
     ↓
   try:
     ↓
Function raises exception?
   ↙             ↘
 NO               YES
 ↓                 ↓
Return result   except catches error
 ↓                 ↓
Success         Try again
```

Example:

```python
def test():
    raise ValueError("Something went wrong")
```

The retry decorator catches that exception and can attempt the function again.

---

## 15. Decorator with Arguments = Decorator Factory

When you write:

```python
@repeat(3)
def greet():
    print("Hello")
```

`repeat(3)` must first return a decorator.

Structure:

```python
def repeat(times):

    def decorator(function):

        def wrapper(*args, **kwargs):
            ...

        return wrapper

    return decorator
```

There are three levels:

```text
repeat(times)
      ↓
decorator(function)
      ↓
wrapper(*args, **kwargs)
```

The outer function receives configuration.

The middle function receives the function being decorated.

The inner wrapper runs when the decorated function is called.

---

## 16. Example: Repeat Decorator

```python
from functools import wraps


def repeat(times):

    def decorator(function):

        @wraps(function)
        def wrapper(*args, **kwargs):

            for _ in range(times):
                function(*args, **kwargs)

        return wrapper

    return decorator
```

Usage:

```python
@repeat(3)
def greet():
    print("Hello")

greet()
```

Output:

```text
Hello
Hello
Hello
```

---

## 17. Multiple Decorators

Example:

```python
@decorator_a
@decorator_b
def greet():
    print("Hello")
```

Equivalent transformation:

```python
greet = decorator_a(
    decorator_b(greet)
)
```

The decorators are applied from the bottom upward.

---

## 18. Real-World Uses

Decorators are commonly used for:

```text
Logging
Timing
Authentication
Authorization
Validation
Caching
Retry logic
Error handling
Monitoring
```

They are especially common in web frameworks and backend software.

---

## 19. Day 20 Mini Project — Function Monitoring System

Recommended project structure:

```text
Day-20/
├── decorators.py
├── main.py
└── README.md
```

The project can contain:

### `logger`
Print:

```text
[LOG] Function started: function_name
[LOG] Function finished: function_name
```

### `timer`
Print the execution time:

```text
[TIMER] function_name took 0.000123 seconds
```

### `handle_errors`
Catch and report exceptions:

```text
[ERROR] function_name: error message
```

### Retry
Retry a failed function a fixed number of times.

Example:

```python
@handle_errors
@timer
@logger
def divide(a, b):
    return a / b
```

---

## 20. Key Mental Model

Remember this:

```text
Decorator
    ↓
receives a function
    ↓
creates a wrapper
    ↓
wrapper adds behavior
    ↓
wrapper calls original function
    ↓
wrapper returns result
```

For retry:

```text
Call function
    ↓
Exception?
   ↙   ↘
 No     Yes
 ↓       ↓
Return  Retry
```

---

## 21. Day 20 Mastery Checklist

Before moving on, make sure you can explain:

- What a decorator is
- Why functions can be passed to other functions
- What `@decorator` means
- Why wrappers use `*args` and `**kwargs`
- Why return values must be preserved
- Why `functools.wraps` is useful
- How a decorator factory works
- What `@retry(3)` means
- How `try/except` detects raised exceptions inside a retry decorator
- How multiple decorators are applied

---

## 22. Quick Revision Template

Use this as your standard decorator template:

```python
from functools import wraps


def decorator(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        # Before

        result = function(*args, **kwargs)

        # After

        return result

    return wrapper
```

Decorator factory template:

```python
from functools import wraps


def decorator_factory(value):

    def decorator(function):

        @wraps(function)
        def wrapper(*args, **kwargs):

            # Extra behavior using `value`

            result = function(*args, **kwargs)

            return result

        return wrapper

    return decorator
```

---

## 23. Day 20 Summary

Day 20 was about **decorators** and how they can add reusable behavior around existing functions.

The most important concepts were:

```text
Higher-order functions
Nested functions
Wrappers
@decorator syntax
*args / **kwargs
Return values
functools.wraps
Decorator factories
Exception handling
Retry logic
Multiple decorators
```

Decorators are an important step toward writing cleaner, reusable, professional Python code.
