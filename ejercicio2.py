edad = int(input("Ingrese su edad: "))
if(edad >= 18):
    print("Eres mayor de edad")
else:
    if(edad <= 0):
        print("Tu edad no puede existir")
    else:
        print("Eres menor de edad")
