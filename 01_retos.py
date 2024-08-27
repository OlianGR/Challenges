"""
Operadores 

"""
##Operadores Aritmeticos
print(f"Suma: 10 + 3 = {10 + 3}") ##Con la f primero ponemos el print y luego añadimos el codigo de suma con las llaves
print(f"Resta: 10 - 3 = {10 - 3}") 
print(f"Multiplicacion: 10 * 3 = {10 * 3}") 
print(f"Division: 10 / 3 = {10 / 3}") 
print(f"Módulo: 10 % 3 = {10 % 3}") 
print(f"Exponente: 10 ** 3 = {10 ** 3}") 
print(f"Division entera: 10 // 3 = {10 // 3}") 

##Operadores de comparación
print(f"Igualdad: 10 == 3 es {10 == 3}")
print(f"Desigualdad: 10 != 3 es {10 != 3}")
print(f"Mayor que: 10 > 3 es {10 > 3}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 >= 10 es {10 >= 10}")
print(f"Menor o igual que: 10 <= 3 es {10 <= 3}")

##Operadores lógicos
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}")
print(f"NOT !: 10 + 3 == 14 es {not 10 + 3 == 14 }")

##Operadores de asignación
my_number = 11 #asignación
print(my_number)
my_number += 1 # suma y asigna
print(my_number)
my_number -= 1 # resta y asigna
print(my_number)
my_number *= 1 # multiplica y asigna
print(my_number)
my_number /=2  # divide y asigna etc etc
print(my_number) 

# Operadores de identidad 
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is my_new_number es {my_number is not my_new_number}")

#Operadores de pertenencia 
print(f"'u' in 'moure' = { 'u' in 'moure'} ")
print(f"'b' not in 'moure' = { 'b' not in 'moure'} ")

#Operadores de bit 

a = 10 # 1010
b = 3 # 0011
print(f"AND: 10 & 3 = {10 & 3}") # 0010
print(f"OR: 10 | 3 = {10 | 3}") # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001

"""
Estructuras de control
"""

## Condicionales

my_string = "OlianDev"

if my_string == "OlianDev":
    print("my_string es 'OlianDev'") 
elif my_string == "Angel":
    print("my_string es 'Angel'")
else:
    print("my_string no es 'OlianDev' ni 'Angel'")

## Iterativas
my_int = 0
 
while my_int >=2 and my_int<10:
    my_int +=1
    if my_int <6:
        print("Es menor que 6")
        my_int +=2
    elif my_int ==4:
        print ("Error continua")
    
    else:
        my_int +=2
        print("Es mayor que 6")

print("La ejecucion continua")
   
for i in range(11):
    print(i)

## Manejo de excepciones 
try:    
    print (10 / 1)
except:
    print("Se ha producido un error ")
finally:
    print("Ha finalizado el manejo de excepciones")

"""
Extra
"""

num = 0

for num in range(10,56):
    if num % 2 == 0 and num !=16 and num % 3 !=0:
        print(num)




