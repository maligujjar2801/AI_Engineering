# Days 1 to 9 — foundations through a first OOP app

[Back to the journey index](Python-Journey.md) · [Home](Home.md)

These nine days go from “what is a variable?” to a budget program built from classes.

## Day 1 — first programs

Notes: [day1_notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-01/day1_notes.md)

The notes answer: what Python is, why it is called interpreted, `int` vs `float`, list vs tuple, variables, strings, slicing, indexing, and dynamic typing.

| File | Idea |
| --- | --- |
| `greeting.py` | Input and a greeting |
| `calculator.py` | Arithmetic on user input |
| `BMI finder.py` | A formula with height and weight |
| `temperature.py` | Convert a temperature |
| `percentage.py` | Percentage from marks |
| `even_or_odd.py` | A first decision |

There is no `README.md` in Day 1. The notes file is the guide.

## Day 2 — variables, types, operators

Notes: [day2_notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-02/day2_notes.md)

Covers declaring variables, integers, floats, strings, booleans, and arithmetic operators. The notes record a real error: you cannot assign to `True`.

| File | Idea |
| --- | --- |
| `personal_introduction.py` | Several variables printed together |
| `rectangle_calculator.py` | Area from length and width |
| `average_calculator.py` | Mean of several numbers |
| `currency_converter.py` | Multiply by a rate |
| `time_convertor.py` | Convert a time unit |

## Day 3 — decisions

[README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-03/README.md) · [day3_notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-03/day3_notes.md)

Topics: `if`, `elif`, `else`, comparison operators, booleans, indentation.

| File | Checks |
| --- | --- |
| `positive_negative.py` | Sign of a number |
| `voting.py` | Age limit |
| `largest_number.py` | Biggest of several values |
| `even_or_odd.py` | Parity, again, now with a branch |
| `pass_fail.py` | A cutoff |
| `grade_calculator.py` | A ladder of grade boundaries. This is the longest Day 3 program |

## Day 4 — loops

[README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-04/README.md) · [day4_notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-04/day4_notes.md)

Topics: `for`, `while`, `range`, loop variables, infinite loops, `break`, `continue`.

| File | Idea |
| --- | --- |
| `print_numbers.py` | Count with a loop |
| `even_numbers.py` | Step through evens |
| `countdown.py` | Count down |
| `multiplication_table.py` | A table for one number |
| `sum_numbers.py` | Accumulate a total |
| `guessing_game.py` | Loop until the guess is right |

## Day 5 — functions

[README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-05/README.md) · [day5_notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-05/day5_notes.md)

The README is a question-and-answer lesson: what a function is, why it exists, how you define and call it, parameters vs arguments, `return`, and why `return` is not the same as `print`.

| File | Function shape |
| --- | --- |
| `greetings.py` | A function with a name parameter |
| `addition.py` | Returns a sum |
| `even_or_odd.py` | Returns a label |
| `largest_number.py` | Returns the max of inputs |
| `percentage_calculator.py` | Returns a percentage |

`README.md` and `day5_notes.md` are the same size in this snapshot. Read one, then the scripts.

## Day 6 — lists

[README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-06/README.md) · [day6_notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-06/day6_notes.md)

Topics named in the README: creating lists, indexing, negative indexes, slicing, item assignment, `append` / `insert` / `extend`, `remove` / `pop` / `del` / `clear`, `sort` / `reverse` / `count` / `index` / `copy`, `len`, `in` / `not in`, loops over lists, nested lists.

| File | Idea |
| --- | --- |
| `favorite_fruit.py` | A small list |
| `student_marks.py` | A list of marks |
| `max_or_min_num.py` | Max or min of a list |
| `remove_subject.py` | Remove an item |
| `car_info.py` | A record made of list data |
| `student_management.py` | Add and show students. The biggest Day 6 program |

## Day 7 — classes and objects

[README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-07/README.md) · [day7_notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-07/day7_notes.md)

First real OOP day.

| File | Class idea |
| --- | --- |
| `student.py` | A minimal class |
| `student_info.py` | Attributes set from arguments |
| `student_methods.py` | Methods that use `self` |
| `car_info.py` | Another small class (a copy of the Day 6 filename, new contents) |
| `ractangle.py` | Rectangle with methods. Filename spells “rectangle” wrong |
| `bank_account.py` | Deposit and withdraw on an object |

## Day 8 — class variables, class methods, static methods

[README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-08/README.md) · [day8_notes.md](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-08/day8_notes.md)

README topics: class variables vs instance variables, `@classmethod`, `@staticmethod`, `__str__`, objects that use other objects (composition).

| File | Role |
| --- | --- |
| `class_method.py` | `@classmethod` |
| `student_methods.py` | Carried forward from Day 7 |
| `employee.py` | A small employee class |
| `book.py` | `__str__` on a book |
| `calculator.py` | `@staticmethod` style utilities |
| `test.py` | Experiments for the day |
| `budget_app.py` | Larger program. The same file also sits in Day 9 |

## Day 9 — budget app

[README](https://github.com/maligujjar2801/AI_Engineering/blob/main/python_journey/Day-09/README.md)

The README title says “Day 6 – Build a Budget App”. The folder is Day 9. Trust the folder and the features list, not the day number in the title. See [Folder-Quirks](Folder-Quirks.md).

The notes file in this folder is `day6_notes.md`, and it is an OOP revision: class, object, instance attributes, nested loops, string formatting, a list of dictionaries, and percentage calculation. It is **not** a copy of Day 6’s list notes (different file, different size).

`budget_app.py` is the program. Features called out in the README: tracking amounts, using classes, and printing a summary. Run it from `python_journey/Day-09/`.

## What you can do after Day 9

You can:

- write a function that returns a value
- branch and loop
- store a list and change it
- define a class with methods
- use a class variable and a class method
- build a small menu-style money program

You have not yet, inside this range, done inheritance properly in its own folder, properties, or file persistence. Those start at Day 10 and Day 16.
