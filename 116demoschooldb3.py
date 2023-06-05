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
'''
import mysql.connector
from datetime import datetime


class Student:
    connection=mysql.connector.connect(host="localhost",user="root",password="SQL1234",database="schooldb")
    mycursor=connection.cursor()
    
    def __init__(self,studentNumber,name,surname,birthdate,gender):
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
    
# faruk=Student("402","Faruk","Akbulut",datetime(2000,10,23),"E")
# faruk.saveStudent()




students=[    
    ("501","Cem","Yılmaz",datetime(2005, 5, 17),"E"),
    ("502","Fatih","Akbulut",datetime(2005, 6, 17),"E"),
    ("503","Rümeysa","Bal",datetime(2005, 7, 7),"K"),
    ("504","Ayşe","Şener",datetime(2005, 9, 23),"K"),
    ("505","Yılmaz","Vural",datetime(2004, 7, 27),"E"),
    ("506","Arda","Turan",datetime(2003, 8, 25),"E")
]

Student.saveStudents(students)'''



# 4- Aşağıdaki sorguları yazınız.
#   a- Tüm öğrenci kayıtlarını alınız.
#   b- Tüm öğrencilerin sadece öğrenci no, ad ve soyad bilgilerini alınız.
#   c- Sadece kız öğrencilerin ad ve soyadlarını alınız.
#   d- 2003 doğumlu öğrenci bilgilerini alınız. 
#   e- İsmi Ali ve doğum tarihi 2005 olan öğrenci bilgilerini alınız.
#   f- ad veya soyadı içinde 'an' ifadesi geçen kayıtları alınız. 
#   g- Kaç erkek öğrenci vardır ?
#   h- Kız öğrencileri harf sırasına göre getiriniz.

import mysql.connector
from datetime import datetime

import mysql.connector
from datetime import datetime


class Student:
    connection=mysql.connector.connect(host="localhost",user="root",password="SQL1234",database="schooldb")
    mycursor=connection.cursor()
    
    def __init__(self,studentNumber,name,surname,birthdate,gender):
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
        # sql="Select * from student limit 5"
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


Student.StudentInfo()