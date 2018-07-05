from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.uic import loadUi

import cargar_muestra
import pintura


class Menu_Muestra(QDialog):

    def __init__(self):
        super().__init__()
        loadUi("interfaz/menu_muestra.ui", self)
        self.lista_muestras = []
        self.agregar.clicked.connect(self.abrir_menu_c)

    def abrir_menu_c(self):
        menu_c = cargar_muestra.Cargar_Muestra()
        menu_c.exec_()
        muestra = menu_c.muestra
        if(muestra != None):
            self.lista_muestras.append(muestra)
            self.actualizar_tabla()

    def actualizar_tabla(self):
        self.tabla.setRowCount(0)
        for muestra in self.lista_muestras:
            self.tabla.insertRow(self.tabla.rowCount())
            self.tabla.setItem(self.tabla.rowCount()-1, 0,
                               QTableWidgetItem(str(muestra.artista)))
            self.tabla.setItem(self.tabla.rowCount()-1, 1,
                               QTableWidgetItem(muestra.titulo))
            self.tabla.setItem(self.tabla.rowCount()-1, 2,
                               QTableWidgetItem(muestra.anio))
            tipo = ""
            if (isinstance(muestra, pintura.Pintura)):
                tipo = "Pintura"
            self.tabla.setItem(self.tabla.rowCount()-1, 3,
                               QTableWidgetItem(tipo))
