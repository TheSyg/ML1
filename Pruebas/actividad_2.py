import numpy as np
import matplotlib.pyplot as plt

# ACTIVIDAD 2: LIBRERÍAS NUMPY Y MATPLOTLIB
# **ADVERTENCIA**: No borrar los comentarios que se encuentran en el código, ya que son necesarios para la evaluación de la actividad.
# **ADVERTENCIA**: No cambiar el nombre del archivo, de lo contrario no se considerará entregado.
# **ADVERTENCIA**: El programa debe ejecutarse una vez y realizar todos los puntos de manera secuencial. No se evaluarán programas que ejecuten solo una parte.
# **ADVERTENCIA**: El código de cada actividad debe escribirse debajo de cada comentario correspondiente.

## ACTIVIDADES CON NUMPY ##
# Visite la documentación de Numpy para obtener más información sobre los métodos utilizados en esta actividad:
# https://numpy.org/doc/stable/reference/index.html

# 1. Crear un array y obtener información sobre su forma y tamaño:
# Enunciado: Crea un array de 2 dimensiones utilizando el método np.array() con los siguientes
#   elementos: [1, 2, 3] y [4, 5, 6]. Luego, utiliza los métodos shape y size para obtener la
#   forma y el tamaño del array, respectivamente. Imprime la forma y el tamaño por consola.

# 2. Realizar operaciones matemáticas con un array:
# Enunciado: Crea un array utilizando el método np.array() con los siguientes elementos: [1, 2, 3, 4, 5].
#   a) Utiliza la función np.square() para calcular el cuadrado de cada elemento del array. Imprime el resultado por consola.
#   b) Utiliza la función np.sqrt() para calcular la raíz cuadrada de cada elemento del array. Imprime el resultado por consola.
#   c) Utiliza la función np.sin() para calcular el seno de cada elemento del array. Imprime el resultado por consola.
#   d) Utiliza la función np.cos() para calcular el coseno de cada elemento del array. Imprime el resultado por consola.
#   e) Utiliza la función np.tan() para calcular la tangente de cada elemento del array. Imprime el resultado por consola.

# 3. Realizar operaciones matemáticas con dos arrays:
# Enunciado: Crea dos arrays utilizando el método np.array() con los siguientes elementos: [1, 2, 3, 4, 5] y [6, 7, 8, 9, 10].
#   a) Utiliza la función np.add() para sumar los elementos de ambos arrays. Imprime el resultado por consola.
#   b) Utiliza la función np.subtract() para restar los elementos de ambos arrays. Imprime el resultado por consola.
#   c) Utiliza la función np.multiply() para multiplicar los elementos de ambos arrays. Imprime el resultado por consola.
#   d) Utiliza la función np.divide() para dividir los elementos de ambos arrays. Imprime el resultado por consola.
#   e) Utiliza la función np.power() para elevar los elementos del primer array a los elementos del segundo array. Imprime el resultado por consola.

# 4. Manipular los elementos de un array:
# Enunciado: Crea un array utilizando el método np.array() con los siguientes elementos: [1, 2, 3, 4, 5].
#   a) Utiliza el método np.reshape() para cambiar la forma del array a (5, 1). Imprime el resultado por consola.
#   b) Utiliza el método np.ravel() para cambiar la forma del array a (1, 5). Imprime el resultado por consola.
#   c) Utiliza el método np.transpose() para cambiar la forma del array a (5, 1). Imprime el resultado por consola.
#   d) Utiliza el método np.resize() para cambiar la forma del array a (3, 3). Imprime el resultado por consola.
#   e) Utiliza el método np.append() para agregar el elemento 6 al array. Imprime el resultado por consola.


## ACTIVIDADES CON MATPLOTLIB ##
# Visite la documentación de Matplotlib para obtener más información sobre los métodos utilizados en esta actividad:
# https://matplotlib.org/stable/api/index.html

# 1. Crear un gráfico de líneas:
# Enunciado: Crea un array utilizando el método np.array() con los siguientes elementos: [1, 2, 3, 4, 5].
#   a) Crea un gráfico de líneas utilizando el método plt.plot().
#   b) Utiliza el método plt.title() para agregar el título "Gráfico de líneas".
#   c) Utiliza el método plt.xlabel() para agregar la etiqueta del eje x "Eje x".
#   d) Utiliza el método plt.ylabel() para agregar la etiqueta del eje y "Eje y".
#   e) Utiliza el método plt.show() para mostrar el gráfico.

unArr = np.array([1, 2, 3, 4, 5])
plt.plot(unArr)
plt.title("Gráfico de líneas")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.show()

# 2. Crear un gráfico de barras:
# Enunciado: Crea un array utilizando el método np.array() con los siguientes elementos: [1, 2, 3, 4, 5].
#   a) Crea un gráfico de barras utilizando el método plt.bar().
#   b) Utiliza el método plt.title() para agregar el título "Gráfico de barras".
#   c) Utiliza el método plt.xlabel() para agregar la etiqueta del eje x "Eje x".
#   d) Utiliza el método plt.ylabel() para agregar la etiqueta del eje y "Eje y".
#   e) Utiliza el método plt.show() para mostrar el gráfico.

plt.bar(unArr, unArr)
plt.title("Gráfico de barras")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.show()

# 3. Crear un gráfico de dispersión con un array de dos dimensiones:
# Enunciado: Crea un array utilizando el método np.array() con los siguientes elementos: [[1, 2], [3, 4], [5, 6]].
#   a) Crea un gráfico de dispersión utilizando el método plt.scatter().
#   b) Utiliza el método plt.title() para agregar el título "Gráfico de dispersión 2D".
#   c) Utiliza el método plt.xlabel() para agregar la etiqueta del eje x "Eje x".
#   d) Utiliza el método plt.ylabel() para agregar la etiqueta del eje y "Eje y".
#   e) Utiliza el método plt.show() para mostrar el gráfico.

otroArr = np.array([[1, 2], [3, 4], [5, 6]])
plt.scatter(otroArr[:, 0], otroArr[:, 1])
plt.title("Gráfico de dispersión 2D")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.show()

# 4. Crear un gráfico de dispersión con un array de tres dimensiones:
# Enunciado: Crea un array utilizando el método np.array() con los siguientes elementos: [[1, 2, 3], [4, 5, 6]].
#   a) Crea un gráfico de dispersión utilizando el método plt.scatter().
#   b) Utiliza el método plt.title() para agregar el título "Gráfico de dispersión 3D".
#   c) Utiliza el método plt.xlabel() para agregar la etiqueta del eje x "Eje x".
#   d) Utiliza el método plt.ylabel() para agregar la etiqueta del eje y "Eje y".
#   e) Utiliza el método plt.show() para mostrar el gráfico.

unaMat = np.array([[1, 2, 3], [4, 5, 6]])
plt.scatter(unaMat[0, :], unaMat[1, :])
plt.title("Gráfico de dispersión 3D")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.show()

# 5. Crear un gráfico de barras con dos arrays:
# Enunciado: Crea dos arrays utilizando el método np.array() con los siguientes elementos: [1, 2, 3, 4, 5] y [6, 7, 8, 9, 10].
#   a) Crea un gráfico de barras utilizando el método plt.bar().
#   b) Utiliza el método plt.title() para agregar el título "Gráfico de barras".
#   c) Utiliza el método plt.xlabel() para agregar la etiqueta del eje x "Eje x".
#   d) Utiliza el método plt.ylabel() para agregar la etiqueta del eje y "Eje y".
#   f) Utiliza el método plt.legend() para agregar la leyenda "Leyenda".
#   g) Utiliza el método plt.xticks() para agregar las etiquetas del eje x "Eje x".
#   h) Utiliza el método plt.yticks() para agregar las etiquetas del eje y "Eje y".
#   i) Utiliza el método plt.grid() para agregar la grilla al gráfico.
#   j) Utiliza el método plt.show() para mostrar el gráfico.

arrDos = np.array([6, 7, 8, 9, 10])
plt.bar(unArr, arrDos, label='Grafico de barras')
plt.title("Gráfico de barras")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.ylim(5, 11)
plt.legend()
plt.xticks(unArr, labels=unArr)
plt.yticks(arrDos, labels=arrDos)
plt.grid(axis="y")
plt.show()
