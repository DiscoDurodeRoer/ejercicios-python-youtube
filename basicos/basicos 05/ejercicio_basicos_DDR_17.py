#!/usr/bin/python3

cadena1 = input("Dame una cadena: ")

cadena_al_reves = cadena1[::-1]

print(cadena_al_reves)

if( cadena1 == cadena_al_reves ):
	print("Es palindromo")
else:
	print("No es palindromo")
