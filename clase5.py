

class Animal():

    def __init__(self):
        self.__nombre = None

    def comer(self):
        return "el animal come"

    def get_nombre(self):
        return self.__nombre


class Perro(Animal):

    def __init__(self):
        self.color_pelo = None

    def comer(self):
        return "el perro come"


class Paloma(Perro):

    def __init__(self):
        self.vuela = None

    def comer(self):
        return "la paloma come"


obj1 = Paloma()
obj2 = Perro()
obj3 = Animal()

lista = [obj1, obj2, obj3]

for elemento in lista:
    print(elemento.comer())
    # if (isinstance(elemento, Perro)):
    #    print(elemento.comer2())

"""

class Animal(object):
    def desplazarse(self):
        print("el animal se mueve")

class Terrestre(object):

    def desplazarse(self):
        print("el animal camina")


class Acuatico(Animal):

    def desplazarse2(self):
        print("el animal nada")


class Cocodrilo(Acuatico, Terrestre):

    def __init__(self):
        pass

    def desplazarse(self):
        #Animal.desplazarse(self)
        #Terrestre.desplazarse(self)
        #Acuatico.desplazarse(self)
        super().desplazarse()
        print("el animal nada o camina depende del medio")


a = Cocodrilo()
a.desplazarse()


from abc import ABCMeta
import abc

class forma(metaclass=ABCMeta):

    __color = None

    @abc.abstractmethod
    def calcular_area(self):
        pass

    #@abc.abstractmethod
    def get_color(self):
        return self.__color


class circulo(forma):

    def __init__(self, radio, color=None):
        self.__color = color
        self.__radio = radio

    def calcular_area(self):
        return 3.14 * (self.__radio**2)

a = circulo(12)

print(a.calcular_area())

class rectangulo(forma):

    def __init__(self, lado1, lado2, color=None):
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__color = color

    def calcular_area(self):
        return self.__lado1 * self.__lado2

"""
