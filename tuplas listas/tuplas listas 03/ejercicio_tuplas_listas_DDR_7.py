#!/usr/bin/python3

lista = []

numero = int(input("Dame un numero: "))

for i in range(1,6):
	resultado = numero*i
	print(numero , "*" , i , "=",resultado)
	lista.append(resultado)

print(lista)
