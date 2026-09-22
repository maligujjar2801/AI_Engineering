# Day 21 — Context Managers

## 📌 Topic

**Python Context Managers**

Day 21 focuses on Python's context-manager protocol, the `with` statement, `__enter__()`, `__exit__()`, exception handling, and resource cleanup.

---

## 🎯 Learning Goals

- Understand context managers
- Understand the `with` statement
- Learn `__enter__()` and `__exit__()`
- Build a class-based context manager
- Understand exception handling inside context managers
- Learn `contextlib.contextmanager`
- Understand automatic resource cleanup

---

## 🧠 Core Concept

A context manager follows this general pattern:

```text
SETUP
  ↓
YOUR CODE
  ↓
CLEANUP
```

The `with` statement provides a clean way to guarantee that cleanup is performed when leaving the block.

---

## 🛠️ Project — LogFile Context Manager

The Day 21 project is a custom `LogFile` context manager.

Example:

```python
with LogFile("log_file.log") as file:
    file.write("Application started\n")
    file.write("Processing data\n")
```

The class opens the log file when entering the context and closes it when leaving.

### Main concepts demonstrated

- `__init__()`
- `__enter__()`
- `__exit__()`
- File handling
- Append mode (`"a"`)
- Exception information
- Cleanup after exceptions

---

## 📂 Suggested Structure

```text
Day-21/
│
├── README.md
├── notes.md
├── context_manager.py
├── timer.py
├── main.py
└── log_file.log
```

---

## ⚠️ Important Debugging Lesson

Do not name a personal Python file:

```text
contextlib.py
```

Python already has a standard-library module named `contextlib`.

That can cause:

```python
from contextlib import contextmanager
```

to import the local file instead of the standard module.

Use a name such as:

```text
context_manager.py
```

instead.

---

## 🔑 Key Learning

A context manager can be implemented using:

### 1. A class

```python
class MyContext:

    def __enter__(self):
        ...

    def __exit__(self, exc_type, exc_value, traceback):
        ...
```

### 2. `contextlib`

```python
from contextlib import contextmanager

@contextmanager
def my_context():
    try:
        yield
    finally:
        ...
```

For learning the underlying mechanism, the class-based implementation is especially important.

---

## 🧪 Testing

The project should be tested both:

### Without an exception

```python
with LogFile("log_file.log") as file:
    file.write("Application started\n")
```

### With an exception

```python
with LogFile("log_file.log") as file:
    file.write("Before error\n")
    raise ValueError("Something went wrong.")
```

The file should still be closed during cleanup.

---

## 📚 Skills Added

- Context managers
- Resource management
- File handling
- Exception handling
- `with` statement
- Python protocols
- `contextlib`
- Debugging relative paths

---

## 🚀 Next Step

After understanding the class-based implementation, recreate the same behavior using:

```python
@contextmanager
```

Then move to **Day 22: Comprehensions + Advanced Patterns**.
