from sqlite3 import *
connection = connect("database.db")
cursor = connection.cursor()
cursor.execute("""
DELETE FROM students WHERE id = 3
""")
connection.commit()
connection.close()