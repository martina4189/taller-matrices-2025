# ejecicio 1 Realice un algoritmo que almacene números en una matriz de 6 * 6. Imprimir la suma de los números almacenados en la matriz.


import random

# Paso 1: Crear una matriz de 6x6 y llenarla con números
filas = 6
columnas = 6
matriz = []

print("Matriz generada:")
for i in range(filas):  # Bucle para las filas
    fila = []  # Creamos una lista vacía para cada fila
    for j in range(columnas):  # Bucle para las columnas
        # Generamos un número aleatorio entre 1 y 10
        numero = random.randint(1, 10)
        fila.append(numero)  # Añadimos el número a la fila
    matriz.append(fila)  # Añadimos la fila completa a la matriz
    print(fila)  # Imprimimos la fila completa aquí

# Paso 2: Calcular la suma de los números en la matriz
suma_total = 0
for fila in matriz:  # Recorremos cada fila de la matriz
    for elemento in fila:  # Recorremos cada elemento de la fila
        suma_total += elemento  # Sumamos el elemento a la suma total

# Paso 3: Imprimir la suma total
print("\nLa suma de los números almacenados en la matriz es:", suma_total)