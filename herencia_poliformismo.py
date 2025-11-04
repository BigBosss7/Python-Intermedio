"""
Ejercicio
"""
class Animal:
    def __init__(self,name:str):
        self.name = name

    def sound():
        pass

class dog(Animal):

    def sound(self):
        print("Guau!")

class Cat(Animal):
    
    def sound(self):
        print("Miau!")

my_animal= Animal("Animal")
my_dog= dog("Mike")
my_dog.sound()