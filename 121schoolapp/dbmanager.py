import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Class import Class
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
    
    def deleteStudent(self,studentid):
        sql="delete from student where id=%s"
        value=(studentid,)
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt silindi.")
        except mysql.connector.Error as err:
            print("Hata: ",err)
    
    def getClasses(self):
        sql="select * from class"
        self.cursor.execute(sql)
        try:
            obj=self.cursor.fetchall()
            return Class.CreateClass(obj)           
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
    def addorEditStudent(self,student: Student):
        if student.id == 0:
            self.addStudent(student)
        else:
            self.editStudent(student)  
    
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
    
    def __del__(self):
        self.connection.close()
        print("db kapandı")
        
    
    
db=DbManager()
student=db.getStudentsById(19)
# student[0].id=0
# student[0].name="Faruk"
# student[0].surname="Hoş"
# student[0].studentNumber="715"
student[0].name="Mustafa"
# student[0].surname="Yılmaz"

# db.addStudent(student[0])   
# db.editStudent(student[0])   
db.addorEditStudent(student[0])   

# students=db.getStudentsByClassId(1)
# print(students[0].name)   
# print(students[4].surname) 

