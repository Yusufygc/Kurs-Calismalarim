import sys
from PyQt5 import QtWidgets # PyQt5 modülü
from PyQt5.QtWidgets import QApplication, QMainWindow ,QToolTip #pencere olusturma için gerekli modüller 
from PyQt5.QtGui import QIcon #ikon ekleme







def Window():
    app = QApplication(sys.argv) #app olusturuldu
    win = QMainWindow() #pencere olusturuldu
    win.setWindowTitle("PyQt5 Window") #pencere basligi
    win.setGeometry(200, 200,450,450) #pencere boyutlari
    win.setWindowIcon(QIcon("9_pyqt5\\img\\software.png")) #pencere ikonu
    win.setToolTip("Bu bir PyQt5 penceresidir") #pencere uzerine gelince aciklama
    win.move(60, 15) #pencere konumu

    lbl_name = QtWidgets.QLabel(win)  # Etiket oluşturuldu ve pencereye eklendi
    lbl_name.setText("Adınız :")  # Etiket metni
    lbl_name.move(50, 30)  # Etiket konumu

    lbl_surname = QtWidgets.QLabel(win)  # Etiket oluşturuldu ve pencereye eklendi
    lbl_surname.setText("Soyadınız :")  # Etiket metni  
    lbl_surname.move(50, 70)  # Etiket konumu

    txt_name = QtWidgets.QLineEdit(win)  # Metin kutusu oluşturuldu ve pencereye eklendi
    txt_name.move(150, 30)  # Metin kutusu konumu
    txt_name.resize(200, 20)  # Metin kutusu boyutu
    txt_name.setPlaceholderText("Adınızı giriniz")  # Yer tutucu metin

    txt_surname = QtWidgets.QLineEdit(win)  # Metin kutusu oluşturuldu ve pencereye eklendi
    txt_surname.move(150, 70)  # Metin kutusu konumu
    txt_surname.resize(200, 20)  # Metin kutusu boyutu
    txt_surname.setPlaceholderText("Soyadınızı giriniz")  # Yer tutucu metin

    def clicked(self):
        print("Butona tıklandı! " + txt_name.text() + " " + txt_surname.text())

    btn_save = QtWidgets.QPushButton(win)  # Buton oluşturuldu ve pencereye eklendi
    btn_save.setText("Kaydet")  # Buton metni   
    btn_save.move(150, 110)  # Buton konumu
    btn_save.resize(100, 30)  # Buton boyutu
    btn_save.clicked.connect(clicked)  # Buton tıklama olayı


    win.show() #pencere gosterildi
    sys.exit(app.exec_()) #çıkış işlemi çarpı butonu ile yapılır
Window()