import mysql.connector
from datetime import datetime
from connection import connection

class Student:
    connection = connection
    mycursor = connection.cursor()
    def __init__(self, student_number, name, surname, birthdate, gender):
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


#Habibe = Student('225', 'Habibe', 'Yağcı', datetime(2002, 8, 10), 'K')
#Habibe.saveStudent()

students = [
    ('226', 'Ali', 'Veli', datetime(2001, 5, 15), 'E'),
    ('227', 'Ayşe', 'Fatma', datetime(2003, 7, 20), 'K'),
    ('228', 'Mehmet', 'Can', datetime(2000, 12, 5), 'E'),

]


Student.saveStudents(students)
