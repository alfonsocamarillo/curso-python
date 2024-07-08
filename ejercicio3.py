empleados = [
    {"id": 1, "nombre": "Juan Lopez", "edad": 34, "sexo": "M", "DNI": "422f95", "trabaja": True},
    {"id": 2, "nombre": "Ivan Jimenez", "edad": 31, "sexo": "M", "DNI": "422f96", "trabaja": False},
    {"id": 3, "nombre": "Adriana Ocampo", "edad": 37, "sexo": "F", "DNI": "422f97", "trabaja": True}
]

print("Añade un nuevo empleado")
id=input("Introduce el nuevo id del nuevo empleado: ")
nombre=input("Introduce el nombre del nuevo empleado: ")
edad=input("Introduce la edad del nuevo empleado: ")
sexo=input("Introduce el sexo del nuevo empleado: ")
dni=input("Introduce el DNI del nuevo empleado: ")
trabaja=input("Trabaja accualmente en la empresa True o False: ")

nuevo_empleado= {"id": id, "nombre": nombre, "edad": edad, "sexo": sexo, "DNI": dni, "trabaja": trabaja}
empleados.append(nuevo_empleado)

for empleado in empleados:
    print(empleados)