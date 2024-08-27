"""
Stack y Colas
"""

pilas = []

## Push
pilas.append(1) 
pilas.append(2) ##Añade
pilas.append(3) ##Añade
print(pilas)

## Pop
pilas_item = pilas[len(pilas)-1] 
del pilas[len(pilas)-1]
print(pilas_item)

print(pilas.pop()) #Elimina el ultimo elemento

print(pilas)

# Cola/Queue (FIFO)

queue = []

queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

# Dequeue
queue_item = queue[0] 
del queue[0]
print(queue_item)

print(queue.pop(0))
print(queue)

"""
Extra
"""

# /Web

def web_navigation():
    stack = []
    

    while True:
        
        action = input(
            "Añade una Url o interactua con adelante/atras/salir:"
        )

        if action == "salir":
            print("Saliendo del navegador Web")
            break
        elif action == "adelante":
            pass
        elif action == "atras":
            if len(stack) > 0:
               stack.pop()
        else:
            stack.append(action)
            print(f"Has navegado a la Web: {stack[len(stack)- 1]}.")
        
web_navigation()

def shared_printed():
    queue = []

    while True:
        
        action = input("Añade un documento o selecciona imprimir/salir: ")

        if action == "salir":
            break
        elif action == "imprimir":
            if len(queue) > 0:
               print(f" Imprimiendo: {queue.pop(0)}")
        else:
            queue.append(action)
         
            print(f"Cola de impresion: {queue}")

shared_printed()


         

         
         
                  


 


        

 

   

