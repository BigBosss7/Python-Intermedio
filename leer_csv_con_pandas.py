import pandas as pd 

#usando la funcion read_csv de pandas para leer un archivo csv
df = pd.read_csv("datos.csv",  encoding="utf-8")
df2 = pd.read_csv("datos.csv",  encoding="utf-8")

#obteniendo los datos de la columna 'nombre' y 'edad'
#nombres = df["nombre"]

#ordenando el dataframe por la columna 'edad'
#df_ordenado = df.sort_values("edad")

#ordenado de forma descendente
df_ordenado_desc = df.sort_values("edad", ascending=False)

#concatenndo los dos dataframes
df_concatenado = pd.concat([df, df2])

#accediendo a la  primer fila  conm head()
primera_fila = df.head(1)   

#accerdiendo a las ultimas 2 filas con tail()
ultimas_filas = df.tail(2)

#accediendo a la cantidad de filas y columnas con shape
filas_totales, columnas_totales = df.shape

#obteniendo estadisticas descriptivas del dataframe con describe()
estadisticas = df.describe()

#accediendo a un elemento especifico con loc (por etiqueta)
elemento_loc = df.loc[0, "nombre"]