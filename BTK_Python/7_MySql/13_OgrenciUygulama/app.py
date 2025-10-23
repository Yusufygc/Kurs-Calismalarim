from dbmanager import DbManager
from Student import Student
import datetime
class App:
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        while True:
            print("1. Öğrenci Listesi")
            print("2. Öğrenci Ekle")
            print("3. Öğrenci Güncelle")
            print("4. Öğrenci Sil")
            print("5. Çıkış")
            choice = input("Seçiminiz: ")

            if choice == '1':
                self.displayStudents()
            elif choice == '2':
                self.addStudent()
            elif choice == '3':
                self.editStudent()
            elif choice == '4':
                self.deleteStudent()
            elif choice == '5':
                self.db.close()    
                break
            else:
                print("Geçersiz seçim, tekrar deneyin.")     
    
    def deleteStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Silinecek öğrenci ID'si: "))
        self.db.deleteStudent(studentid)

    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Güncellenecek öğrenci ID'si: "))

        student = self.db.getStudentById(studentid)
        if not student:
            print("Öğrenci bulunamadı.")
            return

        student[0].name = input("Yeni İsim: ") or student[0].name  # isim boşsa eski ismi koru
        student[0].surname = input("Yeni Soyisim: ") or student[0].surname
        student[0].gender = input("Yeni Cinsiyet (E/K): ") or student[0].gender
        student[0].classid = classid or student[0].classid

        year = input("Yeni Doğum Yılı (boş bırakılırsa değişmez): ") or student[0].birthdate.year
        month = input("Yeni Doğum Ayı (boş bırakılırsa değişmez): ") or student[0].birthdate.month
        day = input("Yeni Doğum Günü (boş bırakılırsa değişmez): ") or student[0].birthdate.day
        student[0].birthdate = datetime.date(int(year), int(month), int(day))
        
        self.db.editStudent(student[0])

    def addStudent(self):
        self.displayClasses()
        classid = int(input("Hangi sınıf: "))
        number = input("Öğrenci Numarası: ")
        name = input("İsim: ")
        surname = input("Soyisim: ")
        year = input("Doğum Yılı: ")
        month = input("Doğum Ayı: ")
        day = input("Doğum Günü: ")
        birthdate = datetime.date(int(year), int(month), int(day))
        gender = input("Cinsiyet (E/K): ")

        student = Student(None, number, name, surname, birthdate, gender, classid)
        self.db.addStudent(student)

    def displayClasses(self):
        classes = self.db.getClasses()
        for c in classes:
            print(f"Sınıf: {c.name} (ID: {c.id})")

    def displayStudents(self):
        self.displayClasses()
        classid = int(input("Hangi sınıf: "))
        students = self.db.getStudentsByClassId(classid)
        print("Öğrenciler:")
        for s in students:
            print(f"{s.id} - {s.name} {s.surname}")
        return classid

app = App()
app.initApp()