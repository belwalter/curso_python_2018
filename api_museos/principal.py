import sys
import menu_muestra

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication


class Principal(QMainWindow):

    def __init__(self):
        super().__init__()
        loadUi("interfaz/principal.ui", self)
        self.setWindowTitle("Menu principal")
        self.setGeometry(50, 50, self.frameGeometry().width(),
                         self.frameGeometry().height())
        self.show()
        self.agregar.clicked.connect(self.abrir_menu_m)

    def abrir_menu_m(self):
        menu_m = menu_muestra.Menu_Muestra()
        menu_m.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Principal()
    sys.exit(app.exec_())
