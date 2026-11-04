# Python journey

[Back to the wiki home](Home.md)

Folder: [python_journey/](https://github.com/maligujjar2801/AI_Engineering/tree/main/python_journey)

26 numbered days plus `rev-1`. The journey README’s “latest session” line points at Day 26.

Days 1–9 are written up together on [Days-01-to-09](Days-01-to-09.md). Days 10–17 are on [Days-10-to-17](Days-10-to-17.md). Days 18–26 are on [Days-18-to-26](Days-18-to-26.md).

## Master index

| Day | Topic the folder is actually about | Start here |
| --- | --- | --- |
| 1 | What Python is, types, variables, indexing and slicing | [day1_notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-01/day1_notes.md) |
| 2 | Variables, `int` / `float` / `str` / `bool`, arithmetic operators | [day2_notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-02/day2_notes.md) |
| 3 | `if` / `elif` / `else`, comparisons, indentation | [README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-03/README.md) |
| 4 | `for`, `while`, `range`, `break`, `continue` | [day4_notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-04/day4_notes.md) |
| 5 | Defining and calling functions, parameters, arguments, `return` vs `print` | [README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-05/README.md) |
| 6 | Lists: index, slice, add, remove, methods, membership, nested lists | [day6_notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-06/day6_notes.md) |
| 7 | Classes and objects, methods, a bank account and a student | [README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-07/README.md) |
| 8 | Class variables, `@classmethod`, `@staticmethod`, `__str__`, composition | [README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-08/README.md) |
| 9 | Budget app workshop (OOP revision). Notes file is still named `day6_notes.md` | [README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-09/README.md) |
| 10 | **Files are encapsulation** (`@property`, getters, setters, public/protected/private). README title says “Inheritance” | [README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-10/README.md) |
| 11 | Inheritance notes **and** encapsulation notes, plus both sets of scripts | [day11_notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-11/day11_notes.md) |
| 12 | Salary tracker: encapsulation and `@property` in one program | [README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-12/README.md) |
| 13 | Dunder methods: `__str__`, `__len__`, `__eq__`, `__add__`, comparisons | [day13_notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-13/day13_notes.md) |
| 14 | Polymorphism through inheritance | [day14_notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-14/day14_notes.md) |
| 15 | Game character stats: properties for health, mana, and level | [day15_notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-15/day15_notes.md) |
| 16 | File handling: create, read, write, append, strip, replace, exceptions | [README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-16/README.md) |
| 17 | Abstraction with `ABC` and `@abstractmethod` | [Day-17_README.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-17/Day-17_README.md) |
| 18 | First-class functions, lambdas, closures, `*args`, `**kwargs`, `filter`, `nonlocal`, decorator introduction | [README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-18/README.md) |
| 19 | Iterators, generators, `yield`, lazy evaluation, log-stream mini project | [README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-19/README.md) |
| 20 | Decorators: wrap a function without rewriting it. Timer and logger examples | [Day-20-README.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-20/Day-20-README.md) |
| 21 | Context managers: `__enter__` / `__exit__` and `contextlib` | [README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-21/README.md) |
| 22 | List, dict, and set comprehensions, including nested data | [Day-22-README.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-22/Day-22-README.md) |
| 23 | Hashing, hash tables, dictionaries, and sets | [README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-23/README.md) |
| 24 | `*args` and `**kwargs` in depth, plus a flexible report | [README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-24/README.md) |
| 25 | SQLite CRUD with the `sqlite3` module | [README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-25/README.md) |
| 26 | Modules, packages, `python -m`, and unittest | [README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-26/README.md) |
| rev-1 | File-handling revision script | [file_rev.py](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/rev-1/file_rev.py) |

## How a day folder is organised

Early pattern (Days 1–8):

```text
Day-0N/
├── README.md          # missing on Days 1 and 2; notes file only
├── dayN_notes.md
└── several small .py programs
```

Later pattern (Days 19–26):

```text
Day-NN/
├── README.md
├── long notes file
├── practice/ or examples/
└── a mini project or a real package
```

## Programs worth running again before Day 27

If you only revisit a few, use these. They combine more than one idea:

| Program | Why |
| --- | --- |
| [Day-06/student_management.py](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-06/student_management.py) | Lists used as a tiny student record |
| [Day-09/budget_app.py](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-09/budget_app.py) | The first larger OOP program |
| [Day-12/salary_tracker.py](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-12/salary_tracker.py) | Properties used for a reason |
| [Day-15/game_stats.py](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-15/game_stats.py) | Validation inside properties |
| [Day-19/mini project/log_stream_processor.py](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-19/mini%20project/log_stream_processor.py) | Generators on a log file |
| [Day-21/mini_project/log_file_context_manager.py](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-21/mini_project/log_file_context_manager.py) | A class that is a context manager |
| [Day-25/sqlite3_CURD.py](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-25/sqlite3_CURD.py) | One file that creates, inserts, updates, and reads |
| [Day-26/study_tracker/](https://github.com/maligujjar2801/AI_Engineering/tree/main/python_journey/Day-26/study_tracker) | The first package, with tests |

## Revision folder

`rev-1/file_rev.py` sits beside the days, not inside one. It is a file-handling review. Run it from `python_journey/rev-1/` if it reads or writes a local file.
