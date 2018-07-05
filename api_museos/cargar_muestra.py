from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

import pintura


class Cargar_Muestra(QDialog):

    def __init__(self):
        super().__init__()
        loadUi("interfaz/cargar_muestra.ui", self)
        self.combobox.currentIndexChanged.connect(self.habilitar)
        self.guardar.clicked.connect(self.cargar)
        self.muestra = None

    def cargar(self):
        if(self.combobox.currentIndex() == 0):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Debe Seleccionar un Tipo de Muestra")
            respuesta = msg.exec()
        elif (self.combobox.currentIndex() == 1):
            self.muestra = pintura.Pintura()
            self.muestra.estilo = self.estilo.text()
            self.muestra.artista = self.artista.text()
            self.muestra.anio = self.anio.date().toString("yyyy")
            self.hide()

    def habilitar(self):
        if (self.combobox.currentIndex() == 0):
            self.estilo.setEnabled(False)
            self.peso.setEnabled(False)
            self.tipo.setEnabled(False)
        if (self.combobox.currentIndex() == 1):
            self.estilo.setEnabled(True)
            self.peso.setEnabled(False)
            self.peso.setText("")
            self.tipo.setEnabled(False)
            self.tipo.setText("")
        elif (self.combobox.currentIndex() == 2):
            self.estilo.setEnabled(False)
            self.peso.setEnabled(True)
            self.tipo.setEnabled(False)
        elif (self.combobox.currentIndex() == 3):
            self.estilo.setEnabled(False)
            self.peso.setEnabled(False)
            self.tipo.setEnabled(True)
