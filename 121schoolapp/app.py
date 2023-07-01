from dbmanager import DbManager
import datetime
from Student import Student
class App:
    def __init__(self):
        self.db=DbManager()
    
    def initApp(self):
        msg="*****\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-Sınıflara Göre Dersler\n7-Çıkış(E/Ç)"
        while True:
            print(msg)
            islem=input("Seçim: ")
            if islem=="1":
                self.displayStudents()
            elif islem=="2":
                self.addStudent()
            elif islem=="3":
                self.editStudent()
            elif islem=="4":
                self.deleteStudent()
                
            elif islem=="5":
                pass
            elif islem=="6":
                pass
            elif islem=="E" or islem=="Ç":
                break
            else:
                print("Yanlış seçim")
    
    def deleteStudent(self):
        
        classid=self.displayStudents()
        studentid=int(input("Öğrenci id: "))

        self.db.deleteStudent(studentid)
        
    def editStudent(self):
        classid=self.displayStudents()
        studentid=int(input("Öğrenci id: "))
        
        student=self.db.getStudentsById(studentid)
        
        student[0].name=input("Adı: ")or student[0].name
        student[0].surname=input("Soyadı: ")or student[0].surname
        student[0].gender=input("Cinsiyet(E/K): ")or student[0].gender
        student[0].classid=input("Sınıfı:")or student[0].classid
        
        year=input("Doğum yılı:") or student[0].birthdate.year
        month=input("Doğum ayı:") or student[0].birthdate.month
        day=input("Doğum günü:") or student[0].birthdate.day
        
        student[0].birthdate= datetime.date(year,month,day)
        self.db.editStudent(student[0])
        
    def addStudent(self):
        self.displayClasses()
        classid=int(input("Hangi sınıf: "))
        number=input("Öğrenci numarası: ")
        name=input("Öğrenci adı: ")
        surname=input("Öğrenci soyadı: ")
        year=int(input("Doğum yılı: "))
        month=int(input("Doğum ayı: "))
        day=int(input("Doğum günü: "))
        birthdate=datetime.date(year,month,day)
        gender=input("Cinsiyet(E/K): ")
        
        student=Student(None,number,name,surname,birthdate,gender,classid)
        self.db.addStudent(student)
    def displayClasses(self):
        classes=self.db.getClasses()
        for c in classes:
            print(f"{c.id}: {c.name}")
        
    def displayStudents(self):
        self.displayClasses()
        classid=int(input("Hangi sınıf: "))
        
        students=self.db.getStudentsByClassId(classid)
        print("Öğrenci Listesi ")
        for std in students:
            print(f'{std.id}-{std.name} {std.surname}')
        return classid
        
app=App()
app.initApp()
