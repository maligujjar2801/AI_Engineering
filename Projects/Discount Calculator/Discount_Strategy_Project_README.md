# 💰 Discount Strategy Engine

A Python Object-Oriented Programming project that demonstrates the **Strategy Design Pattern**, **abstract classes**, **inheritance**, **polymorphism**, and **separation of responsibilities** through a simple product discount system.

---

## 📌 Project Overview

This project simulates an online store that needs to determine the best possible price for a product.

Different discount strategies are represented as separate classes:

- Percentage discount
- Fixed amount discount
- Premium-user discount

The `DiscountEngine` checks every applicable strategy, calculates the resulting prices, and returns the **lowest available price**.

### Example

For a product costing `$50`:

```text
Original Price       → $50.00
10% Discount         → $45.00
$5 Fixed Discount    → $45.00
Premium Discount     → $40.00

Best Price           → $40.00
```

---

## 🎯 Learning Objectives

This project was created to practice:

- Classes and objects
- Constructors
- Instance attributes
- Special methods
- Type hints
- Inheritance
- Abstract Base Classes
- Abstract methods
- Polymorphism
- Encapsulation
- Strategy Design Pattern
- Separation of concerns
- Open/Closed Principle
- List comprehensions
- `min()`
- String formatting
- Python's main-entry-point pattern

---

## 🧠 Concepts Demonstrated

### 1. Abstraction

The abstract class `DiscountStrategy` defines the methods that every discount strategy must implement:

```python
is_applicable()
apply_discount()
```

The individual strategies decide how those methods work.

---

### 2. Inheritance

The concrete discount classes inherit from:

```python
DiscountStrategy
```

They are:

```python
PercentageDiscount
FixedAmountDiscount
PremiumUserDiscount
```

---

### 3. Polymorphism

The `DiscountEngine` does not need to know the exact class of each strategy.

It simply calls:

```python
strategy.is_applicable(...)
strategy.apply_discount(...)
```

Each strategy responds according to its own implementation.

---

### 4. Strategy Pattern

Each discount algorithm is encapsulated inside its own class.

This makes strategies interchangeable and makes the system easier to extend.

A future discount can be added without rewriting the engine.

---

## 🏗️ Architecture

```text
                     DiscountStrategy
                           ▲
             ┌─────────────┼─────────────┐
             │             │             │
             │             │             │
   PercentageDiscount  FixedAmountDiscount  PremiumUserDiscount
             │             │             │
             └─────────────┼─────────────┘
                           │
                           ▼
                    DiscountEngine
                           │
                           ▼
                        Product
```

---

## 📂 Main Classes

### `Product`

Represents a product.

```python
Product("Wireless Mouse", 50.0)
```

Stores:

- `name`
- `price`

It also implements `__str__()` for readable output.

---

### `DiscountStrategy`

Abstract base class defining the common interface.

```python
class DiscountStrategy(ABC):
```

It requires:

```python
is_applicable()
apply_discount()
```

---

### `PercentageDiscount`

Applies a percentage reduction.

Example:

```python
PercentageDiscount(10)
```

For a `$50` product:

```text
$50 × 0.90 = $45
```

---

### `FixedAmountDiscount`

Subtracts a fixed amount.

Example:

```python
FixedAmountDiscount(5)
```

For a `$50` product:

```text
$50 - $5 = $45
```

---

### `PremiumUserDiscount`

Applies a special price to premium users.

The implementation gives premium users a 20% discount.

For a `$50` product:

```text
$50 × 0.80 = $40
```

---

### `DiscountEngine`

The engine receives a list of strategies:

```python
engine = DiscountEngine(strategies)
```

It then:

1. Starts with the original price.
2. Checks each strategy.
3. Determines whether it applies.
4. Calculates the discounted price.
5. Stores applicable prices.
6. Selects the minimum price.

---

## 🔄 Program Flow

```text
             Product
                │
                ▼
        Discount Strategies
                │
                ▼
         Discount Engine
                │
        ┌───────┴────────┐
        ▼                ▼
 Check applicability   Apply discount
        │                │
        └───────┬────────┘
                ▼
        Collect prices
                │
                ▼
          min(prices)
                │
                ▼
           Best Price
```

---

## 💻 Example Code

```python
from abc import ABC, abstractmethod


class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'{self.name} - ${self.price}'


class DiscountStrategy(ABC):
    @abstractmethod
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        pass

    @abstractmethod
    def apply_discount(self, product: Product) -> float:
        pass


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: int) -> None:
        self.percent = percent

    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return self.percent <= 70

    def apply_discount(self, product: Product) -> float:
        return product.price * (1 - self.percent / 100)


class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return product.price * 0.9 > self.amount

    def apply_discount(self, product: Product) -> float:
        return product.price - self.amount


class PremiumUserDiscount(DiscountStrategy):
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return user_tier.lower() == 'premium'

    def apply_discount(self, product: Product) -> float:
        return product.price * 0.8


class DiscountEngine:
    def __init__(self, strategies: list[DiscountStrategy]) -> None:
        self.strategies = strategies

    def calculate_best_price(self, product: Product, user_tier: str) -> float:
        prices = [product.price]

        for strategy in self.strategies:
            if strategy.is_applicable(product, user_tier):
                discounted = strategy.apply_discount(product)
                prices.append(discounted)

        return min(prices)


if __name__ == '__main__':
    product = Product('Wireless Mouse', 50.0)
    user_tier = 'Premium'

    strategies = [
        PercentageDiscount(10),
        FixedAmountDiscount(5),
        PremiumUserDiscount()
    ]

    engine = DiscountEngine(strategies)
    best_price = engine.calculate_best_price(product, user_tier)

    print(
        f'Best price for {product.name} '
        f'for {user_tier} user: ${best_price:.2f}'
    )
```

---

## ▶️ How to Run

Make sure Python is installed.

Then run:

```bash
python discount_strategy.py
```

Expected output:

```text
Best price for Wireless Mouse for Premium user: $40.00
```

---

## 🧪 Example Calculation

Given:

```python
product = Product("Wireless Mouse", 50.0)
user_tier = "Premium"
```

Strategies:

```python
PercentageDiscount(10)
FixedAmountDiscount(5)
PremiumUserDiscount()
```

The engine calculates:

| Strategy | Applicable | Final Price |
|---|---:|---:|
| Original price | Yes | `$50.00` |
| 10% discount | Yes | `$45.00` |
| $5 discount | Yes | `$45.00` |
| Premium discount | Yes | `$40.00` |

Therefore:

```python
min([50.0, 45.0, 45.0, 40.0])
```

returns:

```text
40.0
```

---

## ➕ Extending the Project

One of the biggest advantages of this design is that new discount strategies can be added independently.

For example:

```python
class StudentDiscount(DiscountStrategy):
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return user_tier.lower() == "student"

    def apply_discount(self, product: Product) -> float:
        return product.price * 0.9
```

Then it can be added to the engine:

```python
strategies = [
    PercentageDiscount(10),
    FixedAmountDiscount(5),
    PremiumUserDiscount(),
    StudentDiscount()
]
```

The `DiscountEngine` itself does not need to be modified.

---

## 🧩 Design Principles

### Open/Closed Principle

The system can be extended with new strategies without changing the existing engine.

### Single Responsibility

Each class has a focused responsibility:

- `Product` → product data
- Discount classes → discount rules
- `DiscountEngine` → price selection

### Dependency on Abstraction

The engine works with:

```python
DiscountStrategy
```

instead of depending directly on individual discount implementations.

---

## ⚠️ Current Project Limitations

This is an educational project, so the business rules are intentionally simple.

A production-ready system would ideally also:

- Validate prices.
- Prevent negative discounts.
- Prevent negative final prices.
- Handle money using appropriate financial precision.
- Define discount stacking rules.
- Add automated tests.
- Handle invalid user tiers.
- Add better error handling.
- Support multiple products or shopping carts.

---

## 🚀 Possible Future Features

- [ ] Student discount
- [ ] Seasonal discount
- [ ] Black Friday discount
- [ ] Coupon codes
- [ ] Loyalty discounts
- [ ] Shopping cart support
- [ ] Multiple products
- [ ] Discount stacking rules
- [ ] Discount priorities
- [ ] Input validation
- [ ] Unit tests
- [ ] File/database storage
- [ ] Command-line interface
- [ ] GUI
- [ ] Web API

---

## 📚 Key Takeaways

The most important lesson from this project is that **different algorithms can be separated into different classes and used through a common interface**.

Instead of building one giant discount function, this project creates independent strategies.

That makes the application:

- Easier to understand
- Easier to test
- Easier to extend
- Easier to maintain
- More aligned with professional OOP design

---

## 👨‍💻 Project Status

**Status:** Completed ✅

**Main Topic:** Object-Oriented Programming + Design Patterns

**Design Pattern:** Strategy Pattern

**Language:** Python

**Difficulty:** Intermediate

---

## 📝 Learning Note

This project is especially useful as an OOP practice project because it goes beyond simply creating classes. It demonstrates how multiple classes can cooperate through abstraction and polymorphism to solve a realistic problem.

The key architecture is:

```text
Abstract Strategy
       ↓
Concrete Strategies
       ↓
Discount Engine
       ↓
Best Price
```

---

## 📄 License

This project is intended for learning and educational purposes.
