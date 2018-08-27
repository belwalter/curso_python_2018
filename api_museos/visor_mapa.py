from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage
from PyQt5.QtCore import QUrl


class Mapa():

    def __init__(self):
        self.browser = QWebEngineView()
        self.profile = QWebEngineProfile('storage', self.browser)
        self.webpage = QWebEnginePage(self.profile, self.browser)
        self.browser.setPage(self.webpage)
        self.browser.setMinimumSize(500,500)
        self.browser.load(QUrl("https://maps.googleapis.com/maps/api/staticmap?center=Williamsburg,Brooklyn,NY&zoom=13&size=400x400&markers=color:blue%7Clabel:S%7C11211%7C11206%7C11222"))
        self.browser.show()
