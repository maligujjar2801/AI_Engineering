# Projects

[Back to the wiki home](Home.md) · [How to run them](How-to-Run.md)

`Projects/` holds six programs that sit beside the daily log. They are the bridge between “I know the syntax” and “I built a thing”. None of them is a Phase 5 machine-learning project. Four of them are object-oriented. Two are freeCodeCamp labs. One is a desktop GUI. One is a text menu.

The roadmap’s four “serious” Phase 1 apps are a **target**, not a description of this folder. See [Roadmap](Roadmap.md).

## 1. Discount calculator — strategy pattern

Folder: [Projects/Discount Calculator](https://github.com/maligujjar2801/AI_Engineering/tree/main/Projects/Discount%20Calculator)

| File | Role |
| --- | --- |
| `discount_calculator.py` | The program. **This** is the file to run |
| `Discount_Strategy_Project_README.md` | Overview, classes, flow, how to extend it |
| `Discount_Strategy_Project_Notes.md` | Line-by-line lesson, about 18 KB |

The README tells you to run `python discount_strategy.py`. That filename is **not** in the folder. Use `discount_calculator.py`.

Classes in the program:

| Class | Job |
| --- | --- |
| `Product` | Name and price, with `__str__` |
| `DiscountStrategy` | Abstract base. Requires `is_applicable` and `apply_discount` |
| `PercentageDiscount` | Percent off, only if the percent is at most 70 |
| `FixedAmountDiscount` | Subtract a fixed amount, with its own applicability rule |
| `PremiumUserDiscount` | A discount that cares about the user tier |
| `DiscountEngine` | Tries every strategy that applies and keeps the lowest price |

Concepts the README names on purpose: abstraction, inheritance, polymorphism, the strategy pattern, open/closed (add a strategy without rewriting the engine), single responsibility.

This is the best project in the repo to re-read after Day 17.

## 2. Personal expense tracker — text menu and a file

Folder: [Projects/Expense Tracker](https://github.com/maligujjar2801/AI_Engineering/tree/main/Projects/Expense%20Tracker)

| File | Role |
| --- | --- |
| `Expense Tracker.py` | The menu program. Run this |
| `Expense.txt` | The saved expenses |
| `Personal Expense Tracker — README.md` | Features and the intended design |
| `Linked list.py` | A separate linked-list exercise, not used by the menu |
| `import tkinter as tk.py` and `import tkinter as tk.txt` | The same short Tkinter sketch, stored twice |
| `tkinter .py` | Another small Tkinter experiment. There is a space before `.py` |

The menu in `Expense Tracker.py` is an infinite loop with six choices. The functions are:

1. `add_expense`
2. `veiw_expenses` (spelled that way in the source)
3. `calculate_total`
4. `search_expenses` by category
5. `delete_expense` by index
6. exit

Records are lines of category, amount, and description in `Expense.txt`. Amounts are printed as `Rs.`.

The README describes a file called `main.py` and a future with JSON, categories, and monthly summaries. `main.py` is not in the folder. Compared with roadmap Project 1, this version still needs edit, dates, a monthly summary, and JSON or CSV. It is an honest first version, not the finished tracker.

## 3. Media catalogue — movies, series, validation

Folder: [Projects/Media Catalogue](https://github.com/maligujjar2801/AI_Engineering/tree/main/Projects/Media%20Catalogue)

| File | Role |
| --- | --- |
| `Media Catalogue.py` | The program |
| `Media Catalogue — README.md` | Classes, validation rules, how to run |
| `media_catalogue_project_notes.md` | Long build log, about 39 KB, written as problem → solution |

The README says to run `python media_catalogue.py`. The real file is `Media Catalogue.py` (capital letters and a space).

Design:

| Type | Role |
| --- | --- |
| `MediaError` | Custom exception. Stores the object that caused the failure, and calls `super()` |
| `Movie` | Title, year, director, duration. Checks empty title, year before 1895, empty director, non-positive duration |
| `TVSeries` | The series type. Inherits shared checks instead of copying them |
| `MediaCatalogue` | Holds the collection |

The notes also teach docstrings vs comments, `.strip()`, `isinstance` vs `type`, and `__str__`. The README’s run example does not match the filename. See [How-to-Run](How-to-Run.md).

## 4. Player interface — freeCodeCamp lab

Folder: [Projects/Player Interface](https://github.com/maligujjar2801/AI_Engineering/tree/main/Projects/Player%20Interface)

| File | Role |
| --- | --- |
| `player_interface.py` | `Player` and `Pawn` |
| `README.md` | Lab objective |
| `Player_Interface_Notes.md` | Twenty short sections, from abstract classes to `extend` vs `append` |

The README says the code is in `main.py`. It is in `player_interface.py`.

What the notes cover:

- why `Player` is an abstract base class
- `@abstractmethod`
- `moves` as coordinate pairs (tuples)
- `path` as the history of positions
- `random.choice` to pick a move
- updating `position`
- `Pawn` calling `super()`, then adding diagonal moves
- overriding `make_move`

Good companion to Day 17 and Day 14.

## 5. Polygon area calculator — freeCodeCamp lab

Folder: [Projects/Polygon Area Calculator](https://github.com/maligujjar2801/AI_Engineering/tree/main/Projects/Polygon%20Area%20Calculator)

| File | Role |
| --- | --- |
| `polygon_area_calcullator.py` | The program. “Calculator” is spelled with an extra `l` |
| `polygon_area_calculator_README.md` | Features, formulas, freeCodeCamp status |
| `polygon_area_calculator_notes.md` | The class design **and** eight mistakes from the first attempt |

`Rectangle` can set width and height, and can compute:

- area (`width * height`)
- perimeter (`2 * (width + height)`)
- diagonal (needs `**` and `math.sqrt`, not `^`)
- a picture made of lines of `*`
- how many times another shape fits inside (`//`)

`Square` inherits from `Rectangle`. Both sides stay equal. The notes list the first-attempt bugs in plain language: wrong perimeter, `^` instead of `**`, printing instead of returning, a bad `super()` call, storing `side` but not updating both width and height in the setters.

This notes file is the model for “write down the mistake” in [How-to-Study](How-to-Study.md).

## 6. To-do list — Tkinter desktop app

Folder: [Projects/To Do List App](https://github.com/maligujjar2801/AI_Engineering/tree/main/Projects/To%20Do%20List%20App)

| File | Role |
| --- | --- |
| `To do List.py` | The app. About 4 KB of GUI code |
| `Python_Tkinter_Todo_App_Detailed_Notes.md` | Very detailed widget notes, about 32 KB |

The window is 500×550, not resizable, titled “My To-Do App”. It uses:

- `tk.Label` for the title
- a `Frame` plus `Entry` for the new task
- `Button` widgets whose `command` is a method reference, not a method call
- a `Listbox` with `selectmode=tk.SINGLE`
- a `Scrollbar` packed on the right with `fill=tk.Y`
- `messagebox` for warnings

The notes explain `pack` vs `grid`, `self`, and why some widgets are stored on `self` and some are not. Read those notes if you have only used `print` so far.

Needs a desktop with Tkinter. See [How-to-Run](How-to-Run.md).

## How the projects line up with the days

| Project | Depends on days |
| --- | --- |
| Expense tracker | 3–6 and 16 (branches, loops, lists, files) |
| Polygon calculator | 11 and 13 (inheritance, methods that return values) |
| Player interface | 14 and 17 (override a method, abstract base) |
| Media catalogue | 11, 13, 16-style validation, custom exceptions |
| Discount calculator | 14 and 17, plus the strategy idea |
| To-do app | 7–8 (a class with methods) and a new library: Tkinter |

## Editor support

[Projects/.vscode/launch.json](https://github.com/maligujjar2801/AI_Engineering/blob/main/Projects/.vscode/launch.json) debugs **the file you have open**, with `debugpy`, in the integrated terminal. It does not point at one special main file.
