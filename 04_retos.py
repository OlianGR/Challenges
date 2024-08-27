"""
Cadenas de Caracteres
"""

my_variable = "Hola, mundo"

## Acceso a caracteres especificos

print(my_variable[2])
primer_caracter = my_variable[0]
print(primer_caracter)
ultimo_caracter = my_variable[-1]
print(ultimo_caracter)

## Slicing (porcion)

print (my_variable[0:11])
print (my_variable[0:])

## Longitud de cadenas

print(len(my_variable))

## Concatenacion

other_variable = "Bienvenido"

new_variable = my_variable + other_variable
print(new_variable)

## Repeticion de cadenas 

repetida = my_variable * 3
print(my_variable * 3)

##  Busqueda

print ("a" in my_variable)
print ("b" in my_variable)

## Busqueda al principo y al final

print( my_variable.startswith("Ho"))
print( my_variable.endswith("an"))
print( my_variable.endswith("do"))

## Busqueda por posicion 

print("Brais Moure @moureDev".find("moure"))
print("Brais Moure @moureDev".find("Moure"))
print("Brais Moure @moureDev".find("M"))
print("Brais Moure @moureDev".lower().find("m"))
s1 = "Hola"
s2 = "Phyton"
s3 = "Brais Moure @moureDev"

## Busqueda de ocurrencias

print(s3.lower().count("m"))

## Formateo

print("Saludo:{} , lenguaje:{} ".format(s1,s2))

## Interpolacion de cadenas 

nombre = "Angel"
edad  = 26
saludo = f"hola soy {nombre} y tengo {edad} años"
print(saludo)

##Transformacion

print(list(s3))

## Recorrido 

for caracter in my_variable:
    print(caracter)

## Conversion a mayusculas y minusculas

print(my_variable.upper())
minusculas = my_variable.lower()
print(minusculas)
print("brais moure".title()) ## Pone mayusculas a todas las iniciales de las palabra
print("brais moure".capitalize()) ## pone mayuscula solo a la primera palabra

## Eliminacion de espacios al principio y al final 
print("brais moure".strip() + "@mouredev")

## Remplazo

print(my_variable.replace("mundo", "universo"))

## Division de cadenas
print (my_variable.split("a")) ##Crea una lista

## Union de cadenas

union = "-".join(["Hola", "mundo"])
print(union)


## Conversion de tipos -> Casting
s5 = "12345.345"
s5 = float(s5)
print(type(s5))

s6 = 125.8
s6 = int(s6)
print(type(s6))

## Comprobaciones varias

print(s1.isalnum())
print(s1.isalpha())




"""
Extra
"""

def check (word1:str, word2:str):
    
    # Palíndromos
    print(f"{word1} es un palindromo?:  {word1 == word1[::-1]} ")
    print(f"{word2} es un palindromo?:  {word2 == word2[::-1]} ")

    # Anagramas
    print(f"{word1} es anagrama de {word2}?:  {sorted(word1) == sorted(word2)} ")

        # Isograma
        
    def isogram(word:str) -> bool:

        word_dict = dict()
        for word in word:
            word_dict[word]  = word_dict.get(word,0) + 1

        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break
        return isogram
    
    print(f"{word1} es un isograma:  {isogram(word1)} ")
    print(f"{word2} es un isograma:  {isogram(word2)} ")
    

check("radar", "phytonphyton")
#check("amor", "roma")

