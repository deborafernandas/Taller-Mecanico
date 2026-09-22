from dao.vehiculo_dao import VehiculoDao  # Importa VehiculoDao para la herencia
from model.auto import Auto  # Importa la entidad Auto
from model.modelo import Modelo  # Importa la entidad Modelo para reconstruir la relación
from model.marca import Marca  # Importa la entidad Marca para reconstruir la relación

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

    def insertar(self, auto: Auto):  # Inserta un auto en las tablas correspondientes
        """
        Inserta un auto aprovechando la herencia de tablas:
        1. Inserta en la tabla padre 'vehiculos' (vía super().insertar).
        2. Inserta la clave primaria/foránea en la tabla hija 'autos'.
        """
        super().insertar(auto)  # Inserta patente, año, en_taller y modelo_id en vehiculos
        sql = "INSERT INTO autos (patente) VALUES (?)"  # Consulta para la tabla autos
        self.cursor.execute(sql, (auto.patente,))  # Inserta la clave primaria/foránea en autos

    def buscar(self, patente: str):  # Busca un auto por patente con JOIN múltiple
        """
        Busca un auto por su patente realizando un INNER JOIN múltiple:
        autos -> vehiculos -> modelos -> marcas.
        Reconstruye y retorna toda la jerarquía de objetos: Marca -> Modelo -> Auto.
        Retorna None si no se encuentra.
        """
        sql = """
        SELECT a.patente, v.anio, v.en_taller, m.id, m.nombre, ma.id, ma.nombre
        FROM autos a
        INNER JOIN vehiculos v ON a.patente = v.patente
        INNER JOIN modelos m ON v.modelo_id = m.id
        INNER JOIN marcas ma ON m.marca_id = ma.id
        WHERE a.patente = ?
        """
        self.cursor.execute(sql, (patente,))  # Ejecuta la consulta pasando la patente
        fila = self.cursor.fetchone()  # Recupera el registro encontrado o None
        
        if fila:  # Si el auto fue encontrado
            # 1. Reconstruir Marca asociada
            marca = Marca(fila[6])
            marca.id = fila[5]
            
            # 2. Reconstruir Modelo con su Marca
            modelo = Modelo(fila[4], marca)
            modelo.id = fila[3]
            
            # 3. Reconstruir Auto con su Modelo y atributos
            auto = Auto(fila[0], fila[1], modelo)
            auto._en_taller = bool(fila[2])  # Restaura el estado en taller
            return auto
            
        return None  # Retorna None si no existe auto con esa patente
