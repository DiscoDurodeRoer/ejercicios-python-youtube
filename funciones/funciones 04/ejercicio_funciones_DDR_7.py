def numPares(cadena):

    contador = 0
    for c in cadena:
        digito = int(c)
        if digito % 2 == 0:
            contador = contador + 1
    return contador

num = int(input("Escribe un numero entero: "))
cadena = str(num)
print("El numero de digitos pares es de: ", numPares(cadena))