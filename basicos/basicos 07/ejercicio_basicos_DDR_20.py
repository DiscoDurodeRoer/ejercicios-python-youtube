lado = 20
for fila in range(lado):
    for columna in range(lado):
        if fila == 0 or fila == lado -1 or columna == 0 or columna == lado - 1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()