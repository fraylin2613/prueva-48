print("calculadora" )
print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. division")

opcion = input("elige una opcion: ")

if 1:
    num1 = float(input("ingresa el primer numero: "))
    num2 = float(input("ingresa el segundo numero: "))

    if opcion == "1":
        resultado = num1 + num2
        print("el resultado de la suma es: ", resultado)
    elif opcion == "2":
        resultado = num1 - num2
        print("el resultado de la resta es: ", resultado)
    elif opcion == "3":
        resultado = num1 * num2
        print("el resultado de la multiplicacion es: ", resultado)
    elif opcion == "4":
        if num2 != 0:
            resultado = num1 / num2
            print("el resultado de la division es: ", resultado)
        else:
            print("error: division por cero")
    else:
        print("opcion invalida")