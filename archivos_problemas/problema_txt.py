# 2 listas con nombres otra con apellidos
nombres = ["Saul", "BigBoss", "Camila", "Ana", "Luis"]
apellidos = ["Barrera", "Demencial", "Dalto", "Gomez", "Martinez"]

#registrando en un archivo txt de forma optima
with open("archivos_problemas\\nombres_y_apellidos.txt", "w", encoding="utf-8") as arch:
    arch.writelines("los nombres y apellidos son:\n")
    [arch.writelines(f"{n} {a}\n" for n, a in zip(nombres, apellidos))]