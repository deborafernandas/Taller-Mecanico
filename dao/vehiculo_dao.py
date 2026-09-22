from dao.dao import Dao  # Importa la clase base Dao
from model.vehiculo import Vehiculo  # Importa la entidad base Vehiculo

class VehiculoDao(Dao):  # Define la clase VehiculoDao que hereda de Dao
    """
    Data Access Object para la entidad Vehiculo.
    Hereda de la clase base Dao para utilizar la conexión y el cursor.
    """
    
    def crear_tabla(self):  # Método para crear la tabla base de vehículos
        """
        Crea la tabla 'vehiculos' en la base de datos si no existe.
        La tabla contiene:
        - patente: TEXT PRIMARY KEY
        - anio: INTEGER NOT NULL
        - en_taller: INTEGER (se usará 0 o 1 como booleano)
        - modelo_id: INTEGER NOT NULL (Clave Foránea hacia modelos.id)
        """
        sql = """
        CREATE TABLE IF NOT EXISTS vehiculos(
            patente TEXT PRIMARY KEY,
            anio INTEGER NOT NULL,
            en_taller INTEGER,
            modelo_id INTEGER NOT NULL,
            FOREIGN KEY (modelo_id) REFERENCES modelos (id)
        )
        """
        self.cursor.execute(sql)  # Ejecuta la instrucción de creación de tabla
        self.conexion.commit()  # Confirma los cambios realizados

    def insertar(self, vehiculo: Vehiculo):  # Inserta los atributos comunes del vehículo
        """
        Inserta los datos de un vehículo en la tabla padre 'vehiculos'.
        """
        sql = """
        INSERT INTO vehiculos (patente, anio, en_taller, modelo_id)
        VALUES (?, ?, ?, ?)
        """
        self.cursor.execute(sql, (
            vehiculo.patente,
            vehiculo.anio,
            int(vehiculo._en_taller),
            vehiculo.modelo.id
        ))
