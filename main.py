from vehiculo import Vehiculo # Importa la clase base Vehiculo desde el archivo local vehiculo.py
from auto import Auto # Importa la clase Auto desde el archivo local auto.py
from moto import Moto # Importa la clase Moto desde el archivo local moto.py
from camion import Camion # Importa la clase Camion desde el archivo local camion.py

# =====================================================================
# SUGERENCIA 2: Demostración de Abstracción Segura (TypeError)
# =====================================================================
print("--- PRUEBA 1: Instanciación de clase abstracta ---")
try:
    vehiculo = Vehiculo("XY1234", 2015) # Intenta instanciar la clase abstracta Vehiculo directamente
except TypeError as error:
    print(f"[ERROR CONTROLADO] No se puede instanciar la clase abstracta 'Vehiculo': {error}")
    print("-> Confirmación: El programa continuó su ejecución con normalidad.\n")

# =====================================================================
# SUGERENCIA 1: Demostración de Validación de Patente (ValueError)
# =====================================================================
print("--- PRUEBA 2: Validación de patente en constructor ---")
try:
    auto_invalido = Auto("AB 1", 2022, 450) # Intenta crear un auto con patente inválida (< 6 caracteres y con espacio)
except ValueError as error:
    print(f"[ERROR CONTROLADO] Error al validar patente en constructor: {error}")
    print("-> Confirmación: El programa continuó su ejecución con normalidad.\n")

# =====================================================================
# SUGERENCIA 3: Demostración de Validación de Año (ValueError)
# =====================================================================
print("--- PRUEBA 3: Validación de año en constructor ---")
try:
    moto_invalida = Moto("CD5678", 1850) # Intenta crear una moto con año inválido (< 1900)
except ValueError as error:
    print(f"[ERROR CONTROLADO] Error al validar año en constructor: {error}")
    print("-> Confirmación: El programa continuó su ejecución con normalidad.\n")

# =====================================================================
# Operaciones normales con vehículos válidos
# =====================================================================
print("--- OPERACIONES CON VEHÍCULOS VÁLIDOS ---")

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

# Llamada al método polimórfico tarifa_hora() de cada clase concreta derivada
print(f"Tarifa por hora del auto: ${auto.tarifa_hora()}") # Imprime la tarifa por hora del auto sobrescrita (25000)
print(f"Tarifa por hora de la moto: ${moto.tarifa_hora()}") # Imprime la tarifa por hora de la moto sobrescrita (15000)
print(f"Tarifa por hora del camión: ${camion.tarifa_hora()}") # Imprime la tarifa por hora del camión sobrescrita (40000)

# =====================================================================
# Verificación de Restricción Vehicular
# =====================================================================
print("\n--- VERIFICACIÓN DE RESTRICCIÓN VEHICULAR ---")
# Consulta para el auto moderno (año 2020)
print(f"Año del auto registrado ({auto.patente}): {auto.restriccion}") # Consulta el año mediante el getter restriccion
auto.restriccion = 2020 # Asigna su año (> 2011), imprimirá "auto sin restriccion vehicular"

# Ingreso de un vehículo que efectivamente posee año con restricción
auto_antiguo = Auto("ZZ9988", 2008, 400) # Instancia un auto fabricado en el año 2008
print(f"Llega al taller un auto antiguo patente {auto_antiguo.patente} (año {auto_antiguo.restriccion}).")
try:
    auto_antiguo.restriccion = 2008 # Intenta verificar su año real (<= 2011), lo que activará la restricción
except ValueError as error:
    print(f"[RESTRICCIÓN] Aviso para patente {auto_antiguo.patente}: {error}")
    print("-> Confirmación: El taller registró la condición del vehículo y continúa operando normalmente.")

print("\n-> Confirmación final: El programa finalizó todas sus operaciones y pruebas exitosamente.")

