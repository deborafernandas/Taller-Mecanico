from vehiculo import Vehiculo # Importa la clase base Vehiculo desde vehiculo.py

class Auto(Vehiculo): # Define la clase Auto que hereda de la clase base Vehiculo
    def __init__(self, patente: str, anio: int, capacidad_maletero: int): # Constructor que recibe patente, año y capacidad del maletero en litros
        super().__init__(patente, anio) # Llama al constructor de la clase padre Vehiculo para inicializar patente y año
        self.__capacidad_maletero: int = capacidad_maletero # Guarda la capacidad del maletero en litros como atributo privado

    @property
    def restriccion(self) -> int: # Getter para obtener el año del auto
        return self._Vehiculo__anio # Retorna el año del vehículo

    @restriccion.setter
    def restriccion(self, numero: int): # Setter para validar la restricción vehicular según el año
        if numero > 2011: # Valida que el número sea mayor a 2011
            self._Vehiculo__anio = numero # Actualiza el año del vehículo
            print("auto sin restriccion vehicular") # Muestra mensaje indicando que el auto no tiene restricción
        else:
            raise ValueError("auto sujeto a restriccion vehicular") # Lanza error si el auto está sujeto a restricción

    def tarifa_hora(self) -> int: # Sobrescribe el método tarifa_hora para la clase Auto
        return 25000 # Retorna la tarifa por hora específica para un auto (25000)

