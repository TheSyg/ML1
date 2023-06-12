# ACTIVIDAD 1: EJERCICIOS DE PROGRAMACIÓN BÁSICA EN PYTHON
# **ADVERTENCIA**: No borrar los comentarios que se encuentran en el código, ya que son necesarios para la evaluación de la actividad.
# **ADVERTENCIA**: No cambiar el nombre del archivo, de lo contrario no se considerará entregado.
# **ADVERTENCIA**: El programa debe ejecutarse una vez y realizar todos los puntos de manera secuencial. No se evaluarán programas que ejecuten solo una parte.
# **ADVERTENCIA**: El código de cada actividad debe escribirse debajo de cada comentario correspondiente.

## ACTIVIDADES
# 1. Imprimir "¡Hola, mundo!" en la consola usando print().

print("¡Hola, mundo!")
# 2. Pedir al usuario que ingrese su nombre usando input() e imprimir un saludo en consola usando print().

nombreUsuario = str(input("Ingrese su nombre: "))
print("Buenas tardes, señor/a ", nombreUsuario)
# 3. Sumar dos números ingresados por el usuario mediante input() y luego mostrar el resultado en consola usando print().

print("Ingrese un número entero: ")
unEntero = int(input())
print("Ingrese un segundo entero: ")
otroEntero = int(input())
laSuma = unEntero + otroEntero
print(laSuma)
# 4. Calcular el área de un triángulo a partir de la base y la altura ingresadas por el usuario mediante input() y luego mostrar el resultado en consola.

# Función que retorna true si el argumento es un entero mayor a cero.
def verificaDimension(unaDimension):  
    aux = False
    if unaDimension > 1:
        aux = True
    return aux

# Separador
detenerse = False
altura = 0
base = 0
# Separador

print("Ingrese la base del triangulo: ")
while detenerse == False:
    base = int(input())
    if verificaDimension(base) == True:
        detenerse = True
    else:
        print("Dimensión inválida. Debe ser mayor a cero.")

detenerse = False # Resetea

print("Ingrese la base del triángulo: ")
while detenerse == False:
    altura = int(input())
    if verificaDimension(altura) == True:
        detenerse = True
    else:
        print("Dimensión inválida. Debe ser mayor a cero.")

area = (base * altura) / 2
print("El área del triangulo es: ", area)
# 5. Calcular el promedio de tres números ingresados por el usuario mediante input() y luego mostrar el resultado en consola.

print("Ingrese un numero: ")
numeroUno = int(input())
print("Ingrese un segundo número: ")
numeroDos = int(input())
print("Ingrese un tercer número: ")
numeroTres = int(input())

promedioDeTres = (numeroUno + numeroDos + numeroTres) / 3
print(promedioDeTres)
# 6. Crear una lista con los siguientes números enteros: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] y mostrar por pantalla el resultado de sumar todos los números de la lista.

unaLista = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
listaSumada = (
    unaLista[0]
    + unaLista[1]
    + unaLista[2]
    + unaLista[3]
    + unaLista[4]
    + unaLista[5]
    + unaLista[6]
    + unaLista[7]
    + unaLista[8]
    + unaLista[9]
)
print("La suma de la lista", unaLista, " es ", listaSumada)
# 7. Crear una función que reciba un número entero como parámetro y retorne el resultado de multiplicarlo por 2. Imprimir el resultado de invocarla pasándole como argumento un 5.


def doblaNumero(unNum):
    return unNum * 2


print("El número ingresado multiplicado por dos es: ", doblaNumero(5))  ## Imprime 10

# 8. Crear una función que reciba una cadena de texto como parámetro y retorne la cantidad de caracteres que tiene.


def cuentaCaracteres(unStr):
    return len(unStr)


elStr = "Esto es una cadena."

print("La cantidad de caracteres en la cadena ", elStr, " es : ", cuentaCaracteres(elStr))
# 9. Crear una función que reciba una lista de números enteros como parámetro y retorne el número más grande de la lista.

otraLista = [1, 3, 6, 2, 4, 6]


def buscaMayorEntero(listaEnteros):
    aux = listaEnteros[0]  ## Guarda temporalmente el valor más alto hasta el momento
    for x in range(0, len(listaEnteros)):
        if listaEnteros[x] > aux:
            ## Entra si un valor de la lista fue más grande que el auxiliar
            aux = listaEnteros[x]
    return aux


print("El numero más grande de la lista ", otraLista, " es ", buscaMayorEntero(otraLista))  ## Imprime 6
# 10. Crear una función que reciba una lista de cadenas de texto como parámetro y retorne la cantidad de cadenas que tienen más de 5 caracteres.

listaCadenas = ["unElemento", "otroElemento", "dos", "uno", "ultimoElemento"]


def cadenasConCincoChar(listaString):
    aux = 0
    for a in range(0, len(listaString)):
        if len(str(listaString[a])) > 5:
            aux += 1

    return aux


print(cadenasConCincoChar(listaCadenas))  ## Retorna 3
