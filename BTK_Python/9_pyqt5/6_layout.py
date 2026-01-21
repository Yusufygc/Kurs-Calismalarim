import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPalette, QColor

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True) # arka plan rengini doldurmak için
       
        palette = self.palette() # mevcut paleti al ve değiştir
        palette.setColor(QPalette.Window, QColor(color)) # pencere rengini ayarla
        self.setPalette(palette) # yeni paleti ayarla

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Layout Example")

        # Ana widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        """
        # Dikey layout
        v_layout = QtWidgets.QVBoxLayout() # yatay layout için QHBoxLayout kullanılabilir

        # Renkli widget'lar
        red_widget = Color("red")
        green_widget = Color("green")
        blue_widget = Color("blue")
        purple_widget = Color("purple")

        # Widget'ları layout'a ekle
        v_layout.addWidget(red_widget)
        v_layout.addWidget(green_widget)
        v_layout.addWidget(blue_widget)
        v_layout.addWidget(purple_widget)
        """

        layout = QtWidgets.QGridLayout()
        # Renkli widget'lar
        red_widget = Color("red")
        green_widget = Color("green")
        blue_widget = Color("blue")
        purple_widget = Color("purple")
        # Widget'ları layout'a ekle
        layout.addWidget(red_widget, 0, 0)      # 0. satır, 0. sütun
        layout.addWidget(green_widget, 1, 0)    # 0. satır, 1. sütun
        layout.addWidget(blue_widget, 0, 2)     # 1.satır, 0. sütun
        layout.addWidget(purple_widget, 4, 2)   # 1. satır, 1. sütun
     

        # Ana widget'a layout'u ayarla
        main_widget.setLayout(layout)

def app():
    uygulama = QApplication(sys.argv)
    pencere = MainWindow()
    pencere.show()
    sys.exit(uygulama.exec_())

if __name__ == "__main__":
    app()