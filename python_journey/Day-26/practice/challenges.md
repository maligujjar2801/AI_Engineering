# Day 26 — Independent Practice

Complete these tasks after reading the lesson. Write and run the code yourself; do not copy the example package as your final submission.

## Challenge 1 — Utility module

Create a module named `string_tools.py` with three functions:

- `reverse_text(text)` returns the text in reverse order.
- `count_words(text)` returns the number of whitespace-separated words.
- `capitalize_words(text)` returns a title-cased version of the text.

Import and use all three functions from a separate file.

## Challenge 2 — Import styles

Write three small examples using:

1. `import string_tools`
2. `import string_tools as st`
3. `from string_tools import reverse_text`

Explain what names become available in the importing file and which style makes the source of a function most obvious.

## Challenge 3 — Main guard

Create a module with a function named `main` and the `if __name__ == "__main__":` guard.

- Run the file directly.
- Import it from another file.
- Confirm that importing it does not automatically run the application.

## Challenge 4 — Build a package

Create this package:

```text
book_manager/
    __init__.py
    books.py
    reports.py
```

In `books.py`, write functions to add a book to a list and search for a book by title. In `reports.py`, write a function that formats the current book list. Use a relative import between sibling modules where needed.

## Challenge 5 — Diagnose an import problem

Run a package module directly, then run the package using `python -m` from its parent directory.

Record:
- The command you ran.
- The error or output.
- Why package context matters for relative imports.

## Challenge 6 — Refactor an existing program

Choose one of your earlier single-file programs. Split it into at least two modules with distinct responsibilities. Avoid copying the same function into multiple files.

## Challenge 7 — Draw the dependency direction

Draw a small diagram showing which module imports which other module. Check for circular dependencies and try to keep the dependency direction one-way.

## Submission checklist

- [ ] I created and imported my own module.
- [ ] I tried all three import styles.
- [ ] I used a main guard.
- [ ] I created a package with at least two modules.
- [ ] I used a relative import inside that package.
- [ ] I ran a package with `python -m`.
- [ ] I refactored an earlier program.
- [ ] I can explain my package structure without reading the notes.
