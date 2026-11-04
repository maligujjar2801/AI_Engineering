# Repository map

[Back to the wiki home](Home.md)

Everything below is on the `main` branch. Paths are relative to the repository root.

## Root

| Path | Role |
| --- | --- |
| [README.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/README.md) | Public introduction: why the repo exists, the company-level goal, and the phase list from Python to production AI |
| [Python_to_AI_Engineering_Roadmap.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/Python_to_AI_Engineering_Roadmap.md) | The working curriculum. About 24 KB. Phases, project ideas, a two-year calendar, and the day-note template |
| [.vscode/settings.json](https://github.com/maligujjar2801/AI_Engineering/blob/main/.vscode/settings.json) | Editor settings. Points the Python environment at `Projects/`, turns on unittest discovery (`*test.py`), and turns pytest off |

## `python_journey/`

The daily log. [Its README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/README.md) states the goal (Python → DSA → AI engineering), the learning philosophy, and an 8-step study cycle. The latest session it names is **Day 26 — modules and packages**.

| Path | What it is |
| --- | --- |
| `Day-01/` … `Day-26/` | One study day each. See [Python-Journey](Python-Journey.md) |
| `rev-1/file_rev.py` | A short file-handling revision script, outside the numbered days |
| `.gitattributes` | Line-ending attributes for this folder |

A typical early day is a handful of scripts plus `dayN_notes.md`. From Day 16 onward the notes get much longer, and some days add `practice/`, `mini project/`, or a small package.

There is **no** `Day-27` yet.

## `Projects/`

Standalone programs that reuse earlier lessons. They are not numbered as days.

| Folder | Main idea | Actual program file |
| --- | --- | --- |
| `Discount Calculator/` | Strategy pattern for discounts | `discount_calculator.py` |
| `Expense Tracker/` | Menu-driven expense list saved to a text file | `Expense Tracker.py` |
| `Media Catalogue/` | Movies and TV series with validation and a custom error | `Media Catalogue.py` |
| `Player Interface/` | Abstract `Player` and a `Pawn` (freeCodeCamp lab) | `player_interface.py` |
| `Polygon Area Calculator/` | `Rectangle` and `Square` (freeCodeCamp lab) | `polygon_area_calcullator.py` |
| `To Do List App/` | Tkinter desktop to-do list | `To do List.py` |

`Projects/.vscode/launch.json` is a VS Code debug config: “Python Debugger: Current File”, using the integrated terminal.

Details, class lists, and run commands: [Projects](Projects.md) and [How-to-Run](How-to-Run.md).

## What is not in the repository

These are named in the roadmap or the journey README, but there is no folder for them yet:

- NumPy, Pandas, Matplotlib
- scikit-learn or any trained model
- PyTorch, transformers, or LLM apps
- FastAPI, Docker, cloud configs, or CI workflows
- A root `requirements.txt` or `pyproject.toml`
- SQL beyond the Day 25 SQLite scripts (no separate database-course folder)

## Counts

From the git tree at `8bf809c`:

- 280 tree entries
- 51 directories
- 229 files
- Largest lesson notes include Day 18 (~40 KB), Day 23 (~41 KB), the media-catalogue notes (~39 KB), and the Tkinter to-do notes (~32 KB)

## Languages and tools the code actually uses

- Python (local bytecode in `__pycache__` was produced by **CPython 3.14**)
- Standard library: `abc`, `sqlite3`, `pathlib`-style file I/O, `unittest`, `contextlib`, `random`
- Tkinter for the to-do app and the small Tkinter sketches inside the expense-tracker folder
- Git and VS Code, as named in the journey README
- No third-party packages are imported by the projects reviewed for this wiki
