from vehiculo import Vehiculo
from marca import Marca
from modelo import Modelo
from auto import Auto
from moto import Moto
from camion import Camion
from persona import Persona
from cliente import Cliente
from rol import Rol
from usuario import Usuario
from repuesto import Repuesto
from ordentrabajo import OrdenTrabajo

def main():
    # =====================================================================
    # 1. Demostración de Abstracción Segura y Validaciones de Excepciones
    # =====================================================================
    print("--- PRUEBA 1: Instanciación de clase abstracta ---")
    try:
        vehiculo = Vehiculo("XY1234", 2015)
    except TypeError as error:
        print(f"[ERROR CONTROLADO] No se puede instanciar la clase abstracta 'Vehiculo': {error}")
        print("-> Confirmación: Abstracción verificada exitosamente.\n")

    print("--- PRUEBA 2: Validación de patente en constructor ---")
    try:
        auto_invalido = Auto("AB 1", 2022)
    except ValueError as error:
        print(f"[ERROR CONTROLADO] Error al validar patente: {error}")
        print("-> Confirmación: Patente inválida rechazada correctamente.\n")

    print("--- PRUEBA 3: Validación de año en constructor ---")
    try:
        moto_invalida = Moto("CD5678", 1850)
    except ValueError as error:
        print(f"[ERROR CONTROLADO] Error al validar año: {error}")
        print("-> Confirmación: Año inválido rechazado correctamente.\n")

    # =====================================================================
    # 2. Creación de Marcas y Modelos del Dominio
    # =====================================================================
    print("--- CREACIÓN DE MODELO DE DOMINIO ---")
    marca_toyota = Marca("Toyota")
    modelo_yaris = Modelo("Yaris", marca_toyota)

    marca_honda = Marca("Honda")
    modelo_cbr = Modelo("CBR500R", marca_honda)

    marca_volvo = Marca("Volvo")
    modelo_fh = Modelo("FH16", marca_volvo)

    # =====================================================================
    # 3. Instanciación de Vehículos con sus Modelos
    # =====================================================================
    auto = Auto("AB1234", 2018, modelo_yaris, capacidad_maletero=450)
    moto = Moto("CD5678", 2020, modelo_cbr)
    camion = Camion("EF9012", 2023, modelo_fh, capacidad_carga=5000)

    # =====================================================================
    # 4. Pruebas de Ingreso al Taller
    # =====================================================================
    print("--- Ingreso de Vehículos ---")
    print(auto.ingresar())
    print(moto.ingresar())
    print(camion.ingresar())
    print()

    # =====================================================================
    # 5. Pruebas de Tarifas Polimórficas
    # =====================================================================
    print("--- Tarifas por Hora ---")
    print(f"Tarifa Auto ({auto.modelo.marca.nombre} {auto.modelo.nombre}): ${auto.tarifa_hora()}")
    print(f"Tarifa Moto ({moto.modelo.marca.nombre} {moto.modelo.nombre}): ${moto.tarifa_hora()}")
    print(f"Tarifa Camión ({camion.modelo.marca.nombre} {camion.modelo.nombre}): ${camion.tarifa_hora()}")
    print()

    # =====================================================================
    # 6. Verificación de Restricción Vehicular
    # =====================================================================
    print("--- Verificación de Restricción Vehicular ---")
    print(f"Año del auto registrado ({auto.patente}): {auto.restriccion}")
    auto.restriccion = 2020

    auto_antiguo = Auto("ZZ9988", 2008, modelo_yaris)
    print(f"Llega al taller auto patente {auto_antiguo.patente} (año {auto_antiguo.restriccion}).")
    try:
        auto_antiguo.restriccion = 2008
    except ValueError as error:
        print(f"[RESTRICCIÓN CONTROLADA] {error}")
    print()

    # =====================================================================
    # 7. Crear Personas, Clientes y Usuarios
    # =====================================================================
    persona_mecanico = Persona("12.345.678-9", "Juan Mecánico")
    rol_mecanico = Rol("Mecánico", ["reparar", "cerrar_orden"])
    usuario_mecanico = Usuario("juanm", "hash123", rol_mecanico, persona_mecanico)

    persona_cliente = Persona("9.876.543-2", "Pedro Cliente")
    cliente_pedro = Cliente(persona_cliente)

    # =====================================================================
    # 8. Gestión de Orden de Trabajo y Repuestos
    # =====================================================================
    print("--- Gestión de Orden de Trabajo ---")
    orden1 = OrdenTrabajo(1, "Cambio de aceite y pastillas", auto, usuario_mecanico)
    orden1.agregar_horas(3)

    filtro = Repuesto("F-001", "Filtro de Aceite", 10, False)
    pastillas = Repuesto("P-002", "Pastillas de freno", 5, True)

    orden1.agregar_repuesto(1, 15000, filtro)
    orden1.agregar_repuesto(1, 45000, pastillas)

    print(f"Total de Orden #1 (Mano de obra + Repuestos): ${orden1.total()}")
    orden1.cerrar()
    print("Orden cerrada exitosamente.\n")
    print("-> Todas las pruebas y operaciones se completaron con éxito.")

if __name__ == "__main__":
    main()
