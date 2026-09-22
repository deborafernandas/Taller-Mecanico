from model.vehiculo import Vehiculo  # Import corregido hacia el paquete model
from model.modelo import Modelo  # Import corregido hacia el paquete model

class Moto(Vehiculo):  # Define la clase Moto que hereda de Vehiculo
    def __init__(self, patente: str, anio: int, modelo: Modelo):
        super().__init__(patente, anio, modelo)
        
    def tarifa_hora(self) -> int:  # Tarifa por hora específica para Moto
        return 15000
