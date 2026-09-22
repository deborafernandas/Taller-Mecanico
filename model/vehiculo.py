from abc import ABC, abstractmethod
from model.modelo import Modelo  # Import corregido hacia el paquete model

class Vehiculo(ABC):
    def __init__(self, patente: str, anio: int, modelo: Modelo):
        self.patente = patente
        self.__anio: int = anio
        self._en_taller: bool = False
        self.__modelo: Modelo = modelo

    @property
    def patente(self) -> str:
        return self.__patente

    @patente.setter
    def patente(self, valor: str) -> None:
        if len(valor) < 6 or " " in valor:
            raise ValueError("La patente debe tener al menos 6 caracteres y no debe contener espacios.")
        self.__patente = valor

    @property
    def modelo(self) -> Modelo:
        return self.__modelo

    def ingresar(self) -> str:
        if self._en_taller:
            return "El vehículo ya se encuentra en el taller."
        self._en_taller = True
        return "El vehículo ha ingresado al taller."

    def entregar(self) -> str:
        if not self._en_taller:
            return "El vehículo no se encuentra en el taller."
        self._en_taller = False
        return "El vehículo ha sido entregado."

    @abstractmethod
    def tarifa_hora(self) -> int:
        pass