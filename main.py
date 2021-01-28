from funciones import *
from leer import lee_condiciones
from time import time

#Creamos una lista de 5 objetos de la clase house
casas = list()
for i in range (5):
	casa = house(i+1)
	casas.append(casa)

#Importamos las condiciones usando la funcion leer()
condiciones = lee_condiciones("premisas.txt")

#Bucle principal del programa:
continua = True
t_0 = time()
n = 0
while (continua):
	repasa_condiciones(casas, condiciones)	
	continua = quita_solas(casas)
	quita_repetidas(casas)
	n += 1
t_final = time()

imprime(casas)
print ( "\nResuelto en {} ciclos\nTiempo de ejecucion: {} seg".format(n, t_final-t_0) )

