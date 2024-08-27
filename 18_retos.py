"""
Ejercicio
"""

data = [1,2,3,4,5]

data.append(6)
print(f"Añadiendo elemento al afinal {data}")

data.insert(0,0)
print(f"Añadiendo elemento al principio {data}")

data.extend([7,8,9])
print(f"Añadiendo estructura al afinal {data}")

data[3:3] = [-1,-2,-3]
print(f"Añadiendo estructura en una posicion concreta {data}")

del data[3]
print(f"Borrando un elemento en una posicion concreta{data}")

data[4] = -1
print(f"Actualizando un elemento concreto {data}")

print(f"Comprobar si un elemento existe:  {-1 in data}")

data.clear()
print(f"Eliminar contenido {data}")

"""
Extra
"""

set_1 = {1,2,3,4,5}
set_2 = {1,2,3,6,7}

print(f"Union: {set_1.union(set_2)}")
print(f"Interseccion: {set_1.intersection(set_2)}")
print(f"Diferencias: {set_1.difference(set_2)}")
print(f"Diferencia Asimetrica: {set_1.symmetric_difference(set_2)}")



