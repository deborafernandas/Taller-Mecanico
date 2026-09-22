from model.marca import Marca  # Import corregido hacia el paquete model

class Modelo:
    def __init__(self, nombre: str, marca: Marca):
        self.__id = None  # Identificador numérico asignado por la base de datos
        self.__nombre = nombre
        self.__marca = marca

    @property
    def id(self) -> int:  # Getter para el atributo id
        return self.__id

    @id.setter
    def id(self, valor: int) -> None:  # Setter para asignar el id tras la inserción en la BD
        self.__id = valor

    @property
    def nombre(self) -> str:  # Getter para el nombre del modelo
        return self.__nombre

    @property
    def marca(self) -> Marca:  # Getter para el objeto Marca asociado
        return self.__marca
