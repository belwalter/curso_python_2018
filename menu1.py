
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class mi_dialogo(QDialog):

    def __init__(self, palabra=None):
        super().__init__()
        loadUi("menu1.ui", self)
        if (palabra != None):
            self.texto.setText(palabra)
        self.texto.textChanged.connect(self.validar)

    def devolver_texto(self):
        return self.texto.text()

    def validar(self):
        if(not self.texto.text().isalpha()):
            self.texto.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.texto.setStyleSheet("color: rgb(0, 0, 0);")
