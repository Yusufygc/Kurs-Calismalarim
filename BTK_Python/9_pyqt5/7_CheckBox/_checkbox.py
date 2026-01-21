import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from _checkboxForm import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnSecilenleriAl.clicked.connect(self.secilenleriAl)

    def secilenleriAl(self):
        secilenler = []
        if self.ui.cbSinema.isChecked():
            secilenler.append("Sinema")
        if self.ui.cbKitapOkumak.isChecked():
            secilenler.append("Kitap Okumak")
        if self.ui.cbSpor.isChecked():
            secilenler.append("Spor")

        self.ui.lblResult.setText("Seçilenler: " + ", \n".join(secilenler))

def app():
    uygulama = QApplication(sys.argv)
    pencere = myApp()
    pencere.show()
    sys.exit(uygulama.exec_())

if __name__ == "__main__":
    app()