# AI Engineering Wiki

This is the dedicated wiki for [maligujjar2801/AI_Engineering](https://github.com/maligujjar2801/AI_Engineering).

The same pages are published on the [GitHub wiki](https://github.com/maligujjar2801/AI_Engineering/wiki). This folder is the copy that lives next to the code.

It was written by reading the whole repository: **229 files** across the root roadmap, `python_journey/` (Days 1–26 plus a revision folder), and six projects under `Projects/`.

**Documented snapshot:** commit [`8bf809c`](https://github.com/maligujjar2801/AI_Engineering/commit/8bf809c013123dc43cac1ef119ee08425fc4491a) on `main` (4 November 2026).

The code and the long lesson notes stay in the repository. This wiki is the map: what each folder is for, what you have already learned, how to run it, and what the roadmap says comes next.

## What this repository is

A public learning record of one path:

```text
Python engineering
  → computer science
  → mathematics
  → data science
  → machine learning
  → deep learning
  → transformers and LLMs
  → production AI systems
```

Right now the repository is still inside **Phase 1: finish Python properly**. Days 1–26 are real, checked-in work. Machine learning code is not in the repo yet. That is expected. The roadmap file says Python, projects, and engineering habits come first.

## Where you are

| Area | Status in this snapshot |
| --- | --- |
| Python foundations (Days 1–6) | Done: types, decisions, loops, functions, lists |
| Object-oriented Python (Days 7–17) | Done: classes through abstraction, plus three OOP labs |
| Advanced Python (Days 18–26) | Done: functions, generators, decorators, comprehensions, hashing, `*args`/`**kwargs`, SQLite, modules and packages |
| Phase 1 projects in `Projects/` | Six small projects are in the repo. The roadmap’s larger apps (JSON expense tracker, modular student system, CLI productivity app, API app) are still ahead |
| Computer science, math, data, ML, DL, LLMs, MLOps | Described in the roadmap only. No course folders yet |

## Start here

1. [How-to-Study](How-to-Study.md) — the daily cycle this repo is built around.
2. [Python-Journey](Python-Journey.md) — every day, with the topic and the files that belong to it.
3. [Projects](Projects.md) — what each project actually teaches, and the real filename to run.
4. [How-to-Run](How-to-Run.md) — commands, working directories, and which programs need a desktop.
5. [Roadmap](Roadmap.md) — the long path after Day 26, in the order the roadmap file gives it.
6. [Folder-Quirks](Folder-Quirks.md) — filenames and titles that do not match, so you do not hunt for missing files.

## Wiki pages

| Page | What it answers |
| --- | --- |
| [Repository-Map](Repository-Map.md) | Every top-level area and what lives in it |
| [How-to-Study](How-to-Study.md) | Learn → understand → practise → build → test → document → commit → review |
| [Roadmap](Roadmap.md) | Phases 1–10 and the 24-month outline |
| [Python-Journey](Python-Journey.md) | Index of Days 1–26 and `rev-1` |
| [Days-01-to-09](Days-01-to-09.md) | Foundations through the budget app |
| [Days-10-to-17](Days-10-to-17.md) | Inheritance, encapsulation, dunder methods, polymorphism, abstraction |
| [Days-18-to-26](Days-18-to-26.md) | Advanced functions through packages and tests |
| [Projects](Projects.md) | Discount engine, expense tracker, media catalogue, player, polygons, to-do app |
| [Concepts-Index](Concepts-Index.md) | Topic → day or project |
| [How-to-Run](How-to-Run.md) | How to execute the programs that are actually in the tree |
| [Folder-Quirks](Folder-Quirks.md) | Mismatched titles, typos, and generated files |
| [What-Comes-Next](What-Comes-Next.md) | The next honest step after Day 26 |

## Repository shape

```text
AI_Engineering/
├── README.md
├── Python_to_AI_Engineering_Roadmap.md
├── .vscode/settings.json
├── python_journey/
│   ├── README.md
│   ├── Day-01/ … Day-26/
│   └── rev-1/
└── Projects/
    ├── Discount Calculator/
    ├── Expense Tracker/
    ├── Media Catalogue/
    ├── Player Interface/
    ├── Polygon Area Calculator/
    └── To Do List App/
```

There is no `requirements.txt`, no virtual environment, and no automated test suite at the repository root. Almost everything runs with the Python standard library. The two Tkinter programs need a desktop. Day 26 is the first day with a real `unittest` module.

## How the notes are meant to be used

Later days are not just code dumps. From about Day 18 onward, a day usually contains:

- a README that states the goal
- a long notes file (concept, syntax, mistakes, checklist)
- small practice scripts
- sometimes a mini project
- sometimes challenges you are supposed to solve yourself

The roadmap’s preferred day template is: what it is, why it exists, how it works, under the hood, syntax, examples, prediction questions, mistakes, professional use, exercises, a challenge, a mini project, a review, notes, and a GitHub update. Newer days follow that shape more closely than Days 1–8.

Source of truth for the long-term plan: [Python_to_AI_Engineering_Roadmap.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/Python_to_AI_Engineering_Roadmap.md).
