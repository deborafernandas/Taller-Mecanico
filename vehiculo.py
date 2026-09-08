from abc import ABC, abstractmethod

class Vehiculo(ABC): # Define la clase Vehiculo
    def __init__(self, patente: str, anio: int): # Constructor que recibe patente y año al crear el objeto
        self.patente: str = patente # Asigna la patente a través del setter para ejecutar la validación
        self.anio: int = anio # Asigna el año a través del setter para ejecutar la validación
        self.__en_taller: bool = False # Inicializa el estado en False (no está en el taller por defecto) como privado

    @property
    def patente(self) -> str: # Getter para acceder al atributo privado __patente
        return self.__patente # Retorna la patente del vehículo

    @patente.setter
    def patente(self, nueva_patente: str): # Setter para asignar y validar la patente
        if len(nueva_patente) < 6 or " " in nueva_patente: # Valida que tenga al menos 6 caracteres y no contenga espacios
            raise ValueError("La patente debe tener al menos 6 caracteres y no contener espacios.") # Lanza un error si no cumple las condiciones
        self.__patente: str = nueva_patente # Asigna la patente validada al atributo privado

    @property
    def anio(self) -> int: # Getter para acceder al atributo privado __anio
        return self.__anio # Retorna el año de fabricación del vehículo

    @anio.setter
    def anio(self, nuevo_anio: int): # Setter para asignar y validar el año
        if nuevo_anio < 1900 or nuevo_anio > 2026: # Valida que el año esté en un rango coherente
            raise ValueError("El año de fabricación debe estar entre 1900 y 2026.") # Lanza un error si el año es inválido
        self.__anio: int = nuevo_anio # Asigna el año validado al atributo privado


    def ingresar(self) -> str: # Método para registrar el ingreso del vehículo al taller
        if self.__en_taller: # Verifica si el vehículo ya está marcado como dentro del taller
            return "El vehículo ya se encuentra en el taller." # Devuelve mensaje si ya estaba ingresado
        self.__en_taller = True # Cambia el estado a True (ingresado)
        return "El vehículo ha ingresado al taller." # Devuelve mensaje de éxito

    def entregar(self) -> str: # Método para registrar la salida o entrega del vehículo
        if not self.__en_taller: # Verifica si el vehículo no está en el taller
            return "El vehículo no se encuentra en el taller." # Devuelve mensaje indicando que no se puede entregar
        self.__en_taller = False # Cambia el estado a False (fuera del taller)
        return "El vehículo ha sido entregado." # Devuelve mensaje de éxito

    @abstractmethod
    def tarifa_hora(self) -> int: # Método abstracto que retorna el costo de la tarifa por hora
        pass