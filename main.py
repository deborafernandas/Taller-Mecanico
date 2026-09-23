import conectar  # Importa el módulo conectar para inicializar la base de datos
from dao.marca_dao import MarcaDao  # Importa el DAO de marcas
from dao.modelo_dao import ModeloDao  # Importa el DAO de modelos
from dao.auto_dao import AutoDao  # Importa el DAO de autos (que también gestiona vehículos)
from model.marca import Marca  # Importa el modelo Marca para instanciar objetos
from model.modelo import Modelo  # Importa el modelo Modelo para instanciar objetos
from model.auto import Auto  # Importa el modelo Auto para instanciar objetos

def main():  # Función principal de ejecución
    print("--- Inicializando Base de Datos ---")
    
    # 1. Crear conexión
    conn = conectar.crear_conexion()  # Obtiene la conexión SQLite con Foreign Keys activas
    
    # 2. Instanciar los DAOs pasándoles la conexión
    marca_dao = MarcaDao(conn)  # Instancia MarcaDao
    modelo_dao = ModeloDao(conn)  # Instancia ModeloDao
    auto_dao = AutoDao(conn)  # Instancia AutoDao (crea tablas vehiculos y autos)
    
    # 3. Crear todas las tablas en orden relacional
    marca_dao.crear_tabla()
    modelo_dao.crear_tabla()
    auto_dao.crear_tabla()
    print("Tablas 'marcas', 'modelos', 'vehiculos' y 'autos' listas.\n")
    
    # =========================================================================
    # PRUEBA 1: MARCADao (Insertar, Listar y Buscar)
    # =========================================================================
    print("=================== 1. PRUEBAS MARCADao ===================")
    marca_toyota = Marca("Toyota")
    marca_dao.insertar(marca_toyota)
    conn.commit()
    print(f"[INSERT] Marca '{marca_toyota.nombre}' creada con ID: {marca_toyota.id}")
    
    # Listar marcas
    marcas = marca_dao.listar()
    print(f"[LISTAR] Marcas registradas ({len(marcas)}):")
    for m in marcas:
        print(f"  - ID: {m.id} | Nombre: {m.nombre}")
        
    # Buscar marca por ID
    marca_buscada = marca_dao.buscar(marca_toyota.id)
    if marca_buscada:
        print(f"[BUSCAR] Marca ID {marca_toyota.id} encontrada: {marca_buscada.nombre}")
        
    # Actualizar marca existente
    marca_toyota.nombre = "Toyota Gazoo"
    marca_actualizada = marca_dao.actualizar(marca_toyota)
    if marca_actualizada:
        print(f"[ACTUALIZAR] Marca ID {marca_actualizada.id} actualizada a: '{marca_actualizada.nombre}'")
    else:
        print("[ACTUALIZAR] No se pudo actualizar la marca.")
        
    # Intentar actualizar un ID inexistente
    marca_inexistente = Marca("Fantasma")
    marca_inexistente.id = 9999
    res_falsa = marca_dao.actualizar(marca_inexistente)
    if res_falsa is None:
        print(f"[CONTROLADO] Actualización de ID inexistente (9999) retornó None exitosamente.")
        
    # Prueba eliminar marca existente
    marca_temp = Marca("MarcaTemporal")
    marca_dao.insertar(marca_temp)
    conn.commit()
    print(f"[INSERT TEMPORAL] Marca '{marca_temp.nombre}' creada con ID: {marca_temp.id}")
    
    if marca_dao.eliminar(marca_temp.id):
        print(f"[ELIMINAR] Marca ID {marca_temp.id} eliminada con éxito.")
    else:
        print(f"[ELIMINAR] No se pudo eliminar la marca ID {marca_temp.id}.")
        
    if marca_dao.buscar(marca_temp.id) is None:
        print(f"[CONFIRMACIÓN] Búsqueda de ID {marca_temp.id} tras eliminación retornó None.")
        
    # Prueba eliminar ID inexistente
    if not marca_dao.eliminar(9999):
        print(f"[CONTROLADO] Intento de eliminar ID inexistente (9999) retornó False exitosamente.\n")
        
    # =========================================================================
    # PRUEBA 2: MODELODao (Insertar y Buscar con JOIN a Marca)
    # =========================================================================
    print("=================== 2. PRUEBAS MODELODao (con JOIN) ===================")
    modelo_yaris = Modelo("Yaris", marca_toyota)
    modelo_dao.insertar(modelo_yaris)
    conn.commit()
    print(f"[INSERT] Modelo '{modelo_yaris.nombre}' creado con ID: {modelo_yaris.id} (Marca ID: {modelo_yaris.marca.id})")
    
    # Buscar modelo por ID con JOIN
    modelo_buscado = modelo_dao.buscar(modelo_yaris.id)
    if modelo_buscado:
        print(f"[BUSCAR con JOIN] Modelo ID {modelo_buscado.id}:")
        print(f"  - Nombre Modelo: {modelo_buscado.nombre}")
        print(f"  - Marca asociada: {modelo_buscado.marca.nombre} (ID: {modelo_buscado.marca.id})\n")
    else:
        print(f"[BUSCAR] Modelo con ID {modelo_yaris.id} no encontrado.\n")
        
    # =========================================================================
    # PRUEBA 3: AUTODao (Insertar y Buscar con multi-JOIN)
    # =========================================================================
    print("=================== 3. PRUEBAS AUTODao (con multi-JOIN) ===================")
    auto_nuevo = Auto("AB1234", 2022, modelo_yaris)
    auto_dao.insertar(auto_nuevo)
    conn.commit()
    print(f"[INSERT] Auto con patente '{auto_nuevo.patente}' registrado en 'vehiculos' y 'autos'.")
    
    # Buscar auto por Patente con JOIN múltiple
    auto_buscado = auto_dao.buscar("AB1234")
    if auto_buscado:
        print(f"[BUSCAR con multi-JOIN] Auto encontrado:")
        print(f"  - Patente: {auto_buscado.patente}")
        print(f"  - Año: {auto_buscado.anio}")
        print(f"  - En taller: {auto_buscado._en_taller}")
        print(f"  - Modelo: {auto_buscado.modelo.nombre}")
        print(f"  - Marca: {auto_buscado.modelo.marca.nombre}")
        print(f"  - Tarifa Hora Polimórfica: ${auto_buscado.tarifa_hora()}")
    else:
        print("[BUSCAR] Auto no encontrado.")
        
    # Prueba búsqueda controlada inexistente
    patente_inexistente = "XX9999"
    no_existe = auto_dao.buscar(patente_inexistente)
    if no_existe is None:
        print(f"\n[CONTROLADO] Búsqueda de patente '{patente_inexistente}' retornó None exitosamente.")
        
    # Prueba de restricción de clave foránea (Foreign Key)
    print("\n--- Prueba de Seguridad: Intentar eliminar marca con modelos asociados ---")
    if not marca_dao.eliminar(marca_toyota.id):
        print("[CONTROLADO] El sistema bloqueó la eliminación para proteger la integridad referencial.")

    print("\nProceso finalizado exitosamente.")

if __name__ == "__main__":  # Verifica si el script se está ejecutando directamente
    main()  # Llama a la función principal
