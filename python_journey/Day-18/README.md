
# Day 18 — Advanced Functions

Part of my **Python Engineering / AI Engineering learning journey**.

---

## 🎯 Goal

The goal of Day 18 is to move beyond basic function definitions and understand how Python functions can be used as **reusable, flexible, and composable objects**.

This day focuses on how functions can be passed around, returned from other functions, wrapped with decorators, and used to build flexible data-processing pipelines.

---

## 📚 Topics Covered

- Functions as first-class objects
- Passing functions as arguments
- Returning functions
- Higher-order functions
- `*args`
- `**kwargs`
- Argument unpacking
- Lambda functions
- `map()`
- `filter()`
- `reduce()`
- Closures
- `nonlocal`
- Decorators
- `functools.wraps`
- Recursion
- Function scope
- LEGB rule
- `global`
- Keyword-only arguments
- Positional-only arguments
- Default arguments
- Mutable default argument pitfalls
- Docstrings
- Type hints
- Callback functions
- Function pipelines
- Function design and best practices

---

## 🧠 What I Learned

Day 18 taught me that Python functions are **first-class objects**.

This means functions can be:

```text
Stored
  ↓
Passed
  ↓
Returned
  ↓
Wrapped
  ↓
Combined
  ↓
Reused
````

For example:

```python
def square(x):
    return x ** 2


function = square

print(function(5))
```

Output:

```text
25
```

---

## 🔹 Higher-Order Functions

A higher-order function is a function that accepts another function or returns a function.

Example:

```python
def execute(function, value):
    return function(value)


def square(x):
    return x ** 2


print(execute(square, 5))
```

Output:

```text
25
```

This is an important concept for functional programming and reusable software design.

---

## 🔹 `*args`

`*args` allows a function to accept an arbitrary number of positional arguments.

```python
def add_numbers(*args):

    total = 0

    for number in args:
        total += number

    return total


print(add_numbers(1, 2, 3, 4))
```

Output:

```text
10
```

Inside the function, `args` is a tuple.

---

## 🔹 `**kwargs`

`**kwargs` allows a function to accept an arbitrary number of keyword arguments.

```python
def show_info(**kwargs):

    for key, value in kwargs.items():
        print(f"{key}: {value}")


show_info(
    name="Ali",
    age=17,
    country="Pakistan"
)
```

Inside the function, `kwargs` is a dictionary.

---

## 🔹 Lambda Functions

Lambda functions are small anonymous functions.

```python
square = lambda x: x ** 2

print(square(5))
```

Output:

```text
25
```

They are particularly useful when a small function is needed temporarily, such as with `sort()`, `map()`, and `filter()`.

---

## 🔹 `map()`

`map()` applies a function to every item in an iterable.

```python
numbers = [1, 2, 3, 4, 5]

squares = map(
    lambda x: x ** 2,
    numbers
)

print(list(squares))
```

Output:

```text
[1, 4, 9, 16, 25]
```

---

## 🔹 `filter()`

`filter()` keeps items for which a condition evaluates to true.

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(
    lambda x: x % 2 == 0,
    numbers
)

print(list(even_numbers))
```

Output:

```text
[2, 4, 6]
```

---

## 🔹 `reduce()`

`reduce()` repeatedly combines values into one result.

It is available from the `functools` module.

```python
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(
    lambda a, b: a + b,
    numbers
)

print(result)
```

Output:

```text
10
```

---

## 🔹 Closures

A closure is an inner function that remembers values from its enclosing scope.

Example:

```python
def multiplier(factor):

    def multiply(number):
        return number * factor

    return multiply


double = multiplier(2)
triple = multiplier(3)

print(double(5))
print(triple(5))
```

Output:

```text
10
15
```

Closures are useful for creating customized functions and maintaining state.

---

## 🔹 `nonlocal`

The `nonlocal` keyword allows an inner function to modify a variable from its enclosing function.

```python
def counter():

    count = 0

    def increase():

        nonlocal count

        count += 1

        return count

    return increase


counter_function = counter()

print(counter_function())
print(counter_function())
print(counter_function())
```

Output:

```text
1
2
3
```

---

## 🔹 Decorators

Decorators allow us to modify or extend the behavior of a function without changing the original function's source code.

Example:

```python
def decorator(function):

    def wrapper():

        print("Before function")

        function()

        print("After function")

    return wrapper


@decorator
def greet():

    print("Hello!")


greet()
```

Output:

```text
Before function
Hello!
After function
```

The `@decorator` syntax is essentially syntactic sugar for wrapping the function.

---

## 🔹 Decorators with `*args` and `**kwargs`

Real-world decorators often need to work with functions that accept different arguments.

```python
from functools import wraps


def decorator(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print("Before function")

        result = function(*args, **kwargs)

        print("After function")

        return result

    return wrapper
```

This makes the decorator more flexible.

---

## 🔹 `functools.wraps`

When creating decorators, `functools.wraps` helps preserve metadata from the original function.

```python
from functools import wraps
```

It can preserve information such as:

* function name
* documentation
* metadata

This is considered a good practice when writing decorators.

---

## 🔹 Recursion

Recursion occurs when a function calls itself.

A recursive function normally needs:

1. A base case
2. A recursive case

Example:

```python
def countdown(number):

    if number == 0:
        print("Done!")
        return

    print(number)

    countdown(number - 1)


countdown(5)
```

Output:

```text
5
4
3
2
1
Done!
```

---

## 🔹 Recursive Factorial

```python
def factorial(number):

    if number == 0:
        return 1

    return number * factorial(number - 1)


print(factorial(5))
```

Output:

```text
120
```

Recursion is useful for problems that naturally have recursive structures, but it is not automatically better than iteration.

---

## 🔹 LEGB Scope

Python uses the **LEGB** rule to resolve names.

```text
L → Local
E → Enclosing
G → Global
B → Built-in
```

Python searches these scopes in this order.

Understanding LEGB is particularly important when working with:

* closures
* nested functions
* `global`
* `nonlocal`
* decorators

---

## 🔹 Keyword-Only Arguments

Python can force certain parameters to be passed by keyword.

```python
def create_user(name, *, age, country):

    print(name)
    print(age)
    print(country)
```

Valid:

```python
create_user(
    "Ali",
    age=17,
    country="Pakistan"
)
```

This can make function calls easier to understand.

---

## 🔹 Positional-Only Arguments

Python can also make parameters positional-only using `/`.

```python
def power(base, exponent, /):

    return base ** exponent
```

Valid:

```python
power(2, 3)
```

The parameters before `/` cannot be supplied by keyword.

---

## 🔹 Mutable Default Arguments

One important Python pitfall is using mutable objects such as lists as default arguments.

Avoid:

```python
def add_item(item, items=[]):

    items.append(item)

    return items
```

Prefer:

```python
def add_item(item, items=None):

    if items is None:
        items = []

    items.append(item)

    return items
```

This prevents unexpected state from being shared between calls.

---

## 🔹 Docstrings

Docstrings document what a function does.

```python
def calculate_area(length, width):
    """Return the area of a rectangle."""

    return length * width
```

Docstrings improve readability and maintainability.

---

## 🔹 Type Hints

Type hints communicate expected types.

```python
def add(a: int, b: int) -> int:

    return a + b
```

Type hints help with:

* readability
* IDE support
* static analysis
* documentation
* maintainability

---

# 🤖 Connection to AI Engineering

Advanced functions are an important foundation for AI engineering.

A typical AI/ML pipeline can be organized into reusable functions:

```text
Raw Data
   ↓
load_data()
   ↓
clean_data()
   ↓
transform_data()
   ↓
create_features()
   ↓
train_model()
   ↓
predict()
   ↓
evaluate()
```

Each stage can be represented by a separate function.

This makes large programs:

* modular
* reusable
* testable
* easier to debug
* easier to maintain

---

## 🧠 Why Decorators Matter for AI/Software

Decorators appear throughout the Python ecosystem.

They can be used for:

* logging
* timing
* validation
* authentication
* permissions
* caching
* framework registration

Understanding decorators now will make advanced Python frameworks much easier to understand later.

---

# 🧪 Practice Tasks

## Beginner

### 1. Average with `*args`

Create:

```python
def average(*numbers):
    ...
```

It should return the average of all supplied numbers.

---

### 2. Profile with `**kwargs`

Create a function that accepts arbitrary profile information.

Example:

```python
profile(
    name="Ali",
    age=17,
    country="Pakistan"
)
```

---

### 3. Lambda Cube

Create a lambda function that calculates the cube of a number.

Example:

```python
cube(4)
```

Expected:

```text
64
```

---

### 4. `map()`

Use `map()` to double every number in:

```python
numbers = [1, 2, 3, 4, 5]
```

Expected:

```text
[2, 4, 6, 8, 10]
```

---

### 5. `filter()`

Use `filter()` to keep only numbers greater than `50`.

Example:

```python
numbers = [10, 25, 60, 45, 80, 30]
```

Expected:

```text
[60, 80]
```

---

# 🧩 Intermediate Practice

## 6. Function Processor

Create:

```python
def process(function, numbers):
    ...
```

The function should apply the supplied function to every number.

---

## 7. Power Function Factory

Create:

```python
def power_of(n):
    ...
```

It should return a function.

Example:

```python
square = power_of(2)
cube = power_of(3)

print(square(5))
print(cube(5))
```

Expected:

```text
25
125
```

---

## 8. Logging Decorator

Create a decorator that prints:

```text
Starting...
```

before a function runs and:

```text
Finished.
```

after it finishes.

---

## 9. Recursive Sum

Create:

```python
def recursive_sum(n):
    ...
```

Example:

```python
recursive_sum(5)
```

Expected:

```text
15
```

---

# 🚀 Advanced Challenge

## Function Pipeline

Create a program that:

1. accepts a list of numbers
2. removes negative numbers
3. keeps only even numbers
4. squares the remaining numbers
5. calculates their total

Example:

```python
numbers = [-3, -2, 1, 2, 4, 5, 6]
```

Processing:

```text
[-3, -2, 1, 2, 4, 5, 6]
              ↓
Remove negatives
              ↓
[1, 2, 4, 5, 6]
              ↓
Keep even numbers
              ↓
[2, 4, 6]
              ↓
Square
              ↓
[4, 16, 36]
              ↓
Sum
              ↓
56
```

Try implementing it using:

* normal functions
* `filter()`
* `map()`
* `reduce()`

Then create a simpler version using a comprehension and `sum()`.

---

# 🏆 Day 18 Challenge

Build a small **Function Utility Library**.

Include functions for:

```text
add
subtract
multiply
divide
square
cube
maximum
minimum
average
```

Then create a higher-order function:

```python
calculate(function, ...)
```

that can execute the selected operation.

Add:

* type hints
* docstrings
* error handling
* at least one decorator
* at least one closure

This combines many of the concepts learned during Day 18.

---

# 📁 Suggested Folder Structure

```text
Day-18/
│
├── README.md
├── notes.md
│
└── practice/
    ├── args_kwargs.py
    ├── lambda_functions.py
    ├── map_filter_reduce.py
    ├── closures.py
    ├── decorators.py
    ├── recursion.py
    └── function_pipeline.py
```

Adjust this structure according to the actual files in the repository.

---

# 📈 Learning Progress

```text
Python Foundations
       ↓
Control Flow
       ↓
Data Structures
       ↓
Functions
       ↓
Object-Oriented Programming
       ↓
Exception Handling
       ↓
Advanced Functions  ← Day 18
       ↓
Iterators & Generators
       ↓
Advanced Python
       ↓
AI / ML Engineering
```

---

# 📝 Key Takeaways

The most important lessons from Day 18 are:

* Functions are first-class objects.
* Functions can be passed as arguments.
* Functions can return other functions.
* Higher-order functions enable reusable behavior.
* `*args` handles variable positional arguments.
* `**kwargs` handles variable keyword arguments.
* `*` and `**` can unpack collections.
* Lambda functions are useful for small expressions.
* `map()` transforms data.
* `filter()` selects data.
* `reduce()` combines data.
* Closures allow functions to remember enclosing state.
* `nonlocal` modifies variables in an enclosing scope.
* Decorators extend or modify function behavior.
* `functools.wraps` preserves function metadata.
* Recursion requires a base case.
* Python follows the LEGB scope rule.
* Keyword-only and positional-only parameters can make APIs clearer.
* Mutable default arguments should generally be avoided.
* Type hints and docstrings improve maintainability.
* Good functions should be focused, reusable, readable, and testable.

---

# 🔥 Final Mental Model

Think of a normal function as:

```text
Input
  ↓
Function
  ↓
Processing
  ↓
Output
```

Advanced functions allow functions to work with other functions:

```text
Function A
     ↓
Function B
     ↓
Function C
```

Decorators add behavior around functions:

```text
Original Function
       ↓
Decorator
       ↓
Wrapped Function
```

Closures allow functions to remember configuration:

```text
Function Factory
       ↓
Configured Function
       ↓
Reusable Behavior
```

This flexibility is one of the reasons Python is so powerful for software engineering, automation, data science, and AI.

---

# 📚 Detailed Notes

For the complete explanations, examples, common mistakes, mental models, and practice exercises, see:

**[`notes.md`](notes.md)**

---

# 🚀 Next Step

## Day 19 — Iterators & Generators

The next day will build on Python's function and iterable concepts.

Topics will include:

* Iterables
* Iterators
* `iter()`
* `next()`
* Generator functions
* `yield`
* Generator expressions
* Lazy evaluation
* Memory-efficient processing
* Custom iterators
* Practical iterator/generator projects

---

## 👨‍💻 Project Status

**Day:** 18
**Topic:** Advanced Functions
**Track:** Python Engineering
**Status:** Completed

---

# 🐍 Python Engineering Journey

This repository documents my progress from Python fundamentals toward advanced Python, software engineering, and eventually **AI/ML engineering**.

Each day focuses on learning concepts, writing code, solving problems, and building practical projects.

**Day 18 complete. → Day 19 next.**

```
```
