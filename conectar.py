import sqlite3  # Importa el módulo sqlite3 para interactuar con bases de datos SQLite

def crear_conexion():  # Define la función encargada de establecer la conexión
    """
    Crea y retorna una conexión a la base de datos SQLite 'taller.db'.
    Habilita el uso de Foreign Keys (claves foráneas) por defecto.
    """
    conexion = sqlite3.connect("taller.db")  # Crea la conexión a la base de datos 'taller.db' (la crea si no existe)
    conexion.execute("PRAGMA foreign_keys = ON")  # Ejecuta un comando PRAGMA para habilitar el soporte de claves foráneas
    return conexion  # Retorna el objeto de conexión para ser usado por otras partes del programa
