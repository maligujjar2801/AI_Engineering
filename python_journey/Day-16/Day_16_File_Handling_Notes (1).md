# 🐍 Day 16 — File Handling in Python

## 1. What is File Handling?

**File handling** means using Python to **create, open, read, write, update, and delete files** stored on a computer.

Normally, data stored in variables disappears when the program ends:

```python
name = "Ali"
```

Once the program finishes, `name` is gone.

But if we save the data into a file, the data remains stored even after the program ends.

### Why do we need file handling?

File handling allows programs to:

- Store information permanently
- Read previously saved information
- Create new files
- Modify existing files
- Add new information
- Work with large amounts of data
- Store logs, settings, records, etc.

---

# 2. Types of Files

At your level, you mainly need to understand two types.

## 1. Text Files

Text files contain readable characters.

Examples:

```text
.txt
.csv
.py
.md
.json
```

Example:

```text
name = Ali
age = 17
```

Python commonly handles text files using:

```python
open()
```

## 2. Binary Files

Binary files store data in binary form rather than ordinary readable text.

Examples:

```text
.jpg
.png
.mp3
.mp4
.pdf
.exe
```

For now, focus heavily on **text files**.

---

# 3. The `open()` Function

The most important function in Python file handling is:

```python
open()
```

It is used to open a file.

Basic syntax:

```python
file = open("filename.txt")
```

Example:

```python
file = open("data.txt")
```

Python will try to open `data.txt`.

By default, `open()` uses **read mode (`"r"`)**.

So this:

```python
file = open("data.txt")
```

is essentially:

```python
file = open("data.txt", "r")
```

---

# 4. File Object

When you do:

```python
file = open("data.txt", "r")
```

Python doesn't put the entire file into `file`.

Instead, `file` becomes a **file object**.

You can then use methods on that object:

```python
file.read()
file.readline()
file.close()
```

Think of it like:

```text
data.txt
   ↓
open()
   ↓
file object
   ↓
read / write / modify
```

---

# 5. File Modes

A **file mode** tells Python **what you want to do with the file**.

The most important modes are:

| Mode | Meaning |
|---|---|
| `"r"` | Read |
| `"w"` | Write |
| `"a"` | Append |
| `"x"` | Create |
| `"r+"` | Read + Write |
| `"w+"` | Write + Read |
| `"a+"` | Append + Read |
| `"b"` | Binary mode |
| `"t"` | Text mode |

You can also combine modes.

For example:

```text
"rb"
"wb"
"ab"
"r+"
```

---

# 6. `"r"` — Read Mode

`"r"` means **read**.

```python
file = open("data.txt", "r")
```

It allows you to read the contents of an existing file.

Example:

```python
file = open("data.txt", "r")

content = file.read()

print(content)

file.close()
```

### Important

If the file doesn't exist:

```python
open("data.txt", "r")
```

Python raises:

```text
FileNotFoundError
```

because read mode expects the file to already exist.

---

# 7. `"w"` — Write Mode

`"w"` means **write**.

```python
file = open("data.txt", "w")
```

It allows you to write data to a file.

Example:

```python
file = open("data.txt", "w")

file.write("Hello Python!")

file.close()
```

If `data.txt` doesn't exist, Python **creates it**.

## ⚠️ `"w"` overwrites existing content

Suppose `data.txt` contains:

```text
Hello
Welcome to Python
```

Then:

```python
file = open("data.txt", "w")
file.write("New data")
file.close()
```

The old content is replaced.

The file becomes:

```text
New data
```

Remember:

> `"w"` = write from the beginning and **replace existing content**.

---

# 8. `"a"` — Append Mode

`"a"` means **append**.

It adds new data to the **end of the file**.

Example:

```python
file = open("data.txt", "a")

file.write("New line")

file.close()
```

If the file originally contains:

```text
Hello
Python
```

After this operation:

```text
Hello
Python
New line
```

The existing content isn't deleted.

### If the file doesn't exist?

Python creates it.

So:

```python
open("data.txt", "a")
```

can create the file if necessary.

Remember:

```text
w → replace
a → add to the end
```

---

# 9. `"x"` — Create Mode

`"x"` means **create a new file**.

```python
file = open("newfile.txt", "x")
```

If the file doesn't exist, it is created.

But if it already exists, Python raises:

```text
FileExistsError
```

Example:

```python
file = open("newfile.txt", "x")
file.write("Hello")
file.close()
```

This is useful when you specifically want to make sure you're creating a **new** file rather than accidentally overwriting an existing one.

---

# 10. `"r+"` — Read and Write

`"r+"` allows both:

- Reading
- Writing

Example:

```python
file = open("data.txt", "r+")

content = file.read()
print(content)

file.write("Hello")

file.close()
```

### Important

The file must already exist.

If it doesn't exist:

```python
open("data.txt", "r+")
```

raises:

```text
FileNotFoundError
```

---

# 11. `"w+"` — Write and Read

`"w+"` allows:

- Writing
- Reading

Example:

```python
file = open("data.txt", "w+")

file.write("Hello Python")

file.seek(0)

print(file.read())

file.close()
```

### ⚠️ Important

`"w+"` **clears the existing file first**.

So:

```python
open("data.txt", "w+")
```

can destroy existing content.

It also creates the file if it doesn't exist.

---

# 12. `"a+"` — Append and Read

`"a+"` allows:

- Appending
- Reading

Example:

```python
file = open("data.txt", "a+")

file.write("New data")

file.seek(0)

print(file.read())

file.close()
```

The existing content remains, and new data is added at the end.

---

# 13. Quick Mode Comparison

| Mode | Read | Write | Create if missing | Deletes old content |
|---|---:|---:|---:|---:|
| `"r"` | ✅ | ❌ | ❌ | ❌ |
| `"w"` | ❌ | ✅ | ✅ | ✅ |
| `"a"` | ❌ | ✅ | ✅ | ❌ |
| `"x"` | ❌ | ✅ | ✅ | ❌* |
| `"r+"` | ✅ | ✅ | ❌ | ❌ |
| `"w+"` | ✅ | ✅ | ✅ | ✅ |
| `"a+"` | ✅ | ✅ | ✅ | ❌ |

`"x"` fails if the file already exists, so it doesn't overwrite it.

### Easy memory trick

```text
r = read
w = write
a = append
x = create
+ = add the opposite operation
```

For example:

```text
r  → read
r+ → read + write

w  → write
w+ → write + read

a  → append
a+ → append + read
```

---

# 14. Text and Binary Modes

Python also has:

```text
t = text
b = binary
```

## Text mode

```python
open("data.txt", "rt")
```

`"t"` is the default, so:

```python
open("data.txt", "r")
```

and:

```python
open("data.txt", "rt")
```

are effectively the same for normal text files.

## Binary mode

```python
open("image.jpg", "rb")
```

Common combinations:

```python
"rb"   # read binary
"wb"   # write binary
"ab"   # append binary
```

You don't need to deeply master binary files yet, but you should understand what `b` means.

---

# 15. Reading a File with `.read()`

The `.read()` method reads file contents.

```python
file = open("data.txt", "r")

content = file.read()

print(content)

file.close()
```

If the file contains:

```text
Hello
Python
World
```

`.read()` returns the entire remaining content as a string.

---

# 16. Reading a Specific Number of Characters

You can give `.read()` a number.

```python
file.read(5)
```

This means:

> Read the next 5 characters.

Example:

```python
file = open("data.txt", "r")

print(file.read(5))

file.close()
```

If the file contains:

```text
Python Programming
```

the output would be:

```text
Pytho
```

---

# 17. `.readline()`

`.readline()` reads **one line** at a time.

Example:

```python
file = open("data.txt", "r")

print(file.readline())

file.close()
```

Suppose:

```text
Python
Java
C++
```

Then the first `readline()` reads:

```text
Python
```

You can call it again:

```python
print(file.readline())
print(file.readline())
```

Output:

```text
Python
Java
C++
```

---

# 18. `.readlines()`

`.readlines()` reads all lines and returns them as a **list**.

Example:

```python
file = open("data.txt", "r")

lines = file.readlines()

print(lines)

file.close()
```

If the file contains:

```text
Python
Java
C++
```

you get something like:

```python
['Python\n', 'Java\n', 'C++']
```

Notice the `\n`.

---

# 19. Difference Between `read()`, `readline()`, and `readlines()`

| Method | Returns |
|---|---|
| `.read()` | Entire remaining content as a string |
| `.read(n)` | Next `n` characters |
| `.readline()` | One line |
| `.readlines()` | List containing lines |

Think:

```text
read()       → everything
readline()   → one line
readlines()  → all lines as a list
```

---

# 20. Reading a File Using a `for` Loop

You can directly loop through a file.

```python
file = open("data.txt", "r")

for line in file:
    print(line)

file.close()
```

This is often better than loading the entire file into memory at once, especially for large files.

You can remove the extra newline with:

```python
for line in file:
    print(line.strip())
```

---

# 21. Writing to a File with `.write()`

`.write()` writes a string into a file.

```python
file = open("data.txt", "w")

file.write("Hello Python")

file.close()
```

### Important

`.write()` expects a **string**.

This works:

```python
file.write("Hello")
```

This doesn't directly work:

```python
file.write(100)
```

because `100` is an integer.

You can convert it:

```python
file.write(str(100))
```

---

# 22. Writing Multiple Lines

You can use `\n`.

```python
file = open("data.txt", "w")

file.write("Python\n")
file.write("Java\n")
file.write("C++\n")

file.close()
```

The file becomes:

```text
Python
Java
C++
```

---

# 23. `.writelines()`

`.writelines()` writes multiple strings.

Example:

```python
lines = [
    "Python\n",
    "Java\n",
    "C++\n"
]

file = open("data.txt", "w")

file.writelines(lines)

file.close()
```

### Important

`writelines()` **does not automatically add `\n`**.

So:

```python
file.writelines(["Python", "Java", "C++"])
```

may produce:

```text
PythonJavaC++
```

If you want separate lines:

```python
file.writelines(["Python\n", "Java\n", "C++\n"])
```

---

# 24. The `with` Statement ⭐

This is one of the most important concepts in Python file handling.

Instead of:

```python
file = open("data.txt", "r")

print(file.read())

file.close()
```

you can write:

```python
with open("data.txt", "r") as file:
    print(file.read())
```

Python automatically handles closing the file.

---

# 25. Why Use `with`?

Imagine you forget:

```python
file.close()
```

The file may remain open longer than necessary.

Using:

```python
with open(...) as file:
```

Python automatically closes the file when the block ends.

Example:

```python
with open("data.txt", "r") as file:
    content = file.read()

print(content)
```

After leaving the `with` block, the file is automatically closed.

### Best practice

For normal file handling, prefer:

```python
with open("data.txt", "r") as file:
```

instead of manually managing:

```python
open()
close()
```

---

# 26. `close()`

`.close()` closes the file.

```python
file.close()
```

Example:

```python
file = open("data.txt", "r")

print(file.read())

file.close()
```

After closing, you shouldn't try to perform normal operations on that file object.

---

# 27. Checking Whether a File is Closed

You can use:

```python
file.closed
```

Example:

```python
file = open("data.txt", "r")

print(file.closed)

file.close()

print(file.closed)
```

Output:

```text
False
True
```

---

# 28. File Pointer

A very important concept is the **file pointer**.

When Python reads a file, it keeps track of its current position.

Imagine this file:

```text
Python
```

Initially:

```text
|Python
^
pointer
```

After reading 3 characters:

```text
Pyt|hon
   ^
 pointer
```

The pointer moves as you read or write.

---

# 29. `.tell()`

`.tell()` tells you the current position of the file pointer.

Example:

```python
file = open("data.txt", "r")

print(file.tell())

file.read(5)

print(file.tell())

file.close()
```

If the first 5 characters were read, the pointer will generally have moved accordingly.

---

# 30. `.seek()`

`.seek()` moves the file pointer to a particular position.

Syntax:

```python
file.seek(position)
```

Example:

```python
file = open("data.txt", "r")

file.seek(0)

print(file.read())

file.close()
```

`seek(0)` moves the pointer back to the beginning.

---

# 31. Why `seek()` is Important

Consider:

```python
file = open("data.txt", "r")

print(file.read())
print(file.read())

file.close()
```

The second `.read()` may return nothing because the pointer has already reached the end.

You can reset it:

```python
file = open("data.txt", "r")

print(file.read())

file.seek(0)

print(file.read())

file.close()
```

Now you can read the file again from the beginning.

---

# 32. `seek()` + `tell()` Together

These two methods are closely related.

```python
tell()
```

asks:

> Where am I?

```python
seek()
```

says:

> Move here.

Example:

```python
with open("data.txt", "r") as file:

    print(file.tell())

    file.read(5)

    print(file.tell())

    file.seek(0)

    print(file.tell())
```

---

# 33. Newline Character `\n`

When working with multiple lines, you'll frequently encounter:

```python
\n
```

It represents a **new line**.

Example:

```python
text = "Hello\nPython"
print(text)
```

Output:

```text
Hello
Python
```

You can use it when writing:

```python
file.write("Hello\n")
file.write("Python\n")
```

---

# 34. `.strip()`

When reading lines, you may encounter unwanted whitespace or `\n`.

You can use:

```python
line.strip()
```

Example:

```python
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())
```

`strip()` removes whitespace from the beginning and end of the string, including newline characters.

---

# 35. File Paths

You don't always have to use only:

```python
"data.txt"
```

You can specify a path.

Example:

```python
open("files/data.txt", "r")
```

Windows paths can look like:

```text
C:\Users\Ali\Documents\data.txt
```

But backslashes have special meanings in Python strings.

So this can cause problems:

```python
"C:\new\data.txt"
```

because sequences such as `\n` can be interpreted specially.

---

# 36. Raw Strings for Windows Paths

You can use a raw string:

```python
r"C:\Users\Ali\Documents\data.txt"
```

The `r` tells Python to treat backslashes more literally.

Another option is:

```python
"C:\\Users\\Ali\\Documents\\data.txt"
```

You can also use forward slashes:

```python
"C:/Users/Ali/Documents/data.txt"
```

---

# 37. Relative vs Absolute Paths

## Relative path

A relative path starts from your program's current working directory.

```python
open("data.txt")
```

or:

```python
open("files/data.txt")
```

## Absolute path

An absolute path gives the complete location.

Example:

```python
open("C:/Users/Ali/Documents/data.txt")
```

For beginner projects, relative paths are usually easier to manage.

---

# 38. FileNotFoundError

One of the most common file errors is:

```text
FileNotFoundError
```

Example:

```python
file = open("does_not_exist.txt", "r")
```

If the file isn't there, Python can't open it for reading.

You can handle this using `try-except`.

```python
try:
    with open("data.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File does not exist.")
```

---

# 39. FileExistsError

This commonly happens with `"x"` mode.

```python
file = open("data.txt", "x")
```

If `data.txt` already exists:

```text
FileExistsError
```

You can handle it:

```python
try:
    with open("data.txt", "x") as file:
        file.write("Hello")

except FileExistsError:
    print("File already exists.")
```

---

# 40. Encoding

Text files use an encoding to represent characters.

A common encoding is:

```python
UTF-8
```

You can explicitly specify it:

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

When writing:

```python
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Hello")
```

For modern Python programs, UTF-8 is usually a good default.

---

# 41. `encoding="utf-8"` and Non-English Text

Encoding becomes especially useful when dealing with characters outside basic English.

For example:

```python
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("پاکستان")
```

UTF-8 allows Python to properly handle a huge range of characters.

---

# 42. Important File Object Methods

At your level, know these:

| Method | Purpose |
|---|---|
| `read()` | Read content |
| `readline()` | Read one line |
| `readlines()` | Read lines into a list |
| `write()` | Write a string |
| `writelines()` | Write multiple strings |
| `seek()` | Move file pointer |
| `tell()` | Get pointer position |
| `close()` | Close file |

And useful attributes:

```python
file.closed
file.name
file.mode
```

Example:

```python
with open("data.txt", "r") as file:
    print(file.name)
    print(file.mode)
```

---

# 43. Creating a Simple File

```python
with open("hello.txt", "w") as file:
    file.write("Hello Python!")
```

That's enough to create the file.

---

# 44. Reading a Simple File

```python
with open("hello.txt", "r") as file:
    content = file.read()

print(content)
```

---

# 45. Adding Data to a File

```python
with open("hello.txt", "a") as file:
    file.write("\nWelcome to my Python journey.")
```

---

# 46. A Complete Mini Example

Let's create a simple student file:

```python
with open("student.txt", "w") as file:
    file.write("Name: Ali\n")
    file.write("Age: 17\n")
    file.write("Course: Python\n")
```

Now read it:

```python
with open("student.txt", "r") as file:
    content = file.read()

print(content)
```

Output:

```text
Name: Ali
Age: 17
Course: Python
```

Then append something:

```python
with open("student.txt", "a") as file:
    file.write("Goal: AI Engineer\n")
```

Now the file contains:

```text
Name: Ali
Age: 17
Course: Python
Goal: AI Engineer
```

This combines:

```text
w → create/write
r → read
a → append
```

---

# 47. Updating File Content

Python doesn't have a simple `"update"` mode.

Instead, a common approach is:

1. Read the file
2. Modify the data in Python
3. Write the modified data back

Example:

```python
with open("data.txt", "r") as file:
    content = file.read()

content = content.replace("Python", "AI")

with open("data.txt", "w") as file:
    file.write(content)
```

If the original file contains:

```text
I am learning Python.
```

it becomes:

```text
I am learning AI.
```

This concept will become extremely useful later when you work with real data.

---

# 48. File Handling with Lists

Because `readlines()` returns a list, you can combine file handling with lists.

```python
with open("names.txt", "r") as file:
    names = file.readlines()

print(names)
```

You can process the list:

```python
names = [name.strip() for name in names]

print(names)
```

Now you have a clean list of names.

This is where your previous knowledge of **lists and loops** starts connecting with file handling.

---

# 49. File Handling + Functions

You can also put file operations inside functions.

```python
def read_file(filename):
    with open(filename, "r") as file:
        return file.read()
```

Then:

```python
content = read_file("data.txt")

print(content)
```

This is a great example of combining your **functions + file handling** knowledge.

---

# 50. File Handling + Exception Handling

You can combine `try-except` with files:

```python
try:
    with open("data.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("The file was not found.")
```

This makes your programs much more reliable.

---

# 51. Common Mistakes to Avoid

## Mistake 1 — Forgetting to close the file

```python
file = open("data.txt", "r")

print(file.read())
```

Better:

```python
with open("data.txt", "r") as file:
    print(file.read())
```

---

## Mistake 2 — Using `"w"` when you wanted `"a"`

```python
open("data.txt", "w")
```

can erase existing content.

If you want to add:

```python
open("data.txt", "a")
```

---

## Mistake 3 — Reading a file that doesn't exist

```python
open("missing.txt", "r")
```

causes:

```text
FileNotFoundError
```

---

## Mistake 4 — Forgetting `\n`

This:

```python
file.write("Python")
file.write("Java")
```

can produce:

```text
PythonJava
```

Use:

```python
file.write("Python\n")
file.write("Java\n")
```

---

## Mistake 5 — Expecting `write()` to accept numbers

This:

```python
file.write(100)
```

doesn't work because `write()` expects a string.

Use:

```python
file.write(str(100))
```

---

# 52. The Most Important Mental Model

Remember this entire process:

```text
                 FILE HANDLING

                      ↓
                   open()
                      ↓
              ┌───────┴───────┐
              ↓               ↓
            READ             WRITE
              ↓               ↓
           read()          write()
           readline()      writelines()
           readlines()         ↓
              ↓             append
              ↓
           seek()
           tell()
              ↓
            close()
```

And preferably:

```python
with open(...) as file:
    # perform operation
```

because Python handles closing automatically.

---

# 53. ⭐ File Modes You MUST Know

For your Day 16, make absolutely sure you understand these:

```python
"r"    # read
"w"    # write / overwrite
"a"    # append
"x"    # create new file
"r+"   # read + write
"w+"   # write + read, overwrites
"a+"   # append + read
"rb"   # read binary
"wb"   # write binary
"ab"   # append binary
```

You don't need to memorize every possible combination immediately.

Understand the logic:

```text
r → read
w → write
a → append
x → create
+ → add read/write capability
b → binary
t → text
```

---

# 54. ⭐ Cheat Sheet

```python
# Open
file = open("data.txt", "r")

# Read everything
file.read()

# Read specific characters
file.read(10)

# Read one line
file.readline()

# Read all lines
file.readlines()

# Write
file.write("Hello")

# Write multiple strings
file.writelines(["Hello\n", "Python\n"])

# Current pointer position
file.tell()

# Move pointer
file.seek(0)

# Close
file.close()
```

### Recommended style:

```python
with open("data.txt", "r") as file:
    content = file.read()
```

---

# 55. 🧠 Day 16 — What You Should Be Able to Do

By the end of Day 16, you should be comfortable with:

- What file handling is
- What a file object is
- `open()`
- File modes
- `"r"`
- `"w"`
- `"a"`
- `"x"`
- `"r+"`
- `"w+"`
- `"a+"`
- `"b"` and `"t"`
- `read()`
- `readline()`
- `readlines()`
- `write()`
- `writelines()`
- `close()`
- `with`
- File pointers
- `seek()`
- `tell()`
- `\n`
- `strip()`
- Relative paths
- Absolute paths
- `FileNotFoundError`
- `FileExistsError`
- Basic `try-except` with files
- Basic encoding with UTF-8
- Reading → modifying → rewriting files

## The biggest concepts to master

If you remember nothing else initially, make these **rock solid**:

```text
open()
   ↓
modes
   ↓
read / write / append
   ↓
with open(...)
   ↓
seek / tell
   ↓
exceptions
```

And especially understand the difference between:

```python
"r"  # read
"w"  # overwrite
"a"  # append
"x"  # create
```

These four modes form the foundation of Python file handling.
