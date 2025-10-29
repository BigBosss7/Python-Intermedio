class MiExcepcion(Exception):
    """Clase base para mis excepciones personalizadas."""
    def __init__(self, mensaje):
        print(f"Se ha producido un error personalizado: {mensaje}")
        

#Lanzando la excepción personalizada
#raise MiExcepcion("Este es un mensaje de error personalizado.")

try:
    raise MiExcepcion("Otro error personalizado.")  
except:
    print("Manejando la excepción personalizada.")  