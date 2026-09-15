from persona import Persona

class Cliente:
    def __init__(self, persona: Persona):
        self.__persona = persona

    def tiene_deuda(self) -> bool:
        return False
