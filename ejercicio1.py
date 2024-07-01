print("CALACULADORA")
num1 = float(input("Introduzca un numero: "))
num2 = float(input("Introduzca el segundo numero: "))
operacion = input("Selecione la operacion que desa realizar: \n Suma = S \n Resta = R \n Multiplicacion = M \n Divicion = D \n ¿Operacion? :")

if(operacion == "S" or operacion == "s"):
    resultado=num1+num2
elif (operacion == "R" or operacion == "r"):
    resultado=num1-num2
elif(operacion == "M" or operacion == "m"):
    resultado=num1*num2
elif(operacion == "D" or operacion == "d"):
    if(num2==0):
        resultado="Inf"
        print("No se puede dividir entre 0")
    else:
        resultado=num1/num2
else:
    resultado="N/A"
    print("Opcion invalida")

print("El resultado es: ",resultado)