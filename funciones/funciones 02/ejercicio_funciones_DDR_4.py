#!/usr/bin/python3

from random import *

def generaNumeroAleatorio(minimo,maximo):

	try:
		if minimo > maximo:
			aux = minimo
			minimo = maximo
			maximo = aux

		return randint(minimo, maximo)
	except TypeError:
		print("Debes escribir numeros")
		return -1

i=0
while i<5:
	print(generaNumeroAleatorio(5,10))
	i=i+1