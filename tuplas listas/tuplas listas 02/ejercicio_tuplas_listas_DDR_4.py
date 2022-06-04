#!/usr/bin/python3

lista = []

cadena = input("Dame una cadena: ")

for c in cadena:
	if(c != " "):
		lista.append(c)

print(lista)
