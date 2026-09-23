import sqlite3  # Importa sqlite3 para capturar IntegrityError en restricciones de Foreign Key
from dao.dao import Dao  # Importa la clase base Dao desde el módulo dao.dao
from model.marca import Marca  # Importa la entidad Marca para reconstruir objetos de dominio

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

    def insertar(self, marca: Marca):  # Inserta una nueva marca en la tabla
        """
        Inserta un registro en la tabla marcas y actualiza el atributo id del objeto.
        """
        self.cursor.execute("INSERT INTO marcas (nombre) values (?)", (marca.nombre,))  # Ejecuta el INSERT parametrizado
        marca.id = self.cursor.lastrowid  # Obtiene el ID generado automáticamente por SQLite y lo asigna al modelo

    def buscar(self, id: int):  # Busca una marca específica por su ID
        """
        Busca un registro en la tabla 'marcas' por su clave primaria.
        Retorna un objeto Marca si existe, o None si no se encuentra.
        """
        sql = "SELECT id, nombre FROM marcas WHERE id = ?"  # Consulta parametrizada para buscar por ID
        self.cursor.execute(sql, (id,))  # Ejecuta la consulta pasando el ID como tupla
        fila = self.cursor.fetchone()  # Obtiene el primer (y único) registro coincidente
        
        if fila:  # Si la consulta encontró un registro
            marca = Marca(fila[1])  # Reconstruye el objeto de dominio Marca con el nombre obtenido
            marca.id = fila[0]  # Asigna el ID numérico correspondiente desde la base de datos
            return marca  # Retorna el objeto Marca con todos sus datos cargados
        return None  # Retorna None si no se encontró ningún registro con ese ID

    def listar(self):  # Obtiene todos los registros de marcas existentes
        """
        Recupera todas las marcas almacenadas en la base de datos.
        Retorna una lista de objetos Marca.
        """
        sql = "SELECT id, nombre FROM marcas"  # Consulta para seleccionar todas las filas de la tabla
        self.cursor.execute(sql)  # Ejecuta la consulta SELECT
        filas = self.cursor.fetchall()  # Recupera todas las filas como una lista de tuplas
        
        marcas = []  # Inicializa la lista donde se guardarán los objetos de dominio
        for fila in filas:  # Itera sobre cada registro obtenido de la base de datos
            marca = Marca(fila[1])  # Instancia el objeto Marca con el nombre
            marca.id = fila[0]  # Asigna el ID a la instancia
            marcas.append(marca)  # Agrega la marca a la lista de resultados
            
        return marcas  # Retorna la lista completa de objetos Marca

    def actualizar(self, nueva_marca: Marca):  # Actualiza los datos de una marca existente
        """
        Actualiza el nombre de una marca en la base de datos según su ID.
        Valida mediante cursor.rowcount si se modificó alguna fila y retorna el objeto actualizado.
        Retorna None si el ID no existe en la base de datos.
        """
        sql = "UPDATE marcas SET nombre = ? WHERE id = ?"
        self.cursor.execute(sql, (nueva_marca.nombre, nueva_marca.id))
        
        if self.cursor.rowcount > 0:  # Valida que al menos una fila haya sido afectada por la sentencia
            self.conexion.commit()  # Confirma y persiste los cambios en la base de datos
            return self.buscar(nueva_marca.id)  # Retorna el registro fresco consultado desde la BD
            
        return None  # Retorna None si el registro con ese ID no existía

    def eliminar(self, id: int) -> bool:  # Elimina una marca por su ID
        """
        Elimina una marca de la base de datos según su ID.
        Valida mediante cursor.rowcount si se eliminó el registro.
        Retorna True si fue eliminada con éxito.
        Retorna False si el ID no existe o si no se puede eliminar por restricción de integridad referencial (Foreign Key).
        """
        try:
            sql = "DELETE FROM marcas WHERE id = ?"
            self.cursor.execute(sql, (id,))  # Ejecuta la consulta de eliminación parametrizada
            
            if self.cursor.rowcount > 0:  # Valida que al menos una fila haya sido eliminada
                self.conexion.commit()  # Confirma la eliminación en la base de datos
                return True  # Retorna True confirmando el borrado
                
            return False  # Retorna False si el ID no existía en la tabla
            
        except sqlite3.IntegrityError as error:  # Captura error si la marca tiene modelos asociados
            self.conexion.rollback()  # Revierte cualquier cambio pendiente
            print(f"[RESTRICCIÓN] No se puede eliminar la marca ID {id} porque tiene modelos asociados: {error}")
            return False  # Retorna False impidiendo violar la integridad referencial