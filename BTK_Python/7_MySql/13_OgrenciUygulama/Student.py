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

    @staticmethod
    def CreateStudent(object):
        list=[]
        if isinstance(object,tuple):
            student = Student(object[0], object[1], object[2], object[3], object[4], object[5], object[6])
            list.append(student)
        else:
            for row in object:
                student = Student(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                list.append(student)
        return list