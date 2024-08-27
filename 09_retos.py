"""
Herencia
"""

class Animal:

    def __init__(self, name: str):
        self.name = name

    def sonido(self):
        pass

# Subclases


class Perro(Animal):

    def sonido(self):
        print("Guau!")
 


class Gato(Animal):

      def sonido(self):
        print("Miau!")

def print_sonido(animal: Animal):
    animal.sonido()
 

my_animal = Animal("Animal")
print_sonido(my_animal)

my_animal = Perro("Lennon")
print_sonido(my_animal)

my_animal = Gato("Simba")
print_sonido(my_animal)

"""
Extra
"""

class Empleados:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.employees = []

    def add(self, empleados):
        self.employees.append(empleados)

    def print_empleados(self):
        for empleados in self.employees:
            print(empleados.name)

class Manager(Empleados):
    
    def coordinate_projects(self):
        print(f"{self.name} esta coordinando todos los proyectos de la empresa")

class ProjectManager(Empleados):

    
    def __init__(self, id: int, name: str, project: str):
        super().__init__(id,name)
        self.project = project
    
    
    def coordinate_project(self):
        print(f"{self.name} esta coordinando sus proyectos")


class Programmer(Empleados):

    def __init__(self, id: int, name: str, language: str):
        super().__init__(id,name)
        self.language = language
    
    def code(self):
        print(f"{self.name} está programando en {self.language}")

    def add(self, empleados):
        print("Un programdor no tiene empleados a su cargo")


my_manager = Manager(1, "OlianDev")
my_project_manager = ProjectManager(2, "Angel", "Proyecto 1")
my_project_manager2 = ProjectManager(2, "Pepe", "Proyecto 2")
my_programmer = Programmer(3, "Kontrol", "Phyton")
my_programmer2 = Programmer(4, "Nasos", "Rust")
my_programmer3 = Programmer(5, "Jenni", "Swift")

my_manager.add(my_project_manager)
my_manager.add(my_project_manager2)

my_project_manager.add(my_programmer)
my_project_manager2.add(my_programmer2)
my_project_manager2.add(my_programmer3)
my_programmer.add(my_programmer2)

my_project_manager.coordinate_project()
my_manager.coordinate_projects()
my_manager.print_empleados()
my_project_manager.print_empleados()
my_programmer.print_empleados()




