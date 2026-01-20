import sys
from PyQt5 import QtWidgets # PyQt5 modülü
from PyQt5.QtWidgets import QApplication, QMainWindow ,QToolTip #pencere olusturma için gerekli modüller


class MainForm(QMainWindow): #QMainWindow sınıfından MainForm sınıfı türetildi
    def __init__(self): #sınıfın yapıcı metodu
        super(MainForm, self).__init__() #üst sınıfın yapıcı metodunu çağırma
        self.setWindowTitle("Hesap Makinesi") #pencere başlığı
        self.setGeometry(100,100,300,400) #pencere boyutları
        self.initUI() #arayüz oluşturma metodu çağırma

    def initUI(self): #arayüz oluşturma metodu
        self.label1 = QtWidgets.QLabel(self) #etiket oluşturma
        self.label1.setText("Sayı 1:") #etiket metni
        self.label1.move(20,20) #etiket konumu

        self.textbox1 = QtWidgets.QLineEdit(self) #metin kutusu oluşturma
        self.textbox1.move(100,20) #metin kutusu konumu
        self.textbox1.resize(150,30) #metin kutusu boyutu

        self.label2 = QtWidgets.QLabel(self) #etiket oluşturma
        self.label2.setText("Sayı 2:") #etiket metni
        self.label2.move(20,70) #etiket konumu

        self.textbox2 = QtWidgets.QLineEdit(self) #metin kutusu oluştur
        self.textbox2.move(100,70) #metin kutusu konumu
        self.textbox2.resize(150,30) #metin kutusu boyutu

        self.button_add = QtWidgets.QPushButton(self) #toplama butonu oluşturma
        self.button_add.setText("Topla") #buton metni
        self.button_add.move(40,120) #buton konumu
        self.button_add.clicked.connect(self.add_numbers) #buton tıklama olayı

        self.button_extraction = QtWidgets.QPushButton(self) #çıkarma butonu oluşturma
        self.button_extraction.setText("Çıkar") #buton metni
        self.button_extraction.move(150,120) #buton konumu
        self.button_extraction.clicked.connect(self.extraction_numbers) #buton tıklama olayı

        self.button_multiply = QtWidgets.QPushButton(self) #çarpma butonu oluşturma
        self.button_multiply.setText("Çarp") #buton metni
        self.button_multiply.move(40,170) #buton konumu
        self.button_multiply.clicked.connect(self.multiply_numbers) #buton tıklama olayı

        self.button_divide = QtWidgets.QPushButton(self) #bölme butonu oluşturma
        self.button_divide.setText("Böl") #buton metni
        self.button_divide.move(150,170) #buton konumu
        self.button_divide.clicked.connect(self.divide_numbers) #buton tıklama olayı

    def divide_numbers(self): #sayıları bölme metodu
        num1 = float(self.textbox1.text()) #ilk sayıyı alma
        num2 = float(self.textbox2.text()) #ikinci sayıyı alma
        if num2 != 0: #sıfıra bölme kontrolü
            result = num1 / num2 #sayıları bölme
            QtWidgets.QMessageBox.information(self, "Sonuç", f"Bölüm: {result}") #sonucu gösterme
        else:
            QtWidgets.QMessageBox.warning(self, "Hata", "Sıfıra bölme hatası!") #hata mesajı

    def multiply_numbers(self): #sayıları çarpma metodu
        num1 = float(self.textbox1.text()) #ilk sayıyı alma
        num2 = float(self.textbox2.text()) #ikinci sayıyı alma
        result = num1 * num2 #sayıları çarpma
        QtWidgets.QMessageBox.information(self, "Sonuç", f"Çarpım: {result}") #sonucu gösterme  

    def extraction_numbers(self): #sayıları çıkarma metodu
        num1 = float(self.textbox1.text()) #ilk sayıyı alma
        num2 = float(self.textbox2.text()) #ikinci sayıyı alma
        result = num1 - num2 #sayıları çıkarma
        QtWidgets.QMessageBox.information(self, "Sonuç", f"Fark: {result}") #sonucu gösterme

    def add_numbers(self): #sayıları toplama metodu
        num1 = float(self.textbox1.text()) #ilk sayıyı alma
        num2 = float(self.textbox2.text()) #ikinci sayıyı alma
        result = num1 + num2 #sayıları toplama
        QtWidgets.QMessageBox.information(self, "Sonuç", f"Toplam: {result}") #sonucu gösterme

"""
hesapla fonksiyonu ile bütün işlemleri tek bir fonksiyonda yapabiliriz. 
Bu işlemi sender() metodu ile hangi butona tıklandığını kontrol ederek yapabiliriz.
sender() metodu, tıklanan butonun referansını döner.
Bu referansı kullanarak butonun metnini alabilir ve işlemi buna göre gerçekleştirebiliriz.
Aşağıda bu yöntemi kullanan bir örnek verilmiştir:  
    def calculate(self):
        num1 = float(self.textbox1.text()) #ilk sayıyı alma
        num2 = float(self.textbox2.text()) #ikinci sayıyı alma
        button = self.sender() #tıklanan butonun referansını alma
        operation = button.text() #butonun metnini alma

        if operation == "Topla":
            result = num1 + num2
            QtWidgets.QMessageBox.information(self, "Sonuç", f"Toplam: {result}")
        elif operation == "Çıkar":
            result = num1 - num2
            QtWidgets.QMessageBox.information(self, "Sonuç", f"Fark: {result}")
        elif operation == "Çarp":
            result = num1 * num2
            QtWidgets.QMessageBox.information(self, "Sonuç", f"Çarpım: {result}")
        elif operation == "Böl":
            if num2 != 0:
                result = num1 / num2
                QtWidgets.QMessageBox.information(self, "Sonuç", f"Bölüm: {result}")
            else:
                QtWidgets.QMessageBox.warning(self, "Hata", "Sıfıra bölme hatası!")

"""
    

def window(): #pencere oluşturma fonksiyonu
    app = QApplication(sys.argv) #uygulama oluşturma
    win = MainForm() #pencere oluşturma
    win.show() #pencere gösterme
    sys.exit(app.exec_()) #çıkış işlemi çarpı butonu ile yapılır

window() #pencere oluşturma fonksiyonu çağırma