import random 
#Realice un algoritmo que llene una matriz de 10 * 10. Sumar las columnas e imprimir que columna tuvo la máxima suma y la suma de esa columna.

filas= 10
columnas = 10
matriz = []

print ("matriz generada")
for i in range (filas):
    fila =[]
    for j in range (columnas):
        numero = random.randint(1,50)
        fila.append(numero)
        
    matriz.append(fila)
    print(fila)    
        
# calcular la suma de cada columna 
suma_columnas = [0]*columnas
for fila in matriz :
    for j in range (columnas):
        suma_columnas [j] += fila [j]
        
        
# encontrar la columna con la maxima suma 
max_suma= max(suma_columnas)
columna_maxima = suma_columnas.index(max_suma)
 
 # imprimir los resultados 
print (" la suma de cada columna es : ", suma_columnas)
print ("la columna con la maxima suma es:", {columna_maxima})
print ("la suma de esa columna es : ",{max_suma} )