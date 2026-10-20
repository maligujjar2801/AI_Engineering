from sqlite3 import *
connection = connect("database.db")
cursor = connection.cursor()
cursor.execute("UPDATE students SET marks = 95 WHERE id = 1")
connection.commit()
connection.close()