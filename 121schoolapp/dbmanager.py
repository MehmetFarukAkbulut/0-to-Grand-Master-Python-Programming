import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher

class DbManager:
    def __init__(self):
        self.connection=connection
        self.cursor=self.connection.cursor()
    
    def getStudentsById(self,id):
        sql="select * from student where id=%s"
        value=(id,)
        self.cursor.execute(sql,value)
        try:
            obj=self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("Error: ",err)
    def getStudentsByClassId(self,classid):
        sql="select * from student where classid=%s"
        value=(classid,)
        self.cursor.execute(sql,value)
        try:
            obj=self.cursor.fetchall()
            return Student.CreateStudent(obj)           
        except mysql.connector.Error as err:
            print("Error: ",err)
    def addStudent(self,student: Student):
        pass

    def editStudent(self,student: Student):
        pass

    def addTeacher(self,teacher: Teacher):
        pass

    def editTeacher(self,teacher: Teacher):
        pass
        
db=DbManager()
# student=db.getStudentsById(7)
# print(student[0].name)   
# print(student[0].surname)   

students=db.getStudentsByClassId(1)
print(students[0].name)   
print(students[4].surname) 