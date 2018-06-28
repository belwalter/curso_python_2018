# FUNCIONES
def saludar():
    print("hola")


def sumar(num1, num2, resultado):
    return num1 + num2, num1 * num2


def nueva(num1, num2):
    num1 = num1 + num2


def cargar_lista(lista):
    lista.append(len(lista))


def nueva_funcion(n1=10, n2=6, n3=0):
    return n1 + n2 + n3


def parametros(n1, n2, *otros):
    print(n1 + n2)
    for elemento in otros:
        print(elemento)


n1 = "hola"
n2 = "mundo"

'''
saludar()
suma, producto = sumar_prod(n1, n2)
print(suma, producto)
'''
lista = []
for i in range(0, 10):
    cargar_lista(lista)
# print(lista)

#print(nueva_funcion(n3=1, n1=100))
parametros(4, 9, 90, 100, [1, 2, 3])

def suma(n1, n2):
    """Esta funcion retorna la suma de dos numeros"""
    return n1 + n2

def resta(n1, n2):
    """Esta funcion retorna la diferencia de dos numeros"""
    return n1 - n2

def producto(n1, n2):
    """Esta funcion retorna la multiplicaicon de dos numeros"""
    return n1 * n2

def calc(n1, n2, operador):
    dic = {'+': suma, '-': resta}
    """if(operador == '+'):
        return suma(n1, n2)
    elif(operador == '-'):
        return resta(n1, n2)
    elif(operador == '*'):
        return producto(n1, n2)
    else:
        return ''"""
    if operador in dic:
        return dic[operador](n1, n2)
    else:
        return ''

'''
print(calc(2, 5, '+'))
print(calc(2, 5, '-'))
print(calc(2, 5, '*'))
print(calc(2, 5, 'g'))
'''
# funcion = suma
# print(funcion(2, 5))

def criterio(item):
    return item[2]


lista = [[31, 'bel', 'walter'],[21, 'gonzalez','juan'],
         [55, 'alba','jose'],[55, 'alba','andres']]

lista.sort(key=criterio)
'''
for elemento in lista:
    print(elemento)
'''
