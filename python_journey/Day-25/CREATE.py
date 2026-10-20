from sqlite3 import *
connection = connect("database.db")
cursor = connection.cursor()
cursor.execute(
    """Create TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        marks INTEGER
        )
""")
connection.commit()
connection.close()