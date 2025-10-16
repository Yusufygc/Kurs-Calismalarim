import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher

class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def addStudent(self, student:Student):
        pass

    def editStudent(self, student:Student):
        pass

    def addTeacher(self, teacher:Teacher):
        pass

    def editTeacher(self, teacher:Teacher):
        pass