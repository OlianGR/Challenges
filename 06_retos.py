"""
Recursividad
"""

def countdown(number:int):
    if number >= 0:
        print(number)
        countdown(number - 1)

countdown(10)



"""
Extra
"""


def factorial(number:int) ->int:
    if number <0:
        return 0
    elif number == 0:
        return 1
    else:
        return number * factorial(number - 1)
        
    
print(factorial(5))




def fibonacci(number:int) -> int:
    if number<0 or number == 1:
        return 0
    elif number == 2:
        return 1 
    else:
        return fibonacci(number-1) + fibonacci(number-2)
    
position=2

valor = fibonacci(position)
print(f"El valor en la posicion {position} de la sucesion de fibonacci es: {valor}")





