# funciones

def desapFilas(mat, fil, col):
    suma = 0
    if col < len(mat[fil]):
        suma += mat[fil][col] + desapFilas(mat, fil, col + 1)

    return suma


def suMatRec(mat, fil, arr):
    if fil < len(mat): # CB
        arr[fil] += desapFilas(mat, fil, 0)
        suMatRec(mat, fil + 1, arr) # PR


# main

matriz = [[3, 1, 2], [0, 3, 2], [5, 1, 0]]
arreglo = [0] * len(matriz)
suMatRec(matriz, 0, arreglo)
print(arreglo)
