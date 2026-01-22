from PyQt5 import QtWidgets
import sys
from _comboboxForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # combo = self.ui.cbSehirler
        # combo.addItem("Adana")
        # combo.addItem("İstanbul")
        # combo.addItem("Ankara")
        # combo.addItem("İzmir")
        # combo.addItems(["Bursa", "Antalya", "Trabzon", "Samsun"])
        self.ui.btnGetItem.clicked.connect(self.GetItem)
        self.ui.btnLoadItems.clicked.connect(self.LoadItems)
        self.ui.btnClearItems.clicked.connect(self.ClearItems)

    def ClearItems(self):
        self.ui.cbSehirler.clear()

    def LoadItems(self):
        self.ui.cbSehirler.clear()
        sehirler = ["Adana", "İstanbul", "Ankara", "İzmir", "Bursa", "Antalya", "Trabzon", "Samsun"]
        self.ui.cbSehirler.addItems(sehirler)

    def GetItem(self):
        currentText = self.ui.cbSehirler.currentText()
        currentIndex = self.ui.cbSehirler.currentIndex()
        self.ui.lblResult.setText(f"Index: {currentIndex} - Şehir: {currentText}")

def main():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()