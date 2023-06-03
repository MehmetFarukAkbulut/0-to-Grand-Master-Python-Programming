# 1- Workbench IDE ile schooldb isminde bir database oluşturup Student tablosunu ekleyiniz.
    # Id,StudentNumber,Name,Surname,Birthdate,Gender

# 2- Database bağlantısını oluşturunuz. (connection.py)

import mysql.connector

connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="SQL1234",
    database="schooldb"
)

mycursor=connection.cursor()

