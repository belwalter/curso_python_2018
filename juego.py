
#CURSO 2017
import random

lista = ["piedra","papel","tijera"]

cjug = 0
cpc = 0

while (cjug<3) and (cpc<3):
    ej = input("ingrese opcion")
    epc = random.choice(lista)
    if (ej!=epc):    
        if ((ej==lista[0]) and (epc==lista[2])) or (ej==lista[1]) and (epc==lista[0]) or ((ej==lista[2]) and (epc==lista[1])):
            cjug+=1
            print("gano jugador", ej, cjug)
        elif ((epc==lista[0]) and (ej==lista[2])) or (epc==lista[1]) and (ej==lista[0]) or ((epc==lista[2]) and (epc==lista[1])):
            cpc+=1
            print("gano pc", epc, cpc)
    else:
        print("empate")



 

import random
matrizj = []
for i in range (0,3):
    lista = []    
    for j in range (0,3):
        lista.append("agua")
    matrizj.append(lista)        
matrizpc = []
for i in range (0,3):
    lista = []    
    for j in range (0,3):
        lista.append("agua")
    matrizpc.append(lista)        
barco = 0
while (barco<3):
    fila = random.randint(0,2)
    columna = random.randint(0,2)
    if (matrizpc[fila][columna] == "agua"):
        barco += 1
        matrizpc[fila][columna] = "barco"
barco = 0
while (barco<3):
    fila = random.randint(0,2)
    columna = random.randint(0,2)
    if (matrizj[fila][columna] == "agua"):
        barco += 1
        matrizj[fila][columna] = "barco"

for fila in matrizj:
    print(fila)

cbhj = 0
cbhpc = 0

while(cbhj<3 and cbhpc<3):
    fila = random.randint(0,2)
    columna = random.randint(0,2)
    if (matrizj[fila][columna] == "barco"):
        cbhpc += 1
        print("barco hundido")
    else:
        print("agua")
    fila = int(input('ingrese fila'))
    columna = int(input('ingrese columna'))
    if (matrizpc[fila][columna] == "barco"):
        cbhj += 1
        print("barco hundido")
    else:
        print("agua")
