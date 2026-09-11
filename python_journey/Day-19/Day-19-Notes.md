# Day 19 — Iterators & Generators

## Learning Goal

Understand how Python produces values one at a time, how the iterator protocol works, and how generators let us write memory-efficient code for large or streaming data.

---

## 1. Iterable vs Iterator

### Iterable

An **iterable** is an object that can return its members one at a time.

Common iterables:

- `list`
- `tuple`
- `str`
- `dict`
- `set`
- `range`
- files

Example:

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

A `for` loop can work with `numbers` because the list is iterable.

### Iterator

An **iterator** is an object that keeps track of its current position and produces the next value when requested.

```python
numbers = [10, 20, 30]
iterator = iter(numbers)

print(next(iterator))  # 10
print(next(iterator))  # 20
print(next(iterator))  # 30
```

After the final value:

```python
next(iterator)
```

raises:

```text
StopIteration
```

---

## 2. `iter()`

`iter()` obtains an iterator from an iterable.

```python
names = ["Ali", "Ahmed", "Usman"]
name_iterator = iter(names)
```

Think of it as:

```text
iterable -> iter() -> iterator
```

---

## 3. `next()`

`next()` asks an iterator for its next value.

```python
numbers = iter([1, 2, 3])

print(next(numbers))
print(next(numbers))
print(next(numbers))
```

Output:

```text
1
2
3
```

The iterator remembers where it stopped.

You can also provide a default value:

```python
numbers = iter([1, 2])

print(next(numbers, "Finished"))
print(next(numbers, "Finished"))
print(next(numbers, "Finished"))
```

Output:

```text
1
2
Finished
```

This avoids `StopIteration` for that call.

---

## 4. The Iterator Protocol

An iterator follows Python's iterator protocol.

It must provide:

```python
__iter__()
__next__()
```

An iterator's `__iter__()` normally returns itself:

```python
class Counter:
    def __init__(self, limit):
        self.current = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            value = self.current
            self.current += 1
            return value
        raise StopIteration
```

Usage:

```python
counter = Counter(3)

for value in counter:
    print(value)
```

Output:

```text
0
1
2
```

### Why `StopIteration` matters

It tells Python:

> There are no more values to produce.

A `for` loop handles this internally, which is why you normally do not see the exception when using a loop.

---

## 5. How a `for` Loop Actually Works

This:

```python
for item in items:
    print(item)
```

is conceptually similar to:

```python
iterator = iter(items)

while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break
```

This is one of the most important ideas in today's lesson.

---

# 6. Creating a Custom Iterator

A custom iterator can be useful when an object needs to produce values according to custom rules.

Example: countdown iterator.

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration

        value = self.current
        self.current -= 1
        return value


for number in Countdown(5):
    print(number)
```

Output:

```text
5
4
3
2
1
```

### Important engineering point

Custom iterators are powerful, but they can require more code. Python generators often provide the same behavior more simply.

---

# 7. Generators

A **generator** is a special kind of iterator that produces values lazily.

The easiest way to create one is with `yield`.

```python
def count_up_to(limit):
    number = 1

    while number <= limit:
        yield number
        number += 1
```

Usage:

```python
numbers = count_up_to(5)

print(next(numbers))
print(next(numbers))
print(next(numbers))
```

Output:

```text
1
2
3
```

---

# 8. `yield` vs `return`

### `return`

`return` ends a function and sends back a result.

```python
def square(number):
    return number * number
```

### `yield`

`yield` pauses a generator and sends back one value.

When the generator is resumed, execution continues from where it paused.

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

```python
generator = numbers()

print(next(generator))
print(next(generator))
print(next(generator))
```

The generator keeps its execution state between calls.

---

# 9. Generator Execution Model

Consider:

```python
def demo():
    print("A")
    yield 1
    print("B")
    yield 2
    print("C")
```

Then:

```python
g = demo()
```

At this point, the function body has not run through normally.

Now:

```python
print(next(g))
```

Output:

```text
A
1
```

Another call:

```python
print(next(g))
```

Output:

```text
B
2
```

The generator resumes after the previous `yield`.

---

# 10. Lazy Evaluation

Generators use **lazy evaluation**.

Instead of generating all values immediately, they produce values only when requested.

Example:

```python
def large_numbers():
    for number in range(1, 1_000_001):
        yield number
```

The generator does not need to create one million generated values in a list first.

You can consume values one at a time:

```python
numbers = large_numbers()

print(next(numbers))
print(next(numbers))
```

This can significantly reduce memory usage.

---

# 11. List vs Generator

### List

```python
squares = [number * number for number in range(1_000_000)]
```

The list stores all results.

### Generator expression

```python
squares = (number * number for number in range(1_000_000))
```

The generator produces each result when needed.

The syntax difference is:

```text
[ ... ]  -> list comprehension
( ... )  -> generator expression
```

---

# 12. Generator Expressions

A generator expression is a compact way to create a generator.

```python
numbers = (number * 2 for number in range(5))

for number in numbers:
    print(number)
```

Output:

```text
0
2
4
6
8
```

They are especially useful when you need to process data once rather than store every result.

---

# 13. Generator Functions with Conditions

```python
def even_numbers(limit):
    for number in range(limit + 1):
        if number % 2 == 0:
            yield number
```

Usage:

```python
for number in even_numbers(10):
    print(number)
```

---

# 14. Infinite Generators

Generators can represent sequences that have no natural end.

```python
def infinite_counter():
    number = 0

    while True:
        yield number
        number += 1
```

Use them carefully:

```python
counter = infinite_counter()

for _ in range(5):
    print(next(counter))
```

Output:

```text
0
1
2
3
4
```

Do not blindly convert an infinite generator into a list:

```python
list(infinite_counter())
```

That would never finish because there is no endpoint.

---

# 15. `yield from`

`yield from` lets one generator delegate to another iterable or generator.

```python
def numbers():
    yield from [1, 2, 3]
    yield from [4, 5]
```

Usage:

```python
for number in numbers():
    print(number)
```

This is equivalent in spirit to yielding the values individually, but is cleaner for delegation.

---

# 16. Generator Pipelines

Generators can be chained to build processing pipelines.

```python
def read_numbers():
    for number in range(1, 11):
        yield number


def only_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number


def square(numbers):
    for number in numbers:
        yield number * number
```

Pipeline:

```python
numbers = read_numbers()
evens = only_even(numbers)
squares = square(evens)

for value in squares:
    print(value)
```

Output:

```text
4
16
36
64
100
```

The data moves through stages one value at a time.

This pattern is highly relevant to:

- log processing
- CSV processing
- ETL pipelines
- API pagination
- data science workflows
- machine learning data pipelines
- large file processing
- streaming systems

---

# 17. Generator for Large Files

For a large text file, avoid loading the entire file into memory when you only need to process lines one at a time.

```python
def read_lines(filename):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()
```

Usage:

```python
for line in read_lines("data.txt"):
    print(line)
```

This lets the program process the file incrementally.

---

# 18. Generator `.send()` — Introduction

Generators can also receive values using `.send()`.

Example:

```python
def receiver():
    while True:
        value = yield
        print("Received:", value)
```

Start it:

```python
r = receiver()
next(r)
```

Then send a value:

```python
r.send("Hello")
```

Output:

```text
Received: Hello
```

This is an advanced feature. For Day 19, understand the concept rather than trying to use it everywhere.

---

# 19. Generator `return`

A generator can use `return` to finish.

```python
def sample():
    yield 1
    yield 2
    return "Done"
```

When the generator finishes, the return value is attached to the resulting `StopIteration` exception.

Normal `for` loops simply stop.

---

# 20. Generator Advantages

Generators are useful because they can provide:

### Memory efficiency

Values are produced one at a time rather than stored all at once.

### Lazy execution

Work happens only when values are requested.

### Readability

Complex streaming logic can often be expressed clearly with `yield`.

### Composability

Generators can be chained into data-processing pipelines.

### Scalability

They are often better suited to large datasets and streams than eagerly building huge lists.

---

# 21. When Not to Use Generators

A generator is not automatically better than a list.

Use a list when you need to:

- access items repeatedly
- use indexing frequently
- know the complete collection immediately
- iterate over the data multiple times
- keep the computed results in memory intentionally

Use a generator when you primarily need:

- one-pass processing
- lazy computation
- streaming behavior
- lower memory usage

---

# 22. Important Comparison

| Concept | Main idea |
|---|---|
| Iterable | Can provide values one by one |
| Iterator | Produces the next value and tracks state |
| `iter()` | Gets an iterator from an iterable |
| `next()` | Requests the next value |
| `StopIteration` | Signals that iteration is finished |
| Generator | Iterator created conveniently, usually with `yield` |
| `yield` | Produces a value and pauses execution |
| Generator expression | Compact lazy expression using `(...)` |
| Lazy evaluation | Compute values only when needed |
| `yield from` | Delegate yielding to another iterable/generator |

---

# 23. Common Mistakes

## Mistake 1 — Calling `next()` on a list

Wrong:

```python
numbers = [1, 2, 3]
next(numbers)
```

Correct:

```python
numbers = iter([1, 2, 3])
next(numbers)
```

## Mistake 2 — Forgetting that generators are consumed

```python
g = (x for x in range(3))

print(list(g))
print(list(g))
```

The second result is empty because the generator was already exhausted.

## Mistake 3 — Treating generators like lists

A generator does not normally support indexing like:

```python
generator[0]
```

Instead, consume it with `next()`, a loop, or another iterator-consuming operation.

## Mistake 4 — Accidentally creating an infinite loop

Be careful with `while True` generators and always control consumption.

---

# 24. Practical Examples

## Example A — Fibonacci Generator

```python
def fibonacci(limit):
    a, b = 0, 1

    for _ in range(limit):
        yield a
        a, b = b, a + b


for number in fibonacci(10):
    print(number)
```

## Example B — Temperature Converter Pipeline

```python
def celsius_values():
    for value in [0, 10, 20, 30]:
        yield value


def to_fahrenheit(values):
    for celsius in values:
        yield (celsius * 9 / 5) + 32


for fahrenheit in to_fahrenheit(celsius_values()):
    print(fahrenheit)
```

## Example C — Filter Long Words

```python
def long_words(words, minimum_length):
    for word in words:
        if len(word) >= minimum_length:
            yield word
```

---

# 25. Practice Tasks

## Task 1 — Countdown Generator

Create:

```python
countdown(10)
```

that yields numbers from `10` down to `1`.

## Task 2 — Multiplication Table Generator

Create a generator that yields the first `n` multiples of a number.

Example:

```python
multiples(7, 5)
```

Expected values:

```text
7
14
21
28
35
```

## Task 3 — Even Number Generator

Generate all even numbers from `0` to a supplied maximum.

## Task 4 — File Line Generator

Create a generator that reads a file one line at a time and skips blank lines.

## Task 5 — Generator Pipeline

Build three generators:

```text
numbers -> filter even -> square
```

Then test the pipeline with `range(1, 21)`.

---

# 26. Mini Project — Log Stream Processor

Create a project that simulates processing a large application log without loading all records into a list.

### Requirements

Create generators that:

1. read log lines
2. filter only `ERROR` lines
3. extract the message
4. count or display the resulting errors

Example log format:

```text
INFO: User logged in
ERROR: Database connection failed
INFO: Request completed
ERROR: File not found
```

### Suggested structure

```text
Day-19/
├── notes.md
├── README.md
├── practice/
│   ├── iterator_practice.py
│   └── generator_practice.py
└── project/
    └── log_stream_processor.py
```

### Engineering goal

Focus on **streaming the data through the pipeline** rather than building unnecessary intermediate lists.

---

# 27. Interview Questions

### Q1. What is an iterable?

An object capable of returning its elements one at a time through iteration.

### Q2. What is an iterator?

An object implementing the iterator protocol, especially `__iter__()` and `__next__()`.

### Q3. What does `next()` do?

It requests the next value from an iterator.

### Q4. What happens when an iterator has no more values?

It raises `StopIteration`.

### Q5. What is a generator?

A convenient way to create an iterator, commonly using a function containing `yield`.

### Q6. Why are generators memory efficient?

They usually produce values lazily instead of storing the complete result sequence in memory.

### Q7. What is the difference between `yield` and `return`?

`return` finishes a function; `yield` produces a value while preserving the generator's execution state so it can continue later.

### Q8. What is a generator expression?

A compact lazy expression using parentheses, such as:

```python
(x * x for x in range(10))
```

### Q9. What is `yield from`?

It delegates value production to another iterable or generator.

---

# 28. Day 19 Mastery Checklist

- [ ] I understand iterable vs iterator.
- [ ] I can use `iter()`.
- [ ] I can use `next()`.
- [ ] I understand `StopIteration`.
- [ ] I understand what a `for` loop does internally.
- [ ] I can create a custom iterator.
- [ ] I can write a generator using `yield`.
- [ ] I understand lazy evaluation.
- [ ] I can write a generator expression.
- [ ] I understand why generators save memory.
- [ ] I can build a generator pipeline.
- [ ] I understand `yield from`.
- [ ] I can explain when to choose a list vs a generator.
- [ ] I can complete the Log Stream Processor mini project.

---

# Key Takeaway

> **Iterators give Python a standard way to produce values one at a time, and generators make that pattern simple, lazy, and memory-efficient.**

The engineering mindset for Day 19 is:

```text
Don't always create everything first.
Produce data when it is actually needed.
```
