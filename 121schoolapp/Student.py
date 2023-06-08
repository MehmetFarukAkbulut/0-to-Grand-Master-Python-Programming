class Student:

    def __init__(self,id,studentNumber,name,surname,birthdate,gender,classid):
        if id is None:
            self.id=0
        else:
            self.id=id
        self.studentNumber=studentNumber
        self.name=name
        self.surname=surname
        self.birthdate=birthdate
        self.gender=gender
        self.classid=classid
    