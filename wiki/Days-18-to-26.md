# Days 18 to 26 — advanced Python

[Back to the journey index](Python-Journey.md) · [Home](Home.md)

This is the newest block in the snapshot. The notes are longer, the programs are smaller and sharper, and Day 26 is the first real package.

## Day 18 — functions as objects

[README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-18/README.md) · [day18-notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-18/day18-notes.md) (about 40 KB, the longest notes file in the journey)

Goal, from the README: stop treating a function as only a recipe you call, and start treating it as a value you can pass, return, and wrap.

| File | Topic |
| --- | --- |
| `higher_func.py` | A function that takes or returns a function |
| `lambda.py` | One-expression functions |
| `closure.py` | An inner function that remembers variables |
| `nonlocal.py` | Assigning to a variable from the enclosing function |
| `args.py` | `*args` |
| `kwargs.py` | `**kwargs` |
| `filter().py` | `filter` with a predicate |
| `@decorators.py` | A first decorator. The full decorator lesson is Day 20 |

## Day 19 — iterators and generators

[README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-19/README.md) · [Day-19-Notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-19/Day-19-Notes.md)

The notes go well past “`yield` exists”:

- iterable vs iterator
- `iter`, `next`, and `StopIteration`
- what a `for` loop actually does
- writing your own iterator
- `yield` vs `return`
- lazy evaluation and generator expressions
- infinite generators, `yield from`, pipelines
- generators for large files
- a first look at `.send()`
- when **not** to use a generator
- mistakes: calling `next` on a list, and using a generator twice after it is exhausted

Practice:

| File | Drill |
| --- | --- |
| `practice/countdown.py` | Generate a countdown |
| `practice/fibocanni.py` | Fibonacci. Filename spells Fibonacci wrong |
| `practice/multiples.py` | Multiples |

Mini project: [mini project/log_stream_processor.py](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-19/mini%20project/log_stream_processor.py), with `app.log` beside it. The README frames this as the reason generators matter for an AI engineer: you should not load a huge log into a list if you can stream it.

This folder also contains `.github/agents/permission-gated-code-enhancer.agent.md`. That file is an editor-agent note. It is not part of the Python lesson.

## Day 20 — decorators

[Day-20-README.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-20/Day-20-README.md) · [Day-20-Decorators-Notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-20/Day-20-Decorators-Notes.md)

Topics: first-class functions, higher-order functions, nested functions, and decorators that add behaviour around an existing function.

| File | Wrapper |
| --- | --- |
| `decorators.py` | The main examples |
| `Timer.py` | Time a function |
| `logger.py` | Log calls |

There is no `README.md` here. The guide is `Day-20-README.md`.

## Day 21 — context managers

[README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-21/README.md) · [Day-21_Context_Managers_Notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-21/Day-21_Context_Managers_Notes.md)

The notes walk the protocol:

- why `with` exists
- `__enter__`
- `__exit__(exc_type, exc_value, traceback)`
- returning `True` swallows the exception; returning `False` or `None` lets it propagate
- class-based managers vs `@contextlib.contextmanager`
- a debugging lesson about relative paths

| File | Role |
| --- | --- |
| `context_manager.py` | A class-based manager |
| `context_liberary.py` | `contextlib` (filename says “liberary”) |
| `exception_handling.py` | Exceptions inside `with` |
| `Timer.py` | Timing, separate from Day 20’s timer |
| `mini_project/log_file_context_manager.py` | A `LogFile` manager. Writes `mini_project/log_file.log` |

Run the mini project from `Day-21/` or from `Day-21/mini_project/`, matching whatever relative path the script uses. The notes call out path bugs as the day’s engineering lesson.

## Day 22 — comprehensions

[Day-22-README.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-22/Day-22-README.md) · [Day-22-notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-22/Day-22-notes.md)

Objectives in the README: list comprehensions, filters, conditional expressions, dict and set comprehensions, nested comprehensions, flattening, and keeping the line readable.

| File | Collection |
| --- | --- |
| `list compression.py` | Lists. Filename says “compression”; the lesson is **comprehension** |
| `dict compression.py` | Dicts |
| `set compression.py` | Sets |
| `Day- 22 Challenge.py` | A longer challenge. Note the space after the hyphen |

Guide file is `Day-22-README.md`, not `README.md`.

## Day 23 — hashing, dictionaries, and sets

[README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-23/README.md) · notes file on disk: `Day - 23 notes.md.md`

This is the first day that deliberately goes **under** the syntax. The README says you should be able to tell these apart:

- a map
- a hash map / hash table
- a Python `dict`
- a Python `set`
- the `map()` function

And explain hashes, lookup, and collisions at a conceptual level.

The README links to `Day-23-Hashing-Hash-Tables-Dictionaries-and-Sets.md`. **That file is not in the folder.** The notes that are present are [Day - 23 notes.md.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-23/Day%20-%2023%20notes.md.md) (about 41 KB).

Practice under `Programming practice/`:

| File | Task |
| --- | --- |
| `frequency_calculator.py` | Count how often values appear |
| `unique values.py` | Uniqueness, the job of a set |
| `student database.py` | A dict used as a table |
| `Day 23 Challenge.py` | The day’s challenge |

`mini project.py` (folder root) is a tiny student lookup: a dict of ids to name and marks, then `dict.get`.

`Programming practice/__pycache__/` is generated bytecode. It is not a lesson. See [Folder-Quirks](Folder-Quirks.md).

## Day 24 — `*args` and `**kwargs`

[README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-24/README.md) · [Day-24-Args-and-Kwargs-Deep-Dive.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-24/Day-24-Args-and-Kwargs-Deep-Dive.md)

The README’s path: read the notes, type the examples, predict five outputs, do five challenges, build the mini project, review.

Topics: positional vs keyword arguments, packing into a tuple with `*args`, packing into a dict with `**kwargs`, and forwarding arguments.

| File | Exercise |
| --- | --- |
| `practice/Flexible sum.py` | Sum any count of numbers |
| `practice/print_setting.py` | Options via keywords |
| `practice/Argument forwarding.py` | Pass `*args` and `**kwargs` onward |
| `practice/Make_receipt.py` | Build a receipt from flexible arguments |
| `mini_project.py` | The day’s combined program |

`practice/__pycache__/` is generated. Do not edit it.

## Day 25 — SQLite CRUD

[README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-25/README.md) · [notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-25/notes.md)

Beginner `sqlite3`, one operation per file, plus one combined file. The database file `database.db` is already in the folder. **Run the scripts from `Day-25/`** so `database.db` resolves.

| Order | File | SQL idea |
| --- | --- | --- |
| 1 | `CREATE.py` | Create the `students` table |
| 2 | `INSERT.py` | Insert a row |
| 3 | `READ.py` | Select and print |
| 4 | `UPDATE.py` | Change a student’s marks |
| 5 | `DELETE.py` | Delete by id |
| any time | `sqlite3_CURD.py` | Combined flow. The README notes that `CURD` is a typo for CRUD |

If you run `CREATE.py` again on a database that already has the table, expect the script to fail or to need `IF NOT EXISTS`. Read the file before re-running it.

## Day 26 — modules and packages

[README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-26/README.md) · [notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-26/notes.md) · [practice/challenges.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-26/practice/challenges.md)

This is the latest session named by the journey README.

What the day teaches:

- a module is a `.py` file you can import
- a package is a folder of modules, usually with `__init__.py`
- import styles, and why they matter
- `if __name__ == "__main__"`
- running a package with `python -m`
- a unit test that imports the package

Layout:

```text
Day-26/
├── examples/
│   ├── temperature.py      # a module
│   ├── import_demo.py      # imports it
│   └── __init__.py
├── study_tracker/
│   ├── __init__.py
│   ├── __main__.py         # so `python -m study_tracker` works
│   ├── records.py          # create_study_session(...)
│   └── reports.py          # format_report, build_demo_report
├── tests/
│   └── test_study_tracker.py
├── notes.md
└── practice/challenges.md  # seven challenges, including a submission checklist
```

Commands, from the Day 26 README, **with the shell already in `python_journey/Day-26/`**:

```bash
python -m study_tracker
python -m unittest discover -s tests -v
```

The challenges file asks you to: write a utility module, try import styles, use a main guard, build a package, diagnose a broken import, refactor an old program, and draw which way the dependencies point. Those are homework. The solutions are not pre-filled.

## What Day 26 unlocks

You can now split a program the way the roadmap’s Project 2 and Project 3 require: more than one file, a package, and a test. The next project should use that shape instead of one long script. See [What-Comes-Next](What-Comes-Next.md).
