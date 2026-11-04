# Roadmap

[Back to the wiki home](Home.md)

The full document is [Python_to_AI_Engineering_Roadmap.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/Python_to_AI_Engineering_Roadmap.md). This page is the map of that file, plus where the repository sits on it. It does not replace the file.

## Destination

The roadmap’s destination is not “finish a course”. It is the ability to design, build, ship, and maintain real AI systems, at the level of strong industry teams. The root README names the same goal.

The roadmap is explicit about one trap: do not spend the whole timeline saying “I’m preparing”. The switch it wants is **learn → build → ship → apply**.

## Where the repo is

**You are in Phase 1.** Days 1–26 cover a large part of “finish Python properly”: foundations, OOP, files, exceptions, advanced functions, comprehensions, hashing, flexible arguments, SQLite, and modules/packages with a unit test.

Still listed inside Phase 1 by the roadmap, and **not finished as repository work** yet:

- testing as a habit beyond the single Day 26 test module
- APIs and JSON as a project, not only as a future topic
- the four Phase 1 projects in their full form (see below)
- Git used as a daily engineering tool, not only as storage

Do not start Phase 5 because the folder list feels long. The roadmap treats computer science, math, and data work as the next multi-month blocks.

## Phase 1 — Finish Python properly

**Estimate in the file:** about 8–10 weeks.

The file’s Python track starts at foundations and keeps going after the basics. It says Python is never fully “finished”, but it should be finished *properly* before machine learning.

**Phase 1 projects the roadmap asks for** (these are targets, not claims that the current `Projects/` folder already is these apps):

| # | Project | What it must include |
| --- | --- | --- |
| 1 | Personal expense tracker | Add, delete, edit, search, categories, dates, totals, monthly summary, save/load JSON or CSV, exceptions |
| 2 | Student management system | Classes, files, JSON, exceptions, search, sort, functions, more than one module |
| 3 | CLI productivity app | Tasks, notes, deadlines, search, delete, update, save, load |
| 4 | API-based application | Call a REST API, process the data, display a result |

The current expense tracker is a real Phase 1 exercise, but it stores lines in `Expense.txt` and has no edit or monthly summary. Treat it as version 0 of Project 1, not the finished project. See [Projects](Projects.md).

## Phase 2 — Computer science

**Estimate:** 2–3 months.

- **Data structures:** arrays/lists, strings, stacks, queues, hash tables, linked lists, trees, BSTs, heaps, graphs, sets
- **Algorithms:** searching, sorting, recursion, two pointers, sliding window, binary search, hashing, tree and graph traversal (BFS, DFS), greedy algorithms, dynamic programming
- **Big-O:** be able to say the time and space of a piece of code. The file lists `O(1)`, `O(log n)`, `O(n)`, `O(n log n)`, `O(n²)`
- **Also named:** operating systems, networking, databases

The warning in the file: this is so you think like an engineer, not so you disappear into contest programming.

Day 23 already starts the hashing idea. `Projects/Expense Tracker/Linked list.py` is a small linked-list sketch. Neither one is Phase 2.

## Phase 3 — Mathematics for AI

**Estimate:** 2–3 months.

Linear algebra, probability, statistics, and calculus. No math notes are in the repo yet.

## Phase 4 — Data science stack

**Estimate:** 1–2 months.

NumPy, Pandas, Matplotlib. Not in the repo yet.

## Phase 5 — Machine learning

**Estimate:** 3–4 months.

Supervised learning, unsupervised learning, model evaluation, feature engineering. The file says the important lesson is not the library API. It also asks for several ML projects. None are in the tree yet.

## Phase 6 — Deep learning

Neural networks and **PyTorch**. Project areas named in the file include computer vision. Not started in the repo.

## Phase 7 — Transformers and modern AI

Transformers, then LLM engineering. The file says not to become “only a prompt engineer”. Not started.

## Phase 8 — AI engineering

The file’s AI-engineering block, expanded again in the calendar below, includes LLMs, embeddings, RAG, vector databases, agents, tool calling, fine-tuning, evaluation, FastAPI, and Docker.

## Phase 9 — Cloud

Named as its own phase. No cloud config is in the repo.

## Phase 10 — Docker and MLOps

Containers and production habits. Not started.

## The 24-month calendar in the file

This is the schedule the roadmap says it would actually use. Months overlap on purpose (months 5–7 start while the previous block’s estimate is still in range).

| When | Focus | Also do |
| --- | --- | --- |
| Months 1–2 | Python engineering: foundations, exceptions, advanced Python, generators, decorators, packages, testing, APIs, JSON, Git | 2–3 serious Python projects |
| Months 3–5 | DSA, SQL, databases, networking, Linux, Git, algorithms | Keep building Python projects |
| Months 5–7 | Linear algebra, probability, statistics, calculus basics, NumPy, Pandas, Matplotlib | Data projects |
| Months 7–11 | scikit-learn: regression, classification, trees, ensembles, clustering, features, evaluation | 3–4 ML projects |
| Months 11–15 | PyTorch, neural nets, CNN, RNN, attention, transformers, vision, NLP | 3–4 projects |
| Months 15–18 | LLMs, embeddings, RAG, vector DB, agents, tool calling, fine-tuning, evaluation, FastAPI, Docker | 2–3 AI systems |
| Months 18–21 | Cloud, MLOps, CI/CD, monitoring, databases, scaling, security, system design | Production work |
| Months 21–24 | DSA and system-design interviews, ML and Python interviews, portfolio, open source, applications | Apply before month 21, not only after it |

## Other sections in the roadmap file

Read these in the original file when you want the full wording:

- learning ratio (how to split time)
- six skill pillars
- a portfolio of about 20 serious projects, plus a smaller set of flagship projects
- open source
- “DSA never stops”
- international-company strategy
- the immediate next move, which the file still illustrates with a “Day 1” foundations block — your repo has already gone far past that illustration

## How to use the roadmap without lying to yourself

Mark a phase done only when the repo contains the projects, not when the notes mention the words. By that rule:

- Phase 1 is **in progress** (strong daily Python, projects still small).
- Phases 2–10 are **not started** as repository work.
