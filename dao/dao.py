class Dao:  # Define la clase base Dao (Data Access Object)
    """
    Clase base Data Access Object (DAO).
    Se encarga de inicializar y mantener la conexión a la base de datos y su cursor.
    """
    
    def __init__(self, conexion):  # Define el constructor de la clase, recibe la conexión
        """
        Constructor que recibe un objeto de conexión y establece el cursor.
        
        Args:
            conexion: El objeto de conexión a la base de datos.
        """
        self.conexion = conexion  # Almacena el objeto de conexión como un atributo de la instancia
        self.cursor = self.conexion.cursor()  # Crea y almacena un cursor a partir de la conexión para ejecutar consultas SQL
