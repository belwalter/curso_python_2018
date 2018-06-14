
# PROGRAMACION ORIENTADA A OBJETOS


class persona():

    def __init__(self, nombre=None, apellido=None, hermano=None):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__hermano = hermano

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre.capitalize()

    @property
    def apellido(self):
        return self.__apellido

    def __str__(self):
        return self.__nombre + ' ' + self.__apellido

    def get_hno(self):
        return self.__hermano

# nombre = input('ingrese nombre')


p = persona('walter', 'bel')
p1 = persona('asdasd', 'asdasd', p)

lista = [p, p1]
p.nombre = "nuevo"
print(p.nombre)

def orden(elemento):
    return elemento.get_apellido() + elemento.get_nombre()

'''
lista.sort(key=orden)
for elemento in lista:
    print(elemento)
'''
#print(p1.get_hno().set_nombre('Lucas'))

#print(p.get_nombre())
