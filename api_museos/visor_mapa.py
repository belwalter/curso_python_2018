from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage
from PyQt5.QtCore import QUrl

from mapaurl import MapaUrl

class Mapa():

    def __init__(self, direcciones):
        self.browser = QWebEngineView()
        self.browser.resize(500,500)
        self.profile = QWebEngineProfile('storage', self.browser)
        self.webpage = QWebEnginePage(self.profile, self.browser)
        self.browser.setPage(self.webpage)
        m = MapaUrl()
        m.tipomapa(0)
        m.set_marcadores(direcciones)
        #url = m.get_url()
        url = m.mapa_dinamico()
        print(url)

        self.browser.load(QUrl(url))
        self.browser.show()
