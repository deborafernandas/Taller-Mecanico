from model.vehiculo import Vehiculo  # Import corregido hacia el paquete model
from model.modelo import Modelo  # Import corregido hacia el paquete model

class Auto(Vehiculo):  # Define la clase Auto que hereda de Vehiculo
    def __init__(self, patente: str, anio: int, modelo: Modelo, capacidad_maletero: int = 0):
        super().__init__(patente, anio, modelo)
        self.__capacidad_maletero: int = capacidad_maletero

    @property
    def capacidad_maletero(self) -> int:  # Getter para capacidad del maletero
        return self.__capacidad_maletero

    @property
    def restriccion(self) -> int:  # Getter para consultar año / restricción
        return self.anio

    @restriccion.setter
    def restriccion(self, numero: int):  # Setter para validar restricción vehicular
        if numero > 2011:
            self.anio = numero
            print("auto sin restriccion vehicular")
        else:
            raise ValueError("auto sujeto a restriccion vehicular")

    def tarifa_hora(self) -> int:  # Tarifa por hora específica para Auto
        return 25000
