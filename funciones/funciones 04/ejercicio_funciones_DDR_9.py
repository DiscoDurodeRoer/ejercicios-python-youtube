def crearEmpleado():

    nombreEmpleado = input("Escribe el nombre del empleado")
    sueldoEmpleado = int(input("Escribe el sueldo del empleado"))

    return (nombreEmpleado, sueldoEmpleado)

def empleadoMayor(emp1, emp2):

    if emp1[1] > emp2[1]:
        print(emp1[0], " tiene mayor sueldo")
    else:
        print(emp2[0], " tiene mayor sueldo")

emp1 = crearEmpleado()
emp2 = crearEmpleado()
empleadoMayor(emp1, emp2)