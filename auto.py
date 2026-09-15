from typing import Optional, Union
from vehiculo import Vehiculo # Importa la clase base Vehiculo
from modelo import Modelo # Importa la clase Modelo del dominio

class Auto(Vehiculo): # Define la clase Auto que hereda de Vehiculo
    def __init__(self, patente: str, anio: int, modelo: Optional[Union[Modelo, int]] = None, capacidad_maletero: int = 0):
        if isinstance(modelo, int):
            super().__init__(patente, anio, None)
            self.__capacidad_maletero: int = modelo
        else:
            super().__init__(patente, anio, modelo)
            self.__capacidad_maletero: int = capacidad_maletero

    @property
    def capacidad_maletero(self) -> int: # Getter para capacidad del maletero
        return self.__capacidad_maletero

    @property
    def restriccion(self) -> int: # Getter para consultar año / restricción
        return self.anio

    @restriccion.setter
    def restriccion(self, numero: int): # Setter para validar restricción vehicular
        if numero > 2011:
            self.anio = numero
            print("auto sin restriccion vehicular")
        else:
            raise ValueError("auto sujeto a restriccion vehicular")

    def tarifa_hora(self) -> int: # Tarifa por hora específica para Auto
        return 25000
