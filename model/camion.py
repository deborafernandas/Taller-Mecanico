from model.vehiculo import Vehiculo  # Import corregido hacia el paquete model
from model.modelo import Modelo  # Import corregido hacia el paquete model

class Camion(Vehiculo):  # Define la clase Camion que hereda de Vehiculo
    def __init__(self, patente: str, anio: int, modelo: Modelo, capacidad_carga: int = 0):
        super().__init__(patente, anio, modelo)
        self.__capacidad_carga: int = capacidad_carga

    @property
    def capacidad_carga(self) -> int:  # Getter para capacidad de carga
        return self.__capacidad_carga

    def tarifa_hora(self) -> int:  # Tarifa por hora específica para Camion
        return 40000
