def cargar():

    num1 = int(input("Escribe el primer valor: "))
    num2 = int(input("Escribe el segundo valor: "))
    num3 = int(input("Escribe el tercer valor: "))

    ordenar(num1, num2, num3)

def ordenar(num1, num2, num3):

    lista = [num1, num2, num3]
    lista.sort()

    mostrar(lista)

def mostrar(lista):

    for n in lista:
        print(n, " ", end="")

cargar()