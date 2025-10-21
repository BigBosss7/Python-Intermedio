import csv  

with open("datos.csv", encoding="utf-8", newline='') as archivo_csv:  

    reader = csv.reader(archivo_csv)
    for row in reader:
        print(row)