# Day 25 — SQLite CRUD: Python Notes

## Overview

These files demonstrate a small SQLite database workflow in Python using the standard-library `sqlite3` module. The database stores student records in a `students` table with an automatically assigned `id`, a `name`, an `age`, and `marks`.

## What each file does

- `CREATE.py` opens `database.db`, creates the `students` table if it does not exist, commits the schema change, and closes the connection.
- `INSERT.py` adds one student record and commits it.
- `READ.py` selects every row from `students`, fetches the results, and prints them.
- `UPDATE.py` changes the marks for the row with `id = 1` and commits the change.
- `DELETE.py` deletes the row with `id = 3` and commits the change. The current database contains only an `id = 1` row, so this command currently deletes no row.
- `sqlite3_CURD.py` combines table creation, insertion, update, and reading in one script. The filename uses `CURD`; the usual acronym is CRUD (Create, Read, Update, Delete).
- `database.db` is the SQLite database used by the scripts. It currently contains the `students` table and one record; this Markdown intentionally avoids copying that record's personal details.

## CRUD flow

1. **Create:** Connect to the database and run `CREATE TABLE IF NOT EXISTS`.
2. **Insert:** Add values with an `INSERT` statement, then commit.
3. **Read:** Run a `SELECT`, fetch the rows, and display them.
4. **Update:** Choose a row by its ID, change a field, then commit.
5. **Delete:** Choose a row by its ID, delete it, then commit.

Each separate script connects to the same relative filename, `database.db`. Run the scripts from the folder containing the database so they all open the intended file.

## Key ideas

- `sqlite3.connect("database.db")` opens the database file, creating it if needed.
- A cursor executes SQL statements and retrieves query results.
- `connection.commit()` saves changes made by `CREATE`, `INSERT`, `UPDATE`, and `DELETE`.
- `cursor.fetchall()` returns all rows from the latest query as a list of tuples.
- `id INTEGER PRIMARY KEY AUTOINCREMENT` assigns each new row an integer identifier.
- Closing the connection releases the database resource.

## Improvements to practice

- Use placeholders such as `?` and pass values separately to `cursor.execute()` instead of embedding values in SQL strings.
- Replace `from sqlite3 import *` with `import sqlite3` or explicit imports to make dependencies clear.
- Use `try/finally` or a connection context manager so a connection is closed even if a statement fails.
- Check the `id` values in the database before updating or deleting; the current delete targets an ID that is not present.
- Avoid inserting the same sample row each time `sqlite3_CURD.py` is run, or clearly reset the database for each demonstration.
- A read-only `SELECT` does not need `connection.commit()`.

## Suggested run order

Run `CREATE.py`, then `INSERT.py`, `READ.py`, and `UPDATE.py`. Inspect the selected rows with `READ.py` before running `DELETE.py`, because deleting a row is irreversible unless a backup exists. `sqlite3_CURD.py` is a combined example and can add another sample row each time it runs.



