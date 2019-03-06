from random import randrange, uniform, random

def validMatriz(matriz): # Verifica si la matris es valida
    count = 0
    limite = 7
    for i in range(8):
        aux = 0
        aux2 = 0
        aux3 = 0
        aux4 = 0
        aux5 = 0
        aux6 = 0
        for j in range(8):
            if matriz[i][j] == 1: # Compruebo Filas
                aux += 1

            if matriz[j][i] == 1: # Compruebo Columnas
                aux2 += 1

            if(j <= limite):
                if(matriz[j][j+count] == 1): # Diagonales superiores principales
                    aux3 += 1

                if(matriz[j+count][j] == 1): # Diagonales inferiores principales
                    aux4 += 1

            if(i >= j):
                if(matriz[j][i - j] == 1): # Diagonales superiores secundarias
                    aux5 += 1

            if(i+j <= 7):
                if(matriz[(7-j)][i + j] == 1): # Diagonales inferiores secundarias
                    aux6 += 1

        limite -= 1
        count += 1

        if(aux > 1) or (aux2 > 1) or (aux3 > 1) or (aux4 > 1) or (aux5 > 1) or (aux6 > 1):
            return False

    return True

def mostrarMatriz(matriz): # muestra la matriz de forma ordenada
    string=''
    for i in range(8):
        for j in range(8):
            string=string + str(matriz[i][j]) + ' '
        string= string + '\n'
    print(string)

def llenarMatriz(matriz):# llena la matriz de forma aleatoria
    for i in range(8):
        for j in range(8):
            matriz[i][j]=0
    for i in range(8):
        rand = int(uniform(0,8))
        matriz[i][rand]= 1
    return matriz

def cantCeldasVacias(matriz):
    suma=0
    for i in range(0,8):
        for j in range(0,8):
            if (matriz[i][j]==0):
                suma +=1
    return suma


def cantCeldasAtacadas(matriz):# Cuento la cantidad de lugares atacadas en la ultima fila
    suma=0
    ultimafila=0
    for i in range(0,8):
        for j in range(0,8):
            if (matriz[i][j]==1):
                ultimafila=i

    for j in range(0,8):
        if (matriz[ultimafila][j]==2):            
            suma +=1
    return suma


def llenarCeldaOcupadas(matriz):# Para llenar en que lugares no se puede colocar reinas
    suma=0
    for i in range(8):
        for j in range(8):
            if matriz[i][j] == 1: # Compruebo Filas
                col=j
                fil=i
    
    for i in range(0,8):
        if (i!=fil):
            for j in range(0,8):
                if (j!=col):
                    if(j!=col-i+fil):
                        if (j!=col+i-fil):
                            suma += 1
                        else:
                            matriz[i][j]=2
                    else:
                        matriz[i][j]=2
                else:
                    matriz[i][j]=2
        else:
            for j in range(0,8):
                matriz[i][j]=2     

        matriz[fil][col]=1             

    return matriz