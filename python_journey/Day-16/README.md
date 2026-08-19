# 🐍 Day 16 — File Handling in Python

Welcome to **Day 16** of my Python learning journey!

Today I started learning **File Handling in Python** — an important concept that allows programs to store, read, modify, and manage data using files.

## 📚 What I Learned

### 📂 File Handling Fundamentals

- What file handling is
- Why files are useful
- Text files vs binary files
- File objects
- The `open()` function

### 🔐 File Modes

I learned how different modes control what Python can do with a file:

- `r` — Read
- `w` — Write / overwrite
- `a` — Append
- `x` — Create
- `r+` — Read + Write
- `w+` — Write + Read
- `a+` — Append + Read
- `b` — Binary mode
- `t` — Text mode

### 📖 Reading Files

I practiced:

- `read()`
- `read(n)`
- `readline()`
- `readlines()`
- Reading files using `for` loops

### ✍️ Writing Files

I learned:

- `write()`
- `writelines()`
- Writing multiple lines with `\n`
- The difference between writing and appending
- How `"w"` can overwrite existing content

### 🔄 File Pointers

I learned how Python keeps track of its current position inside a file using:

- `tell()`
- `seek()`

### 🧹 Managing Files

I learned:

- `close()`
- The `with open(...)` statement
- Why using `with` is the preferred way to work with files

### 📍 File Paths

I learned the basics of:

- Relative paths
- Absolute paths
- Windows paths
- Raw strings for Windows paths

### ⚠️ Error Handling

I practiced handling common file-related errors:

- `FileNotFoundError`
- `FileExistsError`
- Using `try-except` with file operations

### 🌐 Encoding

I also learned the basics of:

- File encoding
- `UTF-8`
- Using `encoding="utf-8"`

### 🔗 Connecting Previous Knowledge

Day 16 also helped me combine file handling with concepts I had already learned, such as:

- Lists
- Loops
- Functions
- String methods
- Exception handling

---

## 💡 Important Concepts

The four basic file modes I need to remember are:

```text
r → read
w → write / overwrite
a → append
x → create
```

And:

```text
+ → adds the other read/write capability
b → binary
t → text
```

---

## 🧠 My Key Takeaway

File handling allows a Python program to work with data that can **persist even after the program stops running**.

The basic workflow I learned is:

```text
open()
   ↓
choose a mode
   ↓
read / write / append
   ↓
process the data
   ↓
close()
```

And the recommended approach is:

```python
with open("data.txt", "r") as file:
    content = file.read()
```

---

## 📁 Day 16 Files

This folder contains my Day 16 work and notes on Python File Handling.

```text
Day-16/
│
├── README.md
└── day16_notes.md
```

*More practice programs and projects will be added as I continue learning.*

---

## 🚀 Progress

**Day 16 — Completed ✅**

> One more step toward becoming an **AI Engineer**. 🤖🐍

I'm continuing to build my Python fundamentals one day at a time.
