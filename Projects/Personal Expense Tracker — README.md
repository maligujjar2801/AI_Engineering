# 💰 Personal Expense Tracker

A beginner-friendly command-line **Personal Expense Tracker** built with Python.

This project was created to apply my Python knowledge of **file handling, functions, loops, lists, conditionals, string manipulation, and basic data processing** to a real-world problem.

---

## 📌 About the Project

The Personal Expense Tracker allows users to manage their daily expenses directly from the terminal.

Expenses are stored permanently in a text file (`Expense.txt`), so the data remains available even after the program is closed.

The application provides a simple menu where users can:

- Add new expenses
- View saved expenses
- Calculate total spending
- Search expenses by category
- Delete an expense
- Exit the application

---

## ✨ Features

### 1. Add Expense

Users can enter:

- Category
- Amount
- Description

Example:

```text
Category: Food
Amount: 350
Description: Lunch
```

The information is then appended to `Expense.txt`.

---

### 2. View Expenses

Displays all saved expenses in a formatted table.

Example:

```text
========== EXPENSES ==========

1. Food            Rs.350    Lunch
2. Transport       Rs.120    Rickshaw
3. Education       Rs.500    Python Course
```

---

### 3. Calculate Total

Reads all expenses from the file and calculates the total amount spent.

Example:

```text
Total Expenses: Rs.970
```

---

### 4. Search Expenses

Users can search for expenses using their category.

Example:

```text
Enter Category: Food
```

The program displays all expenses belonging to that category.

If no matching expense exists, the program informs the user.

---

### 5. Delete Expense

Users can select an expense by its displayed number and remove it from the file.

The program:

1. Reads the existing expenses.
2. Removes the selected expense from the list.
3. Opens the file in write mode.
4. Writes the remaining expenses back to the file.

This helped me understand the important **read → modify → rewrite** pattern used when working with text files.

---

### 6. Continuous Menu

The application runs inside a `while` loop, allowing users to perform multiple operations without restarting the program.

The program continues running until the user selects:

```text
6. Exit
```

---

## 🗂️ Project Structure

```text
Expense_Tracker/
│
├── main.py
├── Expense.txt
└── README.md
```

### `main.py`

Contains the complete Python application.

### `Expense.txt`

Stores all expense records.

### `README.md`

Contains documentation for the project.

---

## 💾 Data Storage

Expenses are stored in a simple text-based format:

```text
Date | Category | Amount | Description
```

Example:

```text
2026-08-19 | Food | 350 | Lunch
2026-08-19 | Transport | 120 | Rickshaw
2026-08-19 | Education | 500 | Python Course
```

The project currently uses Python's built-in file handling instead of a database.

---

## 🧠 Python Concepts Used

This project helped me practice:

- Variables
- User input
- Functions
- Function calls
- `if / elif / else`
- `while` loops
- `for` loops
- Lists
- List indexing
- `del`
- String methods
- `.split()`
- `.strip()`
- `.capitalize()`
- f-string formatting
- Type conversion with `int()`
- Boolean variables
- File handling
- `open()`
- `with open()`
- File modes:
  - `"r"` — Read
  - `"w"` — Write
  - `"a"` — Append
- `readlines()`
- `write()`
- Reading, modifying, and rewriting file data

---

## 🔄 How the Program Works

The basic flow of the application is:

```text
                    START
                      │
                      ▼
               Display Menu
                      │
              ┌───────┴────────┐
              │ User's Choice  │
              └───────┬────────┘
                      │
       ┌──────────────┼──────────────┐
       ▼              ▼              ▼
   Add Expense    View Expenses   Calculate Total
       │              │              │
       └──────────────┼──────────────┘
                      │
       ┌──────────────┼──────────────┐
       ▼              ▼              ▼
     Search         Delete          Exit
       │              │              │
       └──────────────┴──────────────┘
                      │
                      ▼
                 Back to Menu
```

---

## 🚀 Future Improvements

This is the first version of the project, so there are several things I plan to improve.

### Version 1.1

- [ ] Automatic current date
- [ ] Better error handling
- [ ] Handle invalid amount input
- [ ] Handle invalid menu choices more safely
- [ ] Improve input validation

### Version 2.0

- [ ] Replace text-file storage with JSON
- [ ] Store structured expense data
- [ ] Add monthly expense summaries
- [ ] Add category-wise totals

### Version 3.0

- [ ] Rebuild the project using Object-Oriented Programming
- [ ] Create an `Expense` class
- [ ] Create an `ExpenseTracker` class
- [ ] Improve project architecture

### Future

- [ ] Database storage
- [ ] Graphical User Interface
- [ ] Expense charts and statistics
- [ ] Export reports
- [ ] More advanced financial analysis

---

## 🎯 What I Learned

The main purpose of this project was to move beyond simply learning Python syntax and actually **use Python to solve a real-world problem**.

Through this project, I learned how to:

> **Take data from a user → store it permanently → read it later → process it → modify it → and display useful information.**

The most important File Handling pattern I learned was:

```text
Read → Process → Modify → Rewrite
```

---

## 👨‍💻 Author

**Muhammad Ali**

This project is part of my Python learning journey and my preparation for a future career in **Software Engineering / AI Engineering**.

---

## 📚 Project Status

**Status:** ✅ Version 1.0 Complete

**Language:** Python

**Level:** Beginner → Early Intermediate

**Main Topic:** File Handling