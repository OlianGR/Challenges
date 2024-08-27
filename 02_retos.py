""""
Funciones básicas

"""

#Funcion Simple

def my_function ():
    print("Esto es una funcion")

my_function()

#Función con parámetros

def arg_greet(name):
    print(f"Hola, {name}")

arg_greet("Brais")

def args_greet(name, surname):
    print(f"Hola, {name} {surname}")

args_greet("Brais" , "Garcia")
args_greet(surname ="Garcia", name="Brais")

def default_arg_greet(name = "Python"):
    print(f"Hola, {name}")

default_arg_greet("Angel")
default_arg_greet()



#Función con retorno
def return_greet():
    return "Hola, Python"

greet = return_greet()
print (greet)

# Funciones con parametros y retorno

def return_args_greet(greet, name):
    return "{greet}, {name}"

print(return_args_greet("Hi" , "Brais"))

# Funcion con retorno de varios valores

def multiple_return_greet():
    return "Hola", "Python" # Dos variables separadas por comas 

greet, name = multiple_return_greet()
print(greet)
print(name)

# Funciones con un numero variable de parametros

def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}")

variable_arg_greet("python" , "Angel" , "Brais", "Comunidad")


def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())
print_upper_texts("angel","pepe")

#  Con un numero variable de paramatros con palabra clave

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})")

variable_key_arg_greet(
    language = "Python" ,
    name = "Angel", 
    alias = "OlianDev",
    age = 26)

"""
Funciones dentro de funciones
"""

def outer_function():
    def inner_function():
        print("Funcion interna: Hola, Python")
    inner_function()


outer_function()

"""
Funciones del lenguaje(built.in)
"""

print(len("OlianDev")) 
print(type(26)) 
print(("OlianDev".upper())) 


"""
Variables locales y globales
"""

variable_global = "Phyton" # Se declara fuera de la función

print(variable_global)

def ejemplo_global():
    print(variable_global)

ejemplo_global()


def ejemplo_local():
    variable_local = "Esto es una variable local" #SOlo se puede acceder mediante la funcion cuando la funcion termina no hay variable
    print(variable_local)
ejemplo_local()
# print(variable_local) Genera un error por esta definida dentro de la función

"""
Ejercicio extra
"""

def funcion_cadena(text1, text2)-> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print (text1 + text2)
        elif number % 3 == 0:
            print(text1)
        elif number % 5 == 0:
            print(text2)
        else:
            print(number)
            count += 1
    return count

print(funcion_cadena("Fizz", "Buzz"))






