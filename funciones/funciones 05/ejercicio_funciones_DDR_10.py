def num_digits(n):

    num = 0

    while n > 0:
        n = n // 10
        num = num + 1
    return num

def get_digit(n, d):
    value = 10**(d-1)
    division = n // value
    residuo = division % 10
    return residuo

def is_good(n):

    numD = num_digits(n)
    suma = 0
    i = 1
    while  i <= numD:
        digit = get_digit(n, i)
        suma = suma + digit**numD
        i = i + 1

    return suma == n

def read():

    valid = False
    while not valid:

        num = int(input("Introduce un numero positivo: "))

        if num > 0:
            valid = True
    return num

a = read()
b = read()

i = a
while i <= b:

    if is_good(i):
        print("Es bueno: ", i)

    i = i + 1

