texto = input("Ingrese un texto: ")
palabra = input("Ingrese la palabra a buscar en el texto: ")
if palabra in texto:
    print("Esa palabra esta en el texto")
else:
    print("Esa palabra no existe en este texto")