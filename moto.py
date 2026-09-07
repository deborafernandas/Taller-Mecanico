from vehiculo import Vehiculo # Importa la clase base Vehiculo desde vehiculo.py

class Moto(Vehiculo): # Define la clase Moto que hereda de Vehiculo
    def tarifa_hora(self) -> int: # Sobrescribe el método tarifa_hora para la clase Moto
        return 15000 # Retorna la tarifa por hora específica para una moto (15000)

