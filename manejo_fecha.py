
# TIME
import time
print(time.strftime("%B - %b"))
"""
print(time.strftime("%H:%M:%S"))
print(time.strftime("%I:%M:%S"))
print(time.strftime("%d/%m/%y"))
print(time.strftime("%c"))
print(time.strftime("%X"))
print(time.strftime("dia %j semana %U"))
"""
fecha = time.strftime("8/9/2015")
# print(fecha)

# DATETIME
from datetime import datetime, date, timedelta

fecha1 = date.today()
print(type(fecha1), fecha1)
fecha2 = datetime.now()
print(type(fecha2), fecha2)

"""
print("Fecha y hora = %s" % fecha2)
print("Fecha y hora en formato ISO = %s" % fecha2.isoformat())
print(u"Año = %s" % fecha2.year)
print("Mes = %s" % fecha2.month)
print("Dia =  %s" % fecha2.day)
print("Formato dd/mm/yyyy =  %s/%s/%s" % (fecha2.day, fecha2.month, fecha2.year))
print("Hora = %s" % fecha2.hour)
print("Minutos = %s" % fecha2.minute)
print("Segundos =  %s" % fecha2.second)
print("Formato hh:mm:ss = %s:%s:%s" % (fecha2.hour, fecha2.month, fecha2.second))
"""
"""
print("Fecha y hora = %s" % fecha1)
print("Fecha y hora en formato ISO = %s" % fecha1.isoformat())
print(u"Anio = %s" % fecha1.year)
print("Mes = %s" % fecha1.month)
print("Dia =  %s" % fecha1.day)
print("Formato dd/mm/yyyy =  %s/%s/%s" % (fecha1.day, fecha1.month, fecha1.year))
"""

# date a partir de string
time = time.strftime("%d/%m/%y")
x = datetime.strptime(time,"%d/%m/%y")
# print(x)

# date a partir de enteros
y = datetime(2015, 12, 31, 19, 45, 20)
# se puede definir hora datetime(2015,12,31,13,12,45)
#print(y)


# sumar o restar dias a un date
b = timedelta(days=3, minutes=30)
# print("%s" %(x - b), "%s" %(x + b))

# comparacion con operadores >, <, >=, <=, !=, ==
# print (x, y)
# print (x>y, x<y, x>=y, x<=y, x!=y, x==y)


""" CALENDAR """
import calendar

# print(calendar.calendar(2018))
# print(calendar.prmonth(2018,9))

'''
Aplicando formatos a fechas y horas (Máscaras)
Las siguientes claves se combinan para aplicar formatos:

%a 	Nombre local abreviado de día de semana
%A 	Nombre local completo de día de semana
%b 	Nombre local abreviado de mes
%B 	Nombre local completo de mes
%c 	Representación local de fecha y hora
%d 	Día de mes [01,31]
%H 	Hora (horario 24 horas) [00,23]
%I 	Hora (horario 12 horas) [01,12]
%j 	Número de día del año [001,366]
%m 	Mes [01,12]
%M 	Minuto [00,59]
%p 	Etiqueta AM o PM
%S 	Segundo
%U 	Nº semana del año. Se considera al Domingo como primer día de semana [00,53]
%w 	Establece el primer día de semana [0(Domingo),1(Lunes)... 6].
%W 	Nº semana del año (Se considera al Lunes como primer día de semana) [00,53]
%x 	Fecha local
%X 	Hora local
%y 	Año en formato corto [00,99]
%Y 	Año en formato largo
%Z 	Nombre de Zona Horaria
'''
