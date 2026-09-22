class Repuesto:
    def __init__(self, codigo: str, nombre: str, stock: int, es_importado: bool):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__stock = stock
        self.__es_importado = es_importado

    def hay_stock(self) -> bool:
        return self.__stock > 0

    def disminuir_stock(self, cantidad: int):
        if self.__stock >= cantidad:
            self.__stock -= cantidad
