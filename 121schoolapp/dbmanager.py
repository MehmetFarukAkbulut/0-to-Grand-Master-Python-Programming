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
        sql="INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender,ClassId) VALUES (%s,%s,%s,%s,%s,%s)" 
        value=(student.studentNumber,student.name,student.surname,student.birthdate,student.gender,student.classid)
        self.cursor.execute(sql,value)
        
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print("Hata: ",err)

    def editStudent(self,student: Student):
        sql="update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s,classid=%s where id=%s" 
        value=(student.studentNumber,student.name,student.surname,student.birthdate,student.gender,student.classid,student.id)
        self.cursor.execute(sql,value)
        
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt güncellendi.")
        except mysql.connector.Error as err:
            print("Hata: ",err)

    def addTeacher(self,teacher: Teacher):
        pass

    def editTeacher(self,teacher: Teacher):
        pass
        
db=DbManager()
student=db.getStudentsById(7)

student[0].name="Mehmet"

# db.addStudent(student[0])   
db.editStudent(student[0])   

# students=db.getStudentsByClassId(1)
# print(students[0].name)   
# print(students[4].surname) 

