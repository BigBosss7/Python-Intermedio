
# creando una función que sume dos números ingresados por el usuario
def sumar_numeros():
    # bucle infinito hasta que se ingresen números válidos
    while True:
        # solicitando al usuario que ingrese dos números
        a = input("Ingrese el primer número: ")
        b = input("Ingrese el segundo número: ")
        # intentando convertir los valores ingresados a enteros y sumarlos
        try:
            resultado = int(a) + int(b)
        #si ocurre una excepción (error) durante la conversión o suma
        except ValueError as e:
            print("Te  he pedido números, no letras ni otros caracteres. Intenta de nuevo.")
            print(f"Detalle del error: {e}")
      
        # si no ocurre ninguna excepción, se rompe el bucle
        else:
            break
        finally:
            print("Gracias por usar la función de suma.")
    # mostrando el resultado de la suma
    return resultado

print(sumar_numeros())