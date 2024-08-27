from functools import reduce
from datetime import datetime


"""
Ejercicio
"""
"""
# Función como argumento

def apply_func(func, x):
    return func(x)

print(apply_func(len,"OlianDev"))

# Retorno de función

def apply_multiplier(n):
    def multiplier(x):
        return n * x
    return multiplier

multiplier = apply_multiplier(2)
print(multiplier(5))
print(apply_multiplier(3)(2))

# Sistema

numbers = [1,3,4,2,5]

# map()

def apply_double(n):
    return n * 2

print(list(map(apply_double, numbers)))

#filter()

def is_even(n):
    return n  % 2 == 0

print(list(filter(is_even, numbers)))

#sorted()

print(sorted(numbers))
print(sorted(numbers, key= lambda x: -x))
print(sorted(numbers, reverse = True))

# reduce()

def sum (x, y):
    return x + y

print(reduce(sum, numbers))

"""

"""
Extra
"""

students = [
    {"name": "Angel" , "birthdate": "04-03-1997", "grades": [5, 8.5, 3, 10]},
    {"name": "Pepe" , "birthdate": "03-03-1999", "grades": [3, 2.5, 5, 1]},
    {"name": "Lola" , "birthdate": "01-08-1995", "grades": [5, 6.2, 1, 0]},
    {"name": "SuperLola" , "birthdate": "02-05-1997", "grades": [9.5, 9, 10, 9.25]},
]


def average(grades):
    return sum(grades) / len(grades)

# Promedio 
  
print(list(map(lambda student: {
    "name": student["name"], 
    "average": average(student["grades"])}, students)))

# Mejores

print(list(map(lambda student:
    student["name"], 
    filter(lambda student: average(student["grades"]) >= 9, students))))

# fecha de nacimiento

print(sorted(students, key= lambda student: datetime.strptime(
    student["birthdate"], "%d-%m-%Y"),reverse = True))

# calificacion mas alta

print(max(map(lambda student: max(student["grades"],students))))

      



