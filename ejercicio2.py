
eleccion=input("Menu \n (1) Agregar \n (2) Mostrar \n (3) Salir \n Operacion ->")
salida=True
while salida==True:
    if eleccion == "1":
        DNI=input("Ingrese 5 DNI: ").split(",")
        DNI_unicos = list(set(DNI))
        eleccion=input("Elije otra opcion: ")

    elif eleccion == "2":
        DNI_unicos.sort()
        print (DNI_unicos)
        eleccion=input("Elije otra opcion: ")
    
    elif eleccion == "3":
        salida=False
        quit()
        


