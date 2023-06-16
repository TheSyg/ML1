import numpy as np
import matplotlib.pyplot as plt

# Prueba 1: lineal
# Sin subplots

x = np.arange(0, 10)
y = np.random.randint(1,10, size=10)

plt.plot(x,y, label='Gráfico de lineas')
plt.title('Test')
plt.ylabel('Y')
plt.xlabel('X')
plt.legend()
plt.grid()
plt.show()

# Prueba 2: barras

y2 = np.random.rand(10)

plt.bar(x,y2, label='Gráfico de barras')
plt.title('Test de barras')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.legend()
plt.grid(axis='y')
plt.show()

# Prueba 3: dispersión

datos = np.random.randint(1,10, size=(2,5))

#plt.scatter(datos[0,:], datos[1,:], label='Gráfico de dispersión')
plt.scatter(np.linspace(0,10,100), np.random.rand(100))
plt.title('Test')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.legend()
plt.grid()
plt.show()