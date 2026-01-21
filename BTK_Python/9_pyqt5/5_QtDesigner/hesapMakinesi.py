from PyQt5 import QtWidgets
import sys
from MainWindow import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.btn_toplama.clicked.connect(self.hesapla)
        self.ui.btn_cikarma.clicked.connect(self.hesapla)
        self.ui.btn_carpma.clicked.connect(self.hesapla)
        self.ui.btn_bolme.clicked.connect(self.hesapla)

    def hesapla(self):
        sender = self.sender().text()
        result = 0

        if sender == "Toplama":
            result = float(self.ui.txt_sayi1.text()) + float(self.ui.txt_sayi2.text())
        elif sender == "Cikarma":
            result = float(self.ui.txt_sayi1.text()) - float(self.ui.txt_sayi2.text())
        elif sender == "Carpma":
            result = float(self.ui.txt_sayi1.text()) * float(self.ui.txt_sayi2.text())
        elif sender == "Bolme":
            result = float(self.ui.txt_sayi1.text()) / float(self.ui.txt_sayi2.text())
        self.ui.label_3.setText("Sonuc : " + str(result))
    

def app():
    uygulama = QtWidgets.QApplication(sys.argv)
    pencere = myApp()
    pencere.show()
    sys.exit(uygulama.exec_())

if __name__ == "__main__":
    app()