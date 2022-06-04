from random import *

nameP1 =input("Inserte el nombre del jugador 1")
nameP2 =input("Inserte el nombre del jugador 2")

gameWinP1 = 0
gameWinP2 = 0

numGame = 1

continueGame = True

while (gameWinP1 < 2 and gameWinP2 < 2) and continueGame:

    print("Partida nº ", numGame)

    objectivo = randint(1,6)

    print("El objetivo es ", objectivo)

    num1P1 = randint(1,6)
    num2P1 = randint(1,6)
    sumaP1 = num1P1 + num2P1

    num1P2 = randint(1,6)
    num2P2 = randint(1,6)
    sumaP2 = num1P2 + num2P2

    print("El jugador " , nameP1, " ha sacado " , num1P1, " y ", num2P1)
    print("El jugador " , nameP2, " ha sacado " , num1P2, " y ", num2P2)

    numWinners = 0
    if sumaP1 == objectivo:
        numWinners = numWinners + 1
        gameWinP1 = gameWinP1 + 1

    if sumaP2 == objectivo:
        numWinners = numWinners + 1
        gameWinP2 = gameWinP2 + 1

    if numWinners == 2:
        print("Han ganado los dos")
    elif numWinners == 1:
        if sumaP1 == objectivo:
            print("Ha ganadio el jugador ", nameP1)
        if sumaP2 == objectivo:
            print("Ha ganadio el jugador ", nameP2)
    else:
        print("No ha ganado nadie")

    continueGame = input("¿Quieres continuar? (S/N)") == "S"

    numGame = numGame + 1

print("Juego terminado")
print("Se han jugado ", numGame," partidas")

if gameWinP1 == 2:
    print("Gana ", nameP1)
if gameWinP2 == 2:
    print("Gana ", nameP2)
