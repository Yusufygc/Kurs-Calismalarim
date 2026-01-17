import sys
from PyQt5 import QtWidgets # PyQt5 modülü
from PyQt5.QtWidgets import QApplication, QMainWindow ,QToolTip #pencere olusturma için gerekli modüller 
from PyQt5.QtGui import QIcon #ikon ekleme

def Window():
    app = QApplication(sys.argv) #app olusturuldu
    win = QMainWindow() #pencere olusturuldu
    win.setWindowTitle("PyQt5 Window") #pencere basligi
    win.setGeometry(200, 200,450,450) #pencere boyutlari
    win.setWindowIcon(QIcon("9_pyqt5\\software.png")) #pencere ikonu
    win.setToolTip("Bu bir PyQt5 penceresidir") #pencere uzerine gelince aciklama
    win.move(60, 15) #pencere konumu
    win.show() #pencere gosterildi
    sys.exit(app.exec_()) #çıkış işlemi çarpı butonu ile yapılır
Window()