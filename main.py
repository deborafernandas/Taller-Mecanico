from vehiculo import Vehiculo # Importa la clase base Vehiculo desde el archivo local vehiculo.py
from auto import Auto # Importa la clase Auto desde el archivo local auto.py
from moto import Moto # Importa la clase Moto desde el archivo local moto.py
from camion import Camion # Importa la clase Camion desde el archivo local camion.py

# Instanciación de un objeto de la clase base para comparar la tarifa original
vehiculo = Vehiculo("XY1234", 2015) # Instancia un objeto base Vehiculo pasándole patente y año

# Instanciación de los objetos de cada clase derivada
auto = Auto("AB1234", 2020, 500) # Instancia un objeto Auto pasándole patente, año y capacidad de maletero
moto = Moto("CD5678", 2021) # Instancia un objeto Moto pasándole patente y año
camion = Camion("EF9012", 2019, 5000) # Instancia un objeto Camion pasándole patente, año y capacidad de carga

# Llamada al método ingresar() de cada vehículo
print(auto.ingresar()) # Ejecuta ingresar() del auto y muestra el mensaje retornado en consola
print(moto.ingresar()) # Ejecuta ingresar() de la moto y muestra el mensaje retornado en consola
print(camion.ingresar()) # Ejecuta ingresar() del camión y muestra el mensaje retornado en consola

pruebaEnc = camion.patente # Accede a la patente del camión a través de la property getter patente
print(f"Patente del camión obtenida: {pruebaEnc}")

# Llamada al método tarifa_hora() de cada vehículo para verificar la sobreescritura
print(f"Tarifa por hora base (Vehiculo): ${vehiculo.tarifa_hora()}") # Imprime la tarifa base original (5000)
print(f"Tarifa por hora del auto: ${auto.tarifa_hora()}") # Imprime la tarifa por hora del auto sobrescrita (25000)
print(f"Tarifa por hora de la moto: ${moto.tarifa_hora()}") # Imprime la tarifa por hora de la moto sobrescrita (15000)
print(f"Tarifa por hora del camión: ${camion.tarifa_hora()}") # Imprime la tarifa por hora del camión sobrescrita (40000)

# Prueba de la property restriccion en la clase Auto
print(f"Año del auto obtenido: {auto.restriccion}") # Prueba del getter
auto.restriccion = 2015 # Asignación válida (> 2011), imprimirá "auto sin restriccion vehicular"

try:
    auto.restriccion = 2010 # Asignación inválida (<= 2011), lanzará ValueError
except ValueError as error:
    print(f"Excepción capturada: {error}") # Muestra el mensaje de la excepción lanzada

