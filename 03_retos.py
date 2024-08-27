"""
Estructuras de Datos
"""
  
    ##  List ##

my_list = list()
my_other_list = ["angel", 26, ' Garcia',2.50, "angel"]

print(type( my_other_list))
print(my_other_list)

print(my_other_list.count("angel"))     #cuenta los string  "angel"
print(my_other_list)
my_other_list.insert(1,"PEPE")  # Insertar en un indice un valor
print(my_other_list)
my_other_list.append("Castor")   # Insertar en el final 
print(my_other_list)
my_other_list.remove("Castor")  # Eliminacion
print(my_other_list)
print(my_other_list[1])     # Acceso
my_other_list [1] = "Garcia"    # Actualización
print(my_other_list)
##my_other_list.sort()    # Ordenación
print(my_other_list)

    ## Tuples ##

my_tuple = tuple()
my_other_tuple = ("Angel", "OlianDev" , "36")

print(type( my_other_tuple))
print(my_other_tuple)


print(my_other_tuple [-3])
print(my_other_tuple [1]) #Indica el indice Acceso
##  my_other_tuple [1] = "Jenni" Hay que pasarala a list para poder insert las tuples son inmutables
my_other_tuple = tuple(sorted(my_other_tuple)) #Ordenacion
print(my_other_tuple)
print(type(my_other_tuple))



    ## Sets ##

my_set = set() ## No admite repetidos y los imprime de forma desordenada, inicialmente es un dict
my_other_set = {2,"Angel", "Garcia" , "Angel"}
print(my_other_set)
my_other_set.add("angel@gmail.com") # Insercion
my_other_set.add("angel@gmail.com")
print(my_other_set)
my_other_set.remove(2) # Eliminacion
print(my_other_set)
my_set = set(sorted(my_other_set)) # No se puede ordenar
print(my_set)
print(type(my_set))

    ## Dict ##

my_dict = dict()
my_other_dict = {
    "name":"Angel" , 
    "name2":"Jenni", 
    "Appellido":"Garcia"
    }
my_other_dict["email"] = "angel@icloud,com" # Insercion
print(my_other_dict)
del my_other_dict["name2"] # Eliminacion
print(my_other_dict["Appellido"]) # Acceso
my_other_dict["name"] = "Jenni" # Actualizacion
print(my_other_dict)
my_other_dict = dict (sorted(my_other_dict.items()))
print(my_other_dict)
print(type(my_other_dict))


"""
Extra
"""

def my_agenda():

    agenda = {}
    
    def insert_contact():
        phone = input("Introduce el nuevo telefono del contacto")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
        else:
            print("Introduce un numero de telefono con menos digitos de 12")
    
    while True:

        print("")
        print("1. Buscar contactos")
        print("2. Añadir contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = input("Selecciona una opcion")

        match option:
            case "1":
              name = input("Introduce el nombre del contacto: ")
              if name in agenda:
                  print(f"El numero de telefono de {name} es {agenda[name]}:  ")
              else:
                  print(f"El contacto {name} no existe")  
                  
            case "2":
                name = input("Introduce el nombre del contacto: ")
                phone = input("Introduce el telefono del contacto: ")
                if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                    agenda[name] = phone
                else:
                    print("Introduce un numero de telefono con menos digitos de 12")
            case "3":
                name = input("Introduce el nombre del contacto para actualizar")
                if name in agenda:
                    insert_contact()
                else:
                    print(f"El contacto {name} no existe")
            case "4":
               name = input("Introduce el nombre del contacto a eliminar") 
               if name in agenda:
                   del agenda[name]
               else:
                   print("El contacto no existe")
            case "5":
                print("Saliendo de la agenada")
                break
            case _:
                print("Opcion no valida. Elige una opcion del 1 al 5")
    

my_agenda()















