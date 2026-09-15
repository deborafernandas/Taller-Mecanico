from typing import Optional
from model.vehiculo import Vehiculo # Importa la clase base Vehiculo
from model.modelo import Modelo # Importa la clase Modelo

class Moto(Vehiculo): # Define la clase Moto que hereda de Vehiculo
    def __init__(self, patente: str, anio: int, modelo: Optional[Modelo] = None):
        super().__init__(patente, anio, modelo)
        
    def tarifa_hora(self) -> int: # Tarifa por hora específica para Moto
        return 15000
