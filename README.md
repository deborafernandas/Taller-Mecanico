# Taller Mecánico

Repositorio para la asignatura de Programación Orientada a Objetos Seguro.

**Profesor:** Michael Arjel
**Institución:** Inacap

---

## Bitácora de Avances

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
