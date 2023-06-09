import sqlite3

connection=sqlite3.connect("chinook.db")
cursor=connection.cursor()

cursor.execute("select * from customers")
result=cursor.fetchall()
for r in result:
    print(r)
connection.close()