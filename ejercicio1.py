almacen=["Manzana","Mango","Uvas"]
eleccion=input("Menu \n (1) Agregar \n (2) Eliminar \n (3) Mostrar \n (4) Salir \n Operacion ->")
salida=True
while salida==True:
    if eleccion == "1":
        fruta = input("Ingrese una fruta nueva: ")
        almacen.append(fruta.capitalize())
        eleccion=input("Elije otra opcion: ")

    elif eleccion == "2":
        eliminar = input("Ingrese una fruta a eliminar: ")
        eliminar=eliminar.capitalize()
        almacen.remove(eliminar)
        eleccion=input("Elije otra opcion: ")
    
    elif eleccion == "3":
        almacen.sort()
        print (almacen)
        eleccion=input("Elije otra opcion: ")

    elif eleccion == "4":
            salida=False
            quit()