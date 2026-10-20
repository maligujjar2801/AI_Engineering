from sqlite3 import *
connection = connect("database.db")
cursor = connection.cursor()
cursor.execute("""
INSERT INTO students(name,age,marks) VALUES("Example Student",0,0)
 """)
connection.commit()
connection.close()
