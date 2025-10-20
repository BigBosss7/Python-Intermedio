import csv  

with open("datos.csv") as archivo_csv:  

    reader = csv.reader(archivo_csv)
    for row in reader:
        print(row)