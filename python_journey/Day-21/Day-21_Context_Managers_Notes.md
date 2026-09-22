# Day 21 — Context Managers in Python

## 🎯 Learning Objectives

By the end of Day 21, you should understand:

- What a context manager is
- Why Python uses the `with` statement
- How `__enter__()` and `__exit__()` work
- How to create a context manager using a class
- How to create one using `contextlib.contextmanager`
- How context managers handle exceptions
- Why cleanup belongs in `__exit__()`
- How context managers are useful for files, databases, locks, and other resources

---

# 1. What Is a Context Manager?

A context manager controls what happens when entering and leaving a block of code.

The basic pattern is:

```text
SETUP
  ↓
YOUR CODE
  ↓
CLEANUP
```

Python usually uses context managers with:

```python
with something:
    # code
```

A familiar example is:

```python
with open("data.txt", "r") as file:
    data = file.read()
```

The file is automatically cleaned up when the `with` block ends.

---

# 2. Why Do We Need Context Managers?

Without a context manager, you might write:

```python
file = open("data.txt", "r")

data = file.read()

file.close()
```

The problem is that an exception can occur before `file.close()`:

```python
file = open("data.txt", "r")

data = file.read()

result = 10 / 0

file.close()  # Never reached
```

A context manager provides a safer structure:

```python
with open("data.txt", "r") as file:
    data = file.read()
```

The cleanup is handled automatically.

---

# 3. Context Manager Protocol

A class-based context manager normally implements:

```python
__enter__()
__exit__()
```

The mental model is:

```text
with Resource() as value:
        ↓
    __enter__()
        ↓
    value = returned value
        ↓
      YOUR CODE
        ↓
    __exit__()
        ↓
      CLEANUP
```

---

# 4. `__enter__()`

`__enter__()` runs when the `with` block begins.

Example:

```python
class MyContext:

    def __enter__(self):
        print("Entering")
        return self
```

The value returned from `__enter__()` is assigned to the variable after `as`.

For example:

```python
with MyContext() as context:
    print(context)
```

Because `__enter__()` returns `self`, `context` refers to the object.

---

# 5. `__exit__()`

`__exit__()` runs when Python leaves the `with` block.

Example:

```python
class MyContext:

    def __enter__(self):
        print("Entering")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting")
```

Usage:

```python
with MyContext():
    print("Working")
```

Output:

```text
Entering
Working
Exiting
```

---

# 6. The Three `__exit__()` Arguments

A context manager normally defines:

```python
def __exit__(self, exc_type, exc_value, traceback):
```

They describe an exception if one occurred.

### `exc_type`

The type/class of the exception.

Example:

```text
ValueError
```

### `exc_value`

The actual exception object/message.

Example:

```text
Something went wrong.
```

### `traceback`

Information about where the exception occurred.

If there was no exception, these values are normally:

```python
None
```

---

# 7. Exception Handling

Consider:

```python
with MyContext():
    10 / 0
```

Even though an exception occurs, `__exit__()` gets a chance to execute.

Conceptually:

```text
__enter__()
    ↓
YOUR CODE
    ↓
EXCEPTION
    ↓
__exit__()
    ↓
CLEANUP
```

This is one of the most important benefits of context managers.

---

# 8. Returning `True` or `False` from `__exit__()`

The return value of `__exit__()` determines whether an exception is suppressed.

### Return `True`

```python
def __exit__(self, exc_type, exc_value, traceback):
    return True
```

This tells Python:

> The exception has been handled; do not propagate it.

### Return `False` or `None`

```python
def __exit__(self, exc_type, exc_value, traceback):
    return False
```

The exception continues normally.

For learning and debugging, `False` is often preferable because you can see the actual error.

---

# 9. Class-Based Context Manager

A simple context manager:

```python
class MyContext:

    def __enter__(self):
        print("Entering")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting")
```

Usage:

```python
with MyContext():
    print("Working")
```

The class version is important for learning because it exposes the actual context-manager protocol.

---

# 10. Day 21 Mini Project — `LogFile`

The project is a context manager that manages a log file.

Desired usage:

```python
with LogFile("log_file.log") as file:
    file.write("Application started\n")
    file.write("Processing data\n")
```

The context manager should:

1. Receive the filename.
2. Open the file when entering the context.
3. Return the opened file.
4. Allow the caller to write to it.
5. Close the file when leaving the context.
6. Still close the file if an exception occurs.
7. Optionally report the exception.

---

# 11. Project Step 1 — Constructor

Store the filename:

```python
class LogFile:

    def __init__(self, filename):
        self.filename = filename
```

Now:

```python
LogFile("log_file.log")
```

stores:

```text
self.filename → "log_file.log"
```

---

# 12. Project Step 2 — Open the File

In `__enter__()`:

```python
def __enter__(self):
    self.file = open(self.filename, "a")
    print("File opened")
    return self.file
```

Why `"a"`?

`"a"` means **append**.

It adds new content to the existing file rather than replacing it.

---

# 13. Project Step 3 — Close the File

In `__exit__()`:

```python
def __exit__(self, exc_type, exc_value, traceback):
    self.file.close()
    print("File closed")
```

Important:

```python
print("File closed")
```

only prints a message.

It does NOT close the file.

The actual operation is:

```python
self.file.close()
```

---

# 14. Project Step 4 — Handle Exceptions

A useful version is:

```python
def __exit__(self, exc_type, exc_value, traceback):
    self.file.close()

    if exc_type:
        print("Exception:", exc_value)

    print("File closed")

    return False
```

Returning `False` allows the exception to propagate normally.

---

# 15. Complete Class-Based Project

```python
class LogFile:

    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "a")
        print("File opened")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

        if exc_type:
            print("Exception:", exc_value)

        print("File closed")

        return False


with LogFile("log_file.log") as file:
    file.write("Application started\n")
    file.write("Processing data\n")
```

---

# 16. Test Exception Handling

Test deliberately:

```python
with LogFile("log_file.log") as file:
    file.write("Before error\n")
    raise ValueError("Something went wrong.")
```

The important sequence is:

```text
File opened
    ↓
write data
    ↓
ValueError occurs
    ↓
__exit__()
    ↓
file.close()
    ↓
Exception information is available
    ↓
exception propagates if return is False
```

Even with an exception, cleanup should happen.

---

# 17. `contextlib.contextmanager`

Python also provides a convenient way to create context managers.

Import:

```python
from contextlib import contextmanager
```

Then:

```python
@contextmanager
def my_context():

    print("Entering")

    try:
        yield

    finally:
        print("Exiting")
```

Usage:

```python
with my_context():
    print("Working")
```

Output:

```text
Entering
Working
Exiting
```

---

# 18. Class vs `contextlib`

These are two different implementation approaches for the same context-manager concept.

```text
                 CONTEXT MANAGER
                        │
              ┌─────────┴─────────┐
              ↓                   ↓
            CLASS             contextlib
              │                   │
        __enter__()         @contextmanager
        __exit__()                 │
              │                  yield
              └─────────┬─────────┘
                        ↓
                   with statement
```

### Class

Best for understanding:

- `__enter__()`
- `__exit__()`
- exception information
- the context-manager protocol

### `contextlib`

Convenient when the setup/cleanup logic is simple.

For Day 21, learn the **class implementation first**, then recreate the same idea with `contextlib` as a bonus.

---

# 19. Important Python Naming Lesson

Do NOT name your own file:

```text
contextlib.py
```

because Python already has a standard-library module called `contextlib`.

Then:

```python
from contextlib import contextmanager
```

may accidentally import your own file instead of Python's standard module.

Use:

```text
context_manager.py
```

instead.

This caused the import error encountered during Day 21.

Other names that can cause similar problems include:

```text
random.py
json.py
logging.py
typing.py
time.py
math.py
```

Avoid shadowing standard-library module names.

---

# 20. Debugging Relative File Paths

If:

```python
open("log_file.log", "a")
```

appears not to modify the file you are viewing, remember that `"log_file.log"` is a relative path.

You can check the exact location with:

```python
from pathlib import Path

print(Path("log_file.log").resolve())
```

This tells you the exact file Python is opening.

This is useful when working with files in VS Code and different working directories.

---

# 🧠 Core Mental Model

Remember:

```text
with Resource() as value:
        ↓
__enter__()
        ↓
setup/acquire resource
        ↓
value returned to `as`
        ↓
YOUR CODE
        ↓
__exit__()
        ↓
cleanup/release resource
```

The central idea is:

> A context manager makes sure that resources are properly managed before and after a block of code.

---

# ✅ Day 21 Checklist

- [ ] Understand what a context manager is
- [ ] Understand the `with` statement
- [ ] Understand `__enter__()`
- [ ] Understand `__exit__()`
- [ ] Understand `exc_type`
- [ ] Understand `exc_value`
- [ ] Understand `traceback`
- [ ] Understand exception suppression
- [ ] Build a class-based context manager
- [ ] Complete the `LogFile` project
- [ ] Test cleanup with an exception
- [ ] Understand `contextlib.contextmanager`
- [ ] Know why `contextlib.py` is a bad filename
- [ ] Know how to find the real path of a relative file

---

# 🔥 Engineering Takeaway

> **Context managers provide a reliable structure for setup, resource usage, and cleanup.**

You will encounter this pattern with:

- files
- databases
- network connections
- locks
- transactions
- temporary resources
- API sessions

The `with` statement is therefore not just a Python trick—it is an important software-engineering pattern.
