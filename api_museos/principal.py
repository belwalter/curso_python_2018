import sys
import menu_muestra
import cargar_museo

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


class Principal(QMainWindow):

    def __init__(self):
        super().__init__()
        loadUi("interfaz/principal.ui", self)
        self.setWindowTitle("Menu principal")
        self.setGeometry(50, 50, self.frameGeometry().width(),
                         self.frameGeometry().height())
        self.show()
        self.lista_museos = []
        self.agregar.clicked.connect(self.abrir_menu_m)
        self.agregar_museo.clicked.connect(self.agregar_museo_)

    def abrir_menu_m(self):
        menu_m = menu_muestra.Menu_Muestra()
        menu_m.exec_()

    def agregar_museo_(self):
        menu_cargam = cargar_museo.Cargar_Museo()
        menu_cargam.exec_()
        self.lista_museos.append(menu_cargam.museo)
        self.actualizar_tabla()

    def actualizar_tabla(self):
        self.tabla.setRowCount(0)
        for museo in self.lista_museos:
            self.tabla.insertRow(self.tabla.rowCount())
            self.tabla.setItem(self.tabla.rowCount()-1, 0,
                               QTableWidgetItem(str(museo.nombre)))
            self.tabla.setItem(self.tabla.rowCount()-1, 1,
                               QTableWidgetItem(museo.direccion))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Principal()
    sys.exit(app.exec_())
