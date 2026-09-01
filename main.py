from auto import Auto # Importa la clase Auto desde el archivo local auto.py
from moto import Moto # Importa la clase Moto desde el archivo local moto.py
from camion import Camion # Importa la clase Camion desde el archivo local camion.py

# Instanciación de los objetos de cada clase derivada
auto = Auto("AB1234", 2020, 500) # Instancia un objeto Auto pasándole patente y año
moto = Moto("CD5678", 2021) # Instancia un objeto Moto pasándole patente y año
camion = Camion("EF9012", 2019, 5000) # Instancia un objeto Camion pasándole patente y año

# Llamada al método ingresar() de cada vehículo
print(auto.ingresar()) # Ejecuta ingresar() del auto y muestra el mensaje retornado en consola
print(moto.ingresar()) # Ejecuta ingresar() de la moto y muestra el mensaje retornado en consola
print(camion.ingresar()) # Ejecuta ingresar() del camión y muestra el mensaje retornado en consola

# Llamada al método tarifa_hora() de cada vehículo
print(f"Tarifa por hora del auto: ${auto.tarifa_hora()}") # Imprime la tarifa por hora del auto
print(f"Tarifa por hora de la moto: ${moto.tarifa_hora()}") # Imprime la tarifa por hora de la moto
print(f"Tarifa por hora del camión: ${camion.tarifa_hora()}") # Imprime la tarifa por hora del camión
