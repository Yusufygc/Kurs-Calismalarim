import sys
from PyQt5 import QtWidgets # PyQt5 modülü
from PyQt5.QtWidgets import QApplication, QMainWindow ,QToolTip #pencere olusturma için gerekli modüller 
from PyQt5.QtGui import QIcon #ikon ekleme


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setWindowTitle("PyQt5 Window") #pencere basligi
        self.setGeometry(200, 200 ,450,450) #pencere boyutlari
        self.setWindowIcon(QIcon("9_pyqt5\\img\\software.png")) 
        self.initUI()

    def initUI(self):
        self.setToolTip("Bu bir PyQt5 penceresidir") #pencere uzerine gelince aciklama
        self.move(60, 15) #pencere konumu

        self.lbl_name = QtWidgets.QLabel(self)  # Etiket oluşturuldu ve pencereye eklendi
        self.lbl_name.setText("Adınız :")  # Etiket metni
        self.lbl_name.move(50, 30)  # Etiket konumu

        self.lbl_surname = QtWidgets.QLabel(self)  # Etiket oluşturuldu ve pencereye eklendi
        self.lbl_surname.setText("Soyadınız :")  # Etiket metni  
        self.lbl_surname.move(50, 70)  # Etiket konumu

        self.txt_name = QtWidgets.QLineEdit(self)  # Metin kutusu oluşturuldu ve pencereye eklendi
        self.txt_name.move(150, 30)  # Metin kutusu konumu
        self.txt_name.resize(200, 20)  # Metin kutusu boyutu
        self.txt_name.setPlaceholderText("Adınızı giriniz")  # Yer tutucu metin

        self.txt_surname = QtWidgets.QLineEdit(self)  # Metin kutusu oluşturuldu ve pencereye eklendi
        self.txt_surname.move(150, 70)  # Metin kutusu konumu
        self.txt_surname.resize(200, 20)  # Metin kutusu boyutu
        self.txt_surname.setPlaceholderText("Soyadınızı giriniz")  # Yer tutucu metin

        self.lbl_result = QtWidgets.QLabel(self)  # Sonuç etiket oluşturuldu ve pencereye eklendi
        self.lbl_result.move(150, 150)  # Sonuç etiket konumu
        self.lbl_result.resize(350, 75)  # Sonuç etiket boyutu


        self.btn_save = QtWidgets.QPushButton(self)  # Buton oluşturuldu ve pencereye eklendi
        self.btn_save.setText("Kaydet")  # Buton metni  
        self.btn_save.move(150, 110)  # Buton konumu
        self.btn_save.resize(100, 30)  # Buton boyutu
        self.btn_save.clicked.connect(self.clicked)  # Buton tıklama olayı

    def clicked(self):
        self.lbl_result.setText("Ad :" + self.txt_name.text() + "\n" +"Soyad :" + self.txt_surname.text())

def Window():
    app = QApplication(sys.argv) #app olusturuldu
    win = MyWindow() #pencere olusturuldu
    win.show() #pencere gosterildi
    sys.exit(app.exec_()) #çıkış işlemi çarpı butonu ile yapılır

Window()