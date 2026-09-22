from dao.dao import Dao  # Importa la clase base Dao desde el módulo dao.dao

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
