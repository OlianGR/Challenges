"""
Ejercicio
"""
from datetime import datetime

now = datetime.now()
birth_date = datetime(1997,3,4,12,0,0)

print(now)
print(birth_date)

difference = now - birth_date

print(type(difference))

print(difference.days //365)

print(birth_date.strftime("%d %m %y"))
print(birth_date.strftime("%d %m %Y"))

print(birth_date.strftime("%H %M %S"))

print(birth_date.strftime("%c"))

print(birth_date.strftime("%h"))

print(birth_date.strftime("%p"))

print(birth_date.strftime("%x"))
print(birth_date.strftime("%X"))

print(birth_date.strftime("%a"))
print(birth_date.strftime("%A"))

print(birth_date.strftime("%B"))
print(birth_date.strftime("%b"))

