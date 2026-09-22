from model.vehiculo import Vehiculo  # Import corregido hacia el paquete model
from model.modelo import Modelo  # Import corregido hacia el paquete model

class Camion(Vehiculo):
    def __init__(self, patente: str, anio: int, modelo: Modelo, capacidad_carga: int):
        super().__init__(patente, anio, modelo)
        self.__capacidad_carga: int = capacidad_carga

    def tarifa_hora(self) -> int:
        return 40000
