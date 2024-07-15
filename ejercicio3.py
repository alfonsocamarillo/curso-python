empleados = [
    {"id": 1, "nombre": "Juan Lopez", "edad": 34, "sexo": "M", "DNI": "422f95", "trabaja": True},
    {"id": 2, "nombre": "Ivan Jimenez", "edad": 31, "sexo": "M", "DNI": "422f96", "trabaja": False},
    {"id": 3, "nombre": "Adriana Ocampo", "edad": 37, "sexo": "F", "DNI": "422f97", "trabaja": True}
]

eleccion = input("Menú\n (1) Agregar\n (2) Mostrar\n (3) Mostrar empleados activos\n (4) Salir\n Operación -> ")
salida = True

while salida:
    if eleccion == "1":
        print("Añade un nuevo empleado")
        id = input("Introduce el nuevo id del nuevo empleado: ")
        nombre = input("Introduce el nombre del nuevo empleado: ")
        edad = input("Introduce la edad del nuevo empleado: ")
        sexo = input("Introduce el sexo del nuevo empleado: ")
        dni = input("Introduce el DNI del nuevo empleado: ")
        trabaja = input("¿Trabaja actualmente en la empresa? (1) Sí o (2) No: ").strip() == '1'
        nuevo_empleado = {"id": id, "nombre": nombre, "edad": edad, "sexo": sexo, "DNI": dni, "trabaja": trabaja}
        empleados.append(nuevo_empleado)
        eleccion = input("Elige otra opción: ")
    
    elif eleccion == "2":
        for empleado in empleados:
            print(empleado)
        eleccion = input("Elige otra opción: ")
    
    elif eleccion == "3":
        for empleado in empleados:
            if empleado["trabaja"]:
                print(empleado)
        eleccion = input("Elige otra opción: ")
    
    elif eleccion == "4":
        salida = False
        print("Saliendo del programa...")

    else:
        print("Opción no válida. Por favor, intente de nuevo.")
        eleccion = input("Elige otra opción: ")
