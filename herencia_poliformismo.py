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

def print_sound(animal : Animal):
    Animal.sound()

my_animal= Animal("Animal")
print_sound(my_animal)
my_dog= dog("Mike")
#print_sound(my_dog)
#my_dog.sound()

"""
Extra
"""

class Employee:

    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name 
        self.employees = []

    def add(self,  employee):
        self.employees.append(employee)

    def print_employess(self):
        for employee in self.employees:
             print (employee.name)


class Manager(Employee):

    def coordinate_projects(self):
        print(f"{self.name} está coordinando todos los proyectos de la empresa")

class ProjectManager(Employee):
     
     def __init__(self, id:int, name:str, project:str):
         super().__init__(id, name)
         self.project = project

     def coordinate_project(self):
        print(f"{self.name} está coordinando su proyecto")


class Programmer(Employee):

    def __init__(self, id:int, name:str, language:str):
        super().__init__(id, name)
        self.laguage = language

    def code(self):
        print(f"{self.name} está progrmando en {self.laguage}")

    def add(self, employee):
        print(f"Un programador no tiene empleados a su cargo. {employee.name} no se añadirá.")

my_manager = Manager(1, "Mouredev")
my_project_manager = ProjectManager (2, "Bigboss", "Projecto1")
my_project_manager2 = ProjectManager (3, "Moure", "Projecto2")
my_programer = Programmer (4, "Kontrol", "Swift")
my_programer2 = Programmer (5, "Ros", "Cobol")
my_programer3 = Programmer (6, "Bushi", "Dart")
my_programer4 = Programmer (7, "Nasos", "Python")

my_manager.add(my_project_manager)
my_manager.add(my_project_manager2)

my_project_manager.add(my_programer)
my_project_manager.add(my_programer2)
my_project_manager2.add(my_programer3)
my_project_manager2.add(my_programer4)

my_programer.add(my_programer2)

my_programer.code()
my_project_manager.coordinate_project()
my_manager.coordinate_projects()
my_manager.print_employess()
my_project_manager.print_employess()