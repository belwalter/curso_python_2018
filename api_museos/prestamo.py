from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from datetime import date, datetime


class Prestamo_Obra(QDialog):

    def __init__(self, muestra, museo, museos):
        super().__init__()
        loadUi("interfaz/prestar.ui", self)
        #self.combobox.currentIndexChanged.connect(self.habilitar)
        self.prestar.clicked.connect(self.prestar_muestra)
        self.lista_museos = museos
        self.museo = museo
        for m in museos:
            if (m != museo):
                self.destino.addItem(m.nombre)
        self.muestra = muestra
        self.descripcion.setText(muestra.get_artista())
        self.desde.setDate(date.today())
        self.hasta.setDate(date.today())

    def prestar_muestra(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        hasta = datetime(int(self.hasta.date().toString("yyyy")),
                         int(self.hasta.date().toString("MM")),
                         int(self.hasta.date().toString("dd")))
        desde = datetime(int(self.desde.date().toString("yyyy")),
                         int(self.desde.date().toString("MM")),
                         int(self.desde.date().toString("dd")))
        cadena = str(hasta.date() - desde.date())
        cantidad = cadena[0:cadena.find('d')]
        museo_destino = self.destino.currentText()
        msg.setText("Debe Prestar la Muestra por "+str(cantidad)+"días?"+
                    " a "+museo_destino)
        respuesta = msg.exec()
        if (respuesta == QMessageBox.Ok):
            print("prestamo")
            for m in self.lista_museos:
                if(museo_destino == m.nombre):
                    if(self.muestra.museo != self.museo):
                        print("no se puede prestar no es dueño")
                    else:
                        m.muestras.append(self.muestra)
        else:
            print("no")
