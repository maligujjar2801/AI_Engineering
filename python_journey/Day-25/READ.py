from sqlite3 import *
connection = connect("database.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM STUDENTS")
records = cursor.fetchall()
for record in records:
    print(record)
connection.commit()
connection.close()