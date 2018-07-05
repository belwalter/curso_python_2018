
from abc import ABCMeta
import abc


class Obra_Muestra(metaclass=abc.ABCMeta):

    def get_artista(self):
        return self.artista

    def get_titulo(self):
        return self.titulo

    def get_anio(self):
        return self.anio

    def get_descripcion(self):
        return self.descripcion

    @abc.abstractmethod
    def __init__(self, artista=None, anio=None, titulo=None, descripcion=None):
        self.artista = artista
        self.anio = anio
        self.titulo = titulo
        self.descripcion = descripcion


# a = Obra_Muestra()
