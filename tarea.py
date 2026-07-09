"""se usa para generar comentarios

nombre = input("Ingrese su nombre: ")
print("Hola", nombre, "me indica cual es la suma que desea realiza ")
num1 = float(input("ingresa el primer numero: "))
num2 = float(input("ingresa el segundo numero: "))
suma = num1 + num2
print("el resultado de la suma es: ", suma)

x = "3.1416"
print(float(x))

print("ingrese la temperatura")
t1 = 27.5
t2 = 28.0
t3 = 29.2
promedio = (t1+ t2 + t3) / 3

print("promedio" , promedio)


lectura_adb = 2048
voltaje = (lectura_adb * 3.3) / 4095
print("el voltaje es: ", voltaje)

temperatura = 31
if temperatura <30:
    print("alerta temperatura alta")
else:
    print("temperatura normal")

temperatura = 24
if temperatura <20:
    print("frio") 
elif temperatura <= 30:
    print ("normal")
else:
    print("normal")

luz = 700
if luz <1000:
    print("lampara encendida")
else:
    print("lampara apagada")
    """
distancia = 15
if distancia < 20:
    print("buzzer encendido")