#!/usr/bin/python3

tupla = (1,2,3,4,5,6,7,8,9,10)

indice = int(input("Dame un indice: "))

if indice>=0 and indice<len(tupla):
	print(tupla[indice])
else:
	print("Indice no valido")
