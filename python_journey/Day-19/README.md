# Day 19 — Iterators & Generators

Part of my **Python Engineering Journey** in the `AI_Engineering` repository.

## 📚 Topic

**Iterators & Generators**

## 🎯 Objective

Learn how Python iteration works internally and how to use iterators, generators, lazy evaluation, and generator pipelines to process data efficiently.

## 🧠 Concepts Covered

- Iterable vs Iterator
- `iter()`
- `next()`
- `StopIteration`
- Iterator protocol
- Custom iterators
- `yield`
- Generator functions
- Generator expressions
- Lazy evaluation
- Infinite generators
- `yield from`
- Generator pipelines
- Streaming large files
- Generator consumption and exhaustion
- Choosing lists vs generators

## 🔍 Why This Matters for AI Engineering

AI and software systems often work with data that is too large or too continuous to process by creating one giant in-memory collection.

Generators provide a foundation for thinking about:

- data pipelines
- large datasets
- streaming data
- log processing
- ETL workflows
- API pagination
- file processing
- machine learning input pipelines

The key idea is to process data **incrementally** instead of unnecessarily loading everything at once.

## 💻 Examples

A simple generator:

```python
def count_up_to(limit):
    number = 1

    while number <= limit:
        yield number
        number += 1
```

Generator expression:

```python
squares = (number * number for number in range(10))
```

Generator pipeline:

```python
def only_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number


def square(numbers):
    for number in numbers:
        yield number * number
```

## 🧪 Practice

Day 19 practice should include:

1. Countdown generator
2. Multiplication-table generator
3. Even-number generator
4. File line generator
5. Generator pipeline

## 🚀 Mini Project

### Log Stream Processor

Build a small streaming log processor that:

1. Reads log records incrementally.
2. Filters `ERROR` records.
3. Extracts useful error messages.
4. Displays or counts the errors.

The project should emphasize generator-based processing instead of unnecessarily storing all records in a list.

## 📁 Suggested Structure

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

## ✅ Completion Criteria

- [ ] Explain iterable vs iterator.
- [ ] Use `iter()` and `next()`.
- [ ] Explain `StopIteration`.
- [ ] Understand the iterator protocol.
- [ ] Build a custom iterator.
- [ ] Write generator functions with `yield`.
- [ ] Use generator expressions.
- [ ] Explain lazy evaluation.
- [ ] Build a generator pipeline.
- [ ] Explain when a generator is preferable to a list.
- [ ] Complete the Log Stream Processor.

## 📈 Engineering Takeaway

```text
Iterable
   ↓
Iterator
   ↓
next()
   ↓
One value at a time
```

And with generators:

```text
data source
    ↓
generator
    ↓
filter generator
    ↓
transform generator
    ↓
consumer
```

This is the foundation of efficient, streaming-style data processing in Python.
