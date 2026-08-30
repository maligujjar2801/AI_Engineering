# Build a Player Interface

## FreeCodeCamp Python Lab

This project implements a simple player movement system using **abstract classes, inheritance, `super()`, abstract methods, tuples, lists, and `random.choice()`**.

### Objective

Create an abstract `Player` class and a concrete `Pawn` class.

The `Player` class manages:

- The player's available moves
- The current position
- The path traveled by the player
- Random movement
- The abstract `level_up()` behavior

The `Pawn` class provides the actual movement options and implements `level_up()`.

---

## Concepts Practiced

- Abstract Base Classes (`ABC`)
- `@abstractmethod`
- Inheritance
- `super()`
- Class initialization with `__init__`
- Instance attributes
- Tuples for `(x, y)` coordinates
- Lists for storing moves and paths
- `random.choice()`
- Method overriding
- Updating object state

---

## Player

`Player` is an abstract base class.

It starts every player at:

```python
(0, 0)
```

It also creates:

```python
self.moves = []
self.position = (0, 0)
self.path = [self.position]
```

`Player` contains the common `make_move()` behavior and requires subclasses to implement `level_up()`.

---

## Pawn

`Pawn` inherits from `Player`.

Its initial movement options are:

```text
Up       (0, 1)
Down     (0, -1)
Left     (-1, 0)
Right    (1, 0)
```

After leveling up, it gains four diagonal moves:

```text
Up-right       (1, 1)
Down-right     (1, -1)
Up-left        (-1, 1)
Down-left      (-1, -1)
```

This gives the Pawn eight possible movement directions.

---

## Example

A Pawn begins at:

```python
(0, 0)
```

If a random move selects:

```python
(1, 0)
```

the new position becomes:

```python
(1, 0)
```

The path becomes:

```python
[(0, 0), (1, 0)]
```

Because `random.choice()` is used, the exact movement can differ each time.

---

## What I Learned

This lab helped me understand how an abstract parent class can define common behavior while a child class provides its own specific implementation.

The important relationship is:

```text
ABC
 |
Player
 |
Pawn
```

`Pawn` inherits the common functionality from `Player` and overrides the abstract `level_up()` method.

---

## Files

- `main.py` — Python implementation of the Player and Pawn classes.
- `README.md` — Project overview and concepts.
- `Player_Interface_Notes.md` — Detailed learning notes.
