import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="SQL1234",
    database="mydatabase"
)
mycursor=mydb.cursor()
