from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from _radiobuttonForm import Ui_MainWindow
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect buttons to their functions
        self.ui.pushButton.clicked.connect(self.show_selected_country)
        self.ui.pushButton_2.clicked.connect(self.show_selected_education)

    def show_selected_country(self):
        if self.ui.radioButton.isChecked():
            self.ui.lblUlke.setText("Türkiye")
        elif self.ui.radioButton_2.isChecked():
            self.ui.lblUlke.setText("Almanya")
        elif self.ui.radioButton_3.isChecked():
            self.ui.lblUlke.setText("Fransa")
        elif self.ui.radioButton_4.isChecked():
            self.ui.lblUlke.setText("İngiltere")
        else:
            self.ui.lblUlke.setText("Seçim yapılmadı")

    def show_selected_education(self):
        if self.ui.radioButton_5.isChecked():
            self.ui.lblEgitim.setText("Lise")
        elif self.ui.radioButton_6.isChecked():
            self.ui.lblEgitim.setText("Ön Lisans")
        elif self.ui.radioButton_7.isChecked():
            self.ui.lblEgitim.setText("Lisans")
        elif self.ui.radioButton_8.isChecked():
            self.ui.lblEgitim.setText("Yüksek Lisans")
        else:
            self.ui.lblEgitim.setText("Seçim yapılmadı")

def app():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    app()