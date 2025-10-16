class Student:
    def __init__(self,id, student_number, name, surname, birthdate, gender,classid):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.student_number = student_number
        if len(name) > 45:
            raise ValueError("45 karakterden uzun isim olamaz")
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.classid = classid