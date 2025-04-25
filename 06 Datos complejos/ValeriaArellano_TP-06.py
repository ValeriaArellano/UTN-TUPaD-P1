#Github: https://github.com/ValeriaArellano/UTN-TUPaD-P1

# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.

lista_frutas = list(precios_frutas.keys())

# 4) Crear una clase llamada Persona que contenga un método __init__ con los atributos
# nombre, pais y edad y el método saludar. El método saludar debe imprimir por pantalla un
# mensaje de saludo que siga la estructura "¡Hola! Soy [nombre], vivo en [pais] y tengo [edad]
# años."

class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años")

# 5) Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y
# calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente.
# Ayuda: el módulo math puede ser de utilidad para usar la constante 𝜋.


import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return round((math.pi * (self.radio ** 2)), 2)

    def calcular_perimetro(self):
        return round((2 * math.pi * self.radio),2)


# 6) Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente
# balanceados usando una pila.

def esta_balanceado(cadena):
    pila = []
    pares = {')': '(', '}': '{', ']': '['}

    for caracter in cadena:
        if caracter in '({[':
            pila.append(caracter)
        elif caracter in ')}]':
            if not pila or pila[-1] != pares[caracter]:
                return False
            pila.pop()
    return len(pila) == 0

# 7) Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir:
# ● Agregar clientes (encolar).
# ● Atender clientes (desencolar).
# ● Mostrar el siguiente cliente en la fila

from collections import deque
class Cola:
    def __init__(self):
        self.elementos = deque()

    def encolar(self, elemento):
        self.elementos.append(elemento)

    def esta_vacia(self):
        return len(self.elementos) == 0

    def desencolar(self):
        return self.elementos.popleft() if not self.esta_vacia() else "La cola está vacía"
    
    def siguiente_cliente(self):
        return self.elementos[0] if not self.esta_vacia() else "La cola está vacía"
    
# 8) Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar
# los valores almacenados.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

lista = ListaEnlazada()
lista.insertar_inicio(10)
lista.insertar_inicio(20)
lista.insertar_inicio(30)

lista.mostrar()

# 9) Dada una lista enlazada, implementa una función para invertirla

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    def invertir(self):
        anterior = None
        actual = self.cabeza

        while actual:
            siguiente = actual.siguiente 
            actual.siguiente = anterior       
            anterior = actual                 
            actual = siguiente                
        self.cabeza = anterior      