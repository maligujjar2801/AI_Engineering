# 📘 Day 12 - Salary Tracker Workshop (OOP)

## Topics Covered

- Encapsulation
- Private Attributes
- Properties (`@property`)
- Property Setters (`@setter`)
- `__repr__()` Method
- Data Validation
- `isinstance()`
- `hasattr()`
- Raising Exceptions
- Dictionary Lookup
- Controlled Attribute Updates

---

## Encapsulation

Encapsulation is one of the four pillars of Object-Oriented Programming. It protects object data by controlling how attributes are accessed and modified.

Instead of modifying private attributes directly:

```python
self._salary
```

we use properties:

```python
self.salary
```

This ensures validation before updating the value.

---

## Private Attributes

Private attributes begin with an underscore (`_`).

Examples:

```python
self._name
self._level
self._salary
```

These attributes should not be modified directly outside the class.

---

## Properties (`@property`)

The `@property` decorator allows a method to behave like an attribute.

Example:

```python
@property
def salary(self):
    return self._salary
```

Usage:

```python
employee.salary
```

instead of

```python
employee.salary()
```

---

## Property Setter (`@setter`)

A setter controls how values are assigned to an attribute.

Example:

```python
@salary.setter
def salary(self, new_salary):
    self._salary = new_salary
```

Whenever we write:

```python
employee.salary = 5000
```

Python automatically calls the setter.

---

## `__repr__()` Method

The `__repr__()` method returns the official string representation of an object.

Example:

```python
Employee("Ali", "Senior")
```

returns

```python
"Employee('Ali', 'Senior')"
```

---

## Data Validation

Validation ensures that only correct values are assigned to object attributes.

Examples:

- Checking data types
- Checking valid employee levels
- Preventing duplicate levels
- Preventing demotion
- Preventing salaries below the minimum allowed salary

---

## `isinstance()`

Used to check whether an object belongs to a particular data type.

Syntax:

```python
isinstance(variable, datatype)
```

Example:

```python
isinstance(age, int)
```

Returns either:

- `True`
- `False`

---

## `hasattr()`

Checks whether an object already contains a particular attribute.

Syntax:

```python
hasattr(object, "attribute")
```

Example:

```python
hasattr(self, "_level")
```

It is commonly used during object initialization to avoid an `AttributeError`.

---

## Exception Handling

Exceptions stop program execution whenever invalid data is provided.

### TypeError

Raised when the data type is incorrect.

Example:

```python
raise TypeError("'salary' must be a number.")
```

### ValueError

Raised when the value is invalid.

Example:

```python
raise ValueError("Cannot change to lower level.")
```

---

## Dictionary Lookup

Instead of comparing employee level names directly, we can compare the values stored in a dictionary.

Example:

```python
Employee._base_salaries[self.level]
```

This returns the minimum salary assigned to the current employee level.

---

## Calling Setters

Instead of updating private attributes directly:

```python
self._salary = value
```

call the property setter:

```python
self.salary = value
```

This automatically performs validation and executes any additional logic written inside the setter.

---

# What I Learned

Today I built a Salary Tracker while learning advanced Object-Oriented Programming concepts. I learned how properties and setters work, how encapsulation protects object data, how private attributes should be accessed through properties, how to validate data using `isinstance()`, how `hasattr()` prevents initialization errors, how to raise `TypeError` and `ValueError`, and why setters should always be used instead of directly modifying private attributes.