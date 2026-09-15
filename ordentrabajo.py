from vehiculo import Vehiculo
from usuario import Usuario
from lineadetalle import LineaDetalle
from repuesto import Repuesto

class OrdenTrabajo:
    def __init__(self, numero: int, descripcion: str, vehiculo: Vehiculo, usuario: Usuario):
        self.__numero = numero
        self.__descripcion = descripcion
        self.__horas = 0
        self.__cerrada = False
        self.__vehiculo = vehiculo
        self.__usuario = usuario
        self.__lineas_detalle = []

    def agregar_horas(self, cantidad: int):
        if not self.__cerrada:
            self.__horas += cantidad

    def agregar_repuesto(self, cantidad: int, precio_unitario: int, repuesto: Repuesto):
        if not self.__cerrada and repuesto.hay_stock():
            linea = LineaDetalle(cantidad, precio_unitario, repuesto)
            self.__lineas_detalle.append(linea)
            repuesto.disminuir_stock(cantidad)

    def cerrar(self):
        self.__cerrada = True

    def total(self) -> int:
        total_repuestos = sum(linea.subtotal() for linea in self.__lineas_detalle)
        total_mano_obra = self.__horas * self.__vehiculo.tarifa_hora()
        return total_repuestos + total_mano_obra
