from model.persona import Persona  # Import corregido hacia el paquete model

class Cliente:
    def __init__(self, persona: Persona):
        self.__persona = persona

    def tiene_deuda(self) -> bool:
        return False
