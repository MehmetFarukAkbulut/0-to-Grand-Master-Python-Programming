# 1- Workbench IDE ile schooldb isminde bir database oluşturup Student tablosunu ekleyiniz.
    # Id,StudentNumber,Name,Surname,Birthdate,Gender

# 2- Database bağlantısını oluşturunuz. (connection.py)

# 3- Aşağıdaki bilgiler için insert sorguları oluşturup kayıtları ekleyiniz.

    # ("301","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
    # ("302","Ali","Can",datetime(2005, 6, 17),"E"),
    # ("303","Canan","Tan",datetime(2005, 7, 7),"K"),
    # ("304","Ayşe","Taner",datetime(2005, 9, 23),"K"),
    # ("305","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
    # ("306","Ali","Cenk",datetime(2003, 8, 25),"E")


# 4- Aşağıdaki sorguları yazınız.
#   a- Tüm öğrenci kayıtlarını alınız.
#   b- Tüm öğrencilerin sadece öğrenci no, ad ve soyad bilgilerini alınız.
#   c- Sadece kız öğrencilerin ad ve soyadlarını alınız.
#   d- 2003 doğumlu öğrenci bilgilerini alınız. 
#   e- İsmi Ali ve doğum tarihi 2005 olan öğrenci bilgilerini alınız.
#   f- ad veya soyadı içinde 'an' ifadesi geçen kayıtları alınız. 
#   g- Kaç erkek öğrenci vardır ?
#   h- Kız öğrencileri harf sırasına göre getiriniz.

# 5- Aşağıdaki güncelleme sorularını yapınız.
#   a- id' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.
#   b- cinsiyet' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.
import mysql.connector
from datetime import datetime

import mysql.connector
from datetime import datetime


class Student:
    connection=mysql.connector.connect(host="localhost",user="root",password="SQL1234",database="schooldb")
    mycursor=connection.cursor()
    
    def __init__(self,id,studentNumber,name,surname,birthdate,gender):
        if id is None:
            self.id=0
        else:
            self.id=id
        self.studentNumber=studentNumber
        self.name=name
        self.surname=surname
        self.birthdate=birthdate
        self.gender=gender
    
            
    def saveStudent(self):
        sql="INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)" 
        value=(self.studentNumber,self.name,self.surname,self.birthdate,self.gender)
        Student.mycursor.execute(sql,value)
        
        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print("Hata: ",err)
        finally:
            Student.connection.close()
    @staticmethod
    def saveStudents(students):
        sql="INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)" 
        values=students
        Student.mycursor.executemany(sql,values)
        
        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print("Hata: ",err)
        finally:
            Student.connection.close()     
    
    @staticmethod
    def StudentInfo():
        sql="Select * from student limit 5"
        # sql="Select * from student"
        # sql="Select studentnumber,name,surname from student"
        # sql="Select studentnumber,name,surname from student where gender='K'"
        # sql="Select * from student where YEAR(birthdate)=2003"
        # sql="Select * from student where YEAR(birthdate)=2005 and name='Ali'"
        # sql="Select * from student where name like '%an%' or surname like '%an%' "
        # sql="Select Count(*) from student where gender='E' "
        # sql="Select name,surname from student where gender='K' order by name,surname"
        
        
        Student.mycursor.execute(sql)
        try:
            results= Student.mycursor.fetchall()
            # print(results)
            for result in results:
                print(f"{result[0]} {result[1]} {result[2]} {result[3]}")
        except mysql.connector.Error as err:
            print("hata ",err)
        finally:
            Student.connection.close()

    @staticmethod
    def getsStudentById(id):
            sql="select * from student where id=%s"
            value=(id,)
            
            Student.mycursor.execute(sql,value)
            
            try:
                obj= Student.mycursor.fetchone()
                return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
            except mysql.connector.Error as err:
                print("Error",err)
    def updateStudent(self):
        sql="update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"     
        values=(self.studentNumber,self.name,self.surname,self.birthdate,self.gender,self.id)       
        Student.mycursor.execute(sql,values)
        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt güncellendi')
        except mysql.connector.Error as err:
                print("Error",err)

    @staticmethod
    def updateStudents(liste):
        sql="update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"     
        values=[]
        order=[1,2,3,4,5,0]
        for item in liste:
            item=[item[i] for i in order]
            values.append(item) 
        Student.mycursor.executemany(sql,values)
        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt güncellendi')
        except mysql.connector.Error as err:
                print("Error",err)

    @staticmethod
    def getsStudentsGender(gender):
            sql="select * from student where gender=%s"
            value=(gender,)
            
            Student.mycursor.execute(sql,value)
            
            try:
                return Student.mycursor.fetchall()
            
            except mysql.connector.Error as err:
                print("Error",err)


# student=Student.getsStudentById(7)

# student.name='Mehmet'
# student.surname='Çetin'
# student.updateStudent()

students=Student.getsStudentsGender('K')
print(students)

liste=[]

for std in students:
    std=list(std)
    std[2]='Mrs '+ std[2]
    liste.append(std)
    
Student.updateStudents(liste)