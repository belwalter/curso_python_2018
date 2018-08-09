from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi


import museo
from funciones_mongo import guardar_museo


class Cargar_Museo(QDialog):

    def __init__(self):
        super().__init__()
        loadUi("interfaz/cargar_museo.ui", self)
        self.cargar.clicked.connect(self.cargar_)
        self.museo = None

    def cargar_(self):
        self.museo = museo.Museo()
        self.museo.nombre = self.nombre.text()
        self.museo.direccion = self.direccion.text()
        guardar_museo(self.museo)
        self.hide()
