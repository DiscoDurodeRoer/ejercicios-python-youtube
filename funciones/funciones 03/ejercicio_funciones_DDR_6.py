#!/usr/bin/python3


def numerosEntre(num1, num2):
	
	if (num1 > num2):

		aux = num1
		num1 = num2
		num2 = aux

	for i in range(num1+1, num2):
		print(i)

numerosEntre(9,10)