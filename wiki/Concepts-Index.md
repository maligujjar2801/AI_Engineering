# Concepts index

[Back to the wiki home](Home.md)

Use this when you remember the idea and need the folder. “Primary” is the day that teaches it. “Used again” is a later project or day that depends on it.

| Concept | Primary | Used again |
| --- | --- | --- |
| What Python is, interpreter, dynamic typing | [Day 1 notes](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-01/day1_notes.md) | Every later day |
| `int`, `float`, `str`, `bool` | Day 2 | Day 1 programs already mix them |
| Arithmetic operators | Day 2 | Discount engine, polygon formulas |
| `if` / `elif` / `else` | Day 3 | Every menu and validator |
| Comparisons and indentation | Day 3 | Day 3 grade calculator |
| `for`, `while`, `range` | Day 4 | Guessing game, expense menu |
| `break`, `continue` | Day 4 | — |
| Functions, parameters, arguments | Day 5 | Day 18, Day 24 |
| `return` vs `print` | Day 5 | Polygon notes, mistake list |
| Lists, slicing, methods | Day 6 | Student management, Day 6 |
| Nested lists | Day 6 | Day 22 nested comprehensions |
| Classes, `self`, methods | Day 7 | Every project |
| Class vs instance variables | Day 8 | — |
| `@classmethod`, `@staticmethod` | Day 8 | — |
| Composition (objects using objects) | Day 8 | Media catalogue, discount engine |
| Public / protected / private | Day 10 files, Day 11 notes | Salary tracker |
| Getters, setters, `@property` | Day 10–12 | Game stats (Day 15) |
| Inheritance, `super()` | Day 11 notes | Square, Pawn, TV series, discounts |
| Method overriding | Day 11, Day 14 | Pawn movement |
| `isinstance`, `issubclass` | Day 11 | Media catalogue README |
| `__str__`, `__len__`, `__eq__`, `__add__` | Day 13 | Product and Movie printing |
| Polymorphism | Day 14 | Discount strategies, notifications |
| Custom exceptions | Media catalogue notes | Day 16 file errors, Day 17 |
| Reading and writing files | Day 16 | Expense tracker, log projects |
| `try` / `except` around files | Day 16 | Day 21 `__exit__` |
| Abstraction, `ABC`, `@abstractmethod` | Day 17 | `DiscountStrategy`, `Player` |
| First-class and higher-order functions | Day 18 | Decorators |
| `lambda` | Day 18 | — |
| Closures, `nonlocal` | Day 18 | Decorators |
| Decorators | Day 20 (intro on Day 18) | — |
| Iterators, `iter` / `next` | Day 19 | — |
| Generators, `yield`, lazy evaluation | Day 19 | Log stream processor |
| Context managers, `with` | Day 21 | Any later file or DB code should use this |
| `contextlib` | Day 21 | — |
| List / dict / set comprehensions | Day 22 | — |
| Hashing, collisions, dict and set internals | Day 23 | Frequency counter, student lookup |
| `*args`, `**kwargs`, forwarding | Day 24 (intro on Day 18) | — |
| SQLite, `CREATE` / `INSERT` / `SELECT` / `UPDATE` / `DELETE` | Day 25 | — |
| Modules and imports | Day 26 | `examples/import_demo.py` |
| Packages, `__init__`, `__main__` | Day 26 | `study_tracker` |
| `unittest` | Day 26 | Root VS Code settings already look for `*test.py` |
| Tkinter widgets, `pack`, `grid`, callbacks | To-do notes | Small sketches in the expense folder |
| Strategy pattern | Discount calculator | — |
| Linked list (sketch only) | `Projects/Expense Tracker/Linked list.py` | Roadmap Phase 2, not started |
| Big-O, trees, graphs, NumPy, Pandas, ML, PyTorch, LLMs | Roadmap only | Not in the code yet |

## By project, the one idea to remember

| Project | One sentence |
| --- | --- |
| Discount calculator | Ask each strategy whether it applies, then keep the best price |
| Expense tracker | A loop can be a program, and a text file can be a database |
| Media catalogue | Validate in the constructor and raise a specific error |
| Player interface | An abstract class can force every piece to know how it moves |
| Polygon calculator | A square is a rectangle that refuses to have two different sides |
| To-do app | A button stores a method; it does not call the method while you build the window |
