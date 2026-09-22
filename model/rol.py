class Rol:
    def __init__(self, nombre: str, permisos: list):
        self.__nombre = nombre
        self.__permisos = permisos

    def tiene_permiso(self, accion: str) -> bool:
        return accion in self.__permisos
