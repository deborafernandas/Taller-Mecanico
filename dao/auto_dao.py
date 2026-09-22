from dao.vehiculo_dao import VehiculoDao  # Importa VehiculoDao para la herencia

class AutoDao(VehiculoDao):  # AutoDao hereda de VehiculoDao (relación jerárquica)
    """
    Data Access Object para la entidad Auto.
    Hereda de VehiculoDao (que a su vez hereda de Dao).
    """
    
    def crear_tabla(self):  # Sobrescribe el método crear_tabla para incluir lógica propia
        """
        Invoca la creación de la tabla padre ('vehiculos') y luego 
        crea la tabla 'autos' en la base de datos si no existe.
        La tabla 'autos' contiene:
        - patente: TEXT PRIMARY KEY, que a su vez es FOREIGN KEY de vehiculos.patente
        """
        # Primero invocamos al método del padre para asegurar que exista la tabla vehiculos
        super().crear_tabla()  # Llama al crear_tabla() de VehiculoDao para asegurar la tabla padre
        
        # Luego creamos la tabla específica de autos
        sql = """
        CREATE TABLE IF NOT EXISTS autos(
            patente TEXT PRIMARY KEY,
            FOREIGN KEY (patente) REFERENCES vehiculos (patente)
        )
        """
        self.cursor.execute(sql)  # Ejecuta la consulta de creación para la tabla hija
        self.conexion.commit()  # Confirma los cambios en la base de datos
