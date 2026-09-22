from dao.dao import Dao  # Importa la clase base Dao desde el módulo dao.dao
from model.modelo import Modelo  # Importa la entidad Modelo para tipado y reconstrucción
from model.marca import Marca  # Importa la entidad Marca para reconstruir la relación

class ModeloDao(Dao):  # Define la clase ModeloDao que hereda de Dao
    """
    Data Access Object para la entidad Modelo.
    Hereda de la clase base Dao para utilizar la conexión y el cursor.
    """
    
    def crear_tabla(self):  # Define el método para crear la tabla de modelos
        """
        Crea la tabla 'modelos' en la base de datos si no existe.
        La tabla contiene:
        - id: INTEGER PRIMARY KEY AUTOINCREMENT
        - nombre: TEXT NOT NULL
        - marca_id: INTEGER NOT NULL (Clave Foránea hacia marcas.id)
        """
        sql = """
        CREATE TABLE IF NOT EXISTS modelos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            marca_id INTEGER NOT NULL,
            FOREIGN KEY (marca_id) REFERENCES marcas (id)
        )
        """
        self.cursor.execute(sql)  # Ejecuta la consulta SQL para crear la tabla
        self.conexion.commit()  # Confirma los cambios en la base de datos

    def insertar(self, modelo: Modelo):  # Inserta un nuevo modelo en la tabla
        """
        Inserta un registro en la tabla modelos guardando la referencia a su marca.
        Actualiza el atributo id del objeto modelo con el autoincremental de SQLite.
        """
        sql = "INSERT INTO modelos (nombre, marca_id) VALUES (?, ?)"  # Consulta parametrizada
        self.cursor.execute(sql, (modelo.nombre, modelo.marca.id))  # Ejecuta con nombre y el id de la marca
        modelo.id = self.cursor.lastrowid  # Asigna el ID autoincremental generado

    def buscar(self, id: int):  # Busca un modelo específico por su ID usando JOIN
        """
        Busca un registro en la tabla 'modelos' por su ID realizando un INNER JOIN con 'marcas'.
        Reconstruye y retorna el objeto Modelo completo junto a su objeto Marca asociado.
        Retorna None si no se encuentra.
        """
        sql = """
        SELECT m.id, m.nombre, ma.id, ma.nombre
        FROM modelos m
        INNER JOIN marcas ma ON m.marca_id = ma.id
        WHERE m.id = ?
        """
        self.cursor.execute(sql, (id,))  # Ejecuta la consulta pasando el ID
        fila = self.cursor.fetchone()  # Recupera una fila o None
        
        if fila:  # Si se encontró el registro
            # 1. Reconstruir el objeto Marca asociado (datos de la tabla marcas)
            marca = Marca(fila[3])
            marca.id = fila[2]
            
            # 2. Reconstruir el objeto Modelo con su Marca ya instanciada
            modelo = Modelo(fila[1], marca)
            modelo.id = fila[0]
            return modelo  # Retorna el objeto Modelo con toda su jerarquía
            
        return None  # Retorna None si no existe el ID
