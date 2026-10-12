# Day 23 — Hashing, Hash Tables, Hash Maps, Dictionaries & Sets 🐍

> **Python Journey · Detailed lecture notes**  
> **Level:** Beginner → Intermediate  
> **Estimated study time:** 60–100 minutes, split into shorter sessions if needed  
> **Prerequisites:** Variables, functions, loops, lists, tuples, dictionaries, sets, and basic Big-O notation

---

## Table of Contents

1. [Learning objectives](#1-learning-objectives)
2. [The big picture: map, hash map, hash table, dict, and set](#2-the-big-picture-map-hash-map-hash-table-dict-and-set)
3. [Why hashing is useful](#3-why-hashing-is-useful)
4. [What is a hash?](#4-what-is-a-hash)
5. [How a hash table works conceptually](#5-how-a-hash-table-works-conceptually)
6. [Collisions and collision resolution](#6-collisions-and-collision-resolution)
7. [Python dictionaries (`dict`) in depth](#7-python-dictionaries-dict-in-depth)
8. [Hashability and valid dictionary keys](#8-hashability-and-valid-dictionary-keys)
9. [The equality-and-hash contract](#9-the-equality-and-hash-contract)
10. [Python sets (`set`) and `frozenset`](#10-python-sets-set-and-frozenset)
11. [Dictionary and set comprehensions](#11-dictionary-and-set-comprehensions)
12. [Common real-world patterns](#12-common-real-world-patterns)
13. [Time complexity and performance](#13-time-complexity-and-performance)
14. [Common mistakes and debugging](#14-common-mistakes-and-debugging)
15. [Mini project: Word Analyzer](#15-mini-project-word-analyzer)
16. [Practice exercises](#16-practice-exercises)
17. [Solutions and explanations](#17-solutions-and-explanations)
18. [Day 23 knowledge check](#18-day-23-knowledge-check)
19. [Final cheat sheet](#19-final-cheat-sheet)
20. [Next step in the roadmap](#20-next-step-in-the-roadmap)

---

## 1. Learning objectives

By the end of this lesson, you should be able to:

- Explain the difference between a **map**, a **hash map**, a **hash table**, Python's `dict`, and a `set`.
- Explain how hashing helps a program find stored data efficiently.
- Use Python's `hash()` function while understanding its limitations.
- Describe a **collision** and why a hash table needs a collision-resolution strategy.
- Create, read, update, and delete dictionary entries.
- Use `.get()`, `.items()`, `.keys()`, `.values()`, `in`, and other useful dictionary operations.
- Explain what makes an object **hashable** and why a list cannot be a dictionary key.
- Use sets for uniqueness, fast membership checks, and mathematical set operations.
- Recognize the average-case and worst-case time complexity of common operations.
- Apply dictionaries and sets to frequency counting, grouping, deduplication, and a small text-analysis project.

---

## 2. The big picture: map, hash map, hash table, `dict`, and `set`

These terms are closely related, but they do not all mean the same thing.

### 2.1 Map: the general idea

A **map** is an abstract data structure that associates a **key** with a **value**.

```text
key  ─────► value
"Ali" ────► 92
"Ahmed" ──► 85
"Hamza" ──► 78
```

You supply a key and retrieve the value associated with it. The abstract concept describes the behavior, not necessarily how it is implemented.

### 2.2 Hash map: a type of map

A **hash map** is a map implemented using hashing. It applies a hash function to a key and uses the result to help locate the corresponding entry.

Other map implementations can use different strategies, such as search trees. So **map** is the broad concept; **hash map** is one implementation strategy.

### 2.3 Hash table: the underlying storage idea

A **hash table** is a data structure organized around hash-based lookup. Hash maps are commonly implemented with hash tables.

In a simplified model, a hash table has slots, and a key's hash helps determine where the program should look. Real implementations must handle collisions, resizing, and other details.

### 2.4 Python's `dict`

Python's built-in `dict` is its standard **mapping** type. In mainstream Python implementations such as CPython, dictionaries use a hash-table-based design.

```python
student_marks = {
    "Ali": 92,
    "Ahmed": 85,
    "Hamza": 78,
}

print(student_marks["Ali"])  # 92
```

This is a Python dictionary and a practical way to use a hash-based map.

### 2.5 Python's `set`

A `set` stores unique, hashable elements. It is useful when you care about whether an item is present, or whether values are unique, rather than associating each key with a separate value.

```python
subjects = {"Math", "Physics", "Python"}
print("Python" in subjects)  # True
```

### 2.6 Do not confuse these with Python's `map()` function

Python also has a built-in function named `map()`. It applies a function to each item of an iterable and returns an iterator. It is **not** a hash map.

```python
numbers = [1, 2, 3, 4]
doubled = map(lambda number: number * 2, numbers)

print(list(doubled))  # [2, 4, 6, 8]
```

**Quick comparison**

| Term | Meaning | Typical Python example |
|---|---|---|
| Map | Abstract key-to-value concept | `student_marks = {"Ali": 92}` |
| Hash map | Map implemented using hashing | A common implementation model for `dict` |
| Hash table | Hash-based storage structure | Conceptual implementation detail |
| Dictionary | Python's built-in mapping type | `dict`, `{ "Ali": 92 }` |
| Set | Unique collection of hashable elements | `{"Math", "Physics"}` |
| `map()` | Function that transforms iterable items | `map(str, [1, 2, 3])` |

---

## 3. Why hashing is useful

Suppose you have a list containing thousands of students and need to find the marks of a student named Ali.

```python
students_list = [
    ("Ahmed", 85),
    ("Hamza", 78),
    ("Bilal", 90),
    ("Ali", 92),
]

for name, marks in students_list:
    if name == "Ali":
        print(marks)
        break
```

A list lookup by value may need to inspect one item after another. If the desired item is near the end—or absent—the program can examine many entries.

With a dictionary, you express the relationship directly:

```python
students = {
    "Ahmed": 85,
    "Hamza": 78,
    "Bilal": 90,
    "Ali": 92,
}

print(students["Ali"])  # 92
```

Typical dictionary lookup is **O(1) on average**, rather than a scan through all entries. This average-case speed is one reason dictionaries and sets are used so often.

Common uses include:

- Looking up a user by ID.
- Counting words or other repeated values.
- Checking whether a username has already been seen.
- Grouping records by category.
- Caching the result of an expensive calculation.
- Indexing products, records, or configuration settings by a key.

**Important:** Average O(1) does not mean every operation takes exactly the same number of CPU instructions. Hash tables still need to calculate hashes, compare keys, handle collisions, and occasionally resize.

---

## 4. What is a hash?

A **hash function** takes an object and produces a hash value. In Python, `hash()` requests the hash value of a hashable object.

```python
print(hash("Ali"))
print(hash(42))
print(hash((1, 2, 3)))
```

The integer produced for a string may vary between separate Python processes because Python randomizes hashes for certain types, including strings, by default. Therefore, do **not** assume that `hash("Ali")` will always produce the same number on every run or machine.

### 4.1 A hash is not an ID

A hash is not guaranteed to be unique. Two different objects can have the same hash value. That situation is called a **hash collision**.

Do not use `hash()` as:

- A permanent identifier for data.
- A stable value to store in a file and expect to match on another run.
- An encryption method or password-security mechanism.
- Proof that two objects are equal.

A hash helps hash-based structures find candidate locations; key equality is still important.

### 4.2 Hashing and table indices are not the same thing

A simplified hash table might use a calculation resembling:

```text
index = hash(key) % table_size
```

This illustrates the general idea of converting a hash into a table position. It is **not a complete description of Python's dictionary or set implementation**. Actual implementations use more sophisticated probing and resizing logic.

### 4.3 Hashing versus encryption

Hashing for data structures is different from encryption. Encryption is designed to be reversed with the appropriate key; a general-purpose hash produces a fixed-size hash value and is not intended to recover the original object. Also, the built-in Python `hash()` is not suitable for cryptographic security.

---

## 5. How a hash table works conceptually

Imagine a simplified table with a number of storage slots:

```text
Slot 0  → entry
Slot 1  → empty
Slot 2  → entry
Slot 3  → entry
Slot 4  → empty
Slot 5  → entry
```

When you look up a key such as `"Ali"`, a simplified conceptual process is:

```text
                 "Ali"
                   │
                   ▼
             hash("Ali")
                   │
                   ▼
        choose a place to examine
                   │
                   ▼
      compare stored key(s) as needed
                   │
                   ▼
             return its value
```

A real hash table must address several practical questions:

1. What if two keys need the same location?
2. What if the table becomes too full?
3. How can the table find a key after a collision?
4. How should it distinguish keys that have the same hash but are not equal?

Collision handling and resizing are part of what makes a hash-table implementation more than a simple array.

---

## 6. Collisions and collision resolution

A **collision** occurs when different keys lead to a conflicting hash-table location. Collisions are normal; a hash table must be designed to handle them correctly.

### 6.1 A simple illustration

Suppose a toy table has eight positions. For teaching purposes only, imagine two keys are directed to position 5:

```text
Key A ──► position 5
Key B ──► position 5
```

The table cannot blindly overwrite Key A's value with Key B's value. It needs a collision-resolution strategy.

### 6.2 Two common approaches

**Separate chaining:** A table position points to a secondary collection of entries that belong there.

```text
Position 5 ──► [Key A, Key B, Key C]
```

**Open addressing:** Entries are stored in the table itself, and the algorithm probes other positions when a collision occurs.

Different languages and implementations choose different approaches. CPython's dictionaries use an open-addressing design with a probing strategy; this section's diagrams are conceptual rather than a precise depiction of CPython's internal memory layout.

### 6.3 What happens during lookup?

When a key's expected position is occupied, the implementation follows its collision-resolution procedure until it finds the matching key or determines the key is absent. The implementation checks key identity/equality as needed; a matching hash alone is not enough to prove that two keys are the same.

### 6.4 Why distribution matters

If keys are spread effectively across the available storage, lookups tend to remain efficient. If many keys conflict, the implementation may have to do more work. A hash table therefore needs a reasonable hash function and a strategy for collisions and resizing.

---

## 7. Python dictionaries (`dict`) in depth

A dictionary stores key-value pairs. Keys must be hashable; values can be objects of many different types, including lists and dictionaries.

### 7.1 Creating dictionaries

```python
# Empty dictionary
empty_dict = {}

# Another way to create an empty dictionary
another_empty_dict = dict()

# Dictionary with initial values
student = {
    "name": "Ali",
    "age": 17,
    "marks": 92,
}
```

Notice that `{}` creates an empty **dictionary**, not an empty set. Use `set()` to create an empty set.

### 7.2 Reading a value with square brackets

```python
student = {"name": "Ali", "marks": 92}

print(student["name"])   # Ali
print(student["marks"])  # 92
```

If a key is missing, square-bracket lookup raises `KeyError`:

```python
# Raises KeyError if "phone" is not a key:
# print(student["phone"])
```

### 7.3 Safe lookup with `.get()`

```python
student = {"name": "Ali", "marks": 92}

print(student.get("name"))             # Ali
print(student.get("phone"))            # None
print(student.get("phone", "Unknown"))  # Unknown
```

General form:

```python
dictionary.get(key, default_value)
```

`get()` returns the default when the key is missing. It does not insert that default into the dictionary.

### 7.4 Adding and updating entries

Assigning to a new key adds an entry. Assigning to an existing key replaces its value.

```python
student = {"name": "Ali", "marks": 92}

student["grade"] = "A"  # Add a new key
student["marks"] = 95   # Update an existing key

print(student)
```

Result:

```python
{"name": "Ali", "marks": 95, "grade": "A"}
```

### 7.5 Deleting entries

```python
student = {"name": "Ali", "age": 17, "marks": 92}

del student["age"]            # Raises KeyError if the key is missing
marks = student.pop("marks")  # Removes and returns the value
last_item = student.popitem()  # Removes and returns the last inserted pair
student.clear()                # Removes all entries
```

Use `pop(key, default)` when you want a fallback if the key might not exist:

```python
phone = student.pop("phone", None)
```

### 7.6 Testing membership

For a dictionary, `in` tests **keys**, not values:

```python
student = {"name": "Ali", "marks": 92}

print("name" in student)  # True
print("Ali" in student)   # False
print(92 in student)      # False
print(92 in student.values())  # True
```

If you need to test a value, use `dictionary.values()` or another appropriate approach.

### 7.7 Getting keys, values, and pairs

```python
student = {"name": "Ali", "age": 17, "marks": 92}

print(student.keys())
print(student.values())
print(student.items())
```

These return dictionary **view objects**, which reflect changes to the dictionary. They are not ordinary lists, although you can turn them into lists when necessary:

```python
keys_as_list = list(student.keys())
```

### 7.8 Iterating through a dictionary

Iterating directly through a dictionary gives its keys:

```python
for key in student:
    print(key)
```

For key-value pairs, use `.items()`:

```python
for key, value in student.items():
    print(key, "→", value)
```

### 7.9 Dictionary insertion order

In modern Python, dictionary iteration preserves insertion order as a language guarantee (Python 3.7+). Updating an existing key does not normally move it to the end; deleting it and adding it again creates a new insertion position.

Do not assume that a **set** has the same ordering guarantee.

### 7.10 Merging dictionaries

The `update()` method adds entries from another mapping and overwrites values for keys that already exist:

```python
profile = {"name": "Ali", "city": "Lahore"}
changes = {"city": "Faisalabad", "course": "Python"}

profile.update(changes)
print(profile)
```

On Python 3.9+, the `|` operator creates a merged dictionary:

```python
combined = {"a": 1, "b": 2} | {"b": 99, "c": 3}
print(combined)  # {'a': 1, 'b': 99, 'c': 3}
```

For overlapping keys, the value from the right-hand dictionary wins.

---

## 8. Hashability and valid dictionary keys

An object is **hashable** when it has a hash value that remains stable during its lifetime and can be compared for equality in a way that follows Python's hashing rules. Hashable objects can be used as dictionary keys and set elements.

### 8.1 Common hashable types

Typical examples include:

```python
person_name = "Ali"      # str
student_id = 101          # int
ratio = 2.5               # float
point = (3, 4)            # tuple of hashable elements
immutable_tags = frozenset({"python", "coding"})
```

A tuple is hashable only if all the tuple's elements are hashable.

### 8.2 Lists cannot be keys

This is invalid:

```python
# Invalid: list is unhashable
# info = {[1, 2]: "coordinates"}
```

Lists are mutable: you can change their contents after creating them. They are therefore unhashable.

A tuple can be used instead, provided all its elements are hashable:

```python
info = {(1, 2): "coordinates"}
print(info[(1, 2)])  # coordinates
```

But this tuple is not hashable because it contains a list:

```python
# Invalid: the tuple contains an unhashable list
# info = {(1, [2, 3]): "data"}
```

### 8.3 Keys and values have different rules

Keys need to be hashable. Values do not.

```python
data = {
    "numbers": [1, 2, 3],
    "settings": {"theme": "dark"},
}
```

This is valid: the keys are strings; the values happen to be a list and a dictionary.

### 8.4 `set` elements also need to be hashable

```python
valid = {1, "Ali", (2, 3)}

# Invalid because lists are unhashable:
# invalid = {[1, 2], [3, 4]}
```

Use a `frozenset` when you need a set-like value that can itself be a dictionary key or an element of another set.

---

## 9. The equality-and-hash contract

Hashing and equality work together.

The most important rule is:

> **If two objects compare equal, they must have the same hash value.**

The reverse is not required: two objects can have the same hash and still compare unequal.

Conceptually:

```text
same hash  does NOT necessarily mean equal objects
same equality result (equal) DOES require same hash
```

### 9.1 Why does the rule matter?

A dictionary or set uses hash information to find where an object may be stored, then uses equality checks where necessary. If two equal objects could have different hashes, a lookup could search the wrong places and fail to find an equal key.

### 9.2 Equal numeric values

Python demonstrates the equality/hash relationship here:

```python
print(1 == True)          # True
print(hash(1) == hash(True))  # True

example = {1: "first", True: "second"}
print(example)            # One entry; True and 1 compare equal
print(len(example))       # 1
```

This surprises people because `bool` is a subclass of `int` in Python, and `True == 1` evaluates to `True`.

### 9.3 Custom classes: an advanced warning

If you implement `__eq__()` in a custom class, you need to consider the hashing contract. Python often makes instances of a class unhashable when you define equality without defining a compatible hash method. Do not make mutable objects hashable based on attributes that can change while the objects are being used as dictionary keys or set elements.

For now, rely on built-in hashable types unless you have a clear reason to define custom hashing.

---

## 10. Python sets (`set`) and `frozenset`

A set stores unique, hashable elements. It is especially useful for membership checks, deduplication, and mathematical set operations.

### 10.1 Creating sets

```python
numbers = {1, 2, 3, 4}
letters = set(["a", "b", "a", "c"])
empty_set = set()
empty_dictionary = {}

print(letters)  # Contains a, b, c; display order is not guaranteed
```

Remember: `{}` is an empty dictionary, while `set()` is an empty set.

### 10.2 Duplicates are removed

```python
numbers = {1, 2, 2, 3, 3, 3}
print(len(numbers))  # 3
```

Sets store a single occurrence of each distinct value according to equality and hashing.

### 10.3 Adding and removing elements

```python
languages = {"Python", "Java"}

languages.add("C++")       # Adds one item
languages.update(["Go", "Rust"])  # Adds items from an iterable
languages.discard("Ruby")  # Does not raise an error if absent
languages.remove("Java")   # Raises KeyError if absent
popped = languages.pop()    # Removes and returns an arbitrary element
languages.clear()           # Removes everything
```

Because sets do not promise an order, do not use `pop()` when you require a specific element.

### 10.4 Membership testing

```python
blocked_users = {"user1", "user2", "user3"}

if "user2" in blocked_users:
    print("Access denied")
```

Set membership is typically O(1) on average.

### 10.5 Mathematical operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Union: {1, 2, 3, 4, 5}
print(a & b)  # Intersection: {3}
print(a - b)  # Difference: {1, 2}
print(a ^ b)  # Symmetric difference: {1, 2, 4, 5}
```

- **Union (`|`)**: elements that are in either set.
- **Intersection (`&`)**: elements common to both sets.
- **Difference (`-`)**: elements in the left set but not the right set.
- **Symmetric difference (`^`)**: elements in either set, but not both.

The corresponding methods are `.union()`, `.intersection()`, `.difference()`, and `.symmetric_difference()`.

### 10.6 Subsets and supersets

```python
required = {"Python", "Git"}
skills = {"Python", "Git", "SQL"}

print(required <= skills)  # True: required is a subset of skills
print(skills >= required)  # True: skills is a superset of required
```

You can also use `.issubset()` and `.issuperset()` for more explicit code.

### 10.7 `frozenset`

A `frozenset` is an immutable set. Its contents cannot be added to or removed from after creation, and it can be hashable if its elements are hashable.

```python
permissions = frozenset({"read", "write"})
lookup = {permissions: "editor"}
print(lookup[permissions])  # editor
```

Use a normal `set` when you need to change the collection; consider `frozenset` for immutable set-like values.

---

## 11. Dictionary and set comprehensions

Comprehensions let you build collections concisely.

### 11.1 Dictionary comprehension

General structure:

```python
{key_expression: value_expression for item in iterable}
```

Example:

```python
squares = {number: number * number for number in range(1, 6)}
print(squares)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

With a condition:

```python
even_squares = {
    number: number * number
    for number in range(1, 11)
    if number % 2 == 0
}
```

### 11.2 Set comprehension

General structure:

```python
{expression for item in iterable}
```

Example:

```python
unique_lengths = {len(word) for word in ["cat", "tiger", "dog", "lion"]}
print(unique_lengths)  # Contains 3, 4, and 5
```

### 11.3 How to tell them apart

```python
{x: x * x for x in range(5)}  # Dictionary: key:value pairs
{x * x for x in range(5)}     # Set: one expression per item
```

### 11.4 Preserve order while removing duplicates

A normal set is great when order does not matter. If you need unique hashable items in first-seen order, you can use `dict.fromkeys()`:

```python
items = ["Python", "Java", "Python", "C++", "Java"]
unique_in_order = list(dict.fromkeys(items))
print(unique_in_order)  # ['Python', 'Java', 'C++']
```

This works because dictionaries preserve insertion order and dictionary keys must be unique. The input items must be hashable.

---

## 12. Common real-world patterns

### 12.1 Frequency counting

Count how many times each item appears:

```python
numbers = [1, 2, 2, 3, 3, 3]
frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

print(frequency)  # {1: 1, 2: 2, 3: 3}
```

Understand this line carefully:

```python
frequency[number] = frequency.get(number, 0) + 1
```

1. Ask the dictionary for the existing count.
2. If the key is missing, use `0` as the starting count.
3. Add `1`.
4. Store the updated count under the key.

Alternative explicit form:

```python
for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1
```

The explicit form can be easier to understand when you are new to the pattern.

### 12.2 Counting words

```python
sentence = "python is useful and python is fun"
frequency = {}

for word in sentence.split():
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)
```

This simple version splits on whitespace and is case-sensitive. A word such as `Python` will be different from `python`, and punctuation may remain attached to words. The mini project later improves the text cleanup.

### 12.3 Grouping records

```python
students = [
    ("Ali", "ICS"),
    ("Ahmed", "Pre-Engineering"),
    ("Hamza", "ICS"),
    ("Bilal", "ICS"),
]

groups = {}

for name, program in students:
    if program not in groups:
        groups[program] = []
    groups[program].append(name)

print(groups)
# {'ICS': ['Ali', 'Hamza', 'Bilal'],
#  'Pre-Engineering': ['Ahmed']}
```

The dictionary maps each category to a list of matching records.

### 12.4 Detecting duplicates

```python
def has_duplicates(items):
    seen = set()

    for item in items:
        if item in seen:
            return True
        seen.add(item)

    return False

print(has_duplicates([1, 2, 3, 2]))  # True
print(has_duplicates([1, 2, 3, 4]))  # False
```

The items need to be hashable for this version. The function can stop as soon as it discovers the first duplicate.

### 12.5 Comparing two collections

```python
registered = {"Ali", "Ahmed", "Hamza"}
attended = {"Ahmed", "Hamza", "Bilal"}

print("Attended and registered:", registered & attended)
print("Registered but absent:", registered - attended)
print("Attended but not registered:", attended - registered)
```

Set operations make overlap and difference tasks straightforward.

### 12.6 Nested dictionaries as a small in-memory database

```python
students = {
    101: {"name": "Ali", "marks": 92},
    102: {"name": "Ahmed", "marks": 85},
    103: {"name": "Hamza", "marks": 78},
}

student_id = 101
student = students.get(student_id)

if student is None:
    print("Student not found")
else:
    print("Name:", student["name"])
    print("Marks:", student["marks"])
```

The outer dictionary finds a student by ID. The inner dictionary stores that student's fields. This is a useful structure for learning, though a real application's persistent data may belong in a database.

### 12.7 Caching and memoization: the basic idea

A **cache** saves previously computed results so the program may reuse them. A dictionary can serve as a simple cache:

```python
cache = {}

def expensive_square(number):
    if number in cache:
        print("Cache hit")
        return cache[number]

    print("Computing")
    result = number * number  # A stand-in for an expensive operation
    cache[number] = result
    return result

print(expensive_square(8))  # Computing, then 64
print(expensive_square(8))  # Cache hit, then 64
```

For this simple square function, caching is unnecessary in practice; it demonstrates the pattern. Python also offers tools such as `functools.lru_cache` for suitable function results.

---

## 13. Time complexity and performance

Big-O notation describes how the amount of work grows as the input size grows. For dictionaries and sets, the following are typical average-case expectations:

| Operation | Typical average-case complexity | Notes |
|---|---:|---|
| Dictionary lookup by key | O(1) | `value = data[key]` when key exists |
| Dictionary insertion/update | O(1) | Occasional resizing takes extra work |
| Dictionary deletion by key | O(1) | Average case |
| Set membership | O(1) | `item in values` |
| Set insertion | O(1) | Average case |
| Set removal | O(1) | Average case |
| Search in an ordinary unsorted list | O(n) | May inspect many items |
| Sort `n` items | O(n log n) | Typical comparison sort behavior |

### 13.1 Why not promise O(1) always?

Hash tables can experience collisions. In unusual or adversarial conditions, individual operations may take longer; worst-case lookup can be O(n). Insertions may also trigger a resizing operation. The average-case description is still useful for deciding when a dictionary or set is a good tool.

### 13.2 Choose the right structure

| Requirement | Good starting choice |
|---|---|
| Preserve a sequence and access items by position | `list` or `tuple` |
| Associate an ID/key with a value | `dict` |
| Store unique values and test membership | `set` |
| Store unique values as an immutable, hashable group | `frozenset` |
| Keep a simple ordered sequence of key-value pairs with duplicates allowed | A list of tuples or records |

Do not choose a dictionary just because it is fast. Choose the structure that matches the problem.

---

## 14. Common mistakes and debugging

### Mistake 1: Using a list as a key

```python
# Raises TypeError: unhashable type: 'list'
# data = {[1, 2]: "value"}
```

**Fix:** Use a tuple if the contents are hashable:

```python
data = {(1, 2): "value"}
```

### Mistake 2: Assuming `.get()` inserts a missing key

```python
data = {}
print(data.get("count", 0))  # 0
print(data)                   # {}
```

`get()` returns a fallback; it does not insert it. Use assignment or a suitable method if you intend to store a value.

### Mistake 3: Checking for values with `in` on a dictionary

```python
data = {"name": "Ali"}
print("Ali" in data)          # False
print("Ali" in data.values()) # True
```

### Mistake 4: Assuming set order

```python
values = {10, 2, 7, 2}
print(values)
```

The set contains unique values, but you should not rely on a particular display or iteration order. Sort the values explicitly if sorted output is required:

```python
print(sorted(values))
```

### Mistake 5: Depending on `hash()` across program runs

Hash values for strings can vary across runs. Do not save a built-in hash and expect it to be a stable external ID.

### Mistake 6: Thinking a hash match guarantees equal keys

Different values may have identical hashes. Hash equality alone does not prove object equality.

### Mistake 7: Mutating a dictionary's size during iteration

Adding or removing entries while iterating through the same dictionary can raise `RuntimeError` or lead to logic problems. Iterate over a snapshot when appropriate:

```python
data = {"a": 1, "b": 2, "c": 3}

for key in list(data):
    if key == "b":
        del data[key]

print(data)  # {'a': 1, 'c': 3}
```

### Mistake 8: Using `{}` for an empty set

```python
not_a_set = {}
empty_set = set()
```

`not_a_set` is a dictionary.

### Mistake 9: Forgetting case and punctuation during text counting

`"Python"`, `"python"`, and `"python,"` are different strings. Normalize text if the application's rules treat them as the same word.

---

## 15. Mini project: Word Analyzer

### Goal

Create a small program that accepts a sentence and reports:

- Total number of words.
- Number of unique words.
- Frequency of each word.
- The most frequent word or words.

This project uses a list-like sequence of tokenized words, a dictionary for frequencies, and a set-like view of unique words through dictionary keys.

### Version 1 — Simple implementation

```python
sentence = input("Enter a sentence: ").strip().lower()
words = sentence.split()

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Total words:", len(words))
print("Unique words:", len(frequency))
print("Frequency:")
for word, count in frequency.items():
    print(f"{word}: {count}")

if frequency:
    highest_count = max(frequency.values())
    most_frequent = [
        word for word, count in frequency.items()
        if count == highest_count
    ]
    print("Most frequent:", ", ".join(most_frequent))
else:
    print("Most frequent: none (no words entered)")
```

Example input:

```text
Python is easy and Python is powerful
```

Example output (formatting may vary):

```text
Total words: 7
Unique words: 5
Frequency:
python: 2
is: 2
easy: 1
and: 1
powerful: 1
Most frequent: python, is
```

This simple implementation normalizes letter case, but punctuation can remain attached to a word. For example, `"python,"` and `"python"` would still count separately.

### Version 2 — Normalize punctuation with `re`

The following version extracts sequences of letters or digits. It uses Python's standard-library `re` module.

```python
import re

sentence = input("Enter a sentence: ").lower()
words = re.findall(r"\b[\w']+\b", sentence)

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Total words:", len(words))
print("Unique words:", len(frequency))
print("Frequency:")
for word, count in frequency.items():
    print(f"{word}: {count}")

if frequency:
    highest_count = max(frequency.values())
    most_frequent = [
        word for word, count in frequency.items()
        if count == highest_count
    ]
    print("Most frequent:", ", ".join(most_frequent))
else:
    print("No words were found.")
```

This is a learning project, not a complete linguistic tokenizer. Different languages, apostrophes, hyphenated words, and Unicode text may need more careful rules depending on the project.

### Extension challenges

1. Print words from highest frequency to lowest frequency.
2. Ignore common words such as `the`, `is`, and `and` when finding the most frequent meaningful word.
3. Display only words that appear at least twice.
4. Put the analyzer into a function named `analyze_text(sentence)`.
5. Add a test for an empty sentence.

---

## 16. Practice exercises

Try the exercises before reading the answer key. Write and run the code yourself where possible.

### Exercise 1 — Predict the dictionary

```python
data = {"a": 10, "b": 20}
data["a"] = 50
data["c"] = 30
print(data)
```

What is printed, and why?

### Exercise 2 — Set uniqueness

```python
items = {1, 2, 2, 3, 3, 3, 4}
print(len(items))
```

Predict the output.

### Exercise 3 — Safe lookup

```python
scores = {"Ali": 90}
print(scores.get("Ahmed", 0))
print(scores)
```

What two lines are printed? Does `.get()` add Ahmed?

### Exercise 4 — Intersection

```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)
```

Predict the result.

### Exercise 5 — Frequency counter

Given:

```python
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
```

Build a dictionary with each number as a key and its frequency as the value.

### Exercise 6 — Unique values in order

Given:

```python
languages = ["Python", "Java", "Python", "C++", "Java"]
```

Create a list with duplicates removed while preserving the first-seen order.

### Exercise 7 — Hashable or not?

For each object, decide whether it can be a dictionary key:

1. `"Ali"`
2. `42`
3. `[1, 2]`
4. `(1, 2)`
5. `(1, [2, 3])`
6. `frozenset({1, 2})`

### Exercise 8 — Dictionary membership

```python
profile = {"name": "Ali", "marks": 95}
print("Ali" in profile)
print("Ali" in profile.values())
```

Explain the two results.

### Exercise 9 — Grouping

Given:

```python
records = [
    ("Ali", "ICS"),
    ("Ahmed", "Pre-Engineering"),
    ("Hamza", "ICS"),
]
```

Build a dictionary mapping each program to a list of student names.

### Exercise 10 — Complexity reasoning

You need to test membership repeatedly for a large collection of unique, hashable IDs. Explain why a `set` can be more suitable than repeatedly scanning a list. Mention the average-case complexity and one caveat.

### Exercise 11 — Mini-project extension

Modify the Word Analyzer to print only words that appear at least twice. Test it with:

```text
python is useful and python is fun
```

### Exercise 12 — Explain in your own words

Explain why two different keys can have the same hash without breaking a dictionary, and why equal keys must have equal hashes.

---

## 17. Solutions and explanations

### Solution 1

```python
{'a': 50, 'b': 20, 'c': 30}
```

The value for `"a"` is updated; `"c"` is added as a new key. Dictionaries preserve insertion order, so the original key positions remain in order and the new key appears at the end.

### Solution 2

```text
4
```

A set stores one occurrence of each distinct value: `1`, `2`, `3`, and `4`.

### Solution 3

```text
0
{'Ali': 90}
```

`.get("Ahmed", 0)` returns `0` because the key is missing. It does not insert the key.

### Solution 4

```text
{3}
```

The intersection contains items present in both sets; here, only `3` is shared.

### Solution 5

```python
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

print(frequency)  # {1: 1, 2: 2, 3: 3, 4: 4}
```

Each loop iteration increments the count for the current number.

### Solution 6

```python
languages = ["Python", "Java", "Python", "C++", "Java"]
unique_languages = list(dict.fromkeys(languages))
print(unique_languages)  # ['Python', 'Java', 'C++']
```

Dictionary keys are unique, and their insertion order is preserved. The input strings are hashable.

### Solution 7

| Object | Can it be a key? | Explanation |
|---|---|---|
| `"Ali"` | Yes | Strings are hashable. |
| `42` | Yes | Integers are hashable. |
| `[1, 2]` | No | Lists are mutable and unhashable. |
| `(1, 2)` | Yes | Tuple elements are hashable. |
| `(1, [2, 3])` | No | A tuple is hashable only if every element is hashable. |
| `frozenset({1, 2})` | Yes | A frozenset with hashable elements is hashable. |

### Solution 8

```text
False
True
```

`in` on a dictionary checks keys, so it checks whether `"Ali"` is a key. The second expression checks the dictionary's values.

### Solution 9

```python
records = [
    ("Ali", "ICS"),
    ("Ahmed", "Pre-Engineering"),
    ("Hamza", "ICS"),
]

groups = {}
for name, program in records:
    if program not in groups:
        groups[program] = []
    groups[program].append(name)

print(groups)
# {'ICS': ['Ali', 'Hamza'], 'Pre-Engineering': ['Ahmed']}
```

Each category becomes a key, and its value is a list that collects names in that category.

### Solution 10

A list membership test may scan up to `n` elements, so it is O(n). Set membership is typically O(1) on average because hashing helps locate an element. One caveat is that collisions and unusual worst-case situations can make an operation slower, and the elements must be hashable.

### Solution 11

After building `frequency`, print entries whose counts are at least two:

```python
for word, count in frequency.items():
    if count >= 2:
        print(f"{word}: {count}")
```

For the sample, `python: 2` and `is: 2` should be displayed. `and` and `fun` appear only once.

### Solution 12

A hash table handles collisions by following a collision-resolution procedure and checking keys for equality where needed. A hash is a way to help locate an entry, not a unique identifier. Equal objects must have equal hashes so that an equal key can be found using the expected hash-based lookup process.

---

## 18. Day 23 knowledge check

You should be able to answer these without looking back:

- [ ] What problem does hashing help solve?
- [ ] How are a map, a hash map, a hash table, and `dict` related?
- [ ] How is Python's `map()` function different from a hash map?
- [ ] What is a collision?
- [ ] Why can two objects share a hash but still be unequal?
- [ ] Why must equal objects have the same hash?
- [ ] Why can a tuple be hashable while a list is not?
- [ ] What does `dictionary.get(key, default)` do when a key is missing?
- [ ] Does `key in dictionary` check keys or values?
- [ ] What are the differences between a `set` and a `frozenset`?
- [ ] When would you use a dictionary instead of a list?
- [ ] Why are hash-table operations described as O(1) on average rather than guaranteed O(1) in every case?

### Suggested completion standard

Before moving on, aim to:

1. Complete Exercises 1–9 without copying the solutions.
2. Explain hashing and collisions in your own words.
3. Build and run the Word Analyzer mini project.
4. Identify at least one place in a real project where a dictionary or set would simplify the code.

You do not need to memorize CPython's internal implementation. Understand the core ideas and be able to use Python's collections correctly.

---

## 19. Final cheat sheet

### Dictionary (`dict`)

```python
data = {"Ali": 92}
data["Ahmed"] = 85
print(data.get("Missing", 0))
print("Ali" in data)       # Checks keys
for key, value in data.items():
    print(key, value)
```

- Stores key-value pairs.
- Keys must be hashable; values may be mutable.
- Dictionary preserves insertion order in modern Python.
- Average-case lookup, insertion, and deletion are O(1).

### Set (`set`)

```python
items = {1, 2, 2, 3}
items.add(4)
print(2 in items)
print({1, 2} | {2, 3})
```

- Stores unique, hashable elements.
- Set order is not guaranteed.
- Useful for membership, uniqueness, and set operations.
- Average-case membership, insertion, and removal are O(1).

### Main concepts

```text
Hashing      → calculate a hash value for a hashable object
Hash table   → hash-based storage structure
Hash map     → map implemented using hashing
Map          → key-to-value abstraction
Python dict  → built-in mapping type
Python set   → collection of unique hashable elements
Collision    → two keys conflict at a hash-table location
Hashability  → eligibility to be used as a dict key or set element
```

### Remember

- Hashes are not guaranteed to be unique.
- Equal objects must have equal hashes.
- Hashes for strings may differ between Python processes.
- `hash()` is not a password-hashing or cryptographic-security tool.
- Use `set()` for an empty set; `{}` is an empty dictionary.

---

## 20. Next step in the roadmap

**Day 23 (current):** Hashing, Hash Tables, Hash Maps, Dictionaries, and Sets.  
**Day 24 (planned):** `*args` and `**kwargs` deep dive.

Day 24 returns to function design. Moving hashing into Day 23 keeps today's data-structures learning focused and avoids trying to study two large topics at once.

---

**Python Journey — Day 23**  
*Learn the data structure, understand the trade-offs, and then use it to solve a real problem.*
