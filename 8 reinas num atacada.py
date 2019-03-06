from random import randrange, uniform, random
import copy

from funciones import validMatriz, mostrarMatriz, llenarCeldaOcupadas, cantCeldasAtacadas


matriz = []#creo una matriz principal
for i in range(8):
    matriz.append([])
    for j in range(8):
        matriz[i].append(None)

tempMatriz = []# creo una matriz temporal
for i in range(8):
    tempMatriz.append([])
    for j in range(8):
        tempMatriz[i].append(None)

ciclo=0
while True:
    for i in range(8):
            for j in range(8):
                matriz[i][j]=0# limpio la matriz colocando todos los valores en cero
    

    rand = int(uniform(1,7))
    matriz[0][rand]=1# coloco una reina en una pocicon aleatoria de la primer fila meno en las esquinas

    matriz= llenarCeldaOcupadas(matriz)
    mostrarMatriz(matriz)
    j=0


    cantMin=0
    valorJ=0
    nvacias=1

    for i in range(1,8):
        tempMatriz = copy.deepcopy(matriz)#copio en la matriz temporal los datos de la matiz principal
        cantMin=8
        valorJ=[]
        nvacias=1

        for j in range(0,8): #recorro toda la fila
            if (matriz[i][j]==0):# veo cuales son los lugares vacios
                tempMatriz[i][j]=1
                if (cantMin >= cantCeldasAtacadas(llenarCeldaOcupadas(tempMatriz))):#cuento la cantidad
                    if (cantMin > cantCeldasAtacadas(llenarCeldaOcupadas(tempMatriz))):# guardo en la lista las posiciones que con la que se obtine la menor cantidad de celdas ocupadas
                        valorJ=[]
                        valorJ.append(j)
                    else:
                        valorJ.append(j)
                    cantMin=cantCeldasAtacadas(llenarCeldaOcupadas(tempMatriz))# guardo la cantidad cantidad de posiciones ocupadas
                    nvacias=0

        if (nvacias==0):# veo si hay lugares vacios
            matriz[i][valorJ[int(uniform(0,valorJ.__len__()))]]=1 #coloco la reina en un lugar aleatorio
            matriz=llenarCeldaOcupadas(matriz)#indico cuales son los lugares donde no puedo colocar reinas
        else:
            print("No queda ningun lugar vacio")
            mostrarMatriz(tempMatriz)
            break

        tempMatriz = copy.deepcopy(matriz)

    suma=0

    


    for f in range(8):#cuento que esten las 8 reinas
                for c in range(8):
                    if (matriz[f][c]==1):
                        suma +=1
    if (suma==8):# Si estan las 8 reinas 
        if (validMatriz(matriz)):#compruebo que la matriz sea valida
            print("matriz validada")
            print("ciclo:",ciclo)
            break #si la matiz es valida salgo del bucle

    ciclo += 1
    print("ciclo",ciclo)

for i in range(0,8):# saco todos los 2 de la matriz
        for j in range(0,8):
            if matriz[i][j]==2:
                matriz[i][j]=0        
mostrarMatriz(matriz)  





