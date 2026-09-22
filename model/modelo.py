from model.marca import Marca  # Import corregido hacia el paquete model

class Modelo:
    def __init__(self, nombre: str, marca: Marca):
        self.__nombre = nombre
        self.__marca = marca

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def marca(self) -> Marca:
        return self.__marca
