"""
funciones definidas por el usuario
"""

# Simple 

def greet():
    print("Hola, Python!")
    
    
greet()

# con retorno de valor

def return_greet():
    return "Hola, Python con retorno!"

print(return_greet())   

# Con un argumento

def arg_greet(name):
    print(f"Hola, {name}!")
    
arg_greet("Juan")

# Con un argumentos

def args_greet(greet, name):
    print(f"{greet}, {name}!")
    
args_greet("Hi","Juan")
args_greet(name="Juan",greet="Hi")

# Con un argumento predeterminado 

def default_arg_greet(name="Python"):
    print(f"Hola, {name}!")
    
default_arg_greet("Juan")
default_arg_greet()

# con argumentos y retorno de valor

def ret_args_greet(greet, name):
    return f"{greet}, {name}!"

print(ret_args_greet("Bon jour","Juan"))

# Con retorno de varios valore 

def multi_ret_greet():
    return "Hola", "Python"

greet, name = multi_ret_greet()
print(greet)
print(name)# funciones con tipos de datos complejos

# Con un número variable de argumentos

def variable_args_greet(*names):
    for name in names:
        print(f"Hola, {name}!")
        
variable_args_greet("Juan","Ana","Luis",)        

# Con un número variable de argumentos con clave

def variable_kw_args_greet(**kwargs):
    for key, value in kwargs.items():
        print(f" {key}: {value}")
        
variable_kw_args_greet(Juan="Hola Juan", Ana="Hola Ana", Luis="Hola Luis")  

"""
Fuciones dentro de funciones
"""

def outer_function():
    def inner_function():
        print("Función interna: Hola desde la función interna!")
    inner_function()

outer_function()

"""
Funciones del lenguaje (built-in functions)
"""

print(len("Hola Python"))  
print(type("Me gusta Python"))
print("Hola Python".upper())

"""
Variables locales y globales
"""

global_var = "Soy una variable global"



def hello_python():
    local_var = "Soy una variable local"
    print(f"{local_var}: {global_var}")


print(global_var)
# print(local_var)  # Esto generará un error porque local_var no está definida en este ámbito
hello_python()

"""
Extra
"""

def print_numbers(text1, text2) -> int:
    count = 0
    for number in range(1, 101):
    
        if number % 3 == 0 and number % 5 == 0:
            print(f"{text1}{text2}")
        elif number % 3 == 0:
            print(f"{text1}")
        elif number % 5 == 0:
            print(f"{text2}")
        else:
            print(number)    
            count += 1
    return count

        
print(print_numbers("Fizz", "Buzz"))