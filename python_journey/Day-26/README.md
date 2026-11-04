# Day 26 — Python Modules & Packages

This session introduces the way Python projects split code into reusable modules and organize related modules into packages.

## Learning path

1. Read **[Detailed Notes](notes.md)** and trace every import example.
2. Run the module demonstrations from this folder.
3. Inspect the `study_tracker` package and understand how its files communicate.
4. Run the package with `python -m study_tracker`.
5. Run the unit tests with `python -m unittest discover -s tests -v`.
6. Complete the independent challenges in **[practice/challenges.md](practice/challenges.md)**.

## Folder structure

```text
Day-26/
├── README.md
├── notes.md
├── examples/
│   ├── __init__.py
│   ├── import_demo.py
│   └── temperature.py
├── study_tracker/
│   ├── __init__.py
│   ├── __main__.py
│   ├── records.py
│   └── reports.py
├── tests/
│   └── test_study_tracker.py
└── practice/
    └── challenges.md
```

## Run the examples

Open a terminal in the `Day-26` directory.

```bash
python -m examples.import_demo
python -m study_tracker
python -m unittest discover -s tests -v
```

Using `python -m` runs a module in its package context, which is especially important when the code uses relative imports.

## Topics covered

- What modules and packages are
- Importing modules, names, and aliases
- How Python locates modules
- The module namespace and `__name__`
- The `if __name__ == "__main__":` guard
- Import caching and repeated imports
- Regular packages and `__init__.py`
- Absolute and relative imports
- Running packages with `python -m`
- Avoiding circular imports and import-time side effects
- Reusable project structure and basic testing

## Completion criteria

Day 26 is complete when you can explain the difference between a module and a package, create your own package, import functions cleanly, run it with `python -m`, and pass the included tests.

**Next roadmap topic:** virtual environments and `pip`.
