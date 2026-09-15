from repuesto import Repuesto

class LineaDetalle:
    def __init__(self, cantidad: int, precio_unitario: int, repuesto: Repuesto):
        self.__cantidad = cantidad
        self.__precio_unitario = precio_unitario
        self.__repuesto = repuesto

    def subtotal(self) -> int:
        return self.__cantidad * self.__precio_unitario
