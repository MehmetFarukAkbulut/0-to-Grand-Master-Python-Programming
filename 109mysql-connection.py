import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="SQL1234"
)
mycursor=mydb.cursor()

mycursor.execute("SHOW DATABASES")
# mycursor.execute("CREATE DATABASE mydatabase")

for x in mycursor:
    print(x)