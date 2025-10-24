"""
valor y referencia
"""

# Tipos de datos por referencia

my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30)    
print(my_list_a)
print(my_list_b)  

# Funciones con datos por valor 

my_int_c = 10 

def my_int_func(my_int: int):
    my_int = 20 
    print(my_int)
    
my_int_func(my_int_c)
print(my_int_c)

# Funciones con datos por referencia    

def my_list_func(my_list: list):
    my_list.append(30)
    print(my_list)
    
    my_list_d = my_list
    my_list_d.append(40)
    
    print(my_list)
    print(my_list_d)

my_list_c = [10,20]
my_list_func(my_list_c)
print(my_list_c)  

"""
Extra
"""

# Por referencia 
def ref(value_a: list, value_b: list)-> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp 
    return value_a, value_b

my_list_e = [10, 20]
my_list_f = [30, 40]
my_list_g, my_list_h = ref(my_list_e, my_list_f)
print(f"{my_list_e}, {my_list_f}")
print(f"{my_list_g},{my_list_h}")