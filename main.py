import conectar  # Importa el módulo conectar para inicializar la base de datos
from dao.marca_dao import MarcaDao  # Importa el DAO de marcas
from dao.modelo_dao import ModeloDao  # Importa el DAO de modelos
from dao.auto_dao import AutoDao  # Importa el DAO de autos (que también gestiona vehículos)

def main():  # Función principal de ejecución
    print("--- Inicializando Base de Datos ---")  # Mensaje de inicio
    
    # 1. Crear conexión
    conn = conectar.crear_conexion()  # Llama a crear_conexion para obtener el objeto de conexión
    
    # 2. Instanciar los DAOs pasándoles la conexión
    marca_dao = MarcaDao(conn)  # Instancia MarcaDao entregando la conexión
    modelo_dao = ModeloDao(conn)  # Instancia ModeloDao entregando la conexión
    auto_dao = AutoDao(conn)  # Instancia AutoDao entregando la conexión
    
    # 3. Crear las tablas
    # Nota: auto_dao.crear_tabla() creará 'vehiculos' y luego 'autos'
    print("Creando tablas...")  # Mensaje informativo
    marca_dao.crear_tabla()  # Ejecuta la creación de la tabla marcas
    modelo_dao.crear_tabla()  # Ejecuta la creación de la tabla modelos
    auto_dao.crear_tabla()  # Ejecuta la creación de las tablas vehiculos y autos (por herencia)
    
    # 4. Validar que las tablas existan en la BD
    cursor = conn.cursor()  # Obtiene un cursor directamente desde la conexión para una consulta general
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")  # Consulta al maestro de SQLite por los nombres de las tablas
    tablas_creadas = [fila[0] for fila in cursor.fetchall()]  # Extrae los nombres de las tablas en una lista
    
    print("\n--- Tablas encontradas en la Base de Datos ---")  # Mensaje informativo
    for tabla in tablas_creadas:  # Itera sobre la lista de tablas encontradas
        # Excluimos la tabla interna de SQLite
        if tabla != "sqlite_sequence":  # Ignora 'sqlite_sequence' que es una tabla del sistema
            print(f"- {tabla}")  # Imprime el nombre de cada tabla de nuestro negocio
    
    print("\nProceso finalizado exitosamente.")  # Mensaje final de éxito

if __name__ == "__main__":  # Verifica si el script se está ejecutando directamente
    main()  # Llama a la función principal
