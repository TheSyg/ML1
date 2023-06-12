import sys
import datetime
import math

# 1
print(
    " Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky."
)
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!")

# 2
print("Version:", sys.version, "\nVersion info:", sys.version_info)

# 3
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))


# 4
"""
def areaCirculo(radio):
    return math.pi * math.pow(radio, 2)


rad = float(input("Ingrese un radio\n"))
area = areaCirculo(rad)
print(area)

# 5
nom = str(input("¿Cuál es su nombre?\n"))
apel = str(input("¿Cuál es su apellido?\n"))

print(apel, nom)"""

# 6
valores = input("Ingrese números separados por comas\n")
unaLista = valores.split(",")
unaTupla = tuple(unaLista)
print(unaLista, "\n", unaTupla)
