# Player Interface — Learning Notes

## 1. Abstract Base Classes

An **abstract class** is a class intended to be used as a blueprint for other classes.

Python provides abstract base classes through the `abc` module.

```python
from abc import ABC, abstractmethod
```

Then:

```python
class Player(ABC):
    ...
```

This makes `Player` an abstract base class.

### Why use an abstract class?

A parent class can define functionality that all subclasses share while requiring subclasses to provide certain behavior themselves.

---

# 2. `@abstractmethod`

An abstract method is a method that a subclass is required to implement.

```python
@abstractmethod
def level_up(self):
    pass
```

`Player` knows that every player should have a `level_up()` method, but it does not define exactly what leveling up should do.

The concrete subclass decides that.

Because `Player` has an abstract method, it cannot normally be instantiated directly:

```python
Player()  # Not allowed
```

A subclass must implement all abstract methods before it can be instantiated.

---

# 3. The `Player` Class

The parent class is:

```python
class Player(ABC):
```

It provides functionality common to players.

Its constructor is:

```python
def __init__(self):
    self.moves = []
    self.position = (0, 0)
    self.path = [self.position]
```

---

# 4. `self.moves`

```python
self.moves = []
```

This creates an empty list for available movements.

The parent class does not know what moves a particular type of player should have.

The concrete class will fill this list.

For example, a Pawn later has:

```python
self.moves = [
    (0, 1),
    (0, -1),
    (-1, 0),
    (1, 0)
]
```

---

# 5. Coordinates and Tuples

A tuple such as:

```python
(2, 3)
```

can represent a position on a 2D coordinate system.

The first value is the `x` coordinate.

The second value is the `y` coordinate.

So:

```text
(x, y)
```

means:

```text
x → horizontal direction
y → vertical direction
```

The starting position is:

```python
(0, 0)
```

---

# 6. Movement Coordinates

The Pawn's four initial movements are:

```python
(0, 1)
(0, -1)
(-1, 0)
(1, 0)
```

They represent:

```text
        (0, 1)
           ↑
           |
(-1, 0) ← (0, 0) → (1, 0)
           |
           ↓
        (0, -1)
```

Each move changes the position by exactly one unit.

---

# 7. `self.path`

The path stores every position visited by the player.

Initially:

```python
self.path = [self.position]
```

Since the starting position is `(0, 0)`:

```python
[(0, 0)]
```

After moving to `(1, 0)`:

```python
[(0, 0), (1, 0)]
```

After moving to `(1, 1)`:

```python
[(0, 0), (1, 0), (1, 1)]
```

So `path` is the player's movement history.

---

# 8. `random.choice()`

The lab requires:

```python
import random
```

Then:

```python
move = random.choice(self.moves)
```

`random.choice()` selects one random item from a sequence.

For example:

```python
moves = [
    (0, 1),
    (0, -1),
    (-1, 0),
    (1, 0)
]
```

A call to:

```python
random.choice(moves)
```

could return:

```python
(1, 0)
```

or:

```python
(0, -1)
```

or any other item in the list.

---

# 9. The `make_move()` Method

The method is:

```python
def make_move(self):
    move = random.choice(self.moves)

    new_x = self.position[0] + move[0]
    new_y = self.position[1] + move[1]

    self.position = (new_x, new_y)
    self.path.append(self.position)

    return self.position
```

Let's break it down.

---

## Step 1 — Select a random move

```python
move = random.choice(self.moves)
```

One movement is randomly selected.

---

## Step 2 — Calculate the new X coordinate

```python
new_x = self.position[0] + move[0]
```

If:

```python
self.position = (2, 3)
move = (1, 0)
```

then:

```text
new_x = 2 + 1
new_x = 3
```

---

## Step 3 — Calculate the new Y coordinate

```python
new_y = self.position[1] + move[1]
```

Using:

```python
self.position = (2, 3)
move = (1, 0)
```

we get:

```text
new_y = 3 + 0
new_y = 3
```

Therefore:

```python
new position = (3, 3)
```

---

# 10. Update `self.position`

```python
self.position = (new_x, new_y)
```

This changes the player's current position.

For example:

```text
Before:
(2, 3)

Move:
(1, 0)

After:
(3, 3)
```

---

# 11. Add the Position to the Path

```python
self.path.append(self.position)
```

This records the new location.

If the path was:

```python
[(0, 0), (1, 0)]
```

and the player moves to `(1, 1)`, it becomes:

```python
[(0, 0), (1, 0), (1, 1)]
```

---

# 12. Returning the Position

At the end:

```python
return self.position
```

This allows code calling `make_move()` to receive the new position.

Example:

```python
new_position = pawn.make_move()
print(new_position)
```

---

# 13. Inheritance

The Pawn class is:

```python
class Pawn(Player):
```

This means `Pawn` inherits from `Player`.

Conceptually:

```text
Player
  |
  └── Pawn
```

Therefore Pawn receives methods such as:

```python
make_move()
```

from the parent class.

---

# 14. `super()`

The Pawn constructor contains:

```python
def __init__(self):
    super().__init__()
```

`super()` is used to call the parent class implementation.

Here:

```python
super().__init__()
```

calls:

```python
Player.__init__()
```

This initializes:

```python
self.moves
self.position
self.path
```

Then Pawn can add its own setup.

---

# 15. Pawn's Initial Moves

After calling the parent constructor, Pawn sets:

```python
self.moves = [
    (0, 1),
    (0, -1),
    (-1, 0),
    (1, 0)
]
```

So the Pawn initially has four possible directions.

---

# 16. Method Overriding

`Player` declares:

```python
@abstractmethod
def level_up(self):
    pass
```

Pawn provides the concrete implementation:

```python
def level_up(self):
    self.moves.extend([
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    ])
```

This is an example of **method overriding / implementing an abstract method**.

---

# 17. Diagonal Movement

The four diagonal moves are:

```python
(1, 1)
(1, -1)
(-1, 1)
(-1, -1)
```

They represent:

```text
(-1, 1)     (0, 1)     (1, 1)
    ↖          ↑          ↗

(-1, 0)       (0, 0)      (1, 0)
    ←            •           →

(-1,-1)     (0,-1)     (1,-1)
    ↙          ↓          ↘
```

After leveling up, the Pawn has eight possible directions.

---

# 18. `extend()` vs `append()`

The lab can use:

```python
self.moves.extend([
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
])
```

`extend()` adds each item individually.

For example:

```python
moves = [(0, 1), (0, -1)]

moves.extend([(1, 1), (-1, -1)])
```

results in:

```python
[(0, 1), (0, -1), (1, 1), (-1, -1)]
```

Using `append()` would add the entire list as one item, which is not what we want here.

---

# 19. Complete Structure

The final design is:

```text
ABC
 |
 └── Player
      |
      ├── __init__()
      │    ├── moves
      │    ├── position
      │    └── path
      │
      ├── make_move()
      │    ├── random.choice()
      │    ├── update position
      │    ├── update path
      │    └── return position
      │
      └── abstract level_up()
              |
              └── Pawn
                   ├── super().__init__()
                   ├── 4 initial moves
                   └── level_up()
                        └── +4 diagonal moves
```

---

# 20. Complete Code

```python
from abc import ABC, abstractmethod
import random


class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        move = random.choice(self.moves)

        new_x = self.position[0] + move[0]
        new_y = self.position[1] + move[1]

        self.position = (new_x, new_y)
        self.path.append(self.position)

        return self.position

    @abstractmethod
    def level_up(self):
        pass


class Pawn(Player):
    def __init__(self):
        super().__init__()

        self.moves = [
            (0, 1),
            (0, -1),
            (-1, 0),
            (1, 0)
        ]

    def level_up(self):
        self.moves.extend([
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1)
        ])
```

---

# Key Takeaways

1. `ABC` creates an abstract base class.
2. `@abstractmethod` requires subclasses to implement a method.
3. `Pawn(Player)` means Pawn inherits from Player.
4. `super().__init__()` calls the parent constructor.
5. `(x, y)` tuples can represent coordinates.
6. `random.choice()` selects a random move.
7. `path` stores the player's movement history.
8. `extend()` adds multiple new moves to a list.
9. `level_up()` demonstrates how a subclass can provide its own implementation of an abstract method.
10. The parent class contains reusable behavior, while the child class provides player-specific behavior.
