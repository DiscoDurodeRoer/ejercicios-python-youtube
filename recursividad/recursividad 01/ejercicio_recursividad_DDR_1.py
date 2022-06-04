def sumaRec(numero):

    if numero == 1:
        return 1
    else:
        return numero + sumaRec(numero - 1)

print(sumaRec(5))