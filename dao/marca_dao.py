from dao.dao import Dao  # Importa la clase base Dao desde el módulo dao.dao

class MarcaDao(Dao):  # Define la clase MarcaDao que hereda de Dao
    """
    Data Access Object para la entidad Marca.
    Hereda de la clase base Dao para utilizar la conexión y el cursor.
    """
    
    def crear_tabla(self):  # Define el método para crear la tabla correspondiente
        """
        Crea la tabla 'marcas' en la base de datos si no existe.
        La tabla contiene:
        - id: INTEGER PRIMARY KEY AUTOINCREMENT
        - nombre: TEXT NOT NULL
        """
        sql = """
        CREATE TABLE IF NOT EXISTS marcas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )
        """
        self.cursor.execute(sql)  # Ejecuta la consulta SQL utilizando el cursor heredado
        self.conexion.commit()  # Confirma (guarda) los cambios en la base de datos utilizando la conexión heredada
