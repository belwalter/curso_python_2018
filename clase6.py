# Ventanas

# PyQt5

import sys

import menu1

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox


class mi_ventana(QMainWindow):

    def __init__(self):
        super().__init__()
        loadUi("principal.ui", self)
        self.setGeometry(100, 50, self.frameGeometry().width(),
                         self.frameGeometry().height())
        self.show()
        self.borrar.clicked.connect(self.cambiar_titulo)
        self.borrar.clicked.connect(self.cambiar)
        self.abrir.clicked.connect(self.abrir_ventana)
        self.msj.clicked.connect(self.cartel)

    def cambiar_titulo(self):
        self.setWindowTitle("holaaa!!!")

    def cambiar(self):
        self.palabra.setText("holaaa!!!")

    def abrir_ventana(self):
        palabra = self.palabra.text()
        dialog = menu1.mi_dialogo(palabra)
        dialog.exec_()
        self.palabra.setText(dialog.devolver_texto())

    def cartel(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("This is a message box")
        msg.setInformativeText("This is additional information")
        msg.setWindowTitle("MessageBox demo")
        msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel |
        QMessageBox.Retry)
        msg.setIcon(QMessageBox.Critical)
        ret = msg.exec_()
        if(QMessageBox.Retry == ret):
            print("ret")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mi_ventana()
    sys.exit(app.exec_())
