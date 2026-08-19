# 🚀 Day 6 - Lists in Python


## 📚 What is a List?


A list is a built-in Python data structure used to store multiple values in a single variable. Lists are ordered, mutable (changeable), and allow duplicate values.


### Syntax


```python
students = ["Ali", "Fatima", "Zainab"]
```


---


## 📚 Creating a List


Lists are created using square brackets `[]`.


### Example


```python
numbers = [10, 20, 30, 40]
fruits = ["Apple", "Mango", "Banana"]
mixed = [1, "Ali", 3.5, True]
```


---


## 📚 Accessing List Elements


List elements are accessed using their index.


```python
fruits = ["Apple", "Mango", "Banana"]


print(fruits[0])
print(fruits[2])
```


---


## 📚 Negative Indexing


Negative indexing starts from the end of the list.


```python
print(fruits[-1])
print(fruits[-2])
```


---


## 📚 List Slicing


Slicing is used to access multiple elements.


### Syntax


```python
list[start:end]
```


### Example


```python
numbers = [10,20,30,40,50]


print(numbers[1:4])
```


---


## 📚 Modifying List Elements


Lists are mutable.


```python
fruits = ["Apple","Mango","Banana"]


fruits[1] = "Orange"
```


---


## 📚 Adding Elements


### append()


Adds an item at the end.


```python
fruits.append("Grapes")
```


### insert()


Adds an item at a specific index.


```python
fruits.insert(1,"Orange")
```


### extend()


Adds multiple items.


```python
fruits.extend(["Peach","Guava"])
```


---


## 📚 Removing Elements


### remove()


Removes an item by value.


```python
fruits.remove("Apple")
```


### pop()


Removes an item using its index.


```python
fruits.pop(2)
```


### del


Deletes an element or the whole list.


```python
del fruits[1]
```


### clear()


Removes all elements.


```python
fruits.clear()
```


---


## 📚 Useful List Methods


### sort()


Sorts the list.


```python
numbers.sort()
```


### reverse()


Reverses the order.


```python
numbers.reverse()
```


### count()


Counts occurrences.


```python
numbers.count(10)
```


### index()


Returns the index of an item.


```python
numbers.index(30)
```


### copy()


Creates a copy of a list.


```python
new_list = numbers.copy()
```


---


## 📚 len() Function


Returns the number of elements.


```python
print(len(numbers))
```


---


## 📚 Membership Operators


### in


```python
if "Ali" in students:
    print("Student found")
```


### not in


```python
if "Ahmed" not in students:
    print("Student not found")
```


---


## 📚 Iterating Through a List


Using a for loop.


```python
for student in students:
    print(student)
```


---


## 📚 Nested Lists


A list inside another list.


```python
students = [
    ["Ali",18],
    ["Fatima",17]
]
```


---


# 💻 Programs Completed


- Student Marks
- Favorite Fruit
- Remove Subject
- Maximum and Minimum Number
- Student Management System


---


# 🎯 What I Learned


Today I learned how to use Python lists to store and manage collections of data efficiently. I practiced creating, accessing, modifying, adding, and removing list elements using different methods. I also learned how to iterate through lists with loops, search for elements, and apply list methods such as `append()`, `remove()`, `sort()`, and `pop()`. By building multiple programs, including a menu-driven Student Management System, I improved my problem-solving skills and gained confidence in working with lists.


---


# ⭐ Key Takeaways


- Lists are ordered and mutable.
- Indexing starts from `0`.
- Negative indexing starts from the end.
- `append()` adds one item.
- `extend()` adds multiple items.
- `remove()` removes by value.
- `pop()` removes by index.
- `len()` returns the number of elements.
- Lists work very well with loops.