import conectar  # Importa el módulo conectar para inicializar la base de datos
from dao.marca_dao import MarcaDao  # Importa el DAO de marcas
# from dao.modelo_dao import ModeloDao  # Importa el DAO de modelos
# from dao.auto_dao import AutoDao  # Importa el DAO de autos (que también gestiona vehículos)
from model.marca import Marca  # Importa el modelo Marca para instanciar objetos

def main():  # Función principal de ejecución
    print("--- Inicializando Base de Datos ---")  # Mensaje de inicio
    
    # 1. Crear conexión
    conn = conectar.crear_conexion()  # Llama a crear_conexion para obtener el objeto de conexión
    
    # 2. Instanciar el DAO pasándole la conexión
    marca_dao = MarcaDao(conn)  # Instancia MarcaDao entregando la conexión
    # modelo_dao = ModeloDao(conn)  # Instancia ModeloDao entregando la conexión
    # auto_dao = AutoDao(conn)  # Instancia AutoDao entregando la conexión
    
    # 3. Asegurar que la tabla exista antes de operar
    marca_dao.crear_tabla()  
    
    # --- PRUEBA DEL MÉTODO INSERTAR ---
    print("\n--- Probando método insertar en MarcaDao ---")
    nueva_marca = Marca("Lexus")  # Instanciamos una nueva marca
    print(f"ID antes de insertar: {nueva_marca.id}")
    
    marca_dao.insertar(nueva_marca)  # Llamamos al método insertar
    conn.commit()  # Guardamos los cambios en la base de datos
    
    print(f"Marca '{nueva_marca.nombre}' insertada exitosamente con el ID: {nueva_marca.id}")
    
    # --- PRUEBA DEL MÉTODO LISTAR ---
    print("\n--- Probando método listar en MarcaDao ---")
    marcas = marca_dao.listar()  # Recupera todas las marcas de la tabla
    print(f"Total de marcas encontradas: {len(marcas)}")
    for m in marcas:  # Recorre e imprime cada objeto Marca recuperado
        print(f"  - ID: {m.id} | Nombre: {m.nombre}")
    
    # --- PRUEBA DEL MÉTODO BUSCAR ---
    print("\n--- Probando método buscar en MarcaDao ---")
    id_a_buscar = nueva_marca.id  # Probamos buscar el ID recién insertado
    marca_encontrada = marca_dao.buscar(id_a_buscar)  # Llama al método buscar
    if marca_encontrada:
        print(f"  [ÉXITO] Marca encontrada -> ID: {marca_encontrada.id}, Nombre: {marca_encontrada.nombre}")
    else:
        print(f"  [NO ENCONTRADO] No existe marca con el ID {id_a_buscar}")
        
    # Probamos buscar un ID inexistente para validar retorno None
    id_inexistente = 9999
    marca_no_existe = marca_dao.buscar(id_inexistente)
    if marca_no_existe:
        print(f"  [ÉXITO] Marca encontrada -> ID: {marca_no_existe.id}, Nombre: {marca_no_existe.nombre}")
    else:
        print(f"  [CONTROLADO] Búsqueda de ID {id_inexistente} retornó None (no existe en BD)")

    # --- RESTO DEL CÓDIGO COMENTADO PARA REFERENCIA ---
    # print("\nCreando resto de las tablas...")
    # modelo_dao.crear_tabla()  # Ejecuta la creación de la tabla modelos
    # auto_dao.crear_tabla()  # Ejecuta la creación de las tablas vehiculos y autos (por herencia)
    
    # 4. Validar que las tablas existan en la BD
    # cursor = conn.cursor()  # Obtiene un cursor directamente desde la conexión para una consulta general
    # cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")  # Consulta al maestro de SQLite por los nombres de las tablas
    # tablas_creadas = [fila[0] for fila in cursor.fetchall()]  # Extrae los nombres de las tablas en una lista
    
    # print("\n--- Tablas encontradas en la Base de Datos ---")  # Mensaje informativo
    # for tabla in tablas_creadas:  # Itera sobre la lista de tablas encontradas
    #     # Excluimos la tabla interna de SQLite
    #     if tabla != "sqlite_sequence":  # Ignora 'sqlite_sequence' que es una tabla del sistema
    #         print(f"- {tabla}")  # Imprime el nombre de cada tabla de nuestro negocio
    
    print("\nProceso finalizado exitosamente.")  # Mensaje final de éxito

if __name__ == "__main__":  # Verifica si el script se está ejecutando directamente
    main()  # Llama a la función principal
