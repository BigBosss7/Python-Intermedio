#cambiar tipo de datos de una columna al leer un csv con pandas

import pandas as pd
df = pd.read_csv("archivos_problemas\\datos.csv", encoding="utf-8")

# convertir a string la columna 'edad'  
df["edad"] = df["edad"].astype(str)


# mostrar el tipo de dato del primer elemento de la columna 'edad'
tipo_dato = type(df["edad"][0])
print(tipo_dato)

#remplzar los datos apellido 'demencial' por 'Lopez' en la columna 'apellido'
df["apellido"].replace("demencial", "Lopez", inplace=True)   

#mostrar el dataframe modificado
print(df["apellido"])

df = df.dropna() 
#print(df)# eliminar filas con valores NaN

#eliminando filas duplicadas
df = df.drop_duplicates()

#creando un dataframe nuevo con los datos modificados
df.to_csv("archivos_problemas\\datos_limpios.csv")