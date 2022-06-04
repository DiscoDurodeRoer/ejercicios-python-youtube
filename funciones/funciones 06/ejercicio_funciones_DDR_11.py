def modifica_pos_impares(lista):

    for i in range(1, len(lista),2):
        lista[i] = lista[i] - lista[i-1]

    return lista

def modifica_valores_multiplesde7 (lista):

    for i in range(0, len(lista)):
        if lista[i] % 7 == 0:
            lista[i] = lista[i] + lista[len(lista)-1]

    return lista

def crea_lista ():

    continuar = True
    lista = []

    while continuar:

        num = int(input("Introduce un numero menor que 1000 (si quieres salir, introduce un numero negativo): "))

        if num < 0:
            continuar = False
        elif num < 1000:
            lista.append(num)
        else:
            print("Debes introducir un numero menor que 1000. Si quieres salir, introduce un numero negativo")

    return lista

lista = crea_lista()

print("Original")
print(lista)

print("Multiplos de 7")
lista = modifica_valores_multiplesde7(lista)
print(lista)

print("Posiciones impares")
modifica_pos_impares(lista)
print(lista)