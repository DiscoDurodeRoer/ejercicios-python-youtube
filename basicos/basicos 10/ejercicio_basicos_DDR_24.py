valid = False
while not valid:

    num = int(input("Introduce un numero positivo e impar"))

    if num > 0 and num % 2 != 0:
        valid = True

numCharacters = 0
numberShow = 1
i = 1
while i <= num:

    if i % 2 == 1:

        j = 1
        while j < num:
            print("=", end="")
            j = j + 1

        print(numberShow)

        if numberShow + 2 > 10:
            numberShow = 1
        else:
            numberShow = numberShow + 2

        numCharacters = numCharacters + num

    else:

        j = 1
        while j < num:
            print(" ", end="")
            j = j + 1

        print("+")

        numCharacters = numCharacters + 1

    i = i + 1

print("El numero diferente a espacios en blanco es de: ", numCharacters)