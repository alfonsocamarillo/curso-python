empleados = [
    {"id": 1, "nombre": "Juan Lopez", "edad": 34, "sexo": "M", "DNI": "422f95", "trabaja": True},
    {"id": 2, "nombre": "Ivan Jimenez", "edad": 31, "sexo": "M", "DNI": "422f96", "trabaja": False},
    {"id": 3, "nombre": "Adriana Ocampo", "edad": 37, "sexo": "F", "DNI": "422f97", "trabaja": True}
]

empleados2 ={
    "001":("Juan", 25, "Masculino", 452582, True),
    "002":("Maria",35, "Masculino", 556252, False),
    "003":("Ivan", 45, "Masculino", 225872, True),
}

print("Añade un nuevo empleado")
id=input("Introduce el nuevo id del nuevo empleado: ")
nombre=input("Introduce el nombre del nuevo empleado: ")
edad=input("Introduce la edad del nuevo empleado: ")
sexo=input("Introduce el sexo del nuevo empleado: ")
dni=input("Introduce el DNI del nuevo empleado: ")
trabaja=bool(input("Trabaja accualmente en la empresa si es asi poner (1) no no lo es (0): "))

nuevo_empleado= {"id": id, "nombre": nombre, "edad": edad, "sexo": sexo, "DNI": dni, "trabaja": trabaja}
nuevo_empleado2= {id:(nombre,edad,sexo,  dni, trabaja)}
empleados.append(nuevo_empleado)
empleados2.update(nuevo_empleado2)

print(empleados)
print(empleados2.keys())

