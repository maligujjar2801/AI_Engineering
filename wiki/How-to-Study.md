# How to study with this repository

[Back to the wiki home](Home.md)

The repository is a diary of learning, not a library you import. The useful way to read a day is to **re-do** it, not only to scroll the notes.

## The cycle

From [python_journey/README.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/README.md):

1. **Learn** — read the concept and its syntax.
2. **Understand** — trace an example and predict the output before you run it.
3. **Practise** — change something small and solve a short exercise without looking.
4. **Build** — put the concept inside a tiny program that does a real job.
5. **Test** — try normal cases and edge cases. If the result surprises you, find out why.
6. **Document** — write the mental model, the mistakes, and one good example in Markdown.
7. **Review** — explain the solution in your own words.
8. **Version** — commit a coherent change.

Short form used in that same README: **Understand → practise → build → test → document → commit → review.**

## Suggested order inside one day

For a day that has both notes and code:

1. Read that day’s README (the goal and the file list).
2. Read the notes once, slowly. Stop at each example.
3. Open the matching `.py` file. Predict, then run it from that day’s folder. See [How-to-Run](How-to-Run.md).
4. Change one value or one condition and run it again.
5. Only then look at the “common mistakes” section. Those sections are part of the lesson, especially Days 16–24 and the polygon-area notes.

Early days (1–8) are shorter. Days 18, 19, 21, 22, 23, and 26 are written as full lessons with objectives, mistakes, and a checklist. Treat those as the pattern for future days.

## The day template the roadmap wants from here on

[The roadmap](https://github.com/maligujjar2801/AI_Engineering/blob/main/Python_to_AI_Engineering_Roadmap.md) asks future days to include, in order:

1. What is it?
2. Why does it exist?
3. How does it work?
4. Under the hood
5. Syntax
6. Basic examples
7. Intermediate examples
8. Prediction questions
9. Common mistakes
10. Professional usage
11. Exercises
12. Challenge
13. Mini project
14. Code review
15. Notes
16. GitHub update
17. Revision

Day 23 (hashing) and Day 26 (modules) are the closest existing examples of that longer shape.

## Rules this repo is already following

- Write the code yourself. The journey README says understanding beats memorising.
- Keep notes next to the code, in the same day folder.
- Prefer small programs with a visible result (a calculator, a grade check, a salary tracker) over empty syntax drills.
- When a concept returns, it returns inside a slightly larger program: lists → student management (Day 6), classes → budget app (Days 8–9), encapsulation → salary tracker (Day 12), generators → log stream processor (Day 19), context managers → log file (Day 21), packages → `study_tracker` (Day 26).

## What “done” means for a day

A day is in good shape when all of these are true:

- The README names the topic in the first heading.
- Every script in the folder runs, or the README says it is a fragment.
- Notes mention at least one mistake that actually happened.
- The commit message says what was learned, not only “update”.

Several older folders do not meet the first bullet. That is recorded in [Folder-Quirks](Folder-Quirks.md) so it does not look like a missing lesson.

## How this wiki fits

- Use [Python-Journey](Python-Journey.md) when you forget which day taught a topic.
- Use [Concepts-Index](Concepts-Index.md) when you remember the topic but not the folder.
- Use [Roadmap](Roadmap.md) when you want to know whether you are allowed to jump to machine learning yet. The roadmap’s answer is: not until the Phase 1 projects and the rest of core Python are solid.
