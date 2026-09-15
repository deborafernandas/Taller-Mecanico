from abc import ABC, abstractmethod
from typing import Optional
from modelo import Modelo

class Vehiculo(ABC): # Define la clase base abstracta Vehiculo
    def __init__(self, patente: str, anio: int, modelo: Optional[Modelo] = None): # Constructor con patente, año y modelo
        self.patente: str = patente # Asigna patente pasando por el setter para validar
        self.anio: int = anio # Asigna año pasando por el setter para validar
        self._en_taller: bool = False # Atributo protegido indicando estado en taller
        self.__modelo: Optional[Modelo] = modelo # Referencia al objeto Modelo de dominio

    @property
    def patente(self) -> str: # Getter para patente
        return self.__patente

    @patente.setter
    def patente(self, nueva_patente: str) -> None: # Setter con validación de longitud y sin espacios
        if len(nueva_patente) < 6 or " " in nueva_patente:
            raise ValueError("La patente debe tener al menos 6 caracteres y no contener espacios.")
        self.__patente = nueva_patente

    @property
    def anio(self) -> int: # Getter para anio
        return self.__anio

    @anio.setter
    def anio(self, nuevo_anio: int) -> None: # Setter con validación de rango de años
        if nuevo_anio < 1900 or nuevo_anio > 2026:
            raise ValueError("El año de fabricación debe estar entre 1900 y 2026.")
        self.__anio = nuevo_anio

    @property
    def modelo(self) -> Optional[Modelo]: # Getter para el modelo del vehículo
        return self.__modelo

    @modelo.setter
    def modelo(self, nuevo_modelo: Optional[Modelo]) -> None: # Setter para el modelo
        self.__modelo = nuevo_modelo

    def ingresar(self) -> str: # Registra el ingreso del vehículo al taller
        if self._en_taller:
            return "El vehículo ya se encuentra en el taller."
        self._en_taller = True
        return "El vehículo ha ingresado al taller."

    def entregar(self) -> str: # Registra la salida o entrega del vehículo
        if not self._en_taller:
            return "El vehículo no se encuentra en el taller."
        self._en_taller = False
        return "El vehículo ha sido entregado."

    @abstractmethod
    def tarifa_hora(self) -> int: # Método abstracto para calcular la tarifa por hora
        pass
