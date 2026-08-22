# Media Catalogue Project — Complete Notes

## 1. Project Overview

This project builds a small **Media Catalogue** using Object-Oriented Programming (OOP) in Python.

The catalogue can store:

- Movies
- TV series

Each movie contains:

- Title
- Release year
- Director
- Duration

Each TV series contains all the movie information plus:

- Number of seasons
- Total number of episodes

The program also performs:

- Input validation
- Custom error handling
- Inheritance
- Method overriding
- Polymorphism
- Object filtering
- Catalogue management
- Formatted output
- Documentation using docstrings

---

# 2. Project Structure

The project contains four important classes:

```text
MediaError
    ↓
Custom exception for catalogue-related errors

Movie
    ↓
Parent/base class for common media information

TVSeries
    ↓
Child/subclass of Movie

MediaCatalogue
    ↓
Stores and manages Movie and TVSeries objects
```

A simplified relationship is:

```text
                Exception
                    ↑
               MediaError


                 Movie
                   ↑
               TVSeries


             MediaCatalogue
                   |
                   ↓
         stores Movie/TVSeries objects
```

---

# 3. Problem → Solution #1: Creating a Custom Error

## Problem

Python already provides built-in exceptions such as:

```python
ValueError
TypeError
FileNotFoundError
```

However, our application has a specific error:

> Someone may try to add an object that is not a movie or TV series to the catalogue.

A normal `ValueError` does not clearly describe this application-specific situation.

## Solution

A custom exception was created:

```python
class MediaError(Exception):
    """Custom exception for media-related errors."""

    def __init__(self, message, obj):
        super().__init__(message)
        self.obj = obj
```

This allows the program to raise an error specifically related to media operations.

---

# 4. New Concept — Custom Exceptions

A **custom exception** is an exception created by the programmer for a specific application.

Your custom exception is:

```python
MediaError
```

It inherits from:

```python
Exception
```

So the relationship is:

```text
Exception
    ↓
MediaError
```

Because `MediaError` inherits from `Exception`, it can be used with:

```python
raise MediaError(...)
```

and:

```python
except MediaError as e:
```

This makes error handling more organized and meaningful.

---

# 5. Problem → Solution #2: Storing the Object That Caused the Error

## Problem

Sometimes the error message alone is not enough.

We may also want to know:

> Which object caused the error?

## Solution

The constructor stores both the message and the problematic object:

```python
def __init__(self, message, obj):
    super().__init__(message)
    self.obj = obj
```

So the exception stores:

```text
message → what went wrong
obj     → what caused the problem
```

For example:

```python
raise MediaError(
    'Only Movie or TVSeries instances can be added',
    media_item
)
```

Later, the object can be inspected:

```python
print(e.obj)
print(type(e.obj))
```

This gives more useful debugging information.

---

# 6. New Concept — `super()` in Exceptions

Inside:

```python
def __init__(self, message, obj):
    super().__init__(message)
```

`super()` calls the parent class constructor.

Since:

```python
class MediaError(Exception):
```

the parent class is `Exception`.

Therefore:

```python
super().__init__(message)
```

passes the error message to Python's built-in `Exception` class.

---

# 7. Problem → Solution #3: Creating the Parent Class

## Problem

Movies need common information.

Every movie should have:

- Title
- Year
- Director
- Duration

Instead of keeping all this information separately, a class is created as a reusable blueprint.

## Solution

```python
class Movie:
    """Parent class representing a movie."""

    def __init__(self, title, year, director, duration):
```

The class defines what a movie object should contain.

Example:

```python
movie1 = Movie('The Matrix', 1999, 'The Wachowskis', 136)
```

The resulting object contains:

```text
movie1
 ├── title
 ├── year
 ├── director
 └── duration
```

---

# 8. New Concept — Docstrings

One important new concept used in this project is the **docstring**.

Example:

```python
class Movie:
    """Parent class representing a movie."""
```

This text:

```python
"""Parent class representing a movie."""
```

is called a **docstring**.

## What is a docstring?

A docstring is documentation written inside a:

- Class
- Function
- Method
- Module

It describes what that piece of code does.

---

# 9. Docstring vs Comment

A comment:

```python
# Check if title is empty
```

is mainly a note for programmers reading the code.

A docstring:

```python
"""Parent class representing a movie."""
```

is official documentation associated with the class or function.

Docstrings can be accessed by Python:

```python
print(Movie.__doc__)
```

You can also use:

```python
help(Movie)
```

to view documentation.

## Why use docstrings?

Docstrings make code:

- Easier to understand
- Easier to maintain
- Easier to document
- Easier to use with documentation tools

---

# 10. Problem → Solution #4: Validating the Title

## Problem

A movie without a title should not be accepted.

For example:

```python
Movie('', 1999, 'Director', 120)
```

is invalid.

Even this should also be rejected:

```python
Movie('     ', 1999, 'Director', 120)
```

because it contains only spaces.

## Solution

```python
if not title.strip():
    raise ValueError('Title cannot be empty')
```

---

# 11. New Concept — `.strip()`

The `strip()` method removes whitespace from the beginning and end of a string.

Example:

```python
'   Matrix   '.strip()
```

becomes:

```text
Matrix
```

And:

```python
'     '.strip()
```

becomes:

```text
''
```

Therefore:

```python
if not title.strip():
```

detects:

- Empty strings
- Strings containing only spaces

This is a useful validation technique.

---

# 12. New Concept — Input Validation

**Input validation** means checking whether data follows the rules before the program accepts it.

Your constructor validates:

```text
title
year
director
duration
```

Validation is important because invalid data is rejected as early as possible.

Instead of creating an invalid object and discovering the problem later, the constructor stops the process immediately.

---

# 13. Problem → Solution #5: Validating the Year

## Problem

The project defines a minimum release year:

```text
1895
```

So a movie should not have a release year before that.

## Solution

```python
if year < 1895:
    raise ValueError('Year must be 1895 or later')
```

For example:

```python
Movie('Test', 1800, 'Director', 100)
```

raises:

```text
ValueError
```

---

# 14. Problem → Solution #6: Validating the Director

## Problem

Every movie should have a director.

This should not be allowed:

```python
Movie('Matrix', 1999, '', 136)
```

## Solution

```python
if not director.strip():
    raise ValueError('Director cannot be empty')
```

Again, `.strip()` ensures that whitespace-only input is rejected.

---

# 15. Problem → Solution #7: Validating Duration

## Problem

A movie cannot have zero or negative duration.

Invalid examples:

```text
0 minutes
-20 minutes
```

## Solution

```python
if duration <= 0:
    raise ValueError('Duration must be positive')
```

The rule becomes:

```text
duration > 0
```

---

# 16. Storing Validated Data

Once all validation succeeds, the object stores its data:

```python
self.title = title
self.year = year
self.director = director
self.duration = duration
```

These are **instance attributes**.

For example:

```python
movie1.title
```

returns:

```text
The Matrix
```

and:

```python
movie1.year
```

returns:

```text
1999
```

---

# 17. Problem → Solution #8: Making Objects Easy to Print

## Problem

Suppose we write:

```python
print(movie1)
```

Python needs to know how the object should be displayed.

Without a custom representation, the output is not very useful.

## Solution

You created:

```python
def __str__(self):
    return f'{self.title} ({self.year}) - {self.duration} min, {self.director}'
```

---

# 18. New Concept — `__str__()`

`__str__()` is a Python **special method**.

It defines the human-readable string representation of an object.

Therefore:

```python
print(movie1)
```

automatically uses:

```python
movie1.__str__()
```

Example output:

```text
The Matrix (1999) - 136 min, The Wachowskis
```

This makes the object much easier to read.

---

# 19. Problem → Solution #9: Avoiding Duplicate Code with Inheritance

## Problem

A TV series also needs:

- Title
- Year
- Director
- Duration

It would be inefficient to copy all the movie code into another unrelated class.

## Solution

The project uses inheritance:

```python
class TVSeries(Movie):
```

This means:

```text
TVSeries IS-A Movie
```

Conceptually:

```text
Movie
  ↑
TVSeries
```

`TVSeries` is the child class and `Movie` is the parent class.

---

# 20. New Concept — Inheritance

**Inheritance** allows a child class to reuse functionality from a parent class.

Parent/base/superclass:

```python
class Movie:
```

Child/subclass:

```python
class TVSeries(Movie):
```

Because `TVSeries` inherits from `Movie`, it can use inherited functionality from the parent.

This reduces code duplication.

---

# 21. Problem → Solution #10: Reusing the Parent Constructor

## Problem

The TV series needs the same common movie information.

Instead of repeating:

```python
self.title = title
self.year = year
self.director = director
self.duration = duration
```

the child class can reuse the parent constructor.

## Solution

```python
super().__init__(title, year, director, duration)
```

This calls the parent `Movie.__init__()`.

The parent then handles:

```text
Title validation
Year validation
Director validation
Duration validation
```

The child only handles TV-specific information.

This is a major advantage of inheritance.

---

# 22. New Concept — `super()`

`super()` lets a child class access functionality from its parent class.

In:

```python
class TVSeries(Movie):

    def __init__(self, title, year, director, duration, seasons, total_episodes):
        super().__init__(title, year, director, duration)
```

the statement:

```python
super().__init__(...)
```

means:

> Run the parent class constructor.

So the parent performs all shared validation and initialization.

---

# 23. Problem → Solution #11: Adding TV-Series-Specific Data

## Problem

Movies do not need:

- Number of seasons
- Total episodes

but a TV series does.

## Solution

The TV series constructor includes:

```python
def __init__(
    self,
    title,
    year,
    director,
    duration,
    seasons,
    total_episodes
):
```

Then it validates the new values.

---

# 24. Validating Seasons

```python
if seasons < 1:
    raise ValueError('Seasons must be 1 or greater')
```

This prevents:

```text
0 seasons
-1 seasons
```

The rule becomes:

```text
seasons >= 1
```

---

# 25. Validating Total Episodes

```python
if total_episodes < 1:
    raise ValueError('Total episodes must be 1 or greater')
```

This prevents:

```text
0 episodes
negative episodes
```

The rule becomes:

```text
total_episodes >= 1
```

---

# 26. Storing TV-Series Data

After validation:

```python
self.seasons = seasons
self.total_episodes = total_episodes
```

Now the object contains both inherited and new information:

```text
TVSeries
 ├── title
 ├── year
 ├── director
 ├── duration
 ├── seasons
 └── total_episodes
```

---

# 27. Problem → Solution #12: Giving TV Series Their Own Output

## Problem

A TV series should not be displayed exactly like a movie.

We also need to show:

- Seasons
- Episodes
- Average duration

## Solution

The child class defines its own `__str__()`:

```python
def __str__(self):
    return f'{self.title} ({self.year}) - {self.seasons} seasons, {self.total_episodes} episodes, {self.duration} min avg, {self.director}'
```

---

# 28. New Concept — Method Overriding

A child class can provide its own version of a method inherited from the parent.

This is called **method overriding**.

Parent:

```python
Movie.__str__()
```

Child:

```python
TVSeries.__str__()
```

Therefore:

```python
print(movie1)
```

uses the Movie implementation.

While:

```python
print(series1)
```

uses the TVSeries implementation.

---

# 29. New Concept — Polymorphism

**Polymorphism** means that the same interface can behave differently depending on the object.

Both objects respond to:

```python
__str__()
```

but produce different output.

```text
Movie     → movie format
TVSeries  → TV-series format
```

This is an example of polymorphism through method overriding.

---

# 30. Problem → Solution #13: Creating the Catalogue

## Problem

We now have media objects, but we need somewhere to store them.

## Solution

A catalogue class is created:

```python
class MediaCatalogue:
    """A catalogue that can store different types of media items."""

    def __init__(self):
        self.items = []
```

The catalogue contains one list:

```python
self.items
```

This list stores media objects.

Example:

```text
self.items

[
    Movie object,
    Movie object,
    TVSeries object,
    TVSeries object
]
```

---

# 31. Problem → Solution #14: Adding Media Safely

## Problem

The catalogue should only contain valid media objects.

This should work:

```python
catalogue.add(movie1)
catalogue.add(series1)
```

But this should not:

```python
catalogue.add(10)
```

or:

```python
catalogue.add("The Matrix")
```

## Solution

```python
def add(self, media_item):
    if not isinstance(media_item, Movie):
        raise MediaError(
            'Only Movie or TVSeries instances can be added',
            media_item
        )
    self.items.append(media_item)
```

This makes the catalogue responsible for protecting its own data.

---

# 32. New Concept — `isinstance()`

The expression:

```python
isinstance(media_item, Movie)
```

asks:

> Is this object an instance of `Movie` or a subclass of `Movie`?

Because:

```python
class TVSeries(Movie):
```

is an inheritance relationship,

```python
isinstance(series1, Movie)
```

returns:

```text
True
```

Therefore the catalogue accepts both:

```text
Movie
TVSeries
```

---

# 33. `isinstance()` vs `type()`

This project uses both concepts.

## `isinstance()`

```python
isinstance(series1, Movie)
```

returns:

```text
True
```

because `TVSeries` inherits from `Movie`.

## `type()`

```python
type(series1) is Movie
```

returns:

```text
False
```

because the exact class of `series1` is:

```text
TVSeries
```

This difference is very important.

---

# 34. Problem → Solution #15: Getting Only Movies

## Problem

The catalogue contains different types of media.

Sometimes we need only movie objects.

## Solution

```python
def get_movies(self):
    return [item for item in self.items if type(item) is Movie]
```

This filters the catalogue and returns exact `Movie` objects.

---

# 35. New Concept — List Comprehension

This:

```python
[item for item in self.items if type(item) is Movie]
```

is a **list comprehension**.

It is equivalent to:

```python
result = []

for item in self.items:
    if type(item) is Movie:
        result.append(item)
```

List comprehensions provide a compact way to create filtered lists.

---

# 36. Why `type(item) is Movie` Instead of `isinstance()`?

This is an important design detail.

If you wrote:

```python
isinstance(item, Movie)
```

then TVSeries objects would also be included because:

```text
TVSeries is a subclass of Movie
```

But `get_movies()` is supposed to return **actual movies only**.

Therefore:

```python
type(item) is Movie
```

means:

> The object's exact class must be `Movie`.

This excludes `TVSeries`.

---

# 37. Problem → Solution #16: Getting Only TV Series

## Problem

We also need a way to retrieve only TV series.

## Solution

```python
def get_tv_series(self):
    return [item for item in self.items if isinstance(item, TVSeries)]
```

Since we want `TVSeries` objects and possible subclasses of `TVSeries`, `isinstance()` is appropriate here.

---

# 38. Problem → Solution #17: Handling an Empty Catalogue

## Problem

What should happen when the catalogue contains nothing?

A clear message is better than displaying an empty block.

## Solution

```python
if not self.items:
    return 'Media Catalogue (empty)'
```

An empty list is considered `False` in Python.

Therefore:

```python
if not self.items:
```

means:

> If there are no items in the catalogue...

---

# 39. Problem → Solution #18: Separating Movies and Series

When the catalogue is not empty:

```python
movies = self.get_movies()
series = self.get_tv_series()
```

Now we have:

```text
movies → all exact Movie objects
series → all TVSeries objects
```

This lets the catalogue display the two categories separately.

---

# 40. New Concept — `len()`

The code uses:

```python
len(self.items)
```

`len()` returns the number of elements in a collection.

If:

```python
self.items = [movie1, movie2, series1, series2]
```

then:

```python
len(self.items)
```

returns:

```text
4
```

---

# 41. Problem → Solution #19: Creating the Catalogue Header

You build the output using:

```python
result = f'Media Catalogue ({len(self.items)} items):\n\n'
```

This creates a readable header such as:

```text
Media Catalogue (4 items):
```

The `\n` characters create new lines.

---

# 42. Problem → Solution #20: Numbering the Movies

The project uses:

```python
for i, movie in enumerate(movies, 1):
    result += f'{i}. {movie}\n'
```

This provides:

```text
1. First movie
2. Second movie
3. Third movie
```

instead of starting from zero.

---

# 43. New Concept — `enumerate()`

Normally, a loop gives values:

```python
for movie in movies:
```

`enumerate()` gives both:

- index
- value

Example:

```python
for i, movie in enumerate(movies, 1):
```

The `1` means numbering starts at 1.

Conceptually:

```text
1 → first movie
2 → second movie
3 → third movie
```

Without `enumerate()`, you would need to manage the counter manually.

---

# 44. New Concept — f-Strings

The project uses f-strings repeatedly:

```python
f'{self.title} ({self.year})'
```

f-strings allow variables and expressions to be inserted directly into strings.

Example:

```python
name = "Ali"
age = 17

print(f"My name is {name} and I am {age}")
```

Output:

```text
My name is Ali and I am 17
```

f-strings make formatted output concise and readable.

---

# 45. Problem → Solution #21: Handling Errors

## Problem

The project can produce different types of errors.

For example:

```python
Movie('', 1999, 'Director', 100)
```

can raise:

```text
ValueError
```

And trying to add the wrong object can raise:

```text
MediaError
```

The program should handle these errors instead of crashing unexpectedly.

## Solution

The code uses:

```python
try:
    ...
except:
    ...
```

---

# 46. New Concept — `try` / `except`

Your code:

```python
try:
    ...
except ValueError as e:
    ...
except MediaError as e:
    ...
```

means:

> Try to execute the code. If a particular exception happens, handle it.

The two exception handlers have different purposes.

---

# 47. Handling `ValueError`

```python
except ValueError as e:
    print(f'Validation Error: {e}')
```

This handles validation problems such as:

- Empty title
- Invalid year
- Empty director
- Invalid duration
- Invalid season count
- Invalid episode count

The exception is stored in:

```python
e
```

and:

```python
str(e)
```

contains the message supplied when the exception was raised.

---

# 48. Handling `MediaError`

```python
except MediaError as e:
    print(f'Media Error: {e}')
    print(f'Unable to add {e.obj}: {type(e.obj)}')
```

This handles invalid catalogue objects.

Because `MediaError` stores:

```python
self.obj = obj
```

the error handler can also identify the object that caused the problem.

---

# 49. Creating the Catalogue Object

The program starts with:

```python
catalogue = MediaCatalogue()
```

This creates an empty catalogue.

Initially:

```text
catalogue.items = []
```

---

# 50. Creating Movie Objects

The first movie:

```python
movie1 = Movie('The Matrix', 1999, 'The Wachowskis', 136)
```

The second movie:

```python
movie2 = Movie('Inception', 2010, 'Christopher Nolan', 148)
```

Each call creates a separate `Movie` object.

Then they are added:

```python
catalogue.add(movie1)
catalogue.add(movie2)
```

---

# 51. Creating TV Series Objects

The first series:

```python
series1 = TVSeries('Scrubs', 2001, 'Bill Lawrence', 24, 9, 182)
```

The second:

```python
series2 = TVSeries('Breaking Bad', 2008, 'Vince Gilligan', 47, 5, 62)
```

Then:

```python
catalogue.add(series1)
catalogue.add(series2)
```

Now the catalogue contains four objects:

```text
1. Movie
2. Movie
3. TVSeries
4. TVSeries
```

---

# 52. Complete Program Logic

The complete program follows this sequence:

```text
START
  ↓
Create MediaCatalogue
  ↓
Create Movie
  ↓
Validate title
  ↓
Validate year
  ↓
Validate director
  ↓
Validate duration
  ↓
Create Movie object
  ↓
Add Movie to catalogue
  ↓
Create TVSeries
  ↓
Call Movie constructor using super()
  ↓
Validate title/year/director/duration
  ↓
Validate seasons
  ↓
Validate total episodes
  ↓
Create TVSeries object
  ↓
Add TVSeries to catalogue
  ↓
Print catalogue
  ↓
Get movies
  ↓
Get TV series
  ↓
Display both categories
  ↓
END
```

If an error occurs:

```text
Invalid data/object
       ↓
Exception raised
       ↓
try block stops
       ↓
Matching except block runs
       ↓
Error message displayed
```

---

# 53. Full OOP Concepts Used

Your project demonstrates the following OOP concepts.

## 1. Classes

```python
class Movie:
class TVSeries(Movie):
class MediaCatalogue:
class MediaError(Exception):
```

A class is a blueprint for creating objects.

---

## 2. Objects

Examples:

```python
movie1 = Movie(...)
series1 = TVSeries(...)
catalogue = MediaCatalogue()
```

Objects are actual instances created from classes.

---

## 3. Constructors

The `__init__()` method initializes objects:

```python
def __init__(self, ...):
```

---

## 4. Instance Attributes

Examples:

```python
self.title
self.year
self.director
self.duration
self.seasons
self.total_episodes
```

These belong to individual objects.

---

## 5. Methods

Examples:

```python
add()
get_movies()
get_tv_series()
__str__()
```

Methods define object behavior.

---

## 6. Encapsulation

Encapsulation means keeping related data and behavior together inside a class.

For example:

```text
Movie
 ├── title
 ├── year
 ├── director
 ├── duration
 └── __str__()
```

The class contains both the object's data and operations related to it.

---

## 7. Inheritance

```python
class TVSeries(Movie):
```

`TVSeries` inherits from `Movie`.

---

## 8. Method Overriding

`TVSeries` creates its own:

```python
def __str__(self):
```

instead of using the parent's exact output.

---

## 9. Polymorphism

Both `Movie` and `TVSeries` respond to:

```python
__str__()
```

but produce different results.

---

## 10. Custom Exceptions

```python
class MediaError(Exception):
```

This gives the application its own meaningful error type.

---

# 54. Other Python Concepts Used

## `.strip()`

Removes surrounding whitespace:

```python
title.strip()
```

---

## `raise`

Manually raises an exception:

```python
raise ValueError('Title cannot be empty')
```

---

## `isinstance()`

Checks whether an object belongs to a class or subclass:

```python
isinstance(media_item, Movie)
```

---

## `type()`

Gets the exact class:

```python
type(item)
```

---

## `len()`

Gets the size of a collection:

```python
len(self.items)
```

---

## List Comprehension

Creates filtered lists:

```python
[item for item in self.items if type(item) is Movie]
```

---

## `enumerate()`

Provides index and value:

```python
enumerate(movies, 1)
```

---

## f-Strings

Formats strings:

```python
f'{self.title} ({self.year})'
```

---

## `try` / `except`

Handles exceptions:

```python
try:
    ...
except ValueError:
    ...
```

---

## `super()`

Calls parent functionality:

```python
super().__init__(...)
```

---

## Special Methods

The project uses special methods such as:

```python
__init__()
__str__()
```

These are sometimes called **dunder methods** because they begin and end with double underscores.

---

# 55. Requirements → Solutions

| Requirement | Solution in the Project |
|---|---|
| Represent movies | `Movie` class |
| Store movie information | Instance attributes |
| Validate title | `title.strip()` |
| Validate year | `if year < 1895` |
| Validate director | `director.strip()` |
| Validate duration | `duration <= 0` |
| Represent TV series | `TVSeries` class |
| Reuse common movie code | Inheritance |
| Reuse parent constructor | `super().__init__()` |
| Add seasons | `self.seasons` |
| Add episodes | `self.total_episodes` |
| Validate seasons | `if seasons < 1` |
| Validate episodes | `if total_episodes < 1` |
| Different TV output | Override `__str__()` |
| Store all media | `MediaCatalogue.items` |
| Add objects | `add()` |
| Reject invalid objects | `MediaError` |
| Get only movies | `get_movies()` |
| Get TV series | `get_tv_series()` |
| Display catalogue | `MediaCatalogue.__str__()` |
| Handle validation errors | `except ValueError` |
| Handle catalogue errors | `except MediaError` |
| Document classes | Docstrings |

---

# 56. Important Design Decision: `type()` vs `isinstance()`

One of the most important details in this project is understanding why both are used.

### In `add()`:

```python
if not isinstance(media_item, Movie):
```

This intentionally accepts:

```text
Movie
TVSeries
```

because `TVSeries` inherits from `Movie`.

### In `get_movies()`:

```python
if type(item) is Movie
```

This intentionally accepts only:

```text
Movie
```

and excludes:

```text
TVSeries
```

So:

```text
isinstance()
    → accepts subclasses

type() is
    → exact class only
```

This distinction becomes very useful in larger OOP projects.

---

# 57. Important Improvement Needed in the Current Code

There is one unfinished part in your current `MediaCatalogue.__str__()` method.

You already calculate:

```python
movies = self.get_movies()
series = self.get_tv_series()
```

and display the movies:

```python
if movies:
    result += '=== MOVIES ===\n'
    for i, movie in enumerate(movies, 1):
        result += f'{i}. {movie}\n'
```

However, `series` is never displayed.

So the function currently prepares the TV series list but does not use it.

## Fix

Add:

```python
if series:
    result += '\n=== TV SERIES ===\n'
    for i, show in enumerate(series, 1):
        result += f'{i}. {show}\n'
```

Then:

```python
return result
```

The logic becomes:

```text
Create header
     ↓
Display movies if they exist
     ↓
Display TV series if they exist
     ↓
Return final string
```

---

# 58. Expected Output After the Fix

Your completed catalogue would look approximately like:

```text
Media Catalogue (4 items):

=== MOVIES ===
1. The Matrix (1999) - 136 min, The Wachowskis
2. Inception (2010) - 148 min, Christopher Nolan

=== TV SERIES ===
1. Scrubs (2001) - 9 seasons, 182 episodes, 24 min avg, Bill Lawrence
2. Breaking Bad (2008) - 5 seasons, 62 episodes, 47 min avg, Vince Gilligan
```

---

# 59. Why This Project Is a Big Step Up

This project is more advanced than simply creating a basic class because you are now designing a **small object-oriented system**.

You had to think about:

```text
What classes are needed?
What data belongs in each class?
What rules should the data follow?
Which classes share properties?
Where should inheritance be used?
How can duplicate code be avoided?
How should errors be represented?
How should objects be stored?
How should objects be filtered?
How should objects display themselves?
```

This is the beginning of actual **software design thinking**.

---

# 60. The Most Important Design Idea

The strongest design idea in this project is:

```python
class TVSeries(Movie):
```

combined with:

```python
super().__init__(...)
```

Instead of thinking:

> Movies and TV series are completely separate.

you recognized that:

> A TV series shares many properties with a movie/media item, so the common functionality can be inherited and reused.

The structure becomes:

```text
Movie
 ├── title
 ├── year
 ├── director
 ├── duration
 │
 └── TVSeries
      ├── seasons
      └── total_episodes
```

This is a practical example of why inheritance exists.

---

# 61. A Simple Real-World Mental Model

Think of the project as a real media company.

### `Movie`

A blueprint for a movie record.

### `TVSeries`

A specialized media record with additional information.

### `MediaCatalogue`

The library that stores and organizes all media records.

### `MediaError`

The rule-enforcer that says:

> This object is not valid media, so it cannot be added.

### `try/except`

The error-handling system that catches problems and displays useful messages rather than allowing the whole program to crash.

This mental model can make the structure easier to remember.

---

# 62. What You Learned From This Project

After completing this project, you should be comfortable with:

```text
Classes
Objects
Constructors
Instance attributes
Methods
Docstrings
Validation
raise
ValueError
Custom exceptions
Inheritance
super()
Method overriding
Polymorphism
isinstance()
type()
List comprehensions
enumerate()
len()
f-strings
try/except
Object collections
Filtering objects
Special methods
```

The most important new concepts from this project are:

```text
Docstrings
    ↓
Custom Exceptions
    ↓
Inheritance
    ↓
super()
    ↓
Method Overriding
    ↓
Polymorphism
    ↓
isinstance() vs type()
```

These concepts will appear repeatedly in larger Python projects.

---

# 63. Final Project Architecture

Your project can ultimately be understood as:

```text
                    ┌─────────────────────┐
                    │      Exception      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     MediaError      │
                    │  Custom exception   │
                    └─────────────────────┘


                    ┌─────────────────────┐
                    │        Movie        │
                    │---------------------│
                    │ title               │
                    │ year                │
                    │ director            │
                    │ duration            │
                    │ __init__()          │
                    │ __str__()           │
                    └──────────┬──────────┘
                               │
                         inheritance
                               │
                               ▼
                    ┌─────────────────────┐
                    │      TVSeries       │
                    │---------------------│
                    │ seasons             │
                    │ total_episodes      │
                    │ __init__()          │
                    │ __str__()           │
                    └─────────────────────┘


                    ┌─────────────────────┐
                    │  MediaCatalogue     │
                    │---------------------│
                    │ items               │
                    │ add()               │
                    │ get_movies()        │
                    │ get_tv_series()     │
                    │ __str__()           │
                    └─────────────────────┘
                              │
                              ▼
                 stores Movie + TVSeries objects
```

---

# 64. Final Takeaway

This project is not just about making a catalogue.

It demonstrates how Python can be used to model a real-world system with:

- Classes for structure
- Objects for actual data
- Validation for reliable data
- Inheritance for code reuse
- `super()` for shared initialization
- Method overriding for specialized behavior
- Polymorphism for flexible object handling
- Custom exceptions for meaningful application errors
- List comprehensions for filtering
- `try/except` for safe error handling
- Docstrings for documentation

The most important lesson is to think about **relationships between objects and responsibilities of classes**, not just individual lines of code.

---

# 65. Original Project Code Structure

The major structure of the project is:

```python
class MediaError(Exception):
    """Custom exception for media-related errors."""

    def __init__(self, message, obj):
        super().__init__(message)
        self.obj = obj


class Movie:
    """Parent class representing a movie."""

    def __init__(self, title, year, director, duration):
        if not title.strip():
            raise ValueError('Title cannot be empty')
        if year < 1895:
            raise ValueError('Year must be 1895 or later')
        if not director.strip():
            raise ValueError('Director cannot be empty')
        if duration <= 0:
            raise ValueError('Duration must be positive')

        self.title = title
        self.year = year
        self.director = director
        self.duration = duration

    def __str__(self):
        return f'{self.title} ({self.year}) - {self.duration} min, {self.director}'


class TVSeries(Movie):
    """Child class representing an entire TV series."""

    def __init__(self, title, year, director, duration, seasons, total_episodes):
        super().__init__(title, year, director, duration)

        if seasons < 1:
            raise ValueError('Seasons must be 1 or greater')
        if total_episodes < 1:
            raise ValueError('Total episodes must be 1 or greater')

        self.seasons = seasons
        self.total_episodes = total_episodes

    def __str__(self):
        return f'{self.title} ({self.year}) - {self.seasons} seasons, {self.total_episodes} episodes, {self.duration} min avg, {self.director}'


class MediaCatalogue:
    """A catalogue that can store different types of media items."""

    def __init__(self):
        self.items = []

    def add(self, media_item):
        if not isinstance(media_item, Movie):
            raise MediaError(
                'Only Movie or TVSeries instances can be added',
                media_item
            )
        self.items.append(media_item)

    def get_movies(self):
        return [item for item in self.items if type(item) is Movie]

    def get_tv_series(self):
        return [item for item in self.items if isinstance(item, TVSeries)]

    def __str__(self):
        if not self.items:
            return 'Media Catalogue (empty)'

        movies = self.get_movies()
        series = self.get_tv_series()

        result = f'Media Catalogue ({len(self.items)} items):\n\n'

        if movies:
            result += '=== MOVIES ===\n'
            for i, movie in enumerate(movies, 1):
                result += f'{i}. {movie}\n'

        # Add this section to display TV series:
        if series:
            result += '\n=== TV SERIES ===\n'
            for i, show in enumerate(series, 1):
                result += f'{i}. {show}\n'

        return result
```

---

# 66. Key Revision Questions

Before considering this project fully understood, you should be able to answer these without looking at the notes:

1. What is a docstring?
2. What is the difference between a docstring and a comment?
3. Why does `MediaError` inherit from `Exception`?
4. Why is `self.obj` stored inside `MediaError`?
5. What does `raise` do?
6. Why does `TVSeries` inherit from `Movie`?
7. What does `super().__init__()` do?
8. Why is `TVSeries.__str__()` different from `Movie.__str__()`?
9. What is method overriding?
10. What is polymorphism?
11. What is the difference between `isinstance()` and `type()`?
12. Why does `get_movies()` use `type(item) is Movie`?
13. Why does `get_tv_series()` use `isinstance(item, TVSeries)`?
14. What does the list comprehension in `get_movies()` do?
15. What does `enumerate(movies, 1)` do?
16. Why does `if not self.items` detect an empty catalogue?
17. Why do we use `try/except`?
18. What kinds of errors produce `ValueError` in this project?
19. What situation produces `MediaError`?
20. Why are docstrings useful in a larger software project?

---

# 67. Project Completion Checklist

- [x] Created a `Movie` class
- [x] Added movie attributes
- [x] Added input validation
- [x] Added `__str__()`
- [x] Created a `TVSeries` child class
- [x] Used inheritance
- [x] Used `super()`
- [x] Added TV-specific attributes
- [x] Added TV-specific validation
- [x] Overrode `__str__()`
- [x] Created a `MediaCatalogue`
- [x] Added object validation
- [x] Created `MediaError`
- [x] Added movie filtering
- [x] Added TV-series filtering
- [x] Added exception handling
- [x] Used docstrings
- [ ] Finish the TV-series output section in `MediaCatalogue.__str__()`

---

# 68. Final Summary

The project follows a clear object-oriented design:

```text
Movie
  │
  └── TVSeries

MediaCatalogue
  │
  └── stores both

MediaError
  │
  └── handles invalid media objects
```

The overall programming flow is:

```text
Define classes
      ↓
Validate data
      ↓
Create objects
      ↓
Reuse code with inheritance
      ↓
Manage objects using MediaCatalogue
      ↓
Filter objects by type
      ↓
Format objects with __str__()
      ↓
Handle errors with custom exceptions
      ↓
Display final catalogue
```

This project represents a strong transition from beginner Python syntax into practical **Object-Oriented Programming and software design**.
