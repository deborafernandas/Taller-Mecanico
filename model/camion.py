from typing import Optional, Union
from model.vehiculo import Vehiculo # Importa la clase base Vehiculo
from model.modelo import Modelo # Importa la clase Modelo

class Camion(Vehiculo): # Define la clase Camion que hereda de Vehiculo
    def __init__(self, patente: str, anio: int, modelo: Optional[Union[Modelo, int]] = None, capacidad_carga: int = 0):
        if isinstance(modelo, int):
            super().__init__(patente, anio, None)
            self.__capacidad_carga: int = modelo
        else:
            super().__init__(patente, anio, modelo)
            self.__capacidad_carga: int = capacidad_carga

    @property
    def capacidad_carga(self) -> int: # Getter para capacidad de carga
        return self.__capacidad_carga

    def tarifa_hora(self) -> int: # Tarifa por hora específica para Camion
        return 40000
