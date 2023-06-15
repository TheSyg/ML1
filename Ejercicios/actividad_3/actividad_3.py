# ACTIVIDAD 3: LIBRERÍA PANDAS
# ADVERTENCIA: No borrar los comentarios que se encuentran en el código, ya que son necesarios para la evaluación de la actividad.
# ADVERTENCIA: No cambiar el nombre del archivo, de lo contrario no se considerará entregado.
# ADVERTENCIA: El programa debe ejecutarse una vez y realizar todos los puntos de manera secuencial. No se evaluarán programas que ejecuten solo una parte.
# ADVERTENCIA: El código de cada actividad debe escribirse debajo de cada comentario correspondiente.

import pandas as pd

## ACTIVIDADES ##
# Visite la documentación de Pandas para obtener más información sobre los métodos utilizados en esta actividad:
# https://pandas.pydata.org/pandas-docs/stable/reference/index.html

# 1. Leer el archivo CSV
# Utilizar el método read_csv() para leer el archivo "datos.csv" y almacenarlo en una variable llamada df.

df = pd.read_csv("datos.csv")

# 2. Mostrar los primeros 5 registros
# Utilizar el método head() para imprimir por consola los primeros 5 registros del DataFrame.

print(df.head())

# 3. Mostrar los últimos 5 registros
# Utilizar el método tail() para imprimir por consola los últimos 5 registros del DataFrame.

print(df.tail())

# 4. Mostrar la cantidad de filas y columnas
# Utilizar el atributo shape para imprimir por consola la cantidad de filas y columnas del DataFrame.

print(df.shape)

# 5. Mostrar la descripción estadística
# Utilizar el método describe() para imprimir por consola la descripción estadística del DataFrame.

print(df.describe())

# 6. Filtrar los registros donde la columna "Producto" sea igual a "Naranja"
# Utilizar el método loc() para obtener los registros donde la columna "Producto" sea igual a "Naranja" y almacenarlos en una variable llamada naranjas.
# Imprimir por consola los registros obtenidos.

naranjas = df.loc[df["Producto"] == "Naranja"]
print(naranjas)

# 7. Filtrar los registros donde la columna "Precio" sea mayor a 10
# Utilizar el método loc() para obtener los registros donde la columna "Precio" sea mayor a 10 y almacenarlos en una variable llamada precios_altos.
# Imprimir por consola los registros obtenidos.

precios_altos = df.loc[df["Precio"] > 10]
print(precios_altos)

# 8. Filtrar los registros donde la columna "Cantidad" sea mayor a 10 y la columna "Precio" sea igual mayor a 10
# Utilizar el método loc() para obtener los registros donde la columna "Cantidad" sea mayor a 10 y la columna "Precio" sea igual mayor a 10 y almacenarlos en una variable llamada filtro_cantidad_precio.
# Imprimir por consola los registros obtenidos.

filtro_cantidad_precio = df.loc[(df["Cantidad"] > 10) & (df["Precio"] >= 10.00)]
print(filtro_cantidad_precio)

# 9. Eliminar la columna "Precio"
# Utilizar el método drop() para eliminar la columna "Precio" del DataFrame.
# Imprimir por consola el DataFrame resultante.

df = df.drop("Precio", axis=1)  # utilizo otro dataframe para verificar posteriormente si funcionó.
print(df)

# 10. Eliminar los registros donde se repita el valor de la columna "Producto"
# Utilizar el método drop_duplicates() para eliminar los registros donde se repita el valor de la columna "Producto" del DataFrame.
# Imprimir por consola el DataFrame resultante.

df = df.drop_duplicates(subset=["Producto"])
print(df)

# Visite la documentación de Pandas para obtener más información sobre el método drop_duplicates():
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html
