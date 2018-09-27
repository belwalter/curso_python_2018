
from abc import ABCMeta
import abc


class Obra_Muestra(metaclass=abc.ABCMeta):

    def get_museo():
        return self.museo

    def get_artista(self):
        return self.artista

    def get_titulo(self):
        return self.titulo

    def get_anio(self):
        return self.anio

    def get_descripcion(self):
        return self.descripcion

    @abc.abstractmethod
    def __init__(self, artista=None, anio=None, titulo=None, descripcion=None,
                 museo=None):
        self.artista = artista
        self.anio = anio
        self.titulo = titulo
        self.descripcion = descripcion
        self.museo = museo


# a = Obra_Muestra()
