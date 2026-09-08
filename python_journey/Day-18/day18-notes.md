# Day 18 — Advanced Functions in Python

## Overview

Day 18 focuses on **advanced functions** in Python.

In earlier lessons, functions were mainly used to organize code into reusable blocks. In this lesson, we go much deeper and learn that functions themselves are objects that can be stored, passed to other functions, returned from functions, and modified using decorators.

Topics covered:

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
- Mutable default arguments
- Docstrings
- Type hints
- Callback functions
- Function pipelines
- Best practices
- Practical exercises

---

# 1. Functions as First-Class Objects

One of the most important concepts in Python is that **functions are first-class objects**.

This means a function can be treated like other Python objects.

A function can be:

- assigned to a variable
- stored in a list
- stored in a dictionary
- passed as an argument
- returned from another function

For example:

```python
def greet():
    return "Hello!"

message = greet

print(message())
````

Output:

```text
Hello!
```

Here:

```python
message = greet
```

does not execute the function.

It stores a reference to the function.

To execute it:

```python
message()
```

---

## Function vs Function Call

This distinction is extremely important.

### Function object

```python
greet
```

This refers to the function itself.

### Function call

```python
greet()
```

This executes the function.

Example:

```python
def greet():
    return "Hello"

print(greet)
print(greet())
```

The first line prints information about the function object.

The second line prints:

```text
Hello
```

---

# 2. Assigning Functions to Variables

Because functions are objects, we can assign them to variables.

```python
def square(number):
    return number ** 2

calculate = square

print(calculate(5))
```

Output:

```text
25
```

Both:

```python
square
```

and:

```python
calculate
```

refer to the same function.

---

# 3. Passing Functions as Arguments

A function can receive another function as an argument.

Example:

```python
def square(number):
    return number ** 2


def apply_function(function, value):
    return function(value)


result = apply_function(square, 5)

print(result)
```

Output:

```text
25
```

Here:

```python
square
```

is passed to:

```python
apply_function()
```

The function is not called while passing it.

We pass:

```python
square
```

not:

```python
square()
```

---

# 4. Why Passing Functions Is Useful

Imagine we want to process numbers differently.

We could create many separate functions:

```python
def square(x):
    return x ** 2


def double(x):
    return x * 2


def cube(x):
    return x ** 3
```

Instead of writing separate processing logic, we can create one reusable function:

```python
def process(function, value):
    return function(value)
```

Then:

```python
print(process(square, 5))
print(process(double, 5))
print(process(cube, 5))
```

Output:

```text
25
10
125
```

This makes our code more flexible.

---

# 5. Higher-Order Functions

A **higher-order function** is a function that:

1. accepts another function as an argument, or
2. returns another function.

It can also do both.

Example:

```python
def execute(function, value):
    return function(value)
```

`execute()` is a higher-order function because it accepts a function.

Another example:

```python
def create_function():
    
    def greet():
        return "Hello!"

    return greet
```

This function returns another function.

---

# 6. Returning Functions

A function can return another function.

Example:

```python
def create_greeting():

    def greeting():
        return "Hello from Python!"

    return greeting


say_hello = create_greeting()

print(say_hello())
```

Output:

```text
Hello from Python!
```

Notice:

```python
create_greeting()
```

returns the inner function.

Then:

```python
say_hello()
```

calls that returned function.

---

# 7. `*args`

`*args` allows a function to accept an arbitrary number of positional arguments.

Example:

```python
def add_numbers(*args):

    total = 0

    for number in args:
        total += number

    return total


print(add_numbers(1, 2, 3))
print(add_numbers(10, 20, 30, 40))
```

Output:

```text
6
100
```

---

## What Is `args`?

Inside the function:

```python
args
```

is a tuple.

Example:

```python
def show_args(*args):
    print(args)
    print(type(args))


show_args(10, 20, 30)
```

Output:

```text
(10, 20, 30)
<class 'tuple'>
```

The name `args` is only a convention.

This also works:

```python
def show_numbers(*numbers):
    print(numbers)
```

The important part is:

```python
*
```

---

# 8. Practical `*args` Example

Create a function that calculates the maximum number:

```python
def find_maximum(*numbers):

    if not numbers:
        return None

    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum


print(find_maximum(10, 20, 5, 30, 15))
```

Output:

```text
30
```

The function can receive any number of numbers.

---

# 9. `**kwargs`

`**kwargs` allows a function to accept an arbitrary number of keyword arguments.

Example:

```python
def show_information(**kwargs):
    print(kwargs)


show_information(
    name="Ali",
    age=17,
    country="Pakistan"
)
```

Output:

```text
{'name': 'Ali', 'age': 17, 'country': 'Pakistan'}
```

---

## What Is `kwargs`?

Inside the function:

```python
kwargs
```

is a dictionary.

Example:

```python
def show_info(**kwargs):

    print(type(kwargs))
    print(kwargs)


show_info(name="Ali", age=17)
```

Output:

```text
<class 'dict'>
{'name': 'Ali', 'age': 17}
```

Again, `kwargs` is only a conventional name.

This is also valid:

```python
def show_info(**details):
    print(details)
```

---

# 10. Looping Through `**kwargs`

Because `kwargs` is a dictionary, we can use dictionary methods.

```python
def student_info(**details):

    for key, value in details.items():
        print(f"{key}: {value}")


student_info(
    name="Ali",
    age=17,
    field="Computer Science"
)
```

Output:

```text
name: Ali
age: 17
field: Computer Science
```

---

# 11. Using `*args` and `**kwargs` Together

We can use both.

```python
def display(*args, **kwargs):

    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


display(
    10,
    20,
    30,
    name="Ali",
    age=17
)
```

Output:

```text
Positional arguments: (10, 20, 30)
Keyword arguments: {'name': 'Ali', 'age': 17}
```

---

# 12. Argument Unpacking with `*`

The `*` operator can unpack a list or tuple.

Example:

```python
numbers = [10, 20, 30]

print(*numbers)
```

Output:

```text
10 20 30
```

It can also be used when calling functions.

```python
def add(a, b, c):
    return a + b + c


numbers = [10, 20, 30]

print(add(*numbers))
```

Output:

```text
60
```

Without unpacking:

```python
add(numbers)
```

would pass the entire list as one argument.

---

# 13. Dictionary Unpacking with `**`

A dictionary can be unpacked using `**`.

```python
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")


person = {
    "name": "Ali",
    "age": 17
}


introduce(**person)
```

Output:

```text
My name is Ali and I am 17 years old.
```

The dictionary keys must match the function's parameter names.

---

# 14. Lambda Functions

A lambda function is a small anonymous function.

Syntax:

```python
lambda parameters: expression
```

Example:

```python
square = lambda x: x ** 2

print(square(5))
```

Output:

```text
25
```

---

# 15. Lambda vs Normal Function

Lambda:

```python
square = lambda x: x ** 2
```

Normal function:

```python
def square(x):
    return x ** 2
```

Both produce the same result.

Lambdas are mainly useful when a small function is needed temporarily.

---

# 16. Lambda with Multiple Parameters

A lambda can have multiple parameters.

```python
add = lambda a, b: a + b

print(add(10, 20))
```

Output:

```text
30
```

Another example:

```python
multiply = lambda a, b: a * b

print(multiply(5, 4))
```

Output:

```text
20
```

---

# 17. Lambda Limitations

A lambda is limited to a single expression.

This is valid:

```python
lambda x: x * 2
```

This is not a good use of lambda:

```python
lambda x:
    print(x)
    return x * 2
```

For multi-step logic, use `def`.

Example:

```python
def process_number(x):

    print(x)

    result = x * 2

    return result
```

---

# 18. Lambda with `sort()`

One of the most useful applications of lambda is sorting.

Consider:

```python
students = [
    ("Ali", 85),
    ("Ahmed", 92),
    ("Hamza", 78)
]
```

We can sort by marks:

```python
students.sort(key=lambda student: student[1])

print(students)
```

Result:

```text
[('Hamza', 78), ('Ali', 85), ('Ahmed', 92)]
```

The lambda tells Python:

> Use the second element of each tuple as the sorting key.

---

# 19. `map()`

`map()` applies a function to every item in an iterable.

Syntax:

```python
map(function, iterable)
```

Example:

```python
numbers = [1, 2, 3, 4, 5]

squares = map(lambda x: x ** 2, numbers)

print(list(squares))
```

Output:

```text
[1, 4, 9, 16, 25]
```

---

# 20. How `map()` Works

Conceptually:

```text
1 → square → 1
2 → square → 4
3 → square → 9
4 → square → 16
5 → square → 25
```

Result:

```text
[1, 4, 9, 16, 25]
```

---

# 21. `map()` Returns an Iterator

In Python 3, `map()` does not immediately create a list.

Example:

```python
numbers = [1, 2, 3]

result = map(lambda x: x * 2, numbers)

print(result)
```

You will see something representing a map object.

To get a list:

```python
print(list(result))
```

Output:

```text
[2, 4, 6]
```

This lazy behavior can be useful for memory efficiency.

---

# 22. `filter()`

`filter()` selects items based on a condition.

Syntax:

```python
filter(function, iterable)
```

The function should return a truthy or falsy result.

Example:

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

# 23. How `filter()` Works

The process is approximately:

```text
1 → even? → False → discard
2 → even? → True  → keep
3 → even? → False → discard
4 → even? → True  → keep
5 → even? → False → discard
6 → even? → True  → keep
```

Final result:

```text
[2, 4, 6]
```

---

# 24. `reduce()`

`reduce()` repeatedly combines values into one result.

It is available from:

```python
functools
```

Example:

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

# 25. Understanding `reduce()`

For:

```python
[1, 2, 3, 4]
```

the process is approximately:

```text
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
```

Final result:

```text
10
```

---

# 26. `reduce()` for Multiplication

```python
from functools import reduce


numbers = [1, 2, 3, 4, 5]

product = reduce(
    lambda a, b: a * b,
    numbers
)

print(product)
```

Output:

```text
120
```

---

# 27. Should You Always Use `reduce()`?

No.

Sometimes a built-in function is clearer.

For example:

```python
sum(numbers)
```

is much easier to understand than:

```python
reduce(lambda a, b: a + b, numbers)
```

The goal is not to use advanced syntax everywhere.

The goal is to write **clear and maintainable code**.

---

# 28. Closures

A closure occurs when an inner function remembers values from its enclosing function.

Example:

```python
def multiplier(factor):

    def multiply(number):
        return number * factor

    return multiply
```

Now:

```python
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

---

# 29. Why Is This a Closure?

When:

```python
double = multiplier(2)
```

the inner function remembers:

```text
factor = 2
```

When:

```python
triple = multiplier(3)
```

another function remembers:

```text
factor = 3
```

So:

```python
double(5)
```

becomes:

```text
5 × 2 = 10
```

while:

```python
triple(5)
```

becomes:

```text
5 × 3 = 15
```

---

# 30. Practical Closure Example

Create a function that generates discount calculators.

```python
def create_discount(percent):

    def calculate(price):
        return price - (price * percent / 100)

    return calculate


student_discount = create_discount(10)
special_discount = create_discount(20)

print(student_discount(1000))
print(special_discount(1000))
```

Output:

```text
900.0
800.0
```

The returned functions remember their discount percentages.

---

# 31. `nonlocal`

Suppose an inner function needs to modify a variable from its enclosing function.

Use:

```python
nonlocal
```

Example:

```python
def counter():

    count = 0

    def increase():

        nonlocal count

        count += 1

        return count

    return increase
```

Now:

```python
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

# 32. Why `nonlocal` Is Necessary

Without:

```python
nonlocal count
```

Python would treat:

```python
count
```

inside `increase()` as a local variable when assigning to it.

`nonlocal` tells Python:

> Use the variable from the nearest enclosing function scope.

---

# 33. Decorators

A decorator is a function that modifies or extends another function's behavior.

Basic decorator:

```python
def decorator(function):

    def wrapper():

        print("Before function")

        function()

        print("After function")

    return wrapper
```

Now:

```python
@decorator
def greet():

    print("Hello!")
```

Calling:

```python
greet()
```

produces:

```text
Before function
Hello!
After function
```

---

# 34. Understanding `@decorator`

This:

```python
@decorator
def greet():
    print("Hello!")
```

is conceptually similar to:

```python
def greet():
    print("Hello!")


greet = decorator(greet)
```

The decorator receives the original function and returns a new function.

---

# 35. Decorators with Function Arguments

Real functions often accept arguments.

Therefore, decorators commonly use:

```python
*args
```

and:

```python
**kwargs
```

Example:

```python
def decorator(function):

    def wrapper(*args, **kwargs):

        print("Before function")

        result = function(*args, **kwargs)

        print("After function")

        return result

    return wrapper
```

Use:

```python
@decorator
def add(a, b):
    return a + b


print(add(10, 20))
```

Output:

```text
Before function
After function
30
```

---

# 36. Why Decorators Are Useful

Decorators allow us to add reusable behavior without modifying the original function.

Common uses include:

* logging
* timing
* authentication
* authorization
* validation
* caching
* error handling
* permissions
* framework registration

For example:

```text
Original function
       ↓
Logging decorator
       ↓
Authentication decorator
       ↓
Validation decorator
       ↓
Function executes
```

---

# 37. `functools.wraps`

When creating decorators, use:

```python
from functools import wraps
```

Example:

```python
from functools import wraps


def decorator(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        return function(*args, **kwargs)

    return wrapper
```

`wraps()` preserves useful metadata from the original function.

For example:

* function name
* docstring
* other metadata

This is a best practice when writing decorators.

---

# 38. Practical Logging Decorator

```python
from functools import wraps


def log_call(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print(f"Calling {function.__name__}")

        result = function(*args, **kwargs)

        print(f"Finished {function.__name__}")

        return result

    return wrapper
```

Use:

```python
@log_call
def multiply(a, b):

    return a * b


print(multiply(4, 5))
```

Output:

```text
Calling multiply
Finished multiply
20
```

---

# 39. Recursion

Recursion occurs when a function calls itself.

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

# 40. Base Case

A recursive function needs a **base case**.

The base case tells the function when to stop.

In:

```python
if number == 0:
    return
```

the base case is:

```text
number == 0
```

Without a base case, recursion could continue until Python raises a recursion-related error.

---

# 41. Recursive Factorial

Factorial:

```text
5! = 5 × 4 × 3 × 2 × 1
```

Recursive implementation:

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

---

# 42. Understanding Recursive Factorial

For:

```python
factorial(5)
```

Python evaluates approximately:

```text
5 × factorial(4)
```

then:

```text
5 × 4 × factorial(3)
```

then:

```text
5 × 4 × 3 × factorial(2)
```

then:

```text
5 × 4 × 3 × 2 × factorial(1)
```

then:

```text
5 × 4 × 3 × 2 × 1
```

result:

```text
120
```

---

# 43. Recursion vs Iteration

Recursive solution:

```python
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)
```

Iterative solution:

```python
def factorial(n):

    result = 1

    for number in range(1, n + 1):
        result *= number

    return result
```

Neither approach is automatically better.

For many simple problems, iteration is more memory-efficient and easier to follow.

Recursion is especially useful when a problem naturally has a recursive structure, such as traversing trees.

---

# 44. Function Scope

Python has different variable scopes.

Example:

```python
x = "global"


def outer():

    x = "enclosing"

    def inner():

        x = "local"

        print(x)

    inner()


outer()
```

Output:

```text
local
```

Python searches for names according to the **LEGB rule**.

---

# 45. LEGB Rule

LEGB means:

```text
L → Local
E → Enclosing
G → Global
B → Built-in
```

Python searches in this order.

### Local

Inside the current function.

### Enclosing

Inside an outer function.

### Global

At module level.

### Built-in

Names built into Python.

Examples:

```python
print()
len()
sum()
max()
min()
```

---

# 46. `global`

The `global` keyword allows a function to assign to a global variable.

Example:

```python
count = 0


def increase():

    global count

    count += 1


increase()

print(count)
```

Output:

```text
1
```

However, excessive use of global variables can make programs harder to understand and test.

Prefer passing values into functions and returning results whenever possible.

---

# 47. Keyword-Only Arguments

Python allows us to force certain parameters to be passed by keyword.

Example:

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

This makes the API more explicit.

---

# 48. Why Keyword-Only Arguments Are Useful

Consider:

```python
create_user("Ali", 17, "Pakistan")
```

It may not immediately be obvious what each value represents.

Instead:

```python
create_user(
    "Ali",
    age=17,
    country="Pakistan"
)
```

is much clearer.

---

# 49. Positional-Only Arguments

Python also allows positional-only parameters using `/`.

Example:

```python
def power(base, exponent, /):

    return base ** exponent
```

Valid:

```python
power(2, 3)
```

But these parameters cannot be passed by keyword:

```python
power(base=2, exponent=3)
```

---

# 50. Combining Parameter Types

Python functions can use positional-only, normal, and keyword-only parameters.

Example:

```python
def example(a, /, b, *, c):

    print(a, b, c)
```

Here:

```text
a → positional-only
b → positional or keyword
c → keyword-only
```

Call:

```python
example(10, 20, c=30)
```

---

# 51. Default Arguments

Functions can provide default values.

Example:

```python
def greet(name="Guest"):

    return f"Hello, {name}!"
```

Now:

```python
print(greet())
print(greet("Ali"))
```

Output:

```text
Hello, Guest!
Hello, Ali!
```

---

# 52. Mutable Default Arguments

One important Python mistake is using a mutable object as a default argument.

Avoid:

```python
def add_item(item, items=[]):

    items.append(item)

    return items
```

The default list can be reused between function calls.

This can create surprising behavior.

---

# 53. Correct Approach

Use `None` as the default:

```python
def add_item(item, items=None):

    if items is None:
        items = []

    items.append(item)

    return items
```

Now each call gets a fresh list when one isn't supplied.

---

# 54. Docstrings

A docstring documents a function.

Example:

```python
def calculate_area(length, width):
    """Return the area of a rectangle."""

    return length * width
```

You can access it:

```python
print(calculate_area.__doc__)
```

Output:

```text
Return the area of a rectangle.
```

Good docstrings make code easier to understand and maintain.

---

# 55. Type Hints

Type hints communicate expected types.

Example:

```python
def add(a: int, b: int) -> int:

    return a + b
```

Here:

```text
a → int
b → int
return value → int
```

Type hints improve:

* readability
* IDE support
* static analysis
* documentation
* maintainability

Type hints do not normally enforce types at runtime by themselves.

---

# 56. Callback Functions

A callback is a function passed to another function so that it can be called later or at an appropriate point.

Example:

```python
def process_data(data, callback):

    result = data * 2

    return callback(result)


def display(value):

    return f"Result: {value}"


print(process_data(10, display))
```

Output:

```text
Result: 20
```

Callbacks are common in:

* event-driven programming
* GUI applications
* asynchronous programming
* APIs
* web development
* data processing

---

# 57. Function Pipelines

Functions can be combined into a processing pipeline.

Example:

```text
Raw Data
   ↓
Filter
   ↓
Transform
   ↓
Aggregate
   ↓
Result
```

Python example:

```python
from functools import reduce


numbers = [1, 2, 3, 4, 5, 6]


even_numbers = filter(
    lambda x: x % 2 == 0,
    numbers
)


squared_numbers = map(
    lambda x: x ** 2,
    even_numbers
)


total = reduce(
    lambda a, b: a + b,
    squared_numbers
)


print(total)
```

Output:

```text
56
```

---

# 58. Understanding the Pipeline

Starting list:

```text
[1, 2, 3, 4, 5, 6]
```

Filter even numbers:

```text
[2, 4, 6]
```

Square:

```text
[4, 16, 36]
```

Add:

```text
4 + 16 + 36 = 56
```

Final result:

```text
56
```

---

# 59. More Readable Alternative

Sometimes a list comprehension is clearer:

```python
numbers = [1, 2, 3, 4, 5, 6]

total = sum(
    x ** 2
    for x in numbers
    if x % 2 == 0
)

print(total)
```

Output:

```text
56
```

The lesson is:

> Advanced features should improve code, not make simple code unnecessarily complicated.

---

# 60. Practical Example — Calculator Using Higher-Order Functions

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b


def calculate(function, a, b):

    return function(a, b)


print(calculate(add, 10, 5))
print(calculate(subtract, 10, 5))
print(calculate(multiply, 10, 5))
print(calculate(divide, 10, 5))
```

Output:

```text
15
5
50
2.0
```

This is a practical example of passing functions as arguments.

---

# 61. Practical Example — Function Factory

A function factory creates specialized functions.

```python
def create_multiplier(factor):

    def multiply(number):

        return number * factor

    return multiply
```

Now:

```python
double = create_multiplier(2)
triple = create_multiplier(3)
ten_times = create_multiplier(10)

print(double(5))
print(triple(5))
print(ten_times(5))
```

Output:

```text
10
15
50
```

This demonstrates:

* higher-order functions
* closures
* returning functions

---

# 62. Practical Example — Decorator for Timing

A decorator can be used to measure how long a function takes.

Example:

```python
from functools import wraps
from time import perf_counter


def timer(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        start = perf_counter()

        result = function(*args, **kwargs)

        end = perf_counter()

        print(
            f"{function.__name__} took "
            f"{end - start:.6f} seconds"
        )

        return result

    return wrapper
```

Use:

```python
@timer
def calculate():

    total = 0

    for number in range(1, 100000):
        total += number

    return total


print(calculate())
```

This demonstrates how decorators can add functionality around an existing function.

---

# 63. Practical Example — Validation Decorator

```python
from functools import wraps


def require_positive(function):

    @wraps(function)
    def wrapper(number):

        if number <= 0:
            raise ValueError(
                "Number must be positive"
            )

        return function(number)

    return wrapper


@require_positive
def square(number):

    return number ** 2


print(square(5))
```

Output:

```text
25
```

If a negative or zero value is passed, the decorator prevents the function from continuing.

---

# 64. Common Mistakes

## Mistake 1 — Calling a function instead of passing it

Incorrect:

```python
apply_function(square(), 5)
```

Correct:

```python
apply_function(square, 5)
```

Remember:

```python
square
```

means the function.

```python
square()
```

means execute the function.

---

# 65. Mistake 2 — Forgetting `return`

Incorrect:

```python
def double(x):

    x * 2
```

This returns:

```python
None
```

Correct:

```python
def double(x):

    return x * 2
```

---

# 66. Mistake 3 — Thinking `args` Is a List

With:

```python
def example(*args):
    print(type(args))
```

the result is:

```text
<class 'tuple'>
```

`*args` collects positional arguments into a tuple.

---

# 67. Mistake 4 — Thinking `kwargs` Is a Tuple

With:

```python
def example(**kwargs):
    print(type(kwargs))
```

the result is:

```text
<class 'dict'>
```

`**kwargs` collects keyword arguments into a dictionary.

---

# 68. Mistake 5 — Overusing Lambda

This:

```python
square = lambda x: x ** 2
```

is fine.

But if a function requires several steps, use:

```python
def process_data(data):

    ...
```

Readable code is more valuable than unnecessarily short code.

---

# 69. Mistake 6 — Forgetting `list()` with `map()` or `filter()`

For example:

```python
numbers = [1, 2, 3]

result = map(lambda x: x * 2, numbers)

print(result)
```

This does not display the transformed list.

Use:

```python
print(list(result))
```

when you need to materialize the results.

---

# 70. Mistake 7 — Missing a Recursive Base Case

Incorrect:

```python
def countdown(n):

    print(n)

    countdown(n - 1)
```

There is no stopping condition.

Correct:

```python
def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)
```

---

# 71. Mistake 8 — Misusing Global Variables

Avoid designing programs where many functions directly modify global state.

Instead of:

```python
count = 0


def increase():
    global count
    count += 1
```

prefer passing data and returning results where practical:

```python
def increase(count):

    return count + 1
```

This is generally easier to test and reason about.

---

# 72. Mistake 9 — Mutable Default Arguments

Avoid:

```python
def function(items=[]):
    ...
```

Prefer:

```python
def function(items=None):

    if items is None:
        items = []
```

---

# 73. Function Design Principles

Good functions should generally be:

### Small

A function should ideally have a focused responsibility.

### Reusable

Avoid hard-coding values unnecessarily.

### Predictable

Given the same inputs, the function should normally produce the expected result.

### Readable

Use meaningful names.

### Testable

A function that accepts inputs and returns outputs is often easy to test.

---

# 74. Pure Functions

A pure function generally:

1. depends only on its inputs
2. produces an output
3. does not modify external state

Example:

```python
def add(a, b):

    return a + b
```

The result depends only on:

```text
a
b
```

Pure functions are useful because they are predictable and easy to test.

---

# 75. Functions and AI Engineering

Advanced function concepts are highly relevant to AI engineering.

A machine-learning workflow can be represented as:

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

Each stage can be represented by a function.

This makes the system modular.

---

# 76. Functions in Data Processing

Suppose we have:

```python
data = [1, 2, 3, 4, 5]
```

We might create:

```python
def clean_data(data):
    ...


def transform_data(data):
    ...


def analyze_data(data):
    ...
```

Each function has a single responsibility.

This becomes increasingly important when projects become large.

---

# 77. Functions in Machine Learning

Machine-learning code frequently uses functions for:

* preprocessing
* feature engineering
* training
* evaluation
* prediction
* metrics
* data loading
* model utilities

Understanding functions deeply will therefore help when moving from Python fundamentals into:

```text
NumPy
   ↓
Pandas
   ↓
Data Processing
   ↓
Machine Learning
   ↓
Deep Learning
   ↓
AI Engineering
```

---

# 78. Functions in Frameworks

Decorators are especially common in Python frameworks.

You may eventually encounter syntax like:

```python
@something
def function():
    ...
```

The decorator may:

* register a function
* validate input
* check permissions
* add middleware
* cache results
* modify behavior

Understanding Day 18 makes such syntax much less mysterious.

---

# 79. Advanced Function Mental Model

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

Higher-order functions allow functions to work with other functions:

```text
Function A
     ↓
Function B
     ↓
Function C
```

Decorators add another layer:

```text
Original Function
       ↓
Decorator
       ↓
Wrapped Function
```

Closures allow a function to remember configuration:

```text
Factory
   ↓
Configured Function
   ↓
Reusable Behavior
```

---

# 80. Key Concepts Table

| Concept               | Meaning                               |
| --------------------- | ------------------------------------- |
| First-class function  | Functions can be treated like objects |
| Higher-order function | Accepts or returns functions          |
| `*args`               | Variable positional arguments         |
| `**kwargs`            | Variable keyword arguments            |
| Argument unpacking    | Expands collections into arguments    |
| Lambda                | Small anonymous function              |
| `map()`               | Transforms items                      |
| `filter()`            | Selects items                         |
| `reduce()`            | Combines items                        |
| Closure               | Function remembers enclosing state    |
| `nonlocal`            | Modifies enclosing variable           |
| Decorator             | Wraps/modifies function behavior      |
| `wraps()`             | Preserves function metadata           |
| Recursion             | Function calls itself                 |
| LEGB                  | Name-resolution order                 |
| `global`              | Access/modify global variable         |
| Keyword-only          | Must be supplied by keyword           |
| Positional-only       | Must be supplied positionally         |
| Docstring             | Function documentation                |
| Type hint             | Communicates expected types           |
| Callback              | Function passed for later execution   |

---

# 81. Best Practices

## 1. Keep functions focused

Avoid creating one giant function that does everything.

---

## 2. Use meaningful names

Prefer:

```python
calculate_average()
```

over:

```python
do_it()
```

---

## 3. Prefer return values

Instead of changing global variables, return results.

---

## 4. Use type hints

Example:

```python
def calculate_area(
    length: float,
    width: float
) -> float:

    return length * width
```

---

## 5. Write docstrings

Especially for public or complicated functions.

---

## 6. Use lambda for small operations

Do not turn complicated logic into unreadable lambda expressions.

---

## 7. Prefer readability

For example:

```python
sum(numbers)
```

is often better than:

```python
reduce(lambda a, b: a + b, numbers)
```

---

## 8. Avoid mutable default arguments

Use:

```python
None
```

instead.

---

## 9. Use decorators carefully

Decorators are powerful, but too many layers can make debugging harder.

---

## 10. Understand before using

Do not use advanced Python features simply because they look advanced.

The goal is:

```text
Readable
+
Reusable
+
Maintainable
```

---

# 82. Beginner Practice Tasks

## Task 1 — Average with `*args`

Create:

```python
def average(*numbers):
    ...
```

The function should return the average of all numbers.

Example:

```python
print(average(10, 20, 30))
```

Expected:

```text
20.0
```

---

## Task 2 — Profile with `**kwargs`

Create a function that accepts arbitrary user information.

Example:

```python
profile(
    name="Ali",
    age=17,
    country="Pakistan"
)
```

Print each key and value.

---

## Task 3 — Lambda Cube

Create a lambda that calculates the cube of a number.

Example:

```python
cube(4)
```

Expected:

```text
64
```

---

## Task 4 — `map()`

Given:

```python
numbers = [1, 2, 3, 4, 5]
```

Use `map()` to create:

```text
[2, 4, 6, 8, 10]
```

---

## Task 5 — `filter()`

Given:

```python
numbers = [10, 25, 60, 45, 80, 30]
```

Keep only numbers greater than `50`.

Expected:

```text
[60, 80]
```

---

# 83. Intermediate Practice Tasks

## Task 6 — Function Processor

Create:

```python
def process(function, numbers):
    ...
```

It should apply the provided function to every number.

Example:

```python
def square(x):
    return x ** 2
```

---

## Task 7 — Power Function Factory

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

## Task 8 — Logging Decorator

Create a decorator that prints:

```text
Starting...
```

before the function runs and:

```text
Finished.
```

after it completes.

---

## Task 9 — Recursive Sum

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

Because:

```text
1 + 2 + 3 + 4 + 5 = 15
```

---

# 84. Advanced Practice Task — Function Pipeline

Build a program that:

1. accepts a list of numbers
2. removes negative numbers
3. keeps only even numbers
4. squares them
5. calculates their total

Example:

```python
numbers = [-3, -2, 1, 2, 4, 5, 6]
```

Expected processing:

```text
[-3, -2, 1, 2, 4, 5, 6]
              ↓
negative removed
              ↓
[1, 2, 4, 5, 6]
              ↓
even numbers
              ↓
[2, 4, 6]
              ↓
square
              ↓
[4, 16, 36]
              ↓
sum
              ↓
56
```

Try solving it using:

* normal functions
* `filter()`
* `map()`
* `reduce()`

Then write a simpler version using a comprehension and `sum()`.

---

# 85. Day 18 Challenge

Create a small **Function Utility Library**.

Your program should contain functions for:

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

This will combine many Day 18 concepts into one mini-project.

---

# 86. Final Revision

Before moving to Day 19, make sure you understand these concepts:

```text
Functions
    ↓
First-Class Objects
    ↓
Higher-Order Functions
    ↓
*args / **kwargs
    ↓
Argument Unpacking
    ↓
Lambda
    ↓
map()
    ↓
filter()
    ↓
reduce()
    ↓
Closures
    ↓
nonlocal
    ↓
Decorators
    ↓
Recursion
    ↓
Scope / LEGB
```

---

# 87. Quick Revision Checklist

* [ ] I understand functions as first-class objects.
* [ ] I can store a function in a variable.
* [ ] I can pass a function to another function.
* [ ] I can return a function from a function.
* [ ] I understand higher-order functions.
* [ ] I can use `*args`.
* [ ] I can use `**kwargs`.
* [ ] I understand argument unpacking.
* [ ] I can write lambda functions.
* [ ] I understand `map()`.
* [ ] I understand `filter()`.
* [ ] I understand `reduce()`.
* [ ] I understand closures.
* [ ] I understand `nonlocal`.
* [ ] I can create decorators.
* [ ] I understand `functools.wraps`.
* [ ] I understand recursion.
* [ ] I know what a base case is.
* [ ] I understand the LEGB rule.
* [ ] I understand `global`.
* [ ] I understand keyword-only arguments.
* [ ] I understand positional-only arguments.
* [ ] I understand mutable default arguments.
* [ ] I can write docstrings.
* [ ] I can use type hints.
* [ ] I understand callbacks.
* [ ] I can build a simple function pipeline.
* [ ] I can design reusable functions.

---

# 88. Final Summary

Day 18 takes Python functions from basic building blocks to powerful programming tools.

The most important idea is:

> **Functions in Python are objects and can be treated like data.**

Because of this, functions can be:

```text
stored
   ↓
passed
   ↓
returned
   ↓
wrapped
   ↓
combined
   ↓
reused
```

The major concepts form a progression:

```text
First-Class Functions
        ↓
Higher-Order Functions
        ↓
*args / **kwargs
        ↓
Lambda
        ↓
map / filter / reduce
        ↓
Closures
        ↓
Decorators
        ↓
Callbacks
        ↓
Function Pipelines
```

These concepts are extremely useful for professional Python development.

They will also become valuable when working with:

* data science
* machine learning
* AI engineering
* web development
* APIs
* automation
* testing
* asynchronous programming
* software architecture

The goal is not simply to memorize advanced syntax.

The real goal is to understand **how to design flexible, reusable, readable functions**.

---

# Day 18 Complete

**Topic:** Advanced Functions
**Track:** Python Engineering
**Status:** Completed

## Next

### Day 19 — Iterators & Generators

The next stage builds naturally on functions and introduces:

* iterators
* iterable objects
* `iter()`
* `next()`
* generator functions
* `yield`
* generator expressions
* lazy evaluation
* memory-efficient data processing
* custom iterators

These concepts will take Python's function and data-processing capabilities to the next level.

```
```
