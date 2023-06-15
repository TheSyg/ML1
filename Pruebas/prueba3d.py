import matplotlib.pyplot as plt
import numpy as np

# usando subplots

x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.scatter(x,y,z, label="Gráfico")
ax.set_title("Prueba de gráfico de dispersión")
ax.set_ylabel("Eje y")
ax.set_xlabel("Eje x")
ax.grid()
ax.legend(title="Leyenda")
plt.show()