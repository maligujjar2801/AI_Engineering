# 🎮 Day 15 - Game Character Stats Tracker (OOP Lab)

## Objective

Today I built my first complete Object-Oriented Programming (OOP) lab project.

The goal was to create a game character that stores its own stats, protects its data using encapsulation, and updates its attributes through properties.

---

# Features Implemented

- Character Name
- Character Health
- Character Mana
- Character Level
- Read-only Name Property
- Health Getter & Setter
- Mana Getter & Setter
- Level Getter
- Level Up System
- Custom String Representation

---

# Constructor (`__init__()`)

The constructor initializes every new game character.

Each character starts with:

- `_name` = Name provided during object creation.
- `_health` = 100
- `_mana` = 50
- `_level` = 1

### Example

```python
hero = GameCharacter("Knight")
```

---

# Encapsulation

The character's data is stored inside private attributes.

```python
self._name
self._health
self._mana
self._level
```

Private attributes should not be modified directly outside the class.

Instead, properties are used.

---

# Read-only Property

The `name` property only has a getter.

```python
@property
def name(self):
    return self._name
```

This allows the name to be viewed but not modified.

---

# Health Property

The health property contains:

- Getter
- Setter

The setter validates the value before assigning it.

Rules:

- Health cannot go below **0**
- Health cannot exceed **100**

Example:

```python
hero.health = -20
```

Stored value:

```text
0
```

Example:

```python
hero.health = 150
```

Stored value:

```text
100
```

---

# Mana Property

The mana property also contains:

- Getter
- Setter

Rules:

- Mana cannot go below **0**
- Mana cannot exceed **50**

---

# Level Property

The level property only has a getter.

```python
@property
def level(self):
    return self._level
```

The level cannot be modified directly from outside the class.

---

# Level Up Method

The `level_up()` method performs multiple operations.

It:

- Increases the level by 1.
- Restores health to 100.
- Restores mana to 50.
- Prints a level-up message.

Example:

```python
hero.level_up()
```

Output:

```text
Knight leveled up to 2!
```

---

# `__str__()` Method

The `__str__()` method returns a readable description of the object.

Example:

```python
print(hero)
```

Output:

```text
Name: Knight
Level: 1
Health: 100
Mana: 50
```

---

# OOP Concepts Used

- Classes
- Objects
- Constructors
- Encapsulation
- Private Attributes
- Properties
- Getters
- Setters
- Validation
- Methods
- Method Calling
- `__str__()` Magic Method

---

# Real-Life Analogy

Imagine a game character.

The player should never be able to directly change internal values like health or mana without following the game's rules.

Instead, the game checks every update before accepting it.

This is exactly how encapsulation and properties work.

---

# What I Learned

Today I built my first complete OOP project by combining multiple concepts together. I learned how encapsulation protects object data using private attributes, how properties control access through getters and setters, and how validation prevents invalid values from being stored. I also practiced implementing business logic inside methods by creating a level-up system that automatically restores health and mana while increasing the character's level. Finally, I learned how the `__str__()` method provides a clean and readable representation of an object.