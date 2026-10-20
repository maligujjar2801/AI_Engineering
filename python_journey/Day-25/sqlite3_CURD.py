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
cursor.execute("""
INSERT INTO students(name,age,marks) VALUES("Example Student",0,0)
 """)
cursor.execute("UPDATE students SET marks = 95 WHERE id = 1")
cursor.execute("SELECT * FROM STUDENTS")
records = cursor.fetchall()
for record in records:
    print(record)
connection.commit()
connection.close()
