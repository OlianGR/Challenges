"""
Ejercicio
"""
from enum import Enum

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

def get_day(number: int):
    print(Weekday(number).name)

get_day(1)
get_day(3)


"""
Extra
"""

class OrderStatus(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4

class Order:

    status = OrderStatus.PENDIENTE

    def __init__(self, id: int) -> None:
        self.id = id

    def enviado(self):
        if self.status == OrderStatus.PENDIENTE:
            self.status = OrderStatus.ENVIADO
            self.display_status()
        else:
            print("El pedido ya ha sido enviado o cancelado")
    
    def entregado(self):
        if  self.status == OrderStatus.ENVIADO:
            self.status = OrderStatus.ENTREGADO
            self.display_status()
        else:
            print("El pedido necesita ser enviado antes de entregarse  ")

    def cancelado(self):
        if self.status != OrderStatus.ENTREGADO:
            self.status = OrderStatus.CANCELADO
            self.display_status()
        else:
            print("El pedido ya se ha entregado no se puede cancelar")

    def display_status(self):
        print(f"El estado del pedido {self.id} es {self.status.name}")

order_1 = Order(1)
order_1.display_status()
order_1.enviado()
order_1.entregado()
order_1.cancelado()


