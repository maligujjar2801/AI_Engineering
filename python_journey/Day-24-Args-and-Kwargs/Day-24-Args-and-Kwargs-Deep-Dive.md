# Day 24 — Deep Dive into `*args` and `**kwargs`

> Python Journey • Learn → Understand → Predict → Practice → Build  
> Prerequisite: functions, positional arguments, keyword arguments, lists, tuples, and dictionaries.

## Learning objectives

By the end of this session, you should be able to:
- Explain positional and keyword arguments.
- Use `*args` to accept a variable number of positional arguments.
- Use `**kwargs` to accept a variable number of keyword arguments.
- Distinguish parameter packing from argument unpacking.
- Understand the order of parameters in a function definition.
- Forward arguments to another function and build flexible wrappers.
- Avoid common mistakes and use these tools appropriately in real projects.

---

## 1. The problem: fixed parameters

A function with a fixed number of parameters works well when the number of inputs is known:

```python
def add(a, b):
    return a + b

print(add(3, 5))  # 8
```

But what if you want to add two, five, or twenty numbers? Defining a separate parameter for every possible number is impractical. Python provides `*args` and `**kwargs` for this flexibility.

## 2. Positional vs keyword arguments

```python
def introduce(name, age):
    print(f"{name} is {age} years old.")

introduce("Sara", 18)             # positional arguments
introduce(name="Sara", age=18)    # keyword arguments
introduce("Sara", age=18)         # mixed
```

Positional arguments are matched by position. Keyword arguments are matched by parameter name.

## 3. `*args`: variable positional arguments

The name `args` is a convention; the asterisk is what matters. Python gathers extra positional arguments into a **tuple**.

```python
def add_all(*args):
    print(args)
    print(type(args))
    return sum(args)

print(add_all(2, 4))          # 6
print(add_all(2, 4, 6, 8))    # 20
print(add_all())              # 0
```

Inside the function, `args` is a tuple. You can loop over it, index it, or pass it to functions that accept an iterable.

### Combine regular parameters and `*args`

```python
def report(first, *args):
    print("First:", first)
    print("Remaining:", args)

report("Python", "Java", "C++")
# First: Python
# Remaining: ('Java', 'C++')
```

The regular parameter receives the first positional argument; `args` collects the remaining positional arguments.

### Practical example: average calculator

```python
def average(*numbers):
    if not numbers:
        raise ValueError("Provide at least one number.")
    return sum(numbers) / len(numbers)

print(average(4, 6, 8))  # 6.0
```

Notice the validation: without it, calculating an average of zero values would divide by zero.

## 4. `**kwargs`: variable keyword arguments

The double asterisk gathers extra keyword arguments into a **dictionary**.

```python
def show_profile(**kwargs):
    print(kwargs)
    print(type(kwargs))

show_profile(name="Ali", track="Python", day=24)
# {'name': 'Ali', 'track': 'Python', 'day': 24}
```

The keys are strings matching the keyword names, and the values are the supplied objects.

### Practical example: configurable user profile

```python
def create_profile(username, **details):
    profile = {"username": username}
    profile.update(details)
    return profile

user = create_profile(
    "learner_01",
    level="beginner",
    language="Python",
    active=True,
)
print(user)
```

Use this pattern when optional settings are genuinely open-ended. If the accepted fields are known and important, explicit parameters may be clearer.

## 5. Use both together

```python
def log_event(event, *values, **metadata):
    print("Event:", event)
    print("Values:", values)
    print("Metadata:", metadata)

log_event("login", "learner_01", "desktop", success=True, retries=1)
```

Expected structure:
- `event` → `"login"`
- `values` → `("learner_01", "desktop")`
- `metadata` → `{"success": True, "retries": 1}`

### Parameter order

A common valid order is:

```python
def example(required, *args, option=True, **kwargs):
    ...
```

- Required parameters come first.
- `*args` collects extra positional arguments.
- Parameters after `*args` can be keyword-only.
- `**kwargs` collects remaining keyword arguments.

Example:

```python
def send_message(message, *recipients, urgent=False, **options):
    print(message, recipients, urgent, options)

send_message(
    "Meeting at 3",
    "Ayesha",
    "Hamza",
    urgent=True,
    channel="email",
)
```

Here, `urgent` is keyword-only, and `channel` is collected in `options`.

## 6. Packing vs unpacking — the crucial distinction

The same symbols have related but different uses depending on context.

### Packing: collect arguments inside a function

```python
def inspect(*items, **settings):
    print(items)     # tuple
    print(settings)  # dictionary

inspect(10, 20, mode="fast")
```

### Unpacking: spread an existing iterable or mapping into a call

```python
def describe(name, age):
    print(name, age)

person = ("Ali", 17)
describe(*person)  # equivalent to describe("Ali", 17)

details = {"name": "Sara", "age": 18}
describe(**details)  # equivalent to describe(name="Sara", age=18)
```

Remember:
- In a function definition, `*args` and `**kwargs` collect.
- In a function call, `*iterable` and `**mapping` spread values into arguments.

Unpacking requirements still apply: the number and names of supplied arguments must fit the function signature.

## 7. Forwarding arguments

A wrapper can accept arguments and pass them to another function without knowing every argument in advance.

```python
def calculate_total(*prices, tax=0):
    subtotal = sum(prices)
    return subtotal * (1 + tax)

def logged_calculation(*args, **kwargs):
    print("Running calculation...")
    result = calculate_total(*args, **kwargs)
    print("Finished.")
    return result

print(logged_calculation(100, 50, tax=0.1))  # 165.0
```

This is useful in decorators, logging, adapters, and APIs. A wrapper should preserve return values and handle exceptions deliberately when needed.

## 8. Common mistakes

### Mistake 1: thinking `args` is a list

```python
def collect(*args):
    print(type(args))  # <class 'tuple'>
```

### Mistake 2: forgetting to unpack

```python
def pair(a, b):
    return a, b

values = (1, 2)
# pair(values)   # TypeError: one argument supplied
print(pair(*values))
```

### Mistake 3: passing unexpected keyword names

```python
def greet(name):
    print(name)

# greet(username="Ali")  # TypeError: unexpected keyword
greet(name="Ali")
```

### Mistake 4: duplicate values for one parameter

```python
def show(value):
    print(value)

# show(1, value=2)  # TypeError: multiple values for value
```

### Mistake 5: using `**kwargs` for everything

Flexible interfaces are not automatically better. Prefer explicit parameters for required or well-known options so that the function is easier to read, document, and validate.

## 9. Quick mental model

| Syntax | Context | Meaning | Result |
|---|---|---|---|
| `*args` | Definition | Pack extra positional arguments | Tuple |
| `**kwargs` | Definition | Pack extra keyword arguments | Dictionary |
| `*items` | Call | Unpack iterable into positional arguments | Multiple positional arguments |
| `**data` | Call | Unpack mapping into keyword arguments | Named arguments |

## 10. Predict the output

Try these before running them.

**Q1**
```python
def f(*args):
    print(len(args), args[0])

f("a", "b", "c")
```

**Q2**
```python
def f(**kwargs):
    print(kwargs["level"])

f(level="beginner", day=24)
```

**Q3**
```python
def f(a, *args, flag=False):
    print(a, args, flag)

f(1, 2, 3, flag=True)
```

**Q4**
```python
def multiply(a, b):
    return a * b

values = (6, 7)
print(multiply(*values))
```

**Q5**
```python
def settings(**kwargs):
    return kwargs

config = {"theme": "dark", "font_size": 14}
print(settings(**config))
```

## 11. Practice challenges

1. **Flexible sum:** write `sum_numbers(*numbers)` that returns the total. Decide what it should do with no numbers.
2. **Keyword report:** write `print_settings(**settings)` that prints each key and value on its own line.
3. **Order receipt:** create `make_receipt(customer, *items, discount=0, **metadata)`. Return a dictionary containing the customer, item tuple, discount, and metadata.
4. **Argument forwarding:** write `run_operation(function, *args, **kwargs)` that calls the function with those arguments and returns its result.
5. **Debugging:** fix a call that raises an error because a tuple was passed as one argument rather than unpacked.

## 12. Mini-project — Flexible command-line style report

Build a report function with this signature:

```python
def build_report(title, *scores, student="Unknown", **metadata):
    ...
```

Requirements:
- Print the report title and student.
- Print all scores and their average (handle an empty score list).
- Print any extra metadata as key-value pairs.
- Return a dictionary with `title`, `student`, `scores`, `average`, and `metadata`.
- Test it with at least three calls using different numbers of scores and different keyword options.

Example call:

```python
report = build_report(
    "Python Quiz",
    82, 91, 88,
    student="Learner",
    topic="args and kwargs",
    attempt=1,
)
```

## 13. Solutions to prediction questions

<details>
<summary>Show answers</summary>

1. `3 a`
2. `beginner`
3. `1 (2, 3) True`
4. `42`
5. `{'theme': 'dark', 'font_size': 14}`

</details>

## Completion checklist

- [ ] I can explain positional and keyword arguments.
- [ ] I know that `*args` becomes a tuple.
- [ ] I know that `**kwargs` becomes a dictionary.
- [ ] I can distinguish packing from unpacking.
- [ ] I can forward arguments to another function.
- [ ] I completed the five practice challenges.
- [ ] I built and tested the mini-project.

**Next step:** solve the challenges without copying the examples, then write your own notes in your words before marking Day 24 complete.
