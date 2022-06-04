#!/usr/bin/python3

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","Julio", "Agosto",
	"Septiembre", "Octubre", "Noviembre", "Diciembre")

mes=1
while mes!=0:

	mes = int(input("Dame un numero entre 1 y 12: "))

	if(mes>=1 and mes<=12):
		print(meses[mes-1])


