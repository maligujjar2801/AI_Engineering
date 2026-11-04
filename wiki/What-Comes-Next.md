# What comes next

[Back to the wiki home](Home.md) · [Roadmap](Roadmap.md)

Day 26 is the latest folder. The roadmap does not say “start PyTorch”. It says finish Python as an engineering tool, then computer science.

## The next repository work, in order

Do these in the repo. They use only skills that are already in Days 1–26.

### 1. Finish the expense tracker up to the roadmap’s Project 1

You already have add, view, total, search, and delete in [Expense Tracker.py](https://github.com/maligujjar2801/AI_Engineering/blob/main/Projects/Expense%20Tracker/Expense%20Tracker.py).

Still missing, and all of it is Phase 1 Python:

- edit one expense
- a date on each expense
- a monthly total
- save and load **JSON** (or CSV) instead of a hand-split text line
- exceptions for bad amounts and bad menu choices
- more than one module, the way `study_tracker` is split

That single upgrade is more valuable than a new Day 27 about a random topic.

### 2. One package-shaped project

Day 26’s challenges already ask for this. Pick either:

- the student system from the roadmap (classes, search, sort, JSON, tests), or
- a small CLI for tasks and notes

Layout to copy:

```text
project_name/
├── README.md
├── package_name/
│   ├── __init__.py
│   └── __main__.py
└── tests/
    └── test_....py
```

Run it with `python -m package_name` and `python -m unittest discover -s tests -v`, from that project’s folder.

### 3. Then an API program

Roadmap Project 4: call one public read-only HTTP API, check the status, read the JSON, and print a clear result. Use the standard library first (`urllib`) so you do not need a dependency file yet. Handle timeouts and a non-200 status. That is the shape of later AI code that calls a model API.

### 4. Only then open Phase 2

Start a `cs/` or `dsa/` area for stacks, queues, and the linked list you already sketched. Day 23’s hashing notes are the entrance, not the whole phase. Big-O should be written next to each new structure, in your own words.

Leave NumPy, scikit-learn, and PyTorch until the calendar in [Roadmap](Roadmap.md) says so. The root README lists them because they are the destination, not because they are the next commit.

## Habits to start on the next commit

- Add a `.gitignore` for `__pycache__/`, `.pyc`, and virtual environments.
- Name the guide `README.md` in every new day.
- When a README names a command, use the real filename.
- Prefer `day-27/topic_name.py` over spaces and double extensions.
- Write one test for any new project that has logic beyond printing.
- In the day notes, keep one “mistakes I actually made” section. The polygon notes and the Day 21 path lesson are the standard.

## How to extend this wiki

When you add a day or a project:

1. Add a row to [Python-Journey](Python-Journey.md) or a section to [Projects](Projects.md).
2. Add the new idea to [Concepts-Index](Concepts-Index.md).
3. If the run command is not obvious, add it to [How-to-Run](How-to-Run.md).
4. Change the “Where you are” table on [Home](Home.md).
5. Bump the snapshot commit mentioned on the home page.

The long lesson stays in the repository. The wiki stays the map.

## A progress check you can do in ten minutes

- [ ] `python -m study_tracker` works from `python_journey/Day-26`
- [ ] `python -m unittest discover -s tests -v` passes there
- [ ] You can explain `__enter__` / `__exit__` without opening Day 21
- [ ] You can say why a generator is better than a list for a large log
- [ ] You can add a new discount strategy without editing `DiscountEngine`’s loop
- [ ] You can name one thing the expense tracker still cannot do

If those six are true, Phase 1 is in good shape and the JSON expense tracker is the right next build.
