from vehiculo import Vehiculo # Importa la clase base Vehiculo desde vehiculo.py

class Camion(Vehiculo): # Define la clase Camion que hereda de la clase base Vehiculo
    def __init__(self, patente: str, anio: int, capacidad_carga: int): # Constructor que recibe patente, año y capacidad de carga en kilos
        super().__init__(patente, anio) # Llama al constructor de la clase padre Vehiculo para inicializar patente y año
        self.__capacidad_carga: int = capacidad_carga # Guarda la capacidad de carga en kilos como atributo privado

    def tarifa_hora(self) -> int: # Sobrescribe el método tarifa_hora para la clase Camion
        return 40000 # Retorna la tarifa por hora específica para un camión (40000)

