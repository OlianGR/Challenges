"""
Ejercicio
"""
from datetime import datetime
import time 
import asyncio

async def task(name: str, duration: int):
    print(f"Tarea: {name}, Duracion: {duration} Inicio: {datetime.now()}" )
    await asyncio.sleep(duration)
    print(f"Tarea: {name}, Fin: {datetime.now()}" )


asyncio.run(task("1",2))

"""
Extra
"""
async def async_tasks():
    await asyncio.gather(task("C",10),task("B",7),task("A",4))
    await task("D",1)


asyncio.run(async_tasks)

