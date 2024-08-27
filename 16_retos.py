import re

"""
Ejercicio
"""

regex = r"[\d]+"

text = "Este es el ejercicio 15 publicado el 15/05/2024"

def find_numbers(text:str)-> list:
     return re.findall(regex,text)

print(find_numbers(text))

"""
Extra
"""

def validate_email(email:str)-> bool:
    return bool(re.match( r"^[\w.+-]+@[\w]+\.[a-zA-Z]+$", email))

print(validate_email("mouredev@gmail.com"))

def validate_phone(phone:str)-> bool:
    return bool(re.match( r"^\+?[\d\s]{3,}$", phone))

print(validate_phone("091"))

def validate_url(url:str)-> bool:
    return bool(re.match( r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]", url))

    
