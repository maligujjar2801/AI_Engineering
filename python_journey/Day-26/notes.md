# Day 26 — Python Modules & Packages

> Python Journey • Learn → Understand → Trace → Practise → Build → Test  
> Prerequisites: functions, variables, dictionaries, file handling basics, and running Python files from a terminal.

## Learning objectives

By the end of this session, you should be able to:

- Explain why a growing Python program should be split across files.
- Define a module and a package and distinguish between them.
- Import a module, selected names, and aliases.
- Explain what happens when Python imports a module.
- Use `__name__` and the main guard correctly.
- Understand, at a practical level, how Python searches for modules.
- Organize related modules inside a package.
- Use absolute and relative imports appropriately.
- Run a package using `python -m`.
- Recognize common import errors, circular imports, and import-time side effects.

---

## 1. Why do modules and packages exist?

Imagine building a study management application. At first, it may contain only a few functions:

```python
def add_session(topic, minutes):
    ...

def calculate_total(sessions):
    ...

def print_report(sessions):
    ...

def validate_topic(topic):
    ...
```

Putting everything into one file is fine for a tiny exercise. As the application grows, one file becomes harder to navigate, test, debug, and maintain.

A better approach is to separate responsibilities:

```text
study_tracker/
    records.py       # create and validate study records
    reports.py       # calculate and format summaries
    storage.py       # save and load data
    cli.py           # interact with the user
```

Each file has a focused responsibility. Other parts of the program can import and reuse its functions.

**Core idea:** a module gives related code a named place; a package groups related modules into a larger structure.

## 2. What is a module?

A Python module is normally a `.py` file.

For example, this file is a module:

`temperature.py`

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def describe_temperature(celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    return f"{celsius}°C is {fahrenheit}°F"
```

The module name is usually the filename without the `.py` extension:

```text
temperature.py  →  temperature
```

The functions defined in that file belong to the module's namespace. The namespace helps keep names organized and avoids putting every function into one global naming space.

### Import and use the module

Place this second file beside `temperature.py`.

`main.py`

```python
import temperature

print(temperature.celsius_to_fahrenheit(25))
print(temperature.describe_temperature(25))
```

When Python sees `import temperature`, it locates and loads the module. The name `temperature` becomes available in the importing file, and you access its members using dot notation:

```python
temperature.celsius_to_fahrenheit(25)
```

The dot means: access this name inside that module.

### Why not just copy the function?

Copying a function into every file creates multiple versions to maintain. Importing one shared implementation means that fixes and improvements can be made in one place.

## 3. Different ways to import

Assume a module named `math_tools.py` contains:

```python
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b
```

### A. Import the whole module

```python
import math_tools

print(math_tools.add(4, 5))
```

This makes the module name available. It keeps the origin of the function clear.

### B. Import selected names

```python
from math_tools import add, multiply

print(add(4, 5))
print(multiply(4, 5))
```

Now the selected functions can be used directly. This is convenient, but the source module is less visible at the call site.

### C. Import with an alias

```python
import math_tools as mt

print(mt.add(4, 5))
```

An alias gives the imported module a shorter local name. Aliases are common for widely used libraries, but choose names that remain understandable.

### D. Alias an imported name

```python
from math_tools import multiply as product

print(product(4, 5))
```

This renames the imported function in the current file. It does not rename the original function inside its module.

### Avoid wildcard imports

```python
from math_tools import *
```

This brings many names into the current namespace. It can make it unclear where a name came from and can overwrite another name accidentally. Prefer importing the module or explicitly naming what you need.

## 4. What happens when Python imports a module?

A useful mental model for a normal first import is:

1. Python checks whether the module is already present in its import cache.
2. If it is not loaded, Python searches for it using the import system and module search path.
3. Python creates a module object and prepares its namespace.
4. Python executes the module's top-level statements.
5. The loaded module is made available for later imports in that running interpreter.

The import cache is exposed through `sys.modules`. It helps prevent the same module from being fully executed again on every import in one interpreter process.

### Important consequence: top-level code runs during import

Consider `announcement.py`:

```python
print("The announcement module is loading")


def announce():
    print("Welcome to Python!")
```

And `app.py`:

```python
import announcement

print("The application is running")
```

The first time this import is performed in that process, the module-level print executes. This is why modules should generally avoid asking for user input, starting major tasks, or performing surprising actions at import time.

Prefer defining functions and classes at module level, then call them explicitly from the application.

## 5. The special variable `__name__`

Python gives each module a special variable named `__name__`.

- When a module is imported, its `__name__` is normally its module name.
- When a file is executed as the program's entry point, its `__name__` is `"__main__"`.

Example: `identity_demo.py`

```python
print("Module name:", __name__)
```

Run it directly:

```bash
python identity_demo.py
```

The output begins with:

```text
Module name: __main__
```

Now import it from another file. The value will be the module's import name rather than `__main__`.

### The main guard

This pattern is extremely important:

```python
def main():
    print("Run the application here")


if __name__ == "__main__":
    main()
```

Read it as:

> Run `main()` only when this file is being executed as the main program, not when another module imports it.

Why is that useful?

A file can be both:
- an executable program, and
- a reusable module.

The main guard allows both uses without automatically launching the application whenever another file imports it.

## 6. Where does Python look for modules?

Python uses an import system to locate modules. The search locations for an interpreter are represented in `sys.path`.

You can inspect it:

```python
import sys

for location in sys.path:
    print(location)
```

The entries depend on how Python was launched and configured. They commonly include the script or working-directory context, configured paths such as `PYTHONPATH`, standard-library locations, and installed package locations.

### A practical rule

For this session, keep the package folder beside the script or run command from the project root:

```text
Day-26/
    examples/
    study_tracker/
```

When you open the terminal in `Day-26`, Python can normally locate those top-level packages.

Do not assume that Python searches every folder on your computer. A folder must be discoverable through the import system.

## 7. What is a package?

A package groups related modules under a package name.

A regular package commonly looks like this:

```text
study_tracker/
    __init__.py
    records.py
    reports.py
```

- `study_tracker` is the package.
- `records.py` is a module inside the package.
- `reports.py` is another module inside the same package.
- `__init__.py` marks and initializes the regular package.

The `__init__.py` file may be empty. It can also contain package documentation, constants, or a deliberately chosen public interface.

Python also supports namespace packages without an `__init__.py` file. Those are useful in some advanced multi-directory layouts. For this learning session, use the regular package structure with `__init__.py`.

### Module vs package

| Feature | Module | Package |
|---|---|---|
| Typical form | One `.py` file | A directory of related modules |
| Organizes | Functions, classes, variables | Related modules and subpackages |
| Example | `records.py` | `study_tracker/` |
| Import example | `import records` | `import study_tracker` |

A package is not a different programming language feature from a module; it is a way to organize a group of modules under a package namespace.

## 8. Importing from a package

Given:

```text
project/
    main.py
    study_tracker/
        __init__.py
        records.py
        reports.py
```

### Import a module using its package path

In `main.py`:

```python
from study_tracker import records

session = records.create_study_session("Python", 45)
print(session)
```

### Import a function from a package module

```python
from study_tracker.records import create_study_session

session = create_study_session("Python", 45)
```

Both styles are valid. The first makes the module visible at the call site; the second is more direct when only a few names are needed.

## 9. Absolute imports vs relative imports

This distinction matters once files live inside packages.

### Absolute import

An absolute import starts from an importable top-level package or module:

```python
from study_tracker.records import create_study_session
```

It clearly shows the package path.

### Relative import

A relative import starts from the current package:

```python
from .records import create_study_session
```

The leading dot means the current package. Two dots mean the parent package.

Relative imports are useful between modules that belong to the same package. They are not intended for a file executed as an unrelated standalone script.

### Why the way you run a file matters

From the `Day-26` directory, run:

```bash
python -m study_tracker
```

This tells Python to execute the package as a module and provides the package context needed by relative imports.

Avoid running the package's internal file directly like this:

```bash
python study_tracker/__main__.py
```

That direct-file execution does not establish the same package context, so relative imports can fail. Use `python -m` for this project.

## 10. What does `__init__.py` do?

A package's `__init__.py` executes when the package is imported for the first time in a process.

It can:
- document the package,
- define package-level constants,
- expose a small, intentional public interface,
- perform lightweight initialization.

Example:

```python
"""Tools for recording and summarizing study sessions."""

__version__ = "1.0.0"
```

You may see packages re-export selected functions from `__init__.py`:

```python
from .records import create_study_session
```

Then users may be able to import the function directly from the package:

```python
from study_tracker import create_study_session
```

Do not turn `__init__.py` into a place for all application logic. Keep it small and predictable.

## 11. Common problems and how to reason about them

### Problem A: `ModuleNotFoundError`

Python cannot locate the requested module or package.

Check:
- Is the spelling and capitalization correct?
- Does the file or package exist?
- Are you running the command from the expected project directory?
- Is the required parent directory on the import path?
- Are you using the correct interpreter or virtual environment?

### Problem B: `ImportError: attempted relative import with no known parent package`

A file containing a relative import is being run without its package context.

For this project, run the package from the `Day-26` directory:

```bash
python -m study_tracker
```

### Problem C: circular imports

A circular import can happen when module A imports module B while module B also imports module A.

```text
records.py  → imports reports.py
reports.py  → imports records.py
```

This creates a dependency cycle and can lead to partially initialized modules or confusing import errors.

Better design:
- Keep responsibilities separate.
- Move shared simple logic into a third module if appropriate.
- Prefer a one-directional dependency structure.
- Import only what a module actually needs.

### Problem D: unexpected code runs after importing

Look for top-level statements that perform application work. Move execution into functions and call those functions from a main guard.

### Problem E: wildcard imports create unclear names

Replace `from package import *` with explicit imports or module-qualified access.

---

## 12. Build: a small reusable `study_tracker` package

The project in this folder is a deliberately small example of package design.

```text
study_tracker/
    __init__.py
    __main__.py
    records.py
    reports.py
```

Responsibility of each module:

- `records.py`: validate and create a study-session record.
- `reports.py`: summarize a collection of records.
- `__init__.py`: document the package and define its version.
- `__main__.py`: provide the package's runnable entry point.

### Follow the data

The entry point creates records by calling a function from `records.py`. It then passes those records to a function from `reports.py`.

```text
python -m study_tracker
        |
        v
   __main__.py
      /    \
     v      v
records.py  reports.py
     \      /
      v    v
    formatted report
```

Notice the separation: record creation and report formatting are not mixed into one giant file.

### Run it

From the `Day-26` folder:

```bash
python -m study_tracker
```

### Run the tests

```bash
python -m unittest discover -s tests -v
```

The tests check expected behaviour and validation without requiring an external testing library.

---

## 13. Predict before running

Write down the output or behaviour first.

### Q1 — Module import

`greeter.py`

```python
language = "Python"

def greet():
    return f"Hello from {language}"
```

`app.py`

```python
import greeter
print(greeter.greet())
```

What is printed?

### Q2 — Alias

```python
import math as m
print(m.sqrt(81))
```

What is the output?

### Q3 — Main guard

```python
def run():
    print("Running")

if __name__ == "__main__":
    run()
```

What happens when this file is imported by another module? What happens when it is executed directly?

### Q4 — Package path

Given `store/inventory.py`, how would you import the `add_item` function from a file outside the `store` package?

### Q5 — Relative import

Inside a package, a module named `reports.py` needs a function from a sibling module named `records.py`. Write the relative import.

### Q6 — Import side effect

A module prints a message at the top level. What happens the first time another module imports it in a fresh Python process?

### Q7 — Module or package?

Is `helpers.py` a module or a package? Is a directory named `helpers/` containing `__init__.py` and `text.py` a regular package?

<details>
<summary>Show prediction answers</summary>

1. `Hello from Python`
2. `9.0`
3. When imported, the guarded call does not run. When executed as the main program, `Running` is printed.
4. `from store.inventory import add_item`
5. `from .records import function_name` (replace the placeholder with the actual function name).
6. Its top-level print statement runs during the first import in that interpreter process.
7. `helpers.py` is a module. The directory with `__init__.py` is a regular package.

</details>

## 14. Practice challenges

Complete these without copying the project implementation:

1. **Create a utility module:** make `string_tools.py` with `reverse_text`, `count_words`, and `capitalize_words`. Import and use each function from another file.
2. **Compare import styles:** use `import string_tools`, an alias, and an explicit function import. Explain which style makes the source of a function clearest.
3. **Add a module entry point:** create a file with a `main()` function and a main guard. Confirm importing it does not start the application.
4. **Build a package:** make a `book_manager` package with `books.py` and `reports.py`. Use a relative import between the sibling modules.
5. **Trace an import error:** intentionally run a package file directly, note the error, and then run it using `python -m`. Explain why the second command works.
6. **Refactor:** take a single-file program you have written and split it into at least two modules with clear responsibilities.
7. **Dependency direction:** draw which modules import which other modules. Try to keep the dependency direction one-way.

See [practice/challenges.md](practice/challenges.md) for the independent submission checklist.

## 15. Good habits to keep

- Give modules meaningful, lowercase names.
- Avoid naming your own files after standard-library modules such as `math.py`, `json.py`, or `random.py`.
- Keep one clear responsibility per module.
- Use explicit imports instead of wildcard imports.
- Avoid expensive or surprising work at import time.
- Use the main guard for executable entry points.
- Use relative imports between sibling modules inside a package when appropriate.
- Run packages with `python -m` when package context is required.
- Test behaviour at module boundaries.

## Completion checklist

- [ ] I can explain why modules are useful.
- [ ] I can distinguish a module from a package.
- [ ] I can use `import`, `from ... import ...`, and aliases.
- [ ] I understand the purpose of `sys.path` and `sys.modules`.
- [ ] I understand `__name__` and the main guard.
- [ ] I can use `__init__.py` and relative imports.
- [ ] I can run a package with `python -m`.
- [ ] I can explain at least two common import errors.
- [ ] I ran the package and its tests.
- [ ] I completed the practice challenges.

**Next session:** virtual environments and `pip` — how to isolate project dependencies and install third-party packages safely.
