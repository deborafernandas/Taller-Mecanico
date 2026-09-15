import sqlite3
from marca import Marca
from modelo import Modelo
from auto import Auto

conexion = sqlite3.connect("taller.db")

cursor = conexion.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Vehiculo(
               patente TEXT PRIMARY KEY, 
               modelo TEXT,
               en_taller INTEGER)""")
marca = Marca("Toyota")
modelo = Modelo ("Yaris", marca)
auto = Auto("AB1235",2027, modelo)

#cursor.execute("INSERT INTO Vehiculo(patente, modelo, en_taller) VALUES (?,?,?)",
#               (auto.patente, auto.modelo.nombre, int(auto._en_taller)))

cursor.execute("Select * from Vehiculo where patente = ?",("AB1235",))
fila= cursor.fetchone()
print(fila)

conexion.commit()

