"""
Ejercicio 1: Definición de Clases y Objetos en Python
----------------------------------------------------------------
""" 

class Programmer:

    surname:str = None

    def __init__(self, name:str, age:int, language:list):
        self.name = name
        self.age = age
        self.language = language
    
    def print(self):
        print(f"Nombre: {self.name}| surname:{self.surname} | Edad: {self.age} | Lenguajes: {self.language}")

my_programmer = Programmer("Ana", 28, ["Python", "JavaScript", "C++"])
my_programmer.print()
my_programmer.surname = "Gomez"
my_programmer.print()
my_programmer.age = 37
my_programmer.print()

"""
ExTRa
"""

class Stack:

    def __init__(self):
        self.stack = []  

    def push(self, item):
        self.stack.append(item) # Agrega un elemento al final de la lista

    def pop(self):
        if self.count() == 0:
            return None
        return self.stack.pop() # Elimina y devuelve el último elemento de la lista
    
    def count(self):
        return len(self.stack)
    
    def print(self):
        for item in self.stack: # Itera sobre los elementos de la lista
            print(item)

my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
print(my_stack.count())  # Salida: 3
my_stack.print()        # Salida: A B C
my_stack.pop()         # Elimina C
print(my_stack.count())  # Salida: 2
print(my_stack.pop())         # Salida: B
print(my_stack.pop())         # Salida: A

class Queue:

    def __init__(self):
        self.queue = []  # Inicializa una lista vacía para la cola

    def enqueue(self, item):
        self.queue.append(item)  # Agrega un elemento al final de la lista

    def dequeue(self):
        if self.count() == 0:
            return None
        return self.queue.pop(0)  # Elimina y devuelve el primer elemento de la lista
    
    def count(self):
        return len(self.queue)
    
    def print(self):
        for item in self.queue:  # Itera sobre los elementos de la lista
            print(item)

my_queue = Queue()
my_queue.enqueue("A")
my_queue.enqueue("B")
my_queue.enqueue("C")
print(my_queue.count())  # Salida: 3
my_queue.print()        # Salida: A B C
my_queue.dequeue()      # Elimina A
print(my_queue.count())  # Salida: 2
print(my_queue.dequeue())      # Salida: B
print(my_queue.dequeue())      # Salida: C
print(my_queue.dequeue())      # Salida: None
print(my_queue.dequeue())      # Salida: None
print(my_queue.count())      # Salida: None
