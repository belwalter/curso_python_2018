from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.uic import loadUi

import cargar_muestra
import pintura
import prestamo


class Menu_Muestra(QDialog):

    def __init__(self, museo, museos):
        super().__init__()
        self.museo = museo
        self.museos = museos
        loadUi("interfaz/menu_muestra.ui", self)
        self.agregar.clicked.connect(self.abrir_menu_c)
        self.prestar.clicked.connect(self.menu_prestar)
        self.actualizar_tabla()

    def menu_prestar(self):
        if(self.tabla.currentRow() >= 0):
            muestra = self.museo.muestras[int(self.tabla.currentRow())]
            menu_p = prestamo.Prestamo_Obra(muestra, self.museo, self.museos)
            menu_p.exec_()

    def abrir_menu_c(self):
        menu_c = cargar_muestra.Cargar_Muestra(self.museo)
        menu_c.exec_()
        muestra = menu_c.muestra
        if(muestra != None):
            self.museo.muestras.append(muestra)
            self.actualizar_tabla()

    def actualizar_tabla(self):
        self.tabla.setRowCount(0)
        for muestra in self.museo.muestras:
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
