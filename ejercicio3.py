frase = input("Ingrese un texto: ")
boleano = input("Ingrese un True O False: ")
entero = input("Ingrese un numero entero: ")
decimal = input("Ingrese un numero desimal: ")

boleano=bool(boleano)
entero=int(entero)
decimal=float(decimal)

print(frase, "es: " , type(frase))
print(boleano, "es: " , type(boleano))
print(entero, "es: " , type(entero))
print(decimal, "es: " , type(decimal))
