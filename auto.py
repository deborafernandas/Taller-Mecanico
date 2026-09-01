from vehiculo import Vehiculo # Importa la clase base Vehiculo desde vehiculo.py

class Auto(Vehiculo): # Define la clase Auto que hereda de la clase base Vehiculo
    def __init__(self, patente: str, anio: int, capacidad_maletero: int): # Constructor que recibe patente, año y capacidad del maletero en litros
        super().__init__(patente, anio) # Llama al constructor de la clase padre Vehiculo para inicializar patente y año
        self.__capacidad_maletero: int = capacidad_maletero # Guarda la capacidad del maletero en litros como atributo privado
