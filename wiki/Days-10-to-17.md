# Days 10 to 17 — object-oriented Python

[Back to the journey index](Python-Journey.md) · [Home](Home.md)

This block is the OOP core: data hiding, inheritance, special methods, polymorphism, a stats project, files, and abstraction.

**Read [Folder-Quirks](Folder-Quirks.md) before Day 10 and Day 11.** The README titles and the code disagree about which day is inheritance and which day is encapsulation.

## Day 10 — encapsulation practice

Folder: [Day-10](https://github.com/maligujjar2801/AI_Engineering/tree/main/python_journey/Day-10)

The README heading says “Inheritance”. The files do not. They are:

| File | Topic in the code |
| --- | --- |
| `public_attributes.py` | Anyone can read and write the attribute |
| `protected_attributes.py` | A single leading underscore, by convention |
| `private_attributes.py` | Double underscore and name mangling |
| `getter.py` | A method that returns the hidden value |
| `setter.py` | A method that checks a new value before storing it |
| `@property.py` | The same idea with `@property` |
| `challenge.py` | A short encapsulation exercise |

There is no inheritance example in this folder. Inheritance notes land in Day 11.

## Day 11 — inheritance notes and encapsulation notes together

Folder: [Day-11](https://github.com/maligujjar2801/AI_Engineering/tree/main/python_journey/Day-11)

The README heading says “Encapsulation”. The folder contains **both** lessons.

Inheritance, in [day10_notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-11/day10_notes.md):

- parent and child classes
- `super()`
- method overriding
- `isinstance()`
- `issubclass()`

Matching scripts: `Inheritance.py`, `inheritance_practice.py`, `overriding.py`.

Encapsulation, in [day11_notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-11/day11_notes.md):

- public, protected, and private attributes
- name mangling
- getters and setters

Matching scripts: the same getter/setter/`@property` set as Day 10, plus a larger `challenge.py`.

Study order that matches the concepts, regardless of the titles:

1. Day 10 scripts (encapsulation mechanics).
2. `Day-11/day11_notes.md` (encapsulation written up).
3. `Day-11/day10_notes.md` (inheritance).
4. `Inheritance.py`, `inheritance_practice.py`, `overriding.py`.

## Day 12 — salary tracker

[README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-12/README.md) · [day12_notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-12/day12_notes.md) · [salary_tracker.py](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-12/salary_tracker.py)

One workshop program instead of many tiny files. It pulls together OOP revision, private attributes, getters, setters, `@property`, and `@setter`. This is the day to re-read if `@property` still feels like syntax instead of a rule for protecting data.

## Day 13 — dunder methods

[README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-13/README.md) · [day13_notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-13/day13_notes.md)

Notes cover `__len__`, `__eq__`, `__add__`, comparison dunders, `NotImplemented`, and operator overloading.

| File | Dunder |
| --- | --- |
| `book_str_len_.py` | `__str__` and `__len__` |
| `student_eq.py` | `__eq__` so two students can be compared with `==` |
| `wallet_add_.py` | `__add__` |
| `reactangle.py` | A rectangle class using the day’s ideas. Spelling in the filename drops an “g” |

## Day 14 — polymorphism

[README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-14/README.md) · [day14_notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-14/day14_notes.md)

The notes define polymorphism and show it through inheritance: one function, several classes, each with its own version of a method.

| File | Shared action |
| --- | --- |
| `Animal_speak.py` | Different animals, a `speak` method |
| `make_sound.py` | Same idea, another example |
| `Vehicle_start.py` | Vehicles that each `start` |
| `employee_work.py` | Employees that each `work` |

## Day 15 — game character stats

[README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-15/README.md) · [day15_notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-15/day15_notes.md) · [game_stats.py](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-15/game_stats.py)

A single character object with:

- a constructor
- encapsulation
- a read-only property
- checked properties for health, mana, and level
- a level-up method
- `__str__`

Also in the folder: `revision.py` and a tiny `example_test.py`. This is a project day, not a syntax day. It is the bridge to the media catalogue and the discount engine in [Projects](Projects.md).

## Day 16 — file handling

[README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-16/README.md) · [Day_16_File_Handling_Notes (1).md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-16/Day_16_File_Handling_Notes%20(1).md)

The notes file is long (about 23 KB) and the filename still has ` (1)` from a download or duplicate. It is the real notes file.

Scripts, named after the method they practise:

| File | Operation |
| --- | --- |
| `create_file.py` | Create a file |
| `.write().py` | Write text |
| `.read().py` | Read text |
| `append_file.py` | Append |
| `.strip().py` | Strip whitespace |
| `.replace().py` | Replace text |
| `exception_handling.py` | What to do when the file is missing or the mode is wrong |
| `functions in file handling.py` | Helpers around files |
| `attributes.py`, `example.py` | Short extra examples |

Text samples checked in next to the scripts: `aligi.txt`, `new.txt`.

Run these from `Day-16/`. Several of them use a relative filename, so running them from the repository root will look in the wrong folder.

A later revision of the same idea is [rev-1/file_rev.py](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/rev-1/file_rev.py).

## Day 17 — abstraction

[Day-17_README.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-17/Day-17_README.md) · [Day-17_Abstraction_Notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-17/Day-17_Abstraction_Notes.md)

There is no file named `README.md` in this folder. Open `Day-17_README.md`.

The notes are a full lesson:

- what abstraction is, and how it differs from encapsulation, inheritance, and polymorphism
- `ABC` and `@abstractmethod`
- why a normal parent class is not enough when you need a blueprint
- what happens if a child does not implement the abstract method
- animals, shapes, payments, and notifications as examples

| File | Example |
| --- | --- |
| `abstract_animal.py` | Animal base, concrete animals |
| `abstraction.py` | The main day’s program |
| `Shapes.py` | Shape hierarchy |
| `payment_system.py` | Payment methods behind one base |
| `notification_system.py` | Notification channels |
| `nootification_system.py` | Same idea, filename typo (“nootification”) |

After this day, the discount calculator and the player interface in `Projects/` should look familiar: both use `ABC`.

## OOP map for this block

```text
class and object          Day 7–8
hide the data             Day 10–12
inherit and override      Day 11
special methods           Day 13
one interface, many forms Day 14–15
save the data             Day 16
force a blueprint         Day 17
```
