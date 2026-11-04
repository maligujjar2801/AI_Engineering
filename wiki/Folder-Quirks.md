# Folder quirks

[Back to the wiki home](Home.md)

The lessons are real. Some filenames and headings are not. This page lists the mismatches so a future search does not look like a missing lesson. Nothing here needs to be “fixed” before you can learn from the code. Fix them when you next touch that folder, in a commit that does only the rename.

## Titles that disagree with the folder

| Folder | Heading you will see | What the files actually are |
| --- | --- | --- |
| `Day-09/` | README says “Day 6 – Build a Budget App” | A budget-app workshop. Notes file is named `day6_notes.md` but it is OOP revision, not the Day 6 list lesson |
| `Day-10/` | README says “Day 10 - Inheritance” | Only encapsulation scripts: public, protected, private, getter, setter, `@property` |
| `Day-11/` | README says “Day 11 - Encapsulation” | Both lessons. Inheritance notes are in `day10_notes.md`. Encapsulation notes are in `day11_notes.md` |

Safe reading order for 10 and 11 is written on [Days-10-to-17](Days-10-to-17.md).

## READMEs that name a file that is not there

| README says | File that exists |
| --- | --- |
| Discount: `python discount_strategy.py` | `discount_calculator.py` |
| Media: `python media_catalogue.py` | `Media Catalogue.py` |
| Player: `main.py` | `player_interface.py` |
| Expense tracker: `main.py` | `Expense Tracker.py` |
| Day 23 README link: `Day-23-Hashing-Hash-Tables-Dictionaries-and-Sets.md` | `Day - 23 notes.md.md` |

## Spelling in filenames

These still run. Quote them.

| Path | Note |
| --- | --- |
| `Day-07/ractangle.py` | “rectangle” |
| `Day-13/reactangle.py` | “rectangle” |
| `polygon_area_calcullator.py` | one extra `l` |
| `Day-19/practice/fibocanni.py` | Fibonacci |
| `Day-21/context_liberary.py` | “library” |
| `Day-17/nootification_system.py` | duplicate of the notification example |
| `Day-22/*compression.py` | the lesson is comprehension, not compression |
| `Day-25/sqlite3_CURD.py` | CRUD |
| `Day-16/Day_16_File_Handling_Notes (1).md` | a duplicate-download name; this is the notes file |
| `Expense Tracker.py` function `veiw_expenses` | spelling is inside the source, not only the filename |

## Guide files that are not named README.md

GitHub and many tools highlight `README.md` first. These days use a different name, so the folder can look empty at a glance:

| Day | Open this instead |
| --- | --- |
| 1 and 2 | `day1_notes.md`, `day2_notes.md` |
| 17 | `Day-17_README.md` |
| 20 | `Day-20-README.md` |
| 22 | `Day-22-README.md` |

## Generated files that were committed

| Path | What it is |
| --- | --- |
| `Day-23/Programming practice/__pycache__/frequency_calculator.cpython-314.pyc` | Bytecode from Python 3.14 |
| `Day-24/practice/__pycache__/Make_receipt.cpython-314.pyc` | Same |
| `Day-25/database.db` | A real SQLite file the scripts expect. This one **should** stay, or the scripts need a create step |
| `Day-19/mini project/app.log` | Sample or output log for the generator project |
| `Day-21/mini_project/log_file.log` | Output from the context-manager project |
| `Projects/Expense Tracker/Expense.txt` | Data for the menu program |
| `Projects/Expense Tracker/import tkinter as tk.txt` | Exact copy of `import tkinter as tk.py` |

A `.gitignore` is not in the tree. `__pycache__/` will keep coming back until one exists.

## Spaces and punctuation

These paths are valid. They are awkward in a terminal and in some tools:

- `Projects/Discount Calculator/`
- `Projects/Expense Tracker/`
- `Projects/Media Catalogue/`
- `Projects/Player Interface/`
- `Projects/Polygon Area Calculator/`
- `Projects/To Do List App/`
- `Projects/To Do List App/To do List.py`
- `Day-19/mini project/`
- `Day-22/Day- 22 Challenge.py` (space after the hyphen)
- `Day-23/Day - 23 notes.md.md` (space, and the extension `.md.md`)
- `Day-16/.read().py`, `.write().py`, `.strip().py`, `.replace().py`

New days are easier to link, test, and import if the folder is `day-27/` and the file is `notes.md` or `README.md`, with no spaces. The roadmap’s package work on Day 26 is the style to copy.

## Day 19 extra file

`python_journey/Day-19/.github/agents/permission-gated-code-enhancer.agent.md` is not a Python exercise. It does not belong to the iterator lesson. Leave it out of study sessions.

## Duplicate programs

Same bytes or the same idea stored twice:

- `Day-08/budget_app.py` and `Day-09/budget_app.py` are the same size (3238 bytes)
- `Day-06/car_info.py` and `Day-07/car_info.py` are the same size (432 bytes)
- `Day-07/student_methods.py` and `Day-08/student_methods.py` are the same size (758 bytes)
- Day 10’s encapsulation scripts are copied into Day 11
- `import tkinter as tk.py` and `.txt` in the expense folder share one git blob

Copies are fine as a snapshot of “I carried this forward”. If you change one, check whether you meant to change the other.
