"""
Ejercicio
"""

# For

for num in range(1,11):
    print(num)

# While

i= 1

while i <=10 : 
    print(i)
    i += 1 

# Recursividad

def count_ten (i=1):
    if i <= 10:
        print(i)
        count_ten(i + 1)

count_ten()

"""
Extra
"""

for e in [1,2,3,4]:
    print (e)

for e in {1,2,3,4}:
    print (e)

for e in {1: "A", 2:"b", 3:"c", 4:"d"}:
    print (e)

print(*[i for i in range(1,11)], sep="\n")