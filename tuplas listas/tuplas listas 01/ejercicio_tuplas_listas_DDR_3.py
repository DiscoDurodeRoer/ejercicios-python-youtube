#!/usr/bin/python3

lista = []

suma = 0
media = 0
numero = 0

for i in range(10):
	numero = int(input("Dame un numero: "))
	lista.append(numero)
	suma += numero

for i in lista:
	print(i)

media = suma / len(lista)

print("La suma es ",suma)
print("La media es ",media)
