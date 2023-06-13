# Función cargar lista
def cargaLista():
    return str(input("Ingrese el caracter: "))
# Función menú


def menu():
    print("Elija una opción: \n\r1. Para cargar un caracter. ")
    print("2. Para detenerse.")
    elec = int(input())

    return elec

# Inicio main


unaLista = ['']*100
contador = 0
print(unaLista)
parar = False
alfabeto = str('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXYZ')

# Carga de elementos
while not parar:
    if menu() == 1:
        unaLista[contador] = cargaLista()
        contador += 1
    else:
        parar = True

parar = False  # reset
contador = 0

# Imprime sólo letras
while not parar:
    if contador < len(unaLista) and unaLista[contador]:
        if unaLista[contador] in alfabeto:
            print(unaLista[contador])
            contador += 1
        else:
            contador += 1

# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA #