# Import

import matplotlib.pyplot as plt
import numpy as np
import math


# Funciones


def redondeo(lista, red):
    for a in lista:
        red.append(round(a))

    return red


def sumaRec(lista, contador):
    suma = 0
    if contador < len(lista):
        print("Vuelta número", (contador + 1), ".")
        suma += lista[contador] + sumaRec(lista, contador + 1)

    return suma


# Main

unaLista = np.linspace(0, 10, 20)
unaListaRed = [] * 20
redondeo(unaLista, unaListaRed)
print(unaListaRed)
print(sumaRec(unaListaRed, 0))
