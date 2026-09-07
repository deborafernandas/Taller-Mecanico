# Taller Mecánico

Repositorio para la asignatura de Programación Orientada a Objetos Seguro.

**Profesor:** Michael Arjel
**Institución:** Inacap

---

## Bitácora de Avances

### 7 de Septiembre de 2026
- **Sobrescritura de Métodos (Polimorfismo):**
  - **Clase Auto (`auto.py`):** Se sobrescribió el método `tarifa_hora()` para retornar un valor entero de `25000`.
  - **Clase Moto (`moto.py`):** Se implementó y sobrescribió el método `tarifa_hora()` retornando un valor entero de `15000`.
  - **Clase Camion (`camion.py`):** Se sobrescribió el método `tarifa_hora()` retornando un valor entero de `40000`.
  - Se mantuvo intacto el método `tarifa_hora()` en la clase base `Vehiculo` (`vehiculo.py`) retornando su valor base de `5000`.
- **Encapsulamiento y Validaciones con Properties (`@property`):**
  - **Clase Vehiculo (`vehiculo.py`):**
    - Se implementó la *property* `patente` (getter) para acceder al atributo privado `__patente`.
    - Se implementó el *setter* para `patente`, validando que posea al menos 6 caracteres y no contenga espacios, lanzando `ValueError` si no cumple.
    - Se actualizó el constructor `__init__` para asignar mediante `self.patente = patente`, aplicando la validación desde la instanciación de cualquier objeto.
  - **Clase Auto (`auto.py`):**
    - Se implementó la *property* `restriccion` (getter) para consultar el año del auto.
    - Se implementó el *setter* para `restriccion`, validando que el año sea mayor a 2011 (`> 2011`) con el mensaje `"auto sin restriccion vehicular"`, o lanzando un `ValueError` con el mensaje `"auto sujeto a restriccion vehicular"`.
- **Actualización del Script de Pruebas (`main.py`):**
  - Se probó la sobreescritura de `tarifa_hora()` en las tres clases derivadas contrastándolas con la clase base `Vehiculo`.
  - Se probó la lectura de atributos encapsulados a través de la propiedad `patente` (`camion.patente`).
  - Se probaron el *getter* y *setter* de la propiedad `restriccion` en `Auto`, incluyendo la captura controlada de la excepción `ValueError`.
- **Documentación:**
  - Se comentaron detalladamente todas las líneas de código añadidas y modificadas con fines educativos.

---

### 31 de Agosto de 2026
- **Implementación de Herencia:**
  - Se crearon tres clases derivadas a partir de la clase base `Vehiculo`:
    - **Clase Auto (`auto.py`):** Hereda de `Vehiculo`, define su propio constructor llamando a `super().__init__(patente, anio)` y añade el atributo privado `__capacidad_maletero` (en litros).
    - **Clase Moto (`moto.py`):** Hereda de `Vehiculo`, creada inicialmente con `pass`.
    - **Clase Camion (`camion.py`):** Hereda de `Vehiculo`, define su propio constructor llamando a `super().__init__(patente, anio)` y añade el atributo privado `__capacidad_carga` (en kilos).
- **Actualización del Script de Pruebas (`main.py`):**
  - Se importaron las clases `Auto`, `Moto` y `Camion`.
  - Se instanciaron objetos de cada una de las clases derivadas.
  - Se ejecutaron los métodos heredados `ingresar()` y `tarifa_hora()`, verificando el correcto funcionamiento de la herencia.
- **Documentación:**
  - Se comentaron detalladamente todas las líneas de código en los archivos nuevos y modificados con fines educativos.

---

### 25 de Agosto de 2026
- **Configuración Inicial:** Vinculación del directorio local con el repositorio de GitHub usando el CLI de GitHub (`gh auth`).
- **Limpieza:** Se eliminó la versión antigua del archivo `vehiculo.py` para construir el proyecto desde cero.
- **Clase Vehiculo (`vehiculo.py`):**
  - Se creó la clase principal del proyecto.
  - Se definieron los atributos privados `__patente`, `__anio` y `__en_taller` en el constructor, aplicando encapsulamiento y *type hints*.
  - Se crearon los métodos `ingresar()` y `entregar()` con validación de estado.
  - Se creó el método `tarifa_hora()` que retorna un valor fijo de 5000.
- **Script de Pruebas (`main.py`):**
  - Se creó el archivo de ejecución principal.
  - Se importó la clase `Vehiculo` y se instanciaron 3 objetos con datos ficticios.
  - Se probó la invocación de métodos y la impresión de la tarifa por hora en consola.
- **Documentación:** Se comentaron todas las líneas de código en ambos archivos (`vehiculo.py` y `main.py`) explicando paso a paso su funcionamiento con fines educativos.
