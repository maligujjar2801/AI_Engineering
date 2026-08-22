# 🎬 Media Catalogue

A Python **Object-Oriented Programming (OOP)** project that builds a simple media catalogue capable of storing and managing **Movies** and **TV Series**.

This project was created as part of my Python learning journey and focuses on applying OOP concepts to a practical problem.

---

## 📌 Project Overview

The Media Catalogue allows you to:

- Create movie objects
- Create TV series objects
- Validate media information
- Store different media types in one catalogue
- Filter movies and TV series
- Display media in a clean format
- Handle invalid data with exceptions
- Create custom exceptions for application-specific errors

The project demonstrates how different OOP concepts can work together in a single Python application.

---

## 🧠 Concepts Demonstrated

### Object-Oriented Programming

- Classes
- Objects
- Constructors
- Instance attributes
- Methods
- Encapsulation
- Inheritance
- Method overriding
- Polymorphism

### Python Concepts

- `__init__()`
- `__str__()`
- Docstrings
- `super()`
- `isinstance()`
- `type()`
- `raise`
- `try` / `except`
- `ValueError`
- Custom exceptions
- List comprehensions
- `enumerate()`
- `len()`
- f-strings
- String `.strip()`

---

## 🏗️ Class Structure

```text
Exception
   │
   └── MediaError
         └── Custom exception for media-related errors


Movie
   │
   └── TVSeries
         └── Inherits common movie functionality


MediaCatalogue
   └── Stores Movie and TVSeries objects
```

### `Movie`

The parent class representing a movie.

Stores:

- `title`
- `year`
- `director`
- `duration`

It also validates the information and provides a custom `__str__()` representation.

### `TVSeries`

A child class of `Movie`.

In addition to inherited information, it stores:

- `seasons`
- `total_episodes`

It also overrides `__str__()` to provide a TV-series-specific representation.

### `MediaCatalogue`

Manages the media objects.

Provides methods to:

- Add media
- Get movies
- Get TV series
- Display the catalogue

### `MediaError`

A custom exception used when an invalid object is added to the catalogue.

---

## ✅ Validation Rules

The program validates media before storing it.

### Movie validation

```text
Title must not be empty
Year must be 1895 or later
Director must not be empty
Duration must be greater than 0
```

### TV Series validation

```text
Seasons must be at least 1
Total episodes must be at least 1
```

Invalid values raise `ValueError`.

Invalid objects added to the catalogue raise the custom `MediaError`.

---

## 🔑 Important OOP Design

One of the main ideas in this project is inheritance:

```python
class TVSeries(Movie):
```

Instead of duplicating all the movie validation and initialization code, `TVSeries` reuses the parent constructor:

```python
super().__init__(title, year, director, duration)
```

This allows the project to keep common functionality in one place.

The `TVSeries` class then adds its own properties:

```python
self.seasons = seasons
self.total_episodes = total_episodes
```

---

## 🔄 Polymorphism

Both `Movie` and `TVSeries` implement:

```python
__str__()
```

but they provide different output formats.

For example:

```text
Movie:
The Matrix (1999) - 136 min, The Wachowskis

TV Series:
Breaking Bad (2008) - 5 seasons, 62 episodes, 47 min avg, Vince Gilligan
```

The same method name behaves differently depending on the object.

---

## 🔍 `isinstance()` vs `type()`

The project intentionally uses both.

### `isinstance()`

```python
isinstance(media_item, Movie)
```

This allows both `Movie` and subclasses such as `TVSeries`.

### `type()`

```python
type(item) is Movie
```

This checks for an exact `Movie` object and therefore excludes `TVSeries`.

This distinction is important when working with inheritance.

---

## ⚠️ Error Handling

The project uses:

```python
try:
    ...
except ValueError:
    ...
except MediaError:
    ...
```

This prevents invalid data or objects from causing an uncontrolled program crash.

A custom exception is used:

```python
class MediaError(Exception):
```

The exception also stores the object that caused the problem:

```python
self.obj = obj
```

---

## 📂 Project Structure

A simple repository structure can look like this:

```text
Media-Catalogue/
│
├── media_catalogue.py
└── README.md
```

You can also keep the detailed learning notes separately:

```text
Media-Catalogue/
│
├── media_catalogue.py
├── README.md
└── NOTES.md
```

---

## ▶️ How to Run

Make sure Python is installed.

Clone the repository:

```bash
git clone <your-repository-url>
```

Move into the project directory:

```bash
cd Media-Catalogue
```

Run the program:

```bash
python media_catalogue.py
```

---

## 💻 Example

The project creates movies:

```python
movie1 = Movie(
    'The Matrix',
    1999,
    'The Wachowskis',
    136
)
```

and TV series:

```python
series1 = TVSeries(
    'Breaking Bad',
    2008,
    'Vince Gilligan',
    47,
    5,
    62
)
```

They are then added to the catalogue:

```python
catalogue.add(movie1)
catalogue.add(series1)
```

---

## 📤 Example Output

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

## 📚 What I Learned

This project helped me move beyond basic Python syntax and apply OOP concepts in a realistic program.

The main things I practiced were:

- Designing classes around real-world entities
- Using inheritance to reuse code
- Using `super()` to call parent functionality
- Overriding methods
- Understanding polymorphism
- Creating custom exceptions
- Validating data
- Filtering objects
- Handling errors safely
- Writing documentation with docstrings

This project was an important step in understanding how larger Python programs can be structured.

---

## 🚀 Possible Future Improvements

Some features that could be added later:

- Remove media from the catalogue
- Search by title
- Search by director
- Sort by year or duration
- Add genres
- Add ratings
- Save catalogue data to a file
- Load catalogue data from a file
- Build a command-line menu
- Add unit tests
- Add more media types such as documentaries or anime
- Store data using JSON or a database

---

## 📝 Notes

The detailed explanation of the project's logic and concepts is available in the project notes.

The notes explain the project using a **Problem → Solution** approach and cover the reasoning behind each major part of the code.

---

## 👨‍💻 Author

**Muhammad Ali**

Part of my ongoing Python and AI Engineering learning journey.

---

⭐ This project represents my progress from learning Python fundamentals toward building more structured, object-oriented applications.