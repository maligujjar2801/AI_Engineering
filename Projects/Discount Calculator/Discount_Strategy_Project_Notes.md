# Discount Strategy Project — Detailed Notes

## 1. Project Overview

This project is a small Python example of **object-oriented design** and the **Strategy Design Pattern**.

The program represents a product, defines multiple discount strategies, checks which discounts are applicable, calculates their resulting prices, and selects the **lowest valid price**.

The main ideas demonstrated are:

- Classes and objects
- Inheritance
- Abstract Base Classes (`ABC`)
- Abstract methods (`@abstractmethod`)
- Polymorphism
- Type hints
- Encapsulation of discount rules
- Strategy Design Pattern
- Separation of responsibilities
- List comprehensions
- `min()`
- A main-entry-point guard: `if __name__ == '__main__':`

---

## 2. Problem Being Solved

Imagine an online store that can offer different kinds of discounts:

1. Percentage discount
2. Fixed-amount discount
3. Premium-user discount

Instead of putting every rule into one huge function, each discount rule is represented by its own class.

The `DiscountEngine` then works with all discount classes through their common interface.

For example, for a `$50` product and a premium user:

- Original price = `$50`
- 10% discount = `$45`
- $5 fixed discount = `$45`
- Premium discount = `$40`

The engine chooses `$40` because it is the lowest applicable price.

---

# 3. Project Structure

The project contains these main classes:

```text
Product
   |
   +----------------------+
                          |
                  DiscountStrategy (abstract)
                          |
          +---------------+---------------+
          |               |               |
 PercentageDiscount  FixedAmountDiscount  PremiumUserDiscount

DiscountEngine
   |
   +--> uses DiscountStrategy objects
```

The important relationship is:

> `DiscountStrategy` defines what every discount must be able to do, while the concrete discount classes define how each specific discount works.

---

# 4. Product Class

```python
class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'{self.name} - ${self.price}'
```

## Purpose

The `Product` class represents an item that can receive a discount.

### Constructor

```python
def __init__(self, name: str, price: float) -> None:
```

It receives:

- `name` → product name
- `price` → original product price

The values are stored in:

```python
self.name = name
self.price = price
```

### Type hints

```python
name: str
price: float
```

These tell the reader that:

- `name` should be a string
- `price` should normally be a floating-point number

`-> None` means the constructor does not return a value.

---

## `__str__`

```python
def __str__(self) -> str:
    return f'{self.name} - ${self.price}'
```

`__str__()` controls the human-readable representation of the object.

For example:

```python
product = Product("Wireless Mouse", 50.0)
print(product)
```

Output:

```text
Wireless Mouse - $50.0
```

---

# 5. Abstract Base Class: DiscountStrategy

```python
class DiscountStrategy(ABC):
```

This class inherits from `ABC`.

`ABC` means **Abstract Base Class**.

An abstract class is useful when we want to define a common interface for several related classes.

The program says:

> Every discount strategy must know how to determine whether it applies and how to calculate its discounted price.

---

# 6. Abstract Method: is_applicable()

```python
@abstractmethod
def is_applicable(self, product: Product, user_tier: str) -> bool:
    pass
```

This method asks:

> Is this discount allowed for this product and this user?

It returns a Boolean:

```text
True
False
```

For example:

```python
PremiumUserDiscount().is_applicable(product, "Premium")
```

returns:

```python
True
```

while:

```python
PremiumUserDiscount().is_applicable(product, "Regular")
```

returns:

```python
False
```

Because the method is abstract, subclasses are required to implement it.

---

# 7. Abstract Method: apply_discount()

```python
@abstractmethod
def apply_discount(self, product: Product) -> float:
    pass
```

This method calculates the new price after applying a discount.

For example:

```text
Original price = $50
10% discount = $45
```

The method returns the resulting price.

---

# 8. Why Use Abstract Methods?

Without an abstract base class, different discount classes could accidentally use different method names.

For example:

```python
PercentageDiscount.calculate()
FixedAmountDiscount.apply()
PremiumUserDiscount.discount()
```

That would make the engine harder to write.

Instead, the abstract class forces every strategy to provide:

```python
is_applicable()
apply_discount()
```

Therefore the engine can treat all strategies consistently.

This is an important OOP concept:

> Program against an interface, not a specific implementation.

---

# 9. PercentageDiscount

```python
class PercentageDiscount(DiscountStrategy):
```

This class inherits from `DiscountStrategy`.

It represents a percentage-based discount.

---

## Constructor

```python
def __init__(self, percent: int) -> None:
    self.percent = percent
```

Example:

```python
PercentageDiscount(10)
```

stores:

```python
self.percent = 10
```

---

## Checking applicability

```python
def is_applicable(self, product: Product, user_tier: str) -> bool:
    return self.percent <= 70
```

This discount is considered applicable when the percentage is no more than 70%.

For example:

```python
PercentageDiscount(10)
```

is applicable.

But:

```python
PercentageDiscount(80)
```

is not.

---

## Applying the discount

```python
def apply_discount(self, product: Product) -> float:
    return product.price * (1 - self.percent / 100)
```

Suppose:

```text
price = 50
percent = 10
```

Then:

```text
50 * (1 - 10 / 100)
= 50 * 0.90
= 45
```

So the final price is:

```text
$45
```

---

# 10. FixedAmountDiscount

```python
class FixedAmountDiscount(DiscountStrategy):
```

This strategy subtracts a fixed amount from the product price.

Example:

```text
$50 - $5 = $45
```

---

## Constructor

```python
def __init__(self, amount: int) -> None:
    self.amount = amount
```

Example:

```python
FixedAmountDiscount(5)
```

stores:

```python
self.amount = 5
```

---

## Applicability Rule

```python
def is_applicable(self, product: Product, user_tier: str) -> bool:
    return product.price * 0.9 > self.amount
```

The rule checks whether 90% of the product's original price is greater than the fixed discount amount.

For a `$50` product:

```text
50 * 0.9 = 45
```

Then:

```text
45 > 5
```

So the discount applies.

---

## Applying the Discount

```python
def apply_discount(self, product: Product) -> float:
    return product.price - self.amount
```

For:

```text
price = $50
amount = $5
```

we get:

```text
50 - 5 = 45
```

Final price:

```text
$45
```

---

# 11. PremiumUserDiscount

```python
class PremiumUserDiscount(DiscountStrategy):
```

This discount is specifically designed for premium users.

---

## Checking Applicability

```python
def is_applicable(self, product: Product, user_tier: str) -> bool:
    return user_tier.lower() == 'premium'
```

The `.lower()` method converts the input to lowercase.

Therefore all of these work:

```text
Premium
premium
PREMIUM
pReMiUm
```

They all become:

```text
premium
```

Then the comparison succeeds.

---

## Applying the Discount

```python
def apply_discount(self, product: Product) -> float:
    return product.price * 0.8
```

This means the customer pays 80% of the original price.

Therefore the discount is 20%.

For a `$50` product:

```text
50 * 0.8 = 40
```

Final price:

```text
$40
```

---

# 12. DiscountEngine

```python
class DiscountEngine:
```

This class is responsible for finding the best price.

It does not need to know the internal details of each discount.

That is one of the biggest strengths of the Strategy Pattern.

---

## Constructor

```python
def __init__(self, strategies: list[DiscountStrategy]) -> None:
    self.strategies = strategies
```

The engine receives a list of discount strategies.

Example:

```python
strategies = [
    PercentageDiscount(10),
    FixedAmountDiscount(5),
    PremiumUserDiscount()
]
```

The engine stores them in:

```python
self.strategies
```

---

# 13. calculate_best_price()

```python
def calculate_best_price(self, product: Product, user_tier: str) -> float:
```

This method calculates the cheapest applicable price.

---

## Step 1 — Start with Original Price

```python
prices = [product.price]
```

If the product costs `$50`:

```python
prices = [50.0]
```

This is important because the program should never return a price higher than the original price just because no discount applies.

---

## Step 2 — Loop Through Strategies

```python
for strategy in self.strategies:
```

The engine processes every discount strategy.

---

## Step 3 — Check Applicability

```python
if strategy.is_applicable(product, user_tier):
```

The engine does not need to know whether the object is:

```text
PercentageDiscount
FixedAmountDiscount
PremiumUserDiscount
```

It simply calls:

```python
strategy.is_applicable(...)
```

This is **polymorphism**.

---

## Step 4 — Calculate Discounted Price

```python
discounted = strategy.apply_discount(product)
```

Again, the engine calls the same method on different objects.

Each class provides its own implementation.

---

## Step 5 — Store the Price

```python
prices.append(discounted)
```

All applicable discounted prices are collected.

For the example:

```python
prices = [
    50.0,
    45.0,
    45.0,
    40.0
]
```

---

## Step 6 — Select the Minimum

```python
return min(prices)
```

Python's `min()` returns the smallest value.

Therefore:

```text
min(50, 45, 45, 40)
```

returns:

```text
40
```

---

# 14. Main Program

```python
if __name__ == '__main__':
```

This is the standard Python main-entry-point pattern.

The code inside this block runs when the file is executed directly.

It does not automatically run when the file is imported as a module.

---

# 15. Creating the Product

```python
product = Product('Wireless Mouse', 50.0)
```

This creates a `Product` object:

```text
Name: Wireless Mouse
Price: $50.00
```

---

# 16. Creating the User Tier

```python
user_tier = 'Premium'
```

The user is a premium customer.

Therefore `PremiumUserDiscount` will be applicable.

---

# 17. Creating Discount Strategies

```python
strategies = [
    PercentageDiscount(10),
    FixedAmountDiscount(5),
    PremiumUserDiscount()
]
```

Three strategy objects are created.

### Strategy 1

```python
PercentageDiscount(10)
```

Gives 10% off.

### Strategy 2

```python
FixedAmountDiscount(5)
```

Takes $5 off.

### Strategy 3

```python
PremiumUserDiscount()
```

Gives premium users 20% off.

---

# 18. Creating the Engine

```python
engine = DiscountEngine(strategies)
```

The engine receives the list of strategies.

Conceptually:

```text
DiscountEngine
    |
    +-- PercentageDiscount(10)
    +-- FixedAmountDiscount(5)
    +-- PremiumUserDiscount()
```

---

# 19. Calculating the Best Price

```python
best_price = engine.calculate_best_price(product, user_tier)
```

The engine checks all applicable strategies.

For the example:

| Strategy | Applicable? | Result |
|---|---:|---:|
| Original price | Yes | $50 |
| 10% discount | Yes | $45 |
| $5 discount | Yes | $45 |
| Premium discount | Yes | $40 |

The best price is:

```text
$40
```

---

# 20. Final Output

```python
print(
    f'Best price for {product.name} '
    f'for {user_tier} user: ${best_price:.2f}'
)
```

The `:.2f` formatting means the price is displayed with exactly two decimal places.

Output:

```text
Best price for Wireless Mouse for Premium user: $40.00
```

---

# 21. Important OOP Concepts Used

## 21.1 Inheritance

These classes inherit from `DiscountStrategy`:

```python
PercentageDiscount
FixedAmountDiscount
PremiumUserDiscount
```

Inheritance allows them to share the same interface.

---

## 21.2 Abstraction

`DiscountStrategy` hides the implementation details.

It defines what a discount strategy must provide:

```python
is_applicable()
apply_discount()
```

The concrete classes decide how those methods work.

---

## 21.3 Polymorphism

The engine can use different strategy objects through the same interface:

```python
strategy.is_applicable(...)
strategy.apply_discount(...)
```

This works regardless of the concrete class.

That is polymorphism.

---

## 21.4 Encapsulation

Each discount class keeps its own rules and data.

For example:

```python
self.percent
```

belongs to `PercentageDiscount`.

The engine does not need to manipulate that value directly.

---

# 22. Strategy Design Pattern

This project is a practical example of the **Strategy Pattern**.

The Strategy Pattern means:

> Define a family of algorithms, put each algorithm in its own class, and make them interchangeable.

Here the algorithms are:

```text
Percentage discount
Fixed amount discount
Premium user discount
```

The `DiscountEngine` can work with any object implementing the `DiscountStrategy` interface.

---

# 23. Why Strategy Pattern Is Better Than One Giant Function

A beginner might write something like:

```python
if discount_type == "percentage":
    ...

elif discount_type == "fixed":
    ...

elif discount_type == "premium":
    ...
```

As the application grows, this can become a very large conditional structure.

With the Strategy Pattern, we can add:

```python
SeasonalDiscount
StudentDiscount
BlackFridayDiscount
LoyaltyDiscount
```

without rewriting the main engine.

For example:

```python
class StudentDiscount(DiscountStrategy):
    ...
```

Then:

```python
strategies.append(StudentDiscount())
```

The engine can use it automatically.

---

# 24. Open/Closed Principle

This project also demonstrates the **Open/Closed Principle**:

> Software entities should be open for extension but closed for modification.

If we want a new discount type, we can create a new strategy class instead of changing the `DiscountEngine`.

For example:

```python
class StudentDiscount(DiscountStrategy):
    def is_applicable(self, product, user_tier):
        return user_tier.lower() == "student"

    def apply_discount(self, product):
        return product.price * 0.9
```

Then the engine can accept it.

---

# 25. Dependency Inversion Idea

`DiscountEngine` depends on the abstract type:

```python
list[DiscountStrategy]
```

rather than depending specifically on:

```python
PercentageDiscount
FixedAmountDiscount
PremiumUserDiscount
```

This makes the engine flexible.

---

# 26. Full Execution Flow

The complete flow is:

```text
Create Product
      |
      v
Create Discount Strategies
      |
      v
Create DiscountEngine
      |
      v
Pass Product + User Tier
      |
      v
Check each strategy
      |
      v
Calculate applicable prices
      |
      v
Store all prices
      |
      v
Find minimum price
      |
      v
Print best price
```

---

# 27. Important Python Features

## `ABC`

```python
from abc import ABC
```

Provides functionality for abstract base classes.

## `abstractmethod`

```python
from abc import abstractmethod
```

Marks a method as abstract.

## `list[DiscountStrategy]`

This is a modern Python type hint indicating a list containing `DiscountStrategy` objects.

## `.lower()`

```python
user_tier.lower()
```

Converts a string to lowercase.

## `min()`

```python
min(prices)
```

Returns the smallest value.

## `:.2f`

```python
f"${best_price:.2f}"
```

Formats a number to two decimal places.

---

# 28. Important Design Observation

The current project intentionally keeps discount rules simple.

However, in a real shopping application, discount validation would normally need additional safeguards.

For example:

- Prevent negative discount percentages.
- Prevent negative fixed discount amounts.
- Prevent a final price below zero.
- Validate the product price.
- Define what happens when multiple discounts can be combined.
- Decide whether discounts can be stacked.
- Use appropriate money handling for production financial calculations.

These are useful improvements for a future version.

---

# 29. Suggested Future Improvements

Possible next versions could include:

1. Add `StudentDiscount`.
2. Add `SeasonalDiscount`.
3. Add a maximum discount limit.
4. Prevent negative prices.
5. Validate discount inputs.
6. Allow multiple products.
7. Create a shopping cart.
8. Add unit tests.
9. Add a CLI menu.
10. Store products and discounts in files.
11. Add coupon codes.
12. Add discount priorities.
13. Add discount stacking rules.
14. Add a database.
15. Build a simple GUI or web application.

---

# 30. Key Lessons

After completing this project, you should understand:

- How abstract base classes work.
- Why abstract methods are useful.
- How inheritance creates a common interface.
- How polymorphism allows one engine to work with many classes.
- How the Strategy Pattern separates algorithms.
- Why separating responsibilities makes code easier to maintain.
- How type hints improve readability.
- How list comprehensions and `min()` can simplify calculations.
- How `if __name__ == '__main__'` controls direct execution.

---

# 31. Quick Revision

### Product

Represents the item being discounted.

### DiscountStrategy

Defines the common interface for all discounts.

### PercentageDiscount

Calculates a percentage-based price reduction.

### FixedAmountDiscount

Subtracts a fixed amount.

### PremiumUserDiscount

Provides a special price for premium users.

### DiscountEngine

Checks applicable strategies and returns the lowest price.

### Strategy Pattern

Allows discount algorithms to be interchangeable.

### Polymorphism

Allows the engine to call the same methods on different strategy objects.

---

# 32. One-Sentence Summary

This project demonstrates how Python OOP and the Strategy Design Pattern can be used to build a flexible discount system where different discount algorithms can be added without changing the core discount engine.
