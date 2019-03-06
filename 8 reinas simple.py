from random import randrange, uniform, random

from funciones import llenarMatriz, mostrarMatriz, validMatriz

matriz = []# creo la matriz y defino el tamaño
for i in range(8):
    matriz.append([])
    for j in range(8):
        matriz[i].append(None)

matriz = llenarMatriz(matriz) # lleno la matriz con numeros aleatorios

i=0
while True:
    i=i+1
    print(i)
    if (validMatriz(matriz)):# si la matriz es valida la muestro y cierro el bucle
        print("Matriz completada en",i,"ciclos")
        mostrarMatriz(matriz)
        break
    else:
        matriz = llenarMatriz(matriz)

