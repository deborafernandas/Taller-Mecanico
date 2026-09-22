from model.rol import Rol  # Import corregido hacia el paquete model
from model.persona import Persona  # Import corregido hacia el paquete model

class Usuario:
    def __init__(self, usuario: str, password_hash: str, rol: Rol, persona: Persona):
        self.__usuario = usuario
        self.__password_hash = password_hash
        self.__rol = rol
        self.__persona = persona

    def autenticar(self, password_hash: str) -> bool:
        return self.__password_hash == password_hash

    def puede(self, accion: str) -> bool:
        return self.__rol.tiene_permiso(accion)
