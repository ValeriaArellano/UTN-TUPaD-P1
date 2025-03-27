# Nombre: Valeria Lucila Arellano

print("Hola mundo!")

nombre = input("Escribe tu nombre: ") 
print(f"Hola, {nombre}")

nombre2 = input("Escribe tu nombre: ") 
apellido = input("Escribe tu apellido: ") 
edad = input("Ingresa tu edad: ") 
lugarResidencia = input("Escribe tu lugar de residencia: ") 
print(f"Soy {nombre2} {apellido}, tengo {edad} años y vivo en {lugarResidencia}") 

radio = float(input("Ingrese el radio del círculo: ")) 
area = 3.14 * radio ** 2 
perimetro = 2 * 3.14 * radio 
print(f"El área del círculo es: {area}") 
print(f"El perímetro del círculo es: {perimetro}") 

cantSegundos = int(input("Ingrese la cantidad de segundos: ")) 
horas = cantSegundos / 3600 
print(f"{cantSegundos} es igual a {horas} horas")

numero = int(input("Ingrese un número: ")) 
for i in range(1, 11): print(numero, "x", i, "=", numero * i) 

numero1 = int(input("Ingrese el primer número: ")) 
numero2 = int(input("Ingrese el segundo número: ")) 
if numero1 == 0 or numero2 == 0: print("Los números deben ser distintos de 0.") 
else: suma = numero1 + numero2 
resta = numero1 - numero2 
multiplicacion = numero1 * numero2 
division = numero1 / numero2 
print(f"Suma: {suma}") 
print(f"Resta: {resta}") 
print(f"Multiplicación: {multiplicacion}") 
print(f"División: {division}")