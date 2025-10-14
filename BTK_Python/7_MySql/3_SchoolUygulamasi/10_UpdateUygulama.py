import mysql.connector
from datetime import datetime
from connection import connection

class Student:
    connection = connection
    mycursor = connection.cursor()
    def __init__(self,id, student_number, name, surname, birthdate, gender):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.student_number = student_number
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
    
    def saveStudent(self):
        sql = "INSERT INTO student (StudentNumber, Name, Surname, Birthdate, Gender) VALUES (%s, %s, %s, %s, %s)"
        values = (self.student_number, self.name, self.surname, self.birthdate, self.gender) # (tuple) self ile çağırdık çünkü nesne içindeki verilere erişiyoruz
        Student.mycursor.execute(sql, values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} kayıt eklendi.')
        except mysql.connector.Error as e:
            print(f'Hata: {e}')
        finally:
            Student.connection.close()
            print("Bağlantı kapandı.")

    @staticmethod # static method olduğu için self almaz çünkü nesneye bağlı değil 
    def saveStudents(students):
        sql = "INSERT INTO student (StudentNumber, Name, Surname, Birthdate, Gender) VALUES (%s, %s, %s, %s, %s)"
        values =students # (tuple) self ile çağırdık çünkü nesne içindeki verilere erişiyoruz
        Student.mycursor.executemany(sql, values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} kayıt eklendi.')
        except mysql.connector.Error as e:
            print(f'Hata: {e}')
        finally:
            Student.connection.close()
            print("Bağlantı kapandı.")

    @staticmethod
    def getStudentById(id):
        sql = "SELECT * FROM student WHERE id=%s"
        value = (id,)
        Student.mycursor.execute(sql, value)

        try:
            #Student.connection.commit()
            print(f'{Student.mycursor.rowcount} kayıt güncellendi.')
            result =Student.mycursor.fetchone() # tek kayıt döner
            return Student(result[0],result[1],result[2],result[3],result[4],result[5])
        except mysql.connector.Error as e:
            print(f'Hata: {e}')


    def updateStudent(self):
        sql = "UPDATE student SET Name=%s, Surname=%s, Birthdate=%s, Gender=%s WHERE id=%s"
        values = (self.name, self.surname, self.birthdate, self.gender, self.id)
        Student.mycursor.execute(sql, values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} kayıt güncellendi.')
        except mysql.connector.Error as e:
            print(f'Hata: {e}')


    @staticmethod   
    def updateStudent(liste):
        sql = "UPDATE student SET studentnumber=%s, Name=%s, Surname=%s, Birthdate=%s, Gender=%s WHERE id=%s"
        values =[]
        order =[1,2,3,4,5,0] # id en sona gelecek şekilde
        for item in liste:
            item = [item[i] for i in order]
            values.append(item)

        Student.mycursor.executemany(sql, values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} kayıt güncellendi.')
        except mysql.connector.Error as e:
            print(f'Hata: {e}')


    @staticmethod
    def getStudentsGender(gender):
        sql = "SELECT * FROM student WHERE Gender=%s"
        value = (gender,)
        Student.mycursor.execute(sql, value)

        try:
            return Student.mycursor.fetchall() # tüm kayıtları döner
        except mysql.connector.Error as e:
            print(f'Hata: {e}')

# student = Student.getStudentById(1)
# student.name =  "Alexander"
# student.surname = "Hamilton"
# student.updateStudent()

students = Student.getStudentsGender("E")
for student in students:
    print(student)

liste = []
for std in students:
    std = list(std)
    std[2] = "mr"+ std[2]

    liste.append(std)

Student.updateStudent(liste)