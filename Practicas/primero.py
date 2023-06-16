# Importa librerias
import matplotlib.pyplot as plt
import numpy as np

# Defino x e y
x = np.linspace(0, 10, 100)
y = 2 * np.sin(x) + 1
# Creo el grafico
plt.plot(x, y)
# Titulo y nombres
plt.title("Funcion y = 2x")
plt.xlabel("x")
plt.ylabel("y")
# Muestra
plt.show()

# Separador

# Define función
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
# Crea pares ordenados
fig, ax = plt.subplots()
# Grafica
ax.plot(x, y1, color="red", label="Seno")
ax.plot(x, y2, color="purple", label="Coseno")
# Titulo y nombres
ax.legend()
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Gráfico 2")
# Muestra gráfico
plt.show()
