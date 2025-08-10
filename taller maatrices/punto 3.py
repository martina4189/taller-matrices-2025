
#3.Realice un algoritmo que llene una matriz de 5 * 5. Calcular la suma de cada fila y almacenarla en un vector, la suma de cada columna y almacenarla en otro vector.
import random 

filas= 5
columnas = 5
matriz = []

print ( "matriz generada ")

for i in range (filas):
    fila=[]
    for j in range (columnas):
       numero= random.randint (1,100) 
       fila.append(numero)
    matriz.append(fila)
    print (fila)
    
# calcular la suma de cada fila
suma_filas = []
for fila in matriz :
   suma_fila = sum(fila)
   suma_filas.append (suma_fila)
   
   #calcular la suma de las columnas 
   suma_columnas = [0]*columnas
   for fila in matriz:
       for j in range (columnas):
           suma_columnas [j]+= fila [j]
           suma_columnas[j]+=fila[j]
           
# imprimir los resultados 
print ("\n la suma de las filas es :", suma_filas)
print ("la suma de las columnas es :", suma_columnas)
