import random
# Paso 1: Crear una matriz de 5x5 y llenarla con números aleatorios únicos
filas = 5
columnas = 5
matriz = []

print("Matriz generada:")
numeros_usados = set()  # Conjunto para almacenar números ya usados y evitar repeticiones

for i in range(filas):
    fila = []
    for j in range(columnas):
        # Generar un número aleatorio único
        while True:
            numero = random.randint(1, 100)  # Generamos un número entre 1 y 100
            if numero not in numeros_usados:  # Verificamos que no esté repetido
                numeros_usados.add(numero)  # Agregamos el número al conjunto
                break
        fila.append(numero)
    matriz.append(fila)
    print(fila)  # Imprimimos la fila para visualizar la matriz

# Paso 2: Encontrar el número mayor y su posición
numero_mayor = matriz[0][0]  # Inicializamos con el primer elemento
posicion_mayor = (0, 0)      # Inicializamos la posición como (fila 0, columna 0)

for i in range(filas):
    for j in range(columnas):
        
        if matriz[i][j] > numero_mayor:
            numero_mayor = matriz[i][j]
            posicion_mayor = (i, j)  # Guardamos la posición (fila, columna)

# Paso 3: Imprimir los resultados
print("\nEl número mayor es:", numero_mayor)
print("Su posición [fila, columna] es:", posicion_mayor)