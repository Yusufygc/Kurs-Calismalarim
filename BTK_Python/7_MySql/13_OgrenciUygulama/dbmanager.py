import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class
class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()
    
    def close(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Bağlantı kapandı.")

    def getStudentById(self, id):
        sql ="SELECT* FROM student WHERE id=%s"
        value=(id,)
        self.cursor.execute(sql,value)
        try:
            result = self.cursor.fetchone()
            return Student.CreateStudent(result)
        except Exception as e:
            print("Error:", e)
          
    def getStudentsByClassId(self,classid):    
        sql ="SELECT* FROM student WHERE classid=%s"
        value=(classid,)
        self.cursor.execute(sql,value)
        try:
            result = self.cursor.fetchall()
            return Student.CreateStudent(result)
        except Exception as e:
            print("Error:", e)

    def addOrEditStudent(self, student:Student):
        if student.id == 0:
            self.addStudent(student)
        else:
            self.editStudent(student)

    def addStudent(self, student:Student):
        sql = "INSERT INTO student (StudentNumber, Name, Surname, Birthdate, Gender, ClassID) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (student.student_number, student.name, student.surname, student.birthdate, student.gender, student.classid)
        self.cursor.execute(sql, values)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} kayit eklendi.')
        except mysql.connector.Error as e:
            print(f'Hata: {e}')
        
    def editStudent(self, student:Student):
        sql = "UPDATE student SET StudentNumber=%s, Name=%s, Surname=%s, Birthdate=%s, Gender=%s, ClassID=%s WHERE id=%s"
        values = (student.student_number, student.name, student.surname, student.birthdate, student.gender, student.classid, student.id)
        self.cursor.execute(sql, values)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} kayit güncellendi.')
        except mysql.connector.Error as e:
            print(f'Hata: {e}')

    def deleteStudent(self, studentid):
        sql = "DELETE FROM student WHERE id=%s"
        value = (studentid,)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} kayit silindi.')
        except mysql.connector.Error as e:
            print(f'Hata: {e}')

    def getClasses(self):
        sql ="SELECT* FROM class"
        self.cursor.execute(sql)
        try:
            result = self.cursor.fetchall()
            return Class.CreateClass(result)
        except Exception as e:
            print("Error:", e)

    def addTeacher(self, teacher:Teacher):
        pass

    def editTeacher(self, teacher:Teacher):
        pass




"""
db = DbManager()
student = db.getStudentById(1)
# print(student[0].name)
# print(student[0].surname)

# students = db.getStudentsByClassId(1)
# print(students[4].name)

# student[0].name ="Yahya"
# student[0].surname ="tahtacı"
# student[0].student_number ="540"

# db.addStudent(student[0])
student[0].name ="Yusufi"
db.editStudent(student[0])



db.close()
"""